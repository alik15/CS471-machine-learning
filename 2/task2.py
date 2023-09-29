list_of_inputs= [0]

while True:
    a = input("Please enter a new input (or 'done' to finish): ")

    if a == "done":
        break

    inp = int(a)

    if not list_of_inputs or inp > list_of_inputs[-1]:
        list_of_inputs.append(inp)
    else:
        for index, value in enumerate(list_of_inputs):
            if inp <= value:
                list_of_inputs.insert(index, inp)
                break

    print(list_of_inputs)

            