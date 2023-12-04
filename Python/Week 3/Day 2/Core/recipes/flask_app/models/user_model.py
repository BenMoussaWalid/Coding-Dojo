from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query = """INSERT INTO users(first_name,last_name,email,password)
                values (%(first_name)s,%(last_name)s,%(email)s,%(password)s); 
            """
        return connectToMySQL(DATABASE).query_db(query, data)
    # ? === GET USER BY ID
    @classmethod
    def get_user_by_id(cls, data):
        query = """
                     SELECT * FROM users
                    WHERE id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    # ? === READ ONE (GET BY EMAIL)
    @classmethod
    def get_by_email(cls, data):
        query = """
                    SELECT * FROM users
                    WHERE users.email = %(email)s;
                """
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    # * ========= USER VALIDATOR =========
    @staticmethod
    def validate(data):
        is_valid = True

        if len(data["first_name"]) < 2:
            is_valid = False
        if len(data["last_name"]) < 2:
            is_valid = False
            flash("name must be at least 3 characters")
        if len(data["email"]) < 1:
            flash("email Required !")
            is_valid = False
        elif not EMAIL_REGEX.match(data["email"]):
            flash("Invalid Email!!!")
            is_valid = False
        else:
            data_for_email = {"email": data["email"]}
            potential_user = User.get_by_email(data_for_email)
            if potential_user:
                is_valid = False
                flash("email already taken, hopefully by you! ")
        if len(data["password"]) < 7:
            is_valid = False
            flash("password must be at least 8 characters")
        elif not data["password"] == data["confirm_password"]:
            is_valid = False
            flash("passwords don't match!")
        return is_valid
