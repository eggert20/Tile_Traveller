# Tile Traveller program
welcome = "Hello world"
print(welcome)

def move_player_x(x ,direction ):
    """
    input: 2 parameters x cordinates and a direction.
    Changes the cordinates based on the direction entered.
    """
    if direction == 'N':
        x += 1
    elif direction == 'S':
        x -= 1
    return x

def move_player_y(y, direction):
    """
    input: 2 parameters x cordinates and a direction.
    Changes the y cordinates based on the direction entered.
    """
     if direction == 'E':
        y += 1
    elif direction == 'A':
        y -= 1
    return y
    


def locate_player():

def possible_direction(x,y):
    if y == 1:
        direction_str = "N"
    if x == 1 and y == 2:
        direction_str = "N or E or S"
    if x == 1 and y == 3:
        direction_str = "E or S"
    if x == y:
        direction_str = "S or W"
    if x == 2 and y == 3:
        direction_str = "E or W"
    if x == 3 and y == 2:
        direction_str = "N or S"
    return direction_str

def check_victory():

victory = False
x_cordinates = 1
y_cordinates = 1


while victory = False:
    print()

# 1.1 (N)orth
# 1.2 (N)orth or (E)ast or (S)outh
# 1.3 (E)ast or (S)outh
# 2.1 (N)orth
# 2.2 (S)outh or (W)est
# 2.3 (E)ast or (W)est
# 3.1 (N)orth
# 3.2 (N)orth or (S)outh
# 3.3 (S)outh or (W)est