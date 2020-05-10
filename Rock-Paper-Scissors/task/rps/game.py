import random

win_table = {'scissors': {'scissors': 'draw', 'rock': 'lose', 'paper': 'win'},
        'rock'         : {'scissors': 'win', 'rock': 'draw', 'paper': 'lose'},
        'paper'        : {'scissors': 'lose', 'rock': 'lose', 'paper': 'draw'}}
item_list = ['scissors', 'rock', 'paper']
a = input()
b = random.choice(item_list)
result = win_table[a][b]
if result == 'draw':
    print(f'There is a draw ({b})')
elif result == 'win':
    print(f'Well done. Computer chose {b} and failed')
elif result == 'lose':
    print(f'Sorry, but computer chose {b}')
