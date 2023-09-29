def mul(num1, num2):
    while(num2>0):
        sum = int()
        
        while(num2>0):
            sum = sum + num1
            num2 = num2 - 1 
            
    return sum             

num1 = 5
num2 = 6

print(f"multiplying {num1} and {num2} results in {mul(num1,num2)}")
