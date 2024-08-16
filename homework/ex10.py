# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0
number=""
for j in range(5):
    numbers=input("Enter number:")
    number+=str(numbers)
    max_number=number
    min_number=number
    for j in range(len(number)):
        if number[j]>max_number:
            max_number=number[j]
        elif number[j]<min_number:
            min_number=number[j]
print("max number:",max_number)
print("min number:",min_number)