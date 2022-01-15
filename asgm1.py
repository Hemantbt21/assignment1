#ques1
x=input("enter first number:")
y=input("enter second number:")
z=input("enter third number:")
avg=(int(x)+int(y)+int(z))/3
print("The average of three numbers is:",avg)

#ques2
x=float(input("Enter your Gross income:"))
y=int(input("Enter number of dependents:"))
a=(x-10000-(3000*y))
b=a*0.2
print("income tax is:",b)

#ques3
x=[enter sid,"km","m","Electrical Engineering",10]
print(x)

#ques4
x=[88,79,89,78,69]
x.sort()
print(x)

#ques5a
x=['Red','Green','White','Black','Pink','Yellow']
x.pop(3)
print(x)

#ques5b
x=['Red','Green','White','Black','Pink','Yellow']
del x[3:5]
x.insert(3,'Purple')
print(x)
