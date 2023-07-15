# Write a program which accepts a sequence of comma separated 4 digit binary numbers as
# its input and then check whether they are divisible by 5 or not. The numbers that are
# divisible by 5 are to be printed in a comma separated sequence.

numbers = input()
temp = numbers.split(",")
ans = []
for item in temp:
    number = int(item,2)
    if number%5==0:
        ans.append(item)
print(','.join(ans))


