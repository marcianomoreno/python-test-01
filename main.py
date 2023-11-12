import datetime

name = input('What is your name?\n')
print('Hi, %s.' % name)

age = input('What is your age?\n')
# get current year
year = datetime.datetime.now().year

year_born = year - int(age)
print('You were born in %d.' % year_born)

beverage = input('What is your favorite beverage?\n')
beverage = beverage.lower()
print(f'I like {beverage} too!')

food = input('What is your favorite food?\n')
food = food.lower()
print(f'Great, I like {food} as well!')

print("Ciao!")
exit()
