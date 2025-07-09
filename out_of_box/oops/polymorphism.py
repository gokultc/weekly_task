# poly = many
# morpjsm = forms

# "one name, many forms".
# one method or function same name
# different classes have diff behavior


class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Woof"

def make_sound(animal):
    print(animal.sound())

make_sound(Cat())  # Meow
make_sound(Dog())  # Woof


# make_sound() - same function
# cat, dog
# one interface, different outputs.

