number = int(input("Enter a number: "))
copy=number
reversed_number=0
while number>0:
    n=number%10
    d=number//10
    reversed_number=reversed_number*10+n
    number=d
if copy==reversed_number:
    print(f"{copy} is a palindrome number.")
else:
    print(f"{copy} is not a palindrome number.")
