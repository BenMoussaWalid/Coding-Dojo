from Ninjas import Ninjas
class Pet:
    def __init__(self,name,type,tricks,health,energy):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=health
        self.energy=energy
    def sleep(self):
        self.energy+=25
        print(self.energy)
    def eat(self):
        self.health+=5
        self.energy+=10
        print(self.energy,self.health)
    def play(self):
        self.health+=5
        print(self.health)
    def noise(self):
        if(self.type=='dog'):
            print(f'{self.name} barks: woof woof')
        else:
            print(f"soud of {self.name}")
class dog(Pet):
    def __init__(self, name, type, tricks, health, energy,age):
        super().__init__(name, type, tricks, health, energy)
        self.age=age
cat=Pet('kiti','cat','fast_moves',10,100)
naruto=Ninjas('naruto','ozomaki','sushi','fish',cat)
naruto.walk().feed().beath()
dog=dog('wanda','dog','kind',20,100,2)
dog.noise()
dog.play()
dog.eat()