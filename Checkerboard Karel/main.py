from karel.stanfordkarel import *

def main():
   
    while left_is_clear():
        row_odd()
        move_up()
        row_even()
        if left_is_clear():
            turn_left()
            move()
            turn_right()
            if left_is_blocked():
                row_odd()
    go_to_case1()

def go_to_case1():
    turn_right()
    while front_is_clear():
        move()
    turn_left()


def move_up():
    if left_is_clear():
        turn_left()
        move()
        turn_right()

def row_even():
    while front_is_clear():
        safe_move()
        put_beeper()
        safe_move()
    go_to_start()
    

def row_odd():
    if front_is_blocked():
        put_beeper()
    while front_is_clear():
        put_beeper()
        safe_move()
        if front_is_clear():
            move()
            if front_is_blocked():
                put_beeper()
    go_to_start()
    
def go_to_start():
    around()
    while front_is_clear():
        safe_move()
    around()


def safe_move():
    if front_is_clear():
        move()



def turn_right():
    for i in range(3):
        turn_left()


def around():
    for i in range(2):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()