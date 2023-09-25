class Player:

  def play(self):
    print("He player is playing cricket.")


class Batsman(Player):

  def play(self):
    print("The bowler is batting.")


class Bowler(Player):

  def play(self):
    print("The bowler is bowling")


batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()
