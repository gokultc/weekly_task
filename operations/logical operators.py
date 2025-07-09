#logical operator

#1. AND  & ambasent (only one is needed for the AND)

#2. OR   | (pipe symbol)

#3. XOR  ^ (cap symbol)

#AND

#0 0 - 0
#0 1 - 0
#1 0 - 0
#1 1 - 1

#AND only works when the two condition become true

#OR

#0 0 - 0
#1 0 - 1
#0 1 - 1
#1 1 - 1

#OR only gets true when the either one condition gets true

#XOR

#0 0 - 0
#0 1 - 1
#1 0 - 1
#1 1 - 0

#this works only when one condition gets true

#eg1
#num1=2
#num2=4

#print(num1&num2)  output : 0

#2 ==> 0 0 1 0
#4 ==> 0 1 0 0
#      0 0 0 0 ==> 0

#eg2
#num1=4
#num2=4

#print(num1&num2) output : 0

#4 ==> 0 1 0 0
#4 ==> 0 1 0 0
#      0 1 0 0 ==> 4


num1=7 #0 1 1 1
num2=6 #0 1 1 0
       #0 1 1 1 ==> 7




