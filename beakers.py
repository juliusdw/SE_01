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

    def check_empty(self, current_to_beaker, current_from_beaker): # for checking if there if the same color os space in the beaker
        f = int(current_from_beaker)
        t = int(current_to_beaker)
        if "0" in beakers[t]: check if there is space in the beaker
            print("beaker has space left")
            return True
        else:
            for layert in beakers[t]:
                if layert == 0: #check if beaker is empty
                    return None
                elif layert != 0: # or if it has a color
                    for layerf in beakers[f]: # go through layers of the from beaker
                        if layerf != 0:
                            if layert == layerf: # return true is there is a match 
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
