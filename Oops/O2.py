class person:
    def setvalue(self,fname,lname,age,gender,phn):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.gender=gender
        self.phn=phn
    def printvalue(self):
        print(self.fname,self.lname,self.age,self.gender,self.phn)
person1=person()
person1.setvalue('vinay','k',23,'m',123)
person1.printvalue()
person2=person()
person2.setvalue('gokul','tc',21,'m',1233)
person2.printvalue()
person3=person()
person3.setvalue('alan','krishna',)
person3.printvalue()