from karel.stanfordkarel import *

# Stone mason karel
# by ricardo monteiro
#

def main():

    # criar 4 colunas

    for i in range(4):
        # build the columns
        build_column()

        # turn de karel 180
        turn_180()

        # mode down
        going_down()

        # put in the same start position
        turn_left()

        # move 4 steps
        for j in range(4):
            safe_move()

def build_column():
    # face north
    turn_left()

    # pput beepers
    for k in range(5):
        put_beeper()
        safe_move()

def safe_move():
    # move if face is clear
    if front_is_clear():
        move()

def going_down():
    # go down
    for l in range(4):
        move()

def turn_180():
    for n in range(2):
        turn_left()

if __name__ == '__main__':
    main()