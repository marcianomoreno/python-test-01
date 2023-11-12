import datetime

name = input('What is your name?\n')
print('Hi, %s.' % name)

age = input('What is your age?\n')
# get current year
year = datetime.datetime.now().year

year_born = year - int(age)
print('You were born in %d.' % year_born)


print("Ciao!")
exit()
