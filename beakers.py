# topmost liquid gets poured
# can only enter beaker if ther is space or the same 

beakers = [["0", "0", "0"], ["2", "1", "2"], ["2", "1", "1"]]

class Game:
    
    def __init__(self):
        print("test")
    def print_beakers(self, beakers):
        for beaker in beakers:
            print(beaker)

    def get_move_from(self):
        from_beaker = input("Which Beaker do you want to pour from!")
        print("pouring from beaker nr: " + from_beaker)
        from_beaker = int(from_beaker)
        from_beaker = from_beaker -1
        return from_beaker
    def get_move_to(self):
        to_beaker = input("Which beaker do you want to pour to?")
        print("pouring into beaker nr: " + to_beaker)
        to_beaker = int(to_beaker)
        to_beaker = to_beaker -1
        return to_beaker

    def check_empty(self, current_to_beaker, current_from_beaker):
        f = int(current_to_beaker)
        t = int(current_to_beaker)
        if "0" in beakers[f]:
            return True
        else:
            for m in beakers[f]:
                if m == 0:
                    return None
                elif m != 0:
                    for z in beakers[t]:
                        if z == m:
                            return True
                        else:
                            return False

           
            print ("there is no space in this beaker!")
            return 


        

  #  def check_same_fluid(self, current_from_beaker, current_to_beaker):

        



g = Game()

g.print_beakers(beakers)
current_from_beaker = g.get_move_from()
current_to_beaker = g.get_move_to()
is_empty = g.check_empty(current_to_beaker, current_from_beaker)
if is_empty == False:
    print("there is no space try again!")
    
else:
    print("there is space or the right color")
#is_empty = g.check_empty(current_to_beaker)
#if is_empty == False:
  #  print("The Beaker if Full!")

#g.check_same_fluid(current_from_beaker, current_to_beaker)
