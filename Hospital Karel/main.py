#  Code in place - Hospital Karel
#  By Ricardo Monteiro
#  Released: 24/04/2025
#

# import libraries
from karel.stanfordkarel import *

# Main programm
def main():

    # street loop
    while front_is_clear():

        # if beeper is present go up and down
        if beepers_present():

            # put beepers going up
            turn_left()
            going_up()

            # go to other avenue
            turn_right()
            move()

            # put beepers going down
            going_down()
            turn_left()
            
        # check if is not the end
        if front_is_clear():
            move()

def going_up():
    # put 2 beepers going up
    for n in range(2):
        move()
        put_beeper()

def going_down():
    # put 3 beepers going down
    turn_right()
    for i in range(2):
        put_beeper()
        move()
    put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()