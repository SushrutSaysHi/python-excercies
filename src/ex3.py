test_string="Hello World"

print(f"Position of 'lo' in the string is {test_string.find('lo')}")

test_string=test_string.replace(" ",",")
print(f"String after replacing space with comma: {test_string}")

if test_string.startswith("H") and test_string.endswith("H"):
    print("True")
else:
    print("False")

test_string=test_string.upper()
print(f"String in uppercase: {test_string}")

print(f"Total occurences of 'O' in the string: {test_string.count('O')}")

count=0
for i in test_string:
    if i in "aeiouAEIOU":
        count+=1

print(f"Total number of vowels in the string: {count}")