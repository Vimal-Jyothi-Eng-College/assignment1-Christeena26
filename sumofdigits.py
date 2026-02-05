num=int(input("Enter the integer:"))
sumdigits=0
while num>0:
    digit=num%10
    sumdigits+=digit
    num//=10
print("Sum of digits:",sumdigits)