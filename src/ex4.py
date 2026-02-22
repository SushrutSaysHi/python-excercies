my_tuple=(10,15,20,25,30,35,40,45)

sum=0
prod=1
for i in my_tuple:
    if i%2==0:
        sum+=i
    else:
        prod*=i

print(f"Sum of all even numbers are is: {sum}")
print(f"Product of all odd numbers is: {prod}")