#  binding data (variables) and methods (functions) together in one unit (class) and restricting direct access

# Data (variables) + code (methods) = class (one unit )

class Person:
    def __init__(self, name, age):
        self.name = name        # public
        self.__age = age        # private

    def get_age(self):
        return self.__age

p = Person("Gokul", 20)
print(p.name)

print(p.get_age())



