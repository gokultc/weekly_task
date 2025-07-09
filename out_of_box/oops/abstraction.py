# Hiding complex logic and showing necessary  part
# interface will only be shown
# Internal logic will be hidden

from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    def stop(self):
        pass

class car(vehicle):
    def go(self):
        print("go")
    def stop(self):
        print("stop")

car1 = car()
car1.go()
car1.stop()




