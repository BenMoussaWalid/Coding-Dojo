from ..config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.dojo_id=data['dojo_id']
        self.age=data['age']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    
    @classmethod
    def save(cls,data):
        query="INSERT INTO ninjas(first_name,last_name,age,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)


    @classmethod
    def get_by_dojo_id(cls,data):
        query="SELECT * FROM ninjas WHERE dojo_id=%(id)s;"
        ninjas=[]
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        for row in results:
            ninjas.append(cls(row))
        return ninjas