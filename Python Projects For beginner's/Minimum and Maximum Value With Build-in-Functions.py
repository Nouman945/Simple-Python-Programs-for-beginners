
# Creating A list 
li = []

#Inserting Values In the List
while True:
    num = int(input("Enter a Number"))
    if num == 100:
        break
    else:
        #Adding items in the list
        li.append(num)
        
#printing full input list
print('list is',li)

#Funtion to Find the Minimum Value In  the List
def Minimum(li):
    lst = li
    x = lst[0]
    for i in lst:
        if i < x:
            x = i
    print("Minimum Value In the List is", x)
#Funtion to Find the Maximum Value In  the List
def Maximum(li):
    lst = li
    y = lst[0]
    for i in lst:
        if i > y:
            y = i
    print("Maximum Value In the List is", y)

#Calling the Functions
Minimum(li)
Maximum(li)
