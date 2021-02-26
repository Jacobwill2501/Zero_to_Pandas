# Start of function learning - video start time 28:58

def say_hello():
    print("Hello There!")
    print("How are you?")


say_hello()


def filter_even(number_list):
    result_list = []
    for number in number_list:
        if number % 2 == 0:
            result_list.append(number)
    return result_list


print(filter_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))


def say_hello(name):
    print("Hello there {}!".format(name))
    

say_hello("Ashley")
