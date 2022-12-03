#XOX
import random
space = '   '
numbers = {'one': space, 'two': space, 'three': space, 'four': space, 'five': space, 'six': space, 'seven': space, 'eight': space, 'nine': space}
x = ' X '
o = ' O '
user_choice, comp_choice = None, None
rand = None
prompt_begin = None
entry = None
gameState = None
result = None
gamePlay1 = ['computer', 'user', 'computer', 'user', 'computer', 'user', 'computer', 'user', 'computer']
gamePlay2 = ['user', 'computer', 'user', 'computer', 'user', 'computer', 'user', 'computer', 'user']
choice_l = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
print()
print('Position template of XOX:-')
print('[1]', '|', '[2]', '|', '[3]')
print('[4]', '|', '[5]', '|', '[6]')
print('[7]', '|', '[8]', '|', '[9]')


#Commencement
print()
i = str(input("Who's first? - (user/computer)"))
if i == 'user':
    gameState = 'user'
    prompt_begin = str(input("X or O"))
    position_begin = str(input("Which position?(one, two, three, four, five, six, seven, eight, nine)"))
    for j in choice_l:
        if j == position_begin:
            entry = position_begin
        else:
            continue
    for j in numbers:
        if j == position_begin:
            if prompt_begin == 'X' or prompt_begin == 'x':
                numbers[position_begin] = x
                user_choice = x
                comp_choice = o
            elif prompt_begin == 'O' or prompt_begin == 'o':
                numbers[position_begin] = o
                user_choice = o
                comp_choice = x
            print(numbers['one'], '|', numbers['two'], '|', numbers['three'],)
            print(numbers['four'], '|', numbers['five'], '|', numbers['six'],)
            print(numbers['seven'], '|', numbers['eight'], '|', numbers['nine'],)
        else:
            continue
    numbers[position_begin] = user_choice
    choice_l.remove(entry)
if i == 'computer':
    gameState = 'computer'
    rand = random.choice(choice_l)
    entry = rand
    prompt_begin = random.choice(['X', 'O'])
    if prompt_begin == 'X':
        numbers[rand] = x
        comp_choice = x
        user_choice = o
    elif prompt_begin == 'O':
        numbers[rand] = o
        comp_choice = o
        user_choice = x
    print('......................................')
    print('...The computer\'s choice is', entry, '...')
    print('......................................')
    print()
    print(numbers['one'], '|', numbers['two'], '|', numbers['three'],)
    print(numbers['four'], '|', numbers['five'], '|', numbers['six'],)
    print(numbers['seven'], '|', numbers['eight'], '|', numbers['nine'],)
    numbers[rand] = comp_choice
    choice_l.remove(entry)


#Proceding further
if gameState == 'user':
    for state in gamePlay1:
        if ((numbers['one'] == numbers['two']) and (numbers['two'] == numbers['three']) and (
                numbers['one'] != space) and (numbers['two'] != space) and (numbers['three'] != space)):
            result = 'Positive'
        elif ((numbers['one'] == numbers['four']) and (numbers['four'] == numbers['seven']) and (
                numbers['one'] != space) and (numbers['four'] != space) and (numbers['seven'] != space)):
            result = 'Positive'
        elif ((numbers['one'] == numbers['five']) and (numbers['five'] == numbers['nine']) and (
                numbers['one'] != space) and (numbers['five'] != space) and (numbers['nine'] != space)):
            result = 'Positive'
        elif ((numbers['two'] == numbers['five']) and (numbers['five'] == numbers['eight']) and (
                numbers['two'] != space) and (numbers['five'] != space) and (numbers['eight'] != space)):
            result = 'Positive'
        elif ((numbers['three'] == numbers['six']) and (numbers['six'] == numbers['nine']) and (
                numbers['three'] != space) and (numbers['six'] != space) and (numbers['nine'] != space)):
            result = 'Positive'
        elif ((numbers['four'] == numbers['five']) and (numbers['five'] == numbers['six']) and (
                numbers['four'] != space) and (numbers['five'] != space) and (numbers['six'] != space)):
            result = 'Positive'
        elif ((numbers['seven'] == numbers['eight']) and (numbers['eight'] == numbers['nine']) and (
                numbers['seven'] != space) and (numbers['eight'] != space) and (numbers['nine'] != space)):
            result = 'Positive'
        elif ((numbers['seven'] == numbers['five']) and (numbers['five'] == numbers['three']) and (
                numbers['seven'] != space) and (numbers['five'] != space) and (numbers['three'] != space)):
            result = 'Positive'

        if result == 'Positive':
            print()
            print('You Wins!')
            gameState = 'end'
            break
        if state == 'computer':
            rand = random.choice(choice_l)
            entry = rand
            numbers[rand] = comp_choice
            print('......................................')
            print('...The computer\'s choice is', entry, '...')
            print('......................................')
            print(numbers['one'], '|', numbers['two'], '|', numbers['three'], )
            print(numbers['four'], '|', numbers['five'], '|', numbers['six'], )
            print(numbers['seven'], '|', numbers['eight'], '|', numbers['nine'], )
            numbers[rand] = comp_choice
            choice_l.remove(entry)
        if state == 'user':
            print('Available positions', choice_l)
            position_begin = str(input("Which position?"))
            if position_begin in choice_l:
                for j in choice_l:
                    if j == position_begin:
                        entry = position_begin
                    else:
                        continue
                for j in numbers:
                    if j == position_begin:
                        numbers[position_begin] = user_choice
                        print(numbers['one'], '|', numbers['two'], '|', numbers['three'], )
                        print(numbers['four'], '|', numbers['five'], '|', numbers['six'], )
                        print(numbers['seven'], '|', numbers['eight'], '|', numbers['nine'], )
                    else:
                        continue
                if result == 'Positive':
                    print('You Win!')
                    gameState = 'end'
                    break
                numbers[position_begin] = user_choice
                choice_l.remove(entry)
if gameState == 'computer':
    for state in gamePlay2:
        if ((numbers['one'] == numbers['two']) and (numbers['two'] == numbers['three']) and (numbers['one'] != space) and (numbers['two'] != space) and (numbers['three'] != space)):
            result = 'Positive'
        elif ((numbers['one'] == numbers['four']) and (numbers['four'] == numbers['seven']) and (numbers['one'] != space) and (numbers['four'] != space) and (numbers['seven'] != space)):
            result = 'Positive'
        elif ((numbers['one'] == numbers['five']) and (numbers['five'] == numbers['nine']) and (numbers['one'] != space) and (numbers['five'] != space) and (numbers['nine'] != space)):
            result = 'Positive'
        elif ((numbers['two'] == numbers['five']) and (numbers['five'] == numbers['eight']) and (numbers['two'] != space) and (numbers['five'] != space) and (numbers['eight'] != space)):
            result = 'Positive'
        elif ((numbers['three'] == numbers['six']) and (numbers['six'] == numbers['nine']) and (numbers['three'] != space) and (numbers['six'] != space) and (numbers['nine'] != space)):
            result = 'Positive'
        elif ((numbers['four'] == numbers['five']) and (numbers['five'] == numbers['six']) and (numbers['four'] != space) and (numbers['five'] != space) and (numbers['six'] != space)):
            result = 'Positive'
        elif ((numbers['seven'] == numbers['eight']) and (numbers['eight'] == numbers['nine']) and (numbers['seven'] != space) and (numbers['eight'] != space) and (numbers['nine'] != space)):
            result = 'Positive'
        elif ((numbers['seven'] == numbers['five']) and (numbers['five'] == numbers['three']) and (numbers['seven'] != space) and (numbers['five'] != space) and (numbers['three'] != space)):
            result = 'Positive'

        if result == 'Positive':
            print('Computer Wins!')
            gameState = 'end'
            break
        if state == 'computer':
            rand = random.choice(choice_l)
            entry = rand
            numbers[rand] = comp_choice
            print('......................................')
            print('...The computer\'s choice is', entry, '...')
            print('......................................')
            print(numbers['one'], '|', numbers['two'], '|', numbers['three'], )
            print(numbers['four'], '|', numbers['five'], '|', numbers['six'], )
            print(numbers['seven'], '|', numbers['eight'], '|', numbers['nine'], )

            if result == 'Positive':
                print('Computer Wins!')
                gameState = 'end'
                break
            numbers[rand] = comp_choice
            choice_l.remove(entry)
        if state == 'user':
            print('Available positions', choice_l)
            position_begin = str(input("Which position?"))
            if position_begin in choice_l:
                for j in choice_l:
                    if j == position_begin:
                        entry = position_begin
                    else:
                        continue
                for j in numbers:
                    if j == position_begin:
                        numbers[position_begin] = user_choice
                        print(numbers['one'], '|', numbers['two'], '|', numbers['three'], )
                        print(numbers['four'], '|', numbers['five'], '|', numbers['six'], )
                        print(numbers['seven'], '|', numbers['eight'], '|', numbers['nine'], )
                    else:
                        continue
                if result == 'Positive':
                    print('User Win!')
                    gameState = 'end'
                    break
                numbers[position_begin] = user_choice
                choice_l.remove(entry)
