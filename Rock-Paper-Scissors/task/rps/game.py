import random


class RockPaperScissors:

    def __init__(self):
        self.win_combinations = {'scissors': 'paper', 'paper': 'rock', 'rock': 'scissors'}
        self.item_list = ['scissors', 'rock', 'paper']
        self.rating_file = 'rating.txt'
        self.players_scores = {}
        self.game()

    def game(self):
        check = True
        self.user_name = input('Enter your name: ')
        print(f'Hello, {self.user_name}')
        self.check_name(self.user_name)
        while check:
            self.human = input()
            if self.human in self.item_list:
                self.check_game()
            elif self.human == '!exit':
                check = False
                print('Bye!')
            elif self.human == '!rating':
                print(f'Your rating: {self.players_scores[self.user_name]}')
            else: print("Invalid input")

    def check_game(self):
        self.cpu = random.choice(self.item_list)
        if self.human == self.cpu:
            print(f'There is a draw ({self.cpu})')
            self.players_scores[self.user_name] += 50
        elif self.win_combinations[self.human] == self.cpu:
            print(f'Well done. Computer chose {self.cpu} and failed')
            self.players_scores[self.user_name] += 100
        else: print(f'Sorry, but computer chose {self.cpu}')

    def check_name(self, name):
        with open(self.rating_file, 'r') as file:
            for line in file.readlines():
                a = line.strip().split()
                self.players_scores[a[0]] = int(a[1])
        if self.players_scores.get(name) is None:
            self.players_scores[name] = 0


RockPaperScissors()
