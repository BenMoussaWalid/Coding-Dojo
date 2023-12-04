from ..config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    
    @classmethod
    def get_all(cls):
        query="SELECT * FROM dojos;"
        dojos=[]
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        for row in results:
            dojos.append(cls(row))
        return dojos
    
    @classmethod
    def save(cls,data):
        query="INSERT INTO dojos(name) VALUES (%(name)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    
    @classmethod
    def get_one_by_id(cls,data):
        query="SELECT * FROM dojos WHERE id=%(id)s;"
        result=connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])
    