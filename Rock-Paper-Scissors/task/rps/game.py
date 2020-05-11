import random


class RockPaperScissors:

    def __init__(self):
        self.item_list = ['paper', 'scissors', 'rock']
        self.rating_file = 'rating.txt'
        self.players_scores = {}
        self.game()

    def game(self):
        check = True
        self.user_name = input('Enter your name: ')
        print(f'Hello, {self.user_name}')
        self.check_name(self.user_name)
        words = input().strip()
        if words != '':
            self.item_list = words.split(',')
        print("Okay, let's start")
        while check:
            self.human = input()
            if self.human in self.item_list:
                self.check_game()
            elif self.human == '!exit':
                check = False
                print('Bye!')
            elif self.human == '!rating':
                print(f'Your rating: {self.players_scores[self.user_name]}')
            else:
                print("Invalid input")

    def check_game(self):
        self.cpu = random.choice(self.item_list)
        human_i = self.item_list.index(self.human)
        half = len(self.item_list) // 2
        if human_i > half:
            temp_list = self.item_list[human_i - half:] + self.item_list[:human_i - half]
        elif human_i < half:
            temp_list = self.item_list[human_i + half + 1:] + self.item_list[:human_i + half + 1]
        else:
            temp_list = self.item_list[:]
        human_i = temp_list.index(self.human)
        cpu_i = temp_list.index(self.cpu)
        if cpu_i == human_i:
            print(f'There is a draw ({self.cpu})')
            self.players_scores[self.user_name] += 50
        elif cpu_i > human_i:
            print(f'Sorry, but computer chose {self.cpu}')
        elif cpu_i < human_i:
            print(f'Well done. Computer chose {self.cpu} and failed')
            self.players_scores[self.user_name] += 100

    def check_name(self, name):
        try:
            with open(self.rating_file, 'r', encoding='utf-8') as file:
                for line in file.readlines():
                    a = line.strip().split()
                    self.players_scores[a[0]] = int(a[1])
        except FileNotFoundError:
            with open(self.rating_file, 'w', encoding='utf-8') as file:
                file.write('')
        with open(self.rating_file, 'r') as file:
            for line in file.readlines():
                a = line.strip().split()
                self.players_scores[a[0]] = int(a[1])
        if self.players_scores.get(name) is None:
            self.players_scores[name] = 0


RockPaperScissors()
