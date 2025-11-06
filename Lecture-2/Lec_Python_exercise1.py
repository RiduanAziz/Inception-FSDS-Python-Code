"""
Excrtise-1
Find the minimum number from 3 given number
"""
num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the second Number: "))
num3 = int(input("Enter the third Number: "))

if num1<num2 and num1<num3:
    print("Minimum Number is: ", num1)

elif num2<num1 and num2<num3:
    print("Minimum Number is: ", num2)
    
else:
    print("Minimum Number is: ", num3)

