import random


class RockPaperScissors:

    def __init__(self):
        self.win_combinations = {'scissors': 'paper', 'paper': 'rock', 'rock': 'scissors'}
        self.item_list = ['scissors', 'rock', 'paper']
        self.game()

    def game(self):
        check = True
        while check:
            self.human = input()
            if self.human in self.item_list:
                self.cpu = random.choice(self.item_list)
                if self.human == self.cpu: print(f'There is a draw ({self.cpu})')
                elif self.win_combinations[self.human] == self.cpu:
                    print(f'Well done. Computer chose {self.cpu} and failed')
                else: print(f'Sorry, but computer chose {self.cpu}')
            elif self.human == '!exit':
                check = False
                print('Bye!')
            else: print("Invalid input")


RockPaperScissors()
