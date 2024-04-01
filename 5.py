mushrooms = int(input())

if mushrooms % 10 == 1:
    print('мы нашли', mushrooms, 'гриб в лесу')
elif mushrooms % 10 <= 4 and mushrooms % 10 != 0:
    print('мы нашли', mushrooms, 'гриба в лесу')
else:
    print('мы нашли', mushrooms, 'грибов в лесу')