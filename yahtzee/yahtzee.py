class Yahtzee:
    def __init__(self, rolls: list):
        self.dice = rolls

        self.tallies = [0] * (len(self.dice) + 1)
        for die in self.dice:
            self.tallies[die - 1] += 1

    def _calculate_sum(self, number):
        sum = 0
        for die in self.dice:
            if die == number:
                sum += number
        return sum

    def chance(self):
        return sum(self.dice)

    def yahtzee(self):
        for i in range(len(self.tallies)):
            if self.tallies[i] == 5:
                return 50
        return 0

    def ones(self):
        return self._calculate_sum(1)

    def twos(self):
        return self._calculate_sum(2)

    def threes(self):
        return self._calculate_sum(3)

    def fours(self):
        return self._calculate_sum(4)

    def fives(self):
        return self._calculate_sum(5)

    def sixes(self):
        return self._calculate_sum(6)

    def score_pair(self):
        for die_value in range(6, 1, -1):
            if self.tallies[die_value - 1] == 2:
                return die_value * 2
        return 0

    def two_pair(self):
        pair_count = 0
        score = 0
        for die_value in range(6):
            if self.tallies[die_value - 1] == 2:
                pair_count += 1
                score += die_value

        if pair_count == 2:
            return score * 2
        else:
            return 0

    def three_of_a_kind(self):
        for die_value in range(6):
            if self.tallies[die_value] == 3:
                return (die_value + 1) * 3
        return 0

    def four_of_a_kind(self):
        for die_value in range(6):
            if self.tallies[die_value] == 4:
                return (die_value + 1) * 4
        return 0

    def small_straight(self):
        if (
            self.tallies[0] == 1
            and self.tallies[1] == 1
            and self.tallies[2] == 1
            and self.tallies[3] == 1
            and self.tallies[4] == 1
        ):
            return 15
        return 0

    def large_straight(self):

        if (
            self.tallies[1] == 1
            and self.tallies[2] == 1
            and self.tallies[3] == 1
            and self.tallies[4] == 1
            and self.tallies[5] == 1
        ):
            return 20
        return 0

    def full_house(self):
        have_pair = False
        pair_value = 0
        have_triple = False
        triple_value = 0

        for i in range(6):
            if self.tallies[i] == 2:
                have_pair = True
                pair_value = i + 1

        for i in range(6):
            if self.tallies[i] == 3:
                have_triple = True
                triple_value = i + 1

        if have_pair and have_triple:
            return pair_value * 2 + triple_value * 3
        else:
            return 0
