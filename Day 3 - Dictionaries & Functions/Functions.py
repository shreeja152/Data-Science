#Functions
def greet_user(first_name, last_name):                     #fuction 1 with parameters
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")                                             #mandatory 2 line break after a function                              
greet_user( last_name="KS", first_name="Shreeja")          #calling the function which also has keyword argument which should always come after positional argument
#greet_user("Abc")       
print("Finish")

