class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict ['team']
        self.nationality = dict['nationality']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.penalties = dict['penalties']
        self.games = dict['games']

    def pisteet(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team}  {self.goals:2} + {self.assists:2} = {self.pisteet():2}"