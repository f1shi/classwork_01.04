years = int(input())

if years % 10 == 1:
    print('мне', years, 'год')
elif years % 10 <= 4 and years % 10 != 0:
    print('мне', years, 'года')
else:
    print('мне', years, 'лет')