                      # Using FOR loop------



num=int(input("Enter a number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial(using for loop):",fact)




                        # Using While loop-----

num=int(input("Enter a number:"))
fact=1
i=1
while i<=num:
    fact=fact*i
    i+=1
print("Factorial(using while loop):",fact)