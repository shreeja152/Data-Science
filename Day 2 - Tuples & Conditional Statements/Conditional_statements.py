#conditional statements, while loops, lists

#conditional statements

tempretature = 25

if tempretature > 30:
    print("Its a hot day")
    print("Drink plenty of water.")
elif tempretature > 20:
    print("Its a nice day.")
elif tempretature > 10: 
    print("Its a bit cold day")
else:
    print("Its a cold day")
print("Done")

#while loops
i = 1
while i<=10:
    print(i * '*')
    i = i + 1

#lists 
names = ["Abc", "Def", "Ghi", "Jkl", "Mno"]
names[3] = "Jhi"
print(names [0])
print(names[-1])
print(names[0:3])
print(names)

#list methods
numbers = [1,2,3,4,5]
numbers.append(6)
numbers.insert(0, -1)
numbers.remove(3)
print(numbers)
print(2 in numbers)
print(len(numbers))

#for loops
num = [7,8,9,10,11,12]
for item in num :
    print(item)

