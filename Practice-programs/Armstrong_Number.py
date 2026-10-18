print("//  Adarsh Gour  //")
n=int(input("Enter number: "))
temp=n
sum=0
while n!=0:
    rem=n%10
    sum=sum+rem**3
    n=n//10

if sum==temp:
    print("Armstrong")
else:
    print("Not Armstrong")

print("//  Adarsh Gour  //")