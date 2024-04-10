#Variables,inputs,type conversion,Strings,Operators in Python

#Variables
name = "Shreeja"
age = 21
new_patient = True
print(name  ,"is" , age , "year old new patient or not? "  , new_patient)

#input
name = input("What's your name?")
print("Hello " , name)

#Type conversion
year_of_birth = input("Please enter your year of birth: ")
current_age = 2024 - int(year_of_birth)
print("Age : " , current_age )

#Strings
language = "Code in Python Language"
print(language.upper())
print(language.find('t'))
print(language.replace('in','2'))
print(language)

#Arithmetic Operations
x=10
print(x + 3)           #Addition
print(x - 3)           #Subtrction
print(x * 3)           #Multiplication
print(x / 3)           #Divion
print(x % 3)           #Percentage
print(x ** 3)          #Power

#Comparion Operators
print(5>2 )               #Greater than
print(5<2)                #lesser than
print(5>=2)               #Greater than or equal to
print(5<=2)               #Lesser than or equal to
print(5==2)               #Equality operator
print(5!=2)               #Not eqaulity operator

#Logical Operstors
age = 25
print("Logical Operators")
print(age > 10 and age <30)       #and (both)
print(age > 10 or age <30)        #or (at least one)
print(not age >10 )               #not (inverses the value)
