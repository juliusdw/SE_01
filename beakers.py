# topmost liquid gets poured
# can only enter beaker if ther is space or the same 

beakers = ["0", "0", "0", "2", "1", "2", "2", "1", "1"]

class Game:
    
    def __init__(self):
        print("test")
    def print_beakers(self, beakers):
        print("Nr1" + str(beakers[0:3]))
        print("Nr2" + str(beakers[3:6]))
        print("Nr3" + str(beakers[6:9]))

    def get_move_from(self):
        from_beaker = input("Which Beaker do you want to pour from!")
        print("pouring from beaker nr: " + from_beaker)
        return from_beaker
    def get_move_to(self):
        to_beaker = input("Which beaker do you want to pour to?")
        print("pouring into beaker nr: " + to_beaker)
        return to_beaker

    def check_empty(self, current_to_beaker):
        

  #  def check_same_fluid(self, current_from_beaker, current_to_beaker):

        



g = Game()

g.print_beakers(beakers)
current_from_beaker = g.get_move_from()
current_to_beaker = g.get_move_to()
#g.check_empty(current_to_beaker)
#is_empty = g.check_empty(current_to_beaker)
#if is_empty == False:
  #  print("The Beaker if Full!")

#g.check_same_fluid(current_from_beaker, current_to_beaker)
