from random import randint

def is_valid(num, n):
    if num.isdigit() and 1<=int(num)<=n:
        return True
    else:
        return False
    
def print_number(n):
    print(f'print number in range (1 - {n}):', end=' ')
    while True:
        num = input()
        if is_valid(num, n):
            return int(num)
        else:
            print(f'number {num} is not correct')

def hint(num, number):
    if num > number:
        print(f'{num} is greater then hidden number')
    else:
        print(f'{num} is less then hidden number')

def next():
    while True:
        print('Yes -> continue/No -> stop:', end=' ')
        answer = input()
            #print('well played, Goodbye')
        if answer.isalpha() and answer.lower() == 'yes':
            return True
        elif answer.isalpha() and answer.lower() == 'no':
            return False
        
        
def game(n):
    number = randint(1, n)
    counter = 0
    while True:
        num = print_number(n)
        if num != number:
            hint(num, number)
            counter += 1
        else:
            print(f'you guess right by {counter+1} attemps')
            break
           


print("Hello player")
n = 0
while True:
    n += 100
    game(n)
    print('Do you want to continue?')
    if not next():
        print("Good game, goodbye")
        break
        


