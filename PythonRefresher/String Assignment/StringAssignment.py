'''
String Assignment we will do together:

Ask the user how many days until their birthday
and print an approx number of weeks until their birthday

Weeks is = 7 days

decimals within the return is allowed..
'''

first_name = input("Enter your first name: ") # assigns input to first_name
print(first_name)

days = int(input("How many days until your birthday? "))

print(f"Hi {first_name}, only {days} days until your birthday!")

weeks = (round(days/7, 2)) # rounds to 2 decimal places

print(f"Hi {first_name}, only {weeks} weeks until your birthday!")

sentence = "Hi {}, only {} weeks until your birthday!"

print(sentence.format(first_name, weeks))