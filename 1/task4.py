first_num = int(input("enter first number: "))
second_num = int(input("enter second number: "))

if((first_num<0) and (second_num < 0)):
    print("both numbers are less than zer0") 
    
if((first_num==0) and (second_num == 0)):
    print("both numbers are equal to zero")
    
    
if((first_num==0) or (second_num == 0)):
    print("at least one of the number is equal to zero")

if((first_num<0)or (second_num<0)) and ((second_num>0) or (first_num>0)):
    print("one number is positive and the other number is negative")


else:
    print("numbers are positive")