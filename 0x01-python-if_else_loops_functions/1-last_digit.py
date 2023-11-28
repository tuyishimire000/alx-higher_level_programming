#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
def get_digit(num):
    num_str=str(num)
    digit=int(num_str[len(num_str)-1])
    return digit
dig=get_digit(number)
if dig>5:
    print('Last digit of'+number+'is'+dig+'and is greater than 5')
elif dig==0:
    print('Last digit of'+number+'is'+dig+'and is 0')
elif dig<6 and (dig!=0):
    print('Last digit of'+number+'is'+dig+'and is less than 6 and not 0')


