"""
day 2
puzzle part 1
"""



class Game(object):


    def __init__(self, line):
        self.id = None
        self.draws = None
        self.num_draws = None

        self.parse(line)


    def parse(self, line):
        id_part, game_part = line.split(':')

        self.id = int(id_part[5:])

        draws = game_part.split(';')

        self.num_draws = len(draws)
        empty = [0] * self.num_draws

        self.draws = {'red' : empty,
                      'green' : empty.copy(),
                      'blue' : empty.copy()}

        for i in range(len(draws)):
            draw = draws[i].split(',')
            for k in draw:
                num, color = k.strip().split(' ')
                self.draws[color][i] = int(num)


    def is_possible(self, num_red, num_green, num_blue):
        return num_red >= max(self.draws['red']) and \
               num_green >= max(self.draws['green']) and \
               num_blue >= max(self.draws['blue'])

    def get_power(self):
        return max(self.draws['red']) * max(self.draws['green']) * max(self.draws['blue'])


    def __repr__(self):
        return f'<Game {self.id}>'





fid = open('input.txt')
lines = fid.readlines()


games = [Game(line) for line in lines]

total = 0
powers = 0

for game in games:

    if game.is_possible(12, 13, 14):
        total += game.id

    powers += game.get_power()

print('result part 1:', total)
print('result part 2:', powers)