def factorial(num):
   
   sum = 1  
   while (num > 0):
       sum = sum * num
       num = num - 1
       
   return sum


print(f"the factorial of 3 is {factorial(3)}")