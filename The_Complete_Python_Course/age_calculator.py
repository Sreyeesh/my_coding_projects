name = input('what is your name ? ')

birth_year = input('what year were your born? ')
year = 2021

current_month = input('please enter current month i.e. (aug): ')
birth_month = input('please input the  month were you born i.e. (feb): ')

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
# here we are going through  a list of months. since jan is 0 we have add one so that when we iterate through a list it starts off as january being the first month of the year


if birth_month not in months:
    print('the month is entered incorrectly')

current_month_value = months.index(current_month) + 1
# print(current_month_value)
birth_month_value = months.index(birth_month) + 1
# print(birth_month_value)

age = year - int(birth_year)

if current_month_value < birth_month_value:
    age = age -1
    newage = age + 1
    newage_nextyear = age + 2
else :
    age = age -1
    newage = age
    newage_nextyear = age + 2


print(
    f'Hello, {name} you were born in the month of {birth_month} in  the year {birth_year}, '
    f'your age is: {age},In the next couple of  months you will be {newAge}. '
    f'Next year you will be {newage_nextyear}')
