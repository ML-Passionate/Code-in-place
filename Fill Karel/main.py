from karel.stanfordkarel import *
#
# Fill Karel
# by ricardo

def main():
    # main loop
    while front_is_clear():
        do_a_street()

def do_a_street():
    # while is not the end put a beeeper and move
    while front_is_clear():
        put_beeper()
        move()
    # put beeper in the last position
    put_beeper()
    # come back to the top of the street
    turn_180()
    return_top_street()

def turn_180():
    # turn 180 degree
    turn_left()
    turn_left()
    
def turn_right():
    # turn right
    for j in range(3):
        turn_left()

def return_top_street():
    # return to the top of the street
    while front_is_clear():
        move()
    move_next_street()

def move_next_street():
    # move to next street
    turn_right()
    # test if is the last street
    if front_is_blocked():
        turn_right()
        while front_is_clear():
            move()
    else:
        move()
        turn_right()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()