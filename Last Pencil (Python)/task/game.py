import random
pencil = []
names = ['Jack', 'John']
index = 0
size_pencil = 0
def pencil_generator(num):
    global pencil
    for i in range(num):
        pencil.append('|')
    print(f'{"".join(pencil)}')
def bot_pencil_generator(num):
    global pencil
    for i in range(num):
        pencil.append('|')
    print(f'{"".join(pencil)}')
    print(f"{names[index]}'s turn:")
    bot_player()
def pencil_deductor(num_deductor):
    for i in range(num_deductor):
        if len(pencil) != 0:
            pencil.pop()
def player(num_deductor):
    global pencil, index
    if len(pencil) <= 0:
        return -1
    if len(pencil) < num_deductor:
        print('Too many pencils were taken')
        return -1
    pencil_deductor(num_deductor)
    print(f'{"".join(pencil)}')
    if index == 0:
        index = 1
    else:
        index = 0
    if len(pencil) != 0:
            print(f"{names[index]}'s turn:")
def bot_player():
    global index
    losing_bot = [5,9,13,17]  # bot takes number between 1 2 or  3
    winning_bot_1 = [4,8,12,16]  # bot takes 3 pencils
    winning_bot_2 = [3,7,11,15]  # bot takes 2 pencils
    winning_bot_3 = [2,6,10,14]  # bot takes 1 pencil
    losing_random_num = random.randint(1,3)
    num_random = random.randint(1,3)
    print_chosen_number = 0
    size = len(pencil)
    if size != 0:
        if size == 1:
            pencil.pop()
            print(1)
        elif isInSequence_5(size):
            pencil_deductor(losing_random_num)
            print_chosen_number = losing_random_num
        elif isInSequence_4(size):
            pencil_deductor(3)
            print_chosen_number = 3
        elif isInSequence_3(size):
            pencil_deductor(2)
            print_chosen_number = 2
        elif isInSequence_2(size):
            pencil_deductor(1)
            print_chosen_number = 1
        else:
            pencil_deductor(num_random)
            print_chosen_number = num_random
            
        if index == 0:
            index = 1
        else:
            index = 0
        if len(pencil) != 0:
            print(f'{print_chosen_number} ')
            print(f'{"".join(pencil)}')
            print(f"{names[index]}'s turn:")
        
def first_p():
    global index
    print('How many pencils would you like to use:')
    
    while True:
        num = input()
        if not num.isdigit():
            print('The number of pencils should be numeric')
            continue
        elif int(num) <= 0:
            print('The number of pencils should be positive')
            continue
        else:
            break
    print('Who will be the first (John, Jack):')
    while True:
        name = input().capitalize()
        if  name not in names:
            print("Choose between 'John' and 'Jack'")
            continue
        else:
            break
    if name == 'Jack':
        index = names.index(name)
        bot_pencil_generator(int(num))
    else:
        pencil_generator(int(num))
        print(f"{name}'s turn:")
        index = names.index(name)
def play():
    first_p()
    end_game = True
    while end_game:
        if len(pencil) == 0:
            end_game = False
            break
        if names[index] == 'John':
            number = input()
            if not number.isdigit():
                print("Possible values: '1', '2' or '3'")
                continue
            holder = int(number)
            if holder == 0 or holder > 3:
                print("Possible values: '1', '2' or '3'")
                continue
            player(holder)
        else:
            bot_player()
        if len(pencil) == 0:
            print(f"{names[index]} won!")
def isInSequence_5(x):
  return x >= 5 and (x - 1) % 4 == 0;
def isInSequence_4(x):
    return x >= 4 and x % 4 == 0;
def isInSequence_3(x):
  return x >= 3 and (x + 1) % 4 == 0;
def isInSequence_2(x): 
  return x >= 2 and (x + 2) % 4 == 0;
play()