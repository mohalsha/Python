

i = int(input("Please enter the number to be checked.  "))

n=1
while n <= i:
    for number in range(2,n):
        if n % number == 0:
            break
        else:
            print(number)
n = n + 1

    

