integers=[4,5,6,7,8,9,10,11,12]

integers.append(15)
integers.insert(2,3)
integers.sort(reverse=True)

print(f"Sorted integers in descending order: {integers}")

print(f"Index of 9 is: {integers.index(9)}")

count=0
primes=[]
composites=[]
#prime number printing
for i in integers:
    for j in range(1, i+1):
        if (i % j) == 0:
            count += 1
    if count == 2:
        primes.append(i)
    else:
        composites.append(i)
    count = 0

print(f"Prime numbers: {primes}")
print(f"Composite numbers: {composites}")