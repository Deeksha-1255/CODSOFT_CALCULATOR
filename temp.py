#PROGRAM FOR A SIMPLE CALCULATOR USING PYTHON

print("SELECT THE OPERATION TO PERFORM:")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
operation = input()
if (operation == "1"):
    num1 = input("ENTER THE FIRST NUMBER:")
    num2 = input("ENTER THE SECOND NUMBER:")
    print("THE SUM IS:" + str(int(num1) + int(num2)))
elif (operation == "2"):
    num1 = input("ENTER THE FIRST NUMBER:")
    num2 = input("ENTER THE SECOND NUMBER:")
    print("THE DIFFERENCE IS:" + str(int(num1) - int(num2)))
elif (operation == "3"):
    num1 = input("ENTER THE FIRST NUMBER:")
    num2 = input("ENTER THE SECOND NUMBER:")
    print("THE PRODUCT IS:" + str(int(num1) * int(num2)))
elif (operation == "4"):
    num1 = input("ENTER THE FIRST NUMBER:")
    num2 = input("ENTER THE SECOND NUMBER:")
    print("THE RESULT IS:" + str(int(num1) / int(num2)))
else:
    print("INVALID ENTRY")