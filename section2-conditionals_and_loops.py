# Start of if-elif-else learning

a_number = 34

if a_number % 2 == 0:
    print("We are inside an if block")
    print("The given number {} is even.".format(a_number))
else:
    print("The given number {} is odd.".format(a_number))

another_number = 33
if another_number % 2 == 0:
    print("The given number {} is even.".format(another_number))
else:
    print("The given number {} is odd.".format(another_number))

the_3_musketeers = ('Athos', 'Porthos', 'Aramis')
a_candidate = "D'Artagnan"
if a_candidate in the_3_musketeers:
    print("{} is a musketeer.".format(a_candidate))
else:
    print("{} is not a musketeer.".format(a_candidate))

today = 'Wednesday'

if today == 'Sunday':
    print("Today is the day of the sun.")
elif today == 'Monday':
    print("Today is the day of the moon.")
elif today == 'Tuesday':
    print("Today is the day of Tyr.")
elif today == 'Wednesday':
    print("Today is the day of Odin.")
elif today == 'Thursday':
    print("Today is the day of Thor.")
elif today == 'Friday':
    print("Today is the day of Frigga.")
elif today == 'Saturday':
    print("Today is the day of Saturn.")
else:
    print("This is not a day of the week.")

if []:
    print("This is an array with values in it.")
else:
    print("This is an array with no values.")

new_number = 13

if new_number % 2 == 0:
    parity = 'even'
else:
    parity = 'odd'
print("The number {} is {}.".format(new_number, parity))

# End of if-elif-else learning - video end time 10:56

# Start of while loop learning - video start time 10:57
result = 1
i = 1
while i <= 10:
    result = result * i
    i = i + 1

print("The factorial of 100 is: {}".format(result))

line = '*'
space = '      '
countingStar = ''
count = 1
max_length = 6

while count <= max_length:
    print(space + countingStar + line + countingStar + space)
    countingStar += '*'
    space = space[:-1]
    count += 1

while count > 0:
    print(space + countingStar + line + countingStar + space)
    space += ' '
    countingStar = countingStar[:-1]
    count -= 1

i = 1
result = 1
while i <= 100:
    result = result * i
    if i == 42:
        print("Magic number is 42!")
        break
    i += 1
print("While loop ended and i is: {} ".format(i))
print("While loop ended and result is: {} ".format(result))

i = 1
result = 1
while i < 20:
    i += 1
    if i % 2 == 0:
        print("Skipping {}".format(i))
        continue
    print("Multiplying with {}".format(i))
    result = result * i
print('i:', i)
print('result:', result)

# End of while loop learning - video start time 20:46
# Start of for loop learning - video start time 20:58

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for day in days:
    print(day)

for char in 'Monday':
    print(char)

person = {
    'name': "Jacob Williams",
    'sex': 'Male',
    'age': 19,
    'married': False
}

for key in person:
    print("Key: {} , Value: {}".format(key, person[key]))

for value in person.values():
    print(value)

for key_value_pair in person.items():
    print(key_value_pair)

for key, value in person.items():
    print("Key: {} , Value: {}".format(key, value))

for i in range(7):
    print(i)

print()

for i in range(3, 7):
    print(i)

print()
# start,end,step
for i in range(3, 14, 4):
    print(i)

a_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for i in range(len(a_list)):
    print("The value at position {} is {}.".format(i, a_list[i]))

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# end of for loop learning - video end time 27:45
