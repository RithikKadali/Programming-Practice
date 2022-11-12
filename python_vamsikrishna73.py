number = int(input("enter an integer"))
binaryNumber = ''
while number>0:
    binaryNumber += str(number%2)
    number //= 2
print("the integer in binary form is",binaryNumber[::-1])