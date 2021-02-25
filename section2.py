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
max_length = 6

while len(line) <= max_length:
    print(line)
    line += '*'

while len(line) > 0:
    print(line)
    line = line[:-1]
