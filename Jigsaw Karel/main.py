from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""

def main():
    # programa principal
    get_first()
    put_first()
    vira180()
    move2()
    vira180()
    turn_left()
    move2()
    move()
    vira180()

# move 2 peças
def move2():
    move()
    move()

# vira 180 graus
def vira180():
    turn_left()
    turn_left()

# anda e pega
def get_first():
    move2()
    pick_beeper()

# coloca no lugar
def put_first():
    move()
    turn_left()
    move2()
    put_beeper()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()