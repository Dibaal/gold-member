import random #Imported this random file

number = random.randint(0,10)

print(number) #this random nmbers are inconsistent if included or ecluded

thresh = 6

if(number>thresh):
    print("Big number") # The this print output keeps changing bc it depends on the print(number) output. If > 6 then it'll print big number
elif(number<thresh): #Connects the 2 blocks togethe
    print("Small number") # This case if number is less than threshold 6 it'll print small number
else:  #elif(number==6). Note = is for assigning values while == is for comparism
    print("Number is", str(thresh))
    
# When dealing with decision block we do not want to hard code values in our print statements, that's why is better to use variables like threshold here

    
    
    
