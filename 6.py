appartaments = int(input())
number = int(input())
if (number % 4 == 0) or (number % 2 != 0 and appartaments % 2!= 0):
    print('сумма четная')
else:
    print('сумма нечетная')