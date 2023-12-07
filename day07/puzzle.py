"""
day 7
"""

# dict to map the value of the cards to a number
keys = ('A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2')
keys_joker = ('A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J')
values = list(range(len(keys)))[::-1]
mapping = dict(zip(keys, values))


class Hand(object):

    def __init__(self, hand, bid):
        self.hand = hand
        self.hand_best = self.replace_joker()
        self.hand_orig = hand
        self.bid = bid


    def __repr__(self):
        return f'<Hand {self.hand_orig} | Best {self.hand_best} | Bid {self.bid}>'


    def get_type(self):

        s = list(set(self.hand))
        n = len(s)

        # five of a kind
        if n == 1:
            return 7

        if n == 2:

            # four of a kind
            if self.hand.count(s[0]) in (1, 4):
                return 6

            # full house
            elif self.hand.count(s[0]) in (2, 3):
                return 5

        if n == 3:
            count = [self.hand.count(i) for i in s]

            # three of a kind
            if max(count) == 3:
                return 4

            # two pairs
            else:
             return 3

        # one pair
        elif n == 4:
            return 2

        # all different
        elif n == 5:
            return 1

        else:
            raise ValueError(f'Cannot determin type of hand {self.hand}')


    def replace_joker(self):
        '''
        Joker conversion rule: always replace with highest count card
        besides J to get best hand

        '''
        no_J = self.hand.replace('J', '')

        if not no_J:
            return 'AAAAA'

        max_num = 0
        max_card = None

        for i in no_J:
            count = no_J.count(i)
            if count > max_num:
                max_num = count
                max_card = i

        if max_num == 1 and len(no_J) != 1:
            return self.hand.replace('J', self.max_card(no_J))
        else:
            return self.hand.replace('J', max_card)


    def max_card(self, cards):
        """
        Return the highest card in a set of individual cards
        """

        max_val = 0
        max_card = None

        for i in cards:
            if mapping[i] > max_val:
                max_val = mapping[i]
                max_card = i

        return max_card


    def __gt__(self, other):
        """
        Compare two hands
        """

        t_self = self.get_type()
        t_other = other.get_type()

        if t_self != t_other:
            return t_self > t_other

        else:
            for i in range(len(self.hand_orig)):
                a = mapping[self.hand_orig[i]]
                b = mapping[other.hand_orig[i]]

                if a != b:
                    return a > b




fid = open('input.txt')

hands = list()

for i in fid.readlines():
    h, b = i.split(' ')
    hands.append(Hand(h, int(b)))



# part 1

hands.sort()
total = 0

for i, hand in enumerate(hands):
    total += (i+1) * hand.bid

print('result part 1', total)



# part 2

# 'J' is lowest card now
mapping = dict(zip(keys_joker, values))

for hand in hands:
    hand.hand = hand.hand_best

hands.sort()
total = 0

for i, hand in enumerate(hands):
    total += (i+1) * hand.bid

print('result part 2', total)