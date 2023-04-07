import random # random is a library
# 2 types of repetitin in python - the while and for loop
numbers = list(range(0,10)) #For is used when we are going to do something in a fixed number of times

print(numbers)

for number in numbers: #iterate over list
    print(number*2)
    
for i in range(0,5): #do something fixed number of times
    print("This is from a for loop", str(i))
# For while loop we are going to do something while a condition is true

number = random.randint(0, 100)

counter = 0
while  number != 52:
    print(number)
    number = random.randint(0, 100)
    counter += 1
    
print(counter, number)
#for while we want to do somwthing until a condition is fals, if we do not change something we'll enter an infinite loop. 


#DEEP END

#doing while loop stuff with "for loop" (bad)
for i in range(1000):
    number = random.randint(0, 100)
    if(number == 52):
        break

print(i, number)

# doing for loop stuff with while loop(bad)
i = 0
while i < 5:
    print("This is from a for loop", str(i))
    i += 1



