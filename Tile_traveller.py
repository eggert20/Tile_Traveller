# Tile Traveller program

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

victory = False
valid_direction = False
x_cordinates = 1
y_cordinates = 1


while victory == False:
    jonni = possible_direction(x_cordinates,y_cordinates)
    
    while valid_direction == False:
        new_move = input("Direction: ")
        new_move = new_move.upper()
        for letter in jonni:
            if letter == new_move:
                valid_direction = True
                break
        else:
            print('Not a valid direction!')
            possible_direction(x_cordinates, y_cordinates)
                

    x_cordinates = move_player_x(x_cordinates, new_move)
    y_cordinates = move_player_y(y_cordinates, new_move)

    if x_cordinates == 3 and y_cordinates == 1:
        print('Victory!')
        break
    valid_direction = False

        



# 1.1 (N)orth
# 1.2 (N)orth or (E)ast or (S)outh
# 1.3 (E)ast or (S)outh
# 2.1 (N)orth
# 2.2 (S)outh or (W)est
# 2.3 (E)ast or (W)est
# 3.1 (N)orth
# 3.2 (N)orth or (S)outh
# 3.3 (S)outh or (W)est