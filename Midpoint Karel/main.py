from karel.stanfordkarel import *


def main():

    # coloca os beebers como placeholders
    move()
    put_beeper()
    while front_is_clear():
        safe_move()
    change_180()
    move()
    put_beeper()
    # end of preparation - 1 beeper in each side

    # put karel inside the placeholders
    if front_is_blocked():
        # 2x2 problem
        change_180()
        move()
        pick_beeper()
        change_180()
        move()
        change_180()
    else:
        move()

        while no_beepers_present():
            # enquanto não estiver sobre o placeholder
        
            while no_beepers_present():
                move()
            change_180()
            move_beeper()
            while no_beepers_present():
                move()
            change_180()
            move_beeper()
        # check if is even
        change_180()
        move()
        if beepers_present():
            pick_beeper()
            change_180()
            move()
            change_180()
        else:
            change_180()
            move()
            

def move_beeper():
    # move beeeper 1 street
    pick_beeper()
    move()
    if no_beepers_present():
        put_beeper()
        move()
    else:
        # when is odd end here
        if facing_west():
            change_180()


def safe_move():
    # confirma que é possível se mover
    if front_is_clear():
        move()

def change_180():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()