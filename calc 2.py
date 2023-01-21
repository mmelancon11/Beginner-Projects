i = 1
while i == 1:
    input_1 = (input("First Number: "))
    if input_1 == "end":
        i = i + 1
    else:
        operation = input("Operation: ")
        input_2 = float(input("Second Number: "))

        if operation == "*":
            print(float(input_1) * input_2)
        elif operation == "/":
            print(float(input_1) / input_2)
        elif operation == "+":
            print(float(input_1) + input_2)
        elif operation == "-":
            print(float(input_1) - input_2)
        else:
            print("Please use operations *,/,+,-.")