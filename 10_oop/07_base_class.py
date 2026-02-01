# Accessing the base class : 3 ways
# 1)==>Duplicate code

class Chai:
    def __init__(self,type_,strength):
        self.type=type_
        self.strength=strength
# class Ginger_chai(Chai):
#     def __init__(self, type_, strength,spice_level):
#         self.type=type_
#         self.strength=strength
#         self.spice_level=spice_level

# 2)==>explicit call
# class Ginger_chai(Chai):
#     def __init__(self, type_, strength,spice_level):
#         Chai.__init__(self,type_,strength)
#         self.spice_level=spice_level

# 3)==>super
class Ginger_chai(Chai):
    def __init__(self, type_, strength,spice_level):
        super().__init__(type_, strength)
        self.spice_level=spice_level

