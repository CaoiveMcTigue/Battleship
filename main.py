"""
Legend:
1. "." = empty space
2. "0" = part of ship
3. "X" = part of the ship that was hit with bullet
4. "#" = empty space that was shot with a bullet, a miss because it hit no ship
"""

grid = [[]] #variable for grid
grid_size = 10 #variable for grid size
num_ships = 8 #variable for number of ships to place
bullets_left = 50 #variable for bullets left
game_over = False #variable for game over
sunk_ships = 0 #variable for number of ships sunk
ship_positions = [[]] #variable for ship positions
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #variable for alphabet

def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    #check to see if its safe to place a ship in certain row or column.
    global grid
    global ship_positions

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_valid


def try_to_place_ship(row, col, direction, length):
    """Based on direction will use above function to help in trying to place a ship on the grid.
        Returns validate_grid_and_place_ship which will either be true or false."""
    global grid_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1
    
    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length
    
    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1
    
    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)

