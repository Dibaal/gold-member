var = [] #Most of the time we are talking about list

print(type(var))

var2 = [251, 386, 493]

print(var2)

var3 = [251, 386, 493, "009"]

var3.append(649) # inplace function bc it auto saves the new function name as the previous one var3
var3 = var3 + [721] # Not an inplace function bc we have to save it

print(var3)

print(dir(var3)) #hidden gem

var3.reverse()

print(var3)

numbers = [1, 2, 3, 4, 5]

print(numbers)

r = range(0,20) # To print from 1 to 101. It's arange type. We can typecasting with this. See below

print(r)

print(list(r))

#iterating through a list. see below

for number in numbers:
    print(number*2) # this is common in aws. We'll in next class, a little bit below:

    
for i in range(0,10):         # This means for i in arange of 0 to 10 something 10times
    print(i)

    print(var3)
    print(var3[1]) # With brackets [] we can access some elements in a list
    
    print(len(var3)) 
    
    for i in range(len(var3)):
        print(var3[i]) #This is a way to access each and every element in var3 and get them printed out
        
    # WE CAN HAVE A LIST IN A LIST
    
    ### DON'T LOOK AT THIS CODE
    
    list_of_list = [[random.randint(0,10) for j in range(5)] for i in range(5)] # List comprihension
    
    ### YOU CAN LOOK AGAIN
    
    print(list_of_list)
    
    for i in list_of_list: #didn't use the variable name list because its a keyword
        print(list_of_list[i])
        for j in  range(len(list_of_list[i])):
            print(list_of_list[i][j])
        






