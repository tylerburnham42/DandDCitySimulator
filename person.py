

class Person:

    def __init__(self, name, profession, skill, money):
        self.name = name
        self.profession = profession
        self.skill = skill
        self.money = money
        self.alive = True

    def __repr__(self):
        return "{} - {} - {}".format(self.name, self.profession, self.skill)


