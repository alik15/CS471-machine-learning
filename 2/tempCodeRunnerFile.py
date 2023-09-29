list_of_inputs= list()

while(True):
    a = str(input("Please enter a new input: "))

    for i in list_of_inputs:
        if (i>a):
            list_of_inputs.append(i)
            
        print(list_of_inputs)
            