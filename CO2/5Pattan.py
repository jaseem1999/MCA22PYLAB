#Display the given pyramid with step number accepted from user.
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()
