str1= input("first string: ")
str2= input("second string: ")
str3= input("third string: ")


count = 0
for i in str1: 
    count = count + 1
    print(i)
    
for j in str2:
    count = count + 1
    print(j)
    
    
for k in str3:
    print(k)
    count = count+1
    
print("total length of all the strings is: ", count)