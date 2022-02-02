# -*- coding: utf-8 -*-


class TennisGame:
    def __init__(self, player1Name, player2Name):
        self.p1Name = player1Name
        self.p2Name = player2Name
        self.p1Points = 0
        self.p2Points = 0

    def won_point(self, n):
        if n == self.p1Name:
            self.p1Points += 1
        else:
            self.p2Points += 1

    def score(self):
        if (self.p1Points < 4 and self.p2Points < 4) and (
            self.p1Points + self.p2Points < 6
        ):
            pointNames = ["Love", "Fifteen", "Thirty", "Forty"]
            scoreString = pointNames[self.p1Points]

            if self.p1Points == self.p2Points:
                scoreString += "-All"
            else:
                scoreString += "-" + pointNames[self.p2Points]
            return scoreString

        else:
            if self.p1Points == self.p2Points:
                return "Deuce"
            if self.p1Points > self.p2Points:
                scoreString = self.p1Name
            else:
                scoreString = self.p2Name

            if (self.p1Points - self.p2Points) * (self.p1Points - self.p2Points) == 1:
                scoreString = "Advantage " + scoreString
            else:
                scoreString = "Win for " + scoreString
            return scoreString
