input_1 = float(input("First Number:"))
operation = input("Operation?")
input_2 = float(input("Second Number:"))

if operation == "*":
    print(input_1 * input_2)
elif operation ==  "/":
    print(input_1 / input_2)
elif operation == "+":
    print(input_1 + input_2)
elif operation == "-":
    print(input_1 - input_2)
else:
    print("Please use operations *,/,+,-.")