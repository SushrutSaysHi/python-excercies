numbers=[]

for item in range(2000, 3201):
    if item%7==0 and item%5!=0:
        print(f'{item} is divisible by seven and not multiple of 5')
        numbers.append(str(item))

