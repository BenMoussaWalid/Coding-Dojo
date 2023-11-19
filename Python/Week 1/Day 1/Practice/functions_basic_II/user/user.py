class User :
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name 
        self.last_name = last_name 
        self.email = email 
        self.age = age 
        self.gold_card_points = 0
        self.is_rewards_member=False
    def display_info(self) :
        print(self.first_name)    
        print(self.last_name)
        print(self.email)
        print(self.age )
        print(self.gold_card_points)
        print(self.is_rewards_member)


    def enroll(self) :
        self.gold_card_points = 200
        self.is_rewards_member=True
        return self
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print ("dont have points")
        else:
            self.gold_card_points=self.gold_card_points-amount
            return self

walid=User("walid","benmoussa","gdmhm",23)
walid.enroll()
walid.spend_points(100)
walid.display_info()
