class Pet:
    sound = "bark"      #class atribute

    def __init__(self, name, age ) -> None:    #inside the (parameters)
        self.name = name   #instance.attribute = parameter
        self.age = age
        
    def introduce(self):               #for the function we need to define the parameter again as self 
        print(f"hello i am {self.name} and im {self.age}")          

pet1 = Pet("buddy", 3)   #creating instance(pet1) inside the class aka we store 2 parameters(name, age) 
pet2 = Pet("albert", 2)

print(pet2.name)     #calling the atribute(name) inside the instance(pet2) 

pet1.introduce()        #here we are calling the function introduce but self will now use the parameters entered when creating the instance