seconds = int(input())
hours = seconds // 3600
seconds -= hours * 3600
minutes = seconds // 60
seconds -= minutes * 60
print('часов:',hours,'\nминут:', minutes,'\nсекунд:', seconds)

