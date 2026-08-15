num=int(input("Enter a number:"))
num_str=str(num)
power=len(num_str)
total=sum(int(digit)**power for digit in num_str)
if total==num:
    print(num,"is an Armstrong Number")
else:
    print(num,"is not an Armstrong Number")