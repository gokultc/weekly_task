class student:
    def set(self,id,fname,lname,course,gender,collname):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.course=course
        self.gender=gender
        self.collagename=collname
    def print(self):
        print(self.id,self.fname,self.lname,self.course,self.gender,self.collagename)

s1=student()
s1.set(12,'aml','raj','futter','m','luminar')
s1.print()
s2=student()
s2.set(12,'bibin','raju','futter','m','luminar')
s2.print()
s3=student()
s3.set(12,'aln','rajappn','futter','m','luminar')
s3.print()
s4=student()
s4.set(12,'vishnu','chinnan','futter','m','luminar')
s4.print()
s5=student()
s5.set(12,'ajun','raj','futter','m','luminar')
s5.print()