total18 = totalFemale20 = totalMale = 0
while True:
    age = int(input('How old are you? '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('What is your sex (M/F): ')).strip().upper()[0]
    if age >= 18:
        total18 += 1
    if sex == 'M':
        totalMale += 1
    if sex == 'F' and age < 20:
        totalFemale20 += 1
    responce = ' '
    while responce not in 'YN':
        responce = str(input('Do you want to continue?(Y/N) ')).strip().upper()[0]
    if responce == 'N':
        break
print(f'There are {total18} people with more than 18 years old')
print(f'There are {totalMale} male registered')
print(f'There are {totalFemale20} female with less than 20 years old')
