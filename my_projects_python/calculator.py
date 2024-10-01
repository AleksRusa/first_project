from math import *

while True:
    x = int(input())
    y = int(input())
    com = input('напишите команду -> ')
    try:
        print(eval(com))
        break
    except Exception as ex:
        print(ex)
        continue