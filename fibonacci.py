n=int(input("Enter the value:"))
a=0
b=1
Sum=0
count=1
print("Fibonacci series is:",end=" ")
while count<=n:
    print(Sum,end=" ")
    count+=1
    a=b
    b=Sum
    Sum=a+b
