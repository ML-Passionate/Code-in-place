"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one!
    """
    
    while front_is_clear():
        safe_move()
        if left_is_clear():
            move_left()
        else:
            if right_is_clear():
                move_right()


def move_left():
    turn_left()
    move()
    if front_is_blocked():
        if left_is_clear():
            turn_left()
        else:
            if right_is_clear():
                turn_right()


def move_right():
    turn_right()
    move()
    if front_is_blocked():
        if left_is_clear():
            turn_left()
        else:
            if right_is_clear():
                turn_right()


def turn_right():
    for i in range(3):
        turn_left()

def safe_move():
    if front_is_clear():
        move()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()