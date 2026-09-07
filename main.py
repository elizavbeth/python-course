class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points

class VIPPlayer(Player):
    def add_score(self, points):
        self.score += (points * 2)
        return self.score

vip_user = VIPPlayer("Anna")
result = vip_user.add_score(10)
print(result)