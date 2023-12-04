from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, render_template, redirect, request, session, flash
from flask_app.models import user_model
class Register:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructione = data["instructione"]
        self.under = data["under"]
        self.date_m_ade = data["date_m_ade"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.creater=None

    #! all register
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for row in results:
            recipe = cls(row)  # Fixed variable name here
            recipes.append(recipe)
        return recipes
    # inserrt
    @classmethod
    def save(cls, data):
        query = """INSERT INTO recipes_schema.recipes(name,description,instructione,under,date_m_ade,user_id)
                VALUES (%(name)s,%(description)s,%(instructione)s,%(under)s,%(date_m_ade)s,%(user_id)s); 
            """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #join general
    @classmethod
    def get_all_recipes(cls):
        query = """
                    select * from recipes join users on users.id=recipes.user_id;
                    
                """
        result = connectToMySQL(DATABASE).query_db(query)
        recipes=[]
        for row in result:
            one_recipes= cls(row)
            
            data={
                **row,
                "id":row["users.id"],
                "created_at":row["users.created_at"],
                "updated_at":row["users.created_at"]}
            one_recipes.creater=user_model.User(data)
            recipes.append(one_recipes)
        return recipes
#____________________________________________

    @classmethod
    def get_recipes_id(cls,data):
        query = """
                    select * from recipes join users on users.id=recipes.user_id where recipes.id =%(id)s
                """
        result = connectToMySQL(DATABASE).query_db(query,data)
        recipes_one=cls(result[0])
        dataa={ **result[0],
                    "id":result[0]["users.id"],
                    "created_at":result[0]["users.created_at"],
                    "updated_at":result[0]["users.updated_at"]
                    }
        recipes_one.creater=user_model.User(dataa)
        return recipes_one
#___________________________________________
    @classmethod
    def update(cls,data):
        query = """
                UPDATE recipes
                SET name = %(name)s, 
                description = %(description)s, 
                instructione=%(instructione)s , 
                under=%(under)s , 
                date_m_ade=%(date_m_ade)s , 
                user_id=%(user_id)s
                WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)

#_______________________________________________


    @classmethod
    def delete(cls, data):
        query = """
                delete from recipes
                where id=%(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

#____________________________________________________
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data["name"]) < 1:
            is_valid = False
            flash("name must not be blank")
        if len(data["description"]) < 1:
            is_valid = False
            flash("description must not be blank")
        if len(data["instructione"]) < 1:
            is_valid = False
            flash("instructione must not be blank")
        return is_valid

