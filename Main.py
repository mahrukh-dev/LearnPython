import math

msg = "hello"
print(msg)
print(math.floor(3.65))
print(math.cos(3.6))
print(type(msg))
print(msg.capitalize())
print(msg.find("e"))
print(msg.upper()) ##print in uppercase
print(msg.lower()) ##print in lowercase

items = [1,2,3, "mah"] ##list in python
print(items)
print(type(items))
items[0] = 5
items[1] = "hello"

tup1 = (1,2,3) ##tuple in python
##cannot change value in tuple

dict1 = {} ##dictionary in python
print(type(dict1))
print(dict1)
dict1["key"] = 1
print(dict1.get("key"))
print(dict1.items())
print(dict1.keys())

list1 = [1,2,3,4,4,2]
s1 = set(list1) ##set doesnt contain repeated values

##conditional statements

var = int(input())
print(var)

if (var>4):
    print("var is greater")
elif(var==4):
    print("var is 4")
else:
    print("var is not greater")

##loops

for i in range(5,10):
    print(i)

i=0
while(i<4):
    print(i)
    i=i+1

##function
def avrg(num1,num2):
    avr = (num1+num2)/2
    return avr

print(avrg(5,15))

##exception handling
try:
    print(index)
except Exception as e:
    print(e)


##file handling
f = open("new.txt", "w")
f.write("learning python")
f.close()
f1=open("new.txt", "r")
content = f1.read()
f1.close()
print(content)
