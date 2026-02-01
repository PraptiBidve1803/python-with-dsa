
# inheritance
class Basechai:
    def __init__(self,type_):
        self.type=type_
    def prepare(self):
        print(f"Preparing a {self.type} chai....")
        
class Masala_chai(Basechai):    #Inheritance-is a relashionship (masalachai is a basechai )
    def add_spices(self):
         print(f"Add spices cardmom,cloves,black papper") 
         
class chaishop:
    # “This shop uses BaseChai to make tea”
    chai_cls=Basechai #composition starts,has a relationship,a class can be stored in a variable in Python.         
    def __init__(self):
        self.chai=self.chai_cls("Regular")  #giving type of chai,“Make one cup of Regular chai using BaseChai recipe and keep it inside the shop”
    def serve(self):
        print(f"serving {self.chai_cls} chai in the shop")    
        self.chai.prepare()
        
class Fancy_shop(chaishop):
    chai_cls=Masala_chai 
    
shop=chaishop()
fancy=Fancy_shop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()           
         
          
                 
        
    