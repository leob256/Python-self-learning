stats = input("Tell me your football players...Name, Position, Pace, Shotting, Passing...")
name,position,pace,shooting,passing = stats.split(",")
class Player:
    def __init__(self,name,position,pace,shooting,passing):
        self.name = name
        self.position = position
        self.pace = pace   
        self.shooting = shooting
        self.passing = passing
    def rating(self):
        total = (int(self.pace) + int(self.shooting) + int(self.passing)) // 3
        return round(total,1)
player1 = Player(name,position,pace,shooting,passing)
print(player1.name+"'s rating is",player1.rating())
