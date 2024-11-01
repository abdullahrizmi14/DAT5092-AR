u_num = int(input('Input a number'))

i = 2
count = 0

while i <= 10:
    if u_num % i == 0:
        print(i)
        i += 1
        count += 1
    else:
        i += 1


if count == 0:
    print("Prime number")