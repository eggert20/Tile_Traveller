import random

# Tile Traveller program
# https://github.com/eggert20/Tile_Traveller.git

def move_player_x(x ,direction ):
    """
    input: 2 parameters x cordinates and a direction.
    Changes the cordinates based on the direction entered.
    """
    if direction == 'E':
        x += 1
    elif direction == 'W':
        x -= 1
    return x

def move_player_y(y, direction):
    """
    input: 2 parameters x cordinates and a direction.
    Changes the y cordinates based on the direction entered.
    """
    if direction == 'N':
        y += 1
    elif direction == 'S':
        y -= 1
    return y
    

def possible_direction(x,y):
    if x == 1 and y == 1: # (1,1)
        direction_str = "N"
        print("You can travel: (N)orth.")
    elif x == 1 and y == 2: # (1,2)
        direction_str = "NES"
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif x == 1 and y == 3: # (1,3)
        direction_str = "ES"
        print("You can travel: (E)ast or (S)outh.")
    elif x == 2 and y == 1: # (2,1)
        direction_str = "NE"
        print("You can travel: (N)orth.")
    elif x == 2 and y == 2: # (2,2)
        direction_str = "SW"
        print("You can travel: (S)outh or (W)est.")
    elif x == 2 and y == 3: # (2,3)
        direction_str = "EW"
        print("You can travel: (E)ast or (W)est.")
    elif x == 3 and y == 1: # (3,1)
        direction_str = "N"
        print("You can travel: (N)orth.")
    elif x == 3 and y == 2: # (3,2)
        direction_str = "NS"
        print("You can travel: (N)orth or (S)outh.")
    elif x == 3 and y == 3: # (3,3)
        direction_str = "SW"
        print("You can travel: (S)outh or (W)est.")
    return direction_str

def get_move(direction, x, y):
    valid_direction = False
    while valid_direction == False:
        new_move = random.choice(['N', 'E', 'S', 'W'])
        for letter in direction:
            if letter == new_move:
                valid_direction = True
                break
        else:
            print('Not a valid direction!')
            possible_direction(x, y)
    return new_move
                

def is_lever(x,y):
    if x == 1 and y == 1: # (1,1)
        return False
    elif x == 1 and y == 2: # (1,2)
        return True
    elif x == 1 and y == 3: # (1,3)
        return False
    elif x == 2 and y == 1: # (2,1)
        return False
    elif x == 2 and y == 2: # (2,2)
        return True
    elif x == 2 and y == 3: # (2,3)
        return True
    elif x == 3 and y == 1: # (3,1)
        return False
    elif x == 3 and y == 2: # (3,2)
        return True
    elif x == 3 and y == 3: # (3,3)
        return False

def lever_functionality(coin_counter):
    the_input = random.choice(['Y', 'N'])

    if the_input == 'Y':
        coin_counter += 1
        print('You received 1 coin, your total is now {}.'.format(coin_counter))
    return coin_counter

def play():
    victory = False
    valid_direction = False
    x_cordinates = 1
    y_cordinates = 1
    coin_counter = 0
    while victory == False:
        possible_directions = possible_direction(x_cordinates,y_cordinates)
        
        new_move = get_move(possible_directions, x_cordinates, y_cordinates)
                
        x_cordinates = move_player_x(x_cordinates, new_move)
        y_cordinates = move_player_y(y_cordinates, new_move)

        
        if is_lever(x_cordinates, y_cordinates):
            coin_counter = lever_functionality(coin_counter)

        if x_cordinates == 3 and y_cordinates == 1:
            print('Victory! Total coins {}.'.format(coin_counter))
            return None

def main():
    seed = input("Input seed: ")
    yes_or_no = 'Y'
    while yes_or_no == 'Y':
        play()
        yes_or_no = input('Play again (y/n): ')
        yes_or_no = yes_or_no.upper()

main()





# 1.1 (N)orth
# 1.2 (N)orth or (E)ast or (S)outh
# 1.3 (E)ast or (S)outh
# 2.1 (N)orth
# 2.2 (S)outh or (W)est
# 2.3 (E)ast or (W)est
# 3.1 (N)orth
# 3.2 (N)orth or (S)outh
# 3.3 (S)outh or (W)est