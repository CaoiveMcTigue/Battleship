import random
import time

"""
Legend:
1. "." = empty space
2. "0" = part of ship
3. "X" = part of the ship that was hit with bullet
4. "#" = empty space that was shot with a bullet, a miss because it hit no ship
"""

# variable for grid
grid = [[]]
# variable for grid size
grid_size = 10
# variable for number of ships to place
num_ships = 8
# variable for bullets left
bullets_left = 50
# variable for game over
game_over = False
# variable for ships sunk
sunk_ships = 0
# variable for ship positions
ship_positions = [[]]
# variable for alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def validate_grid_and_place_ship(
        start_row, end_row, start_col, end_col):

    # check to see if its safe to place a ship in certain row or column.

    global grid
    global ship_positions

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != '.':
                all_valid = False
                break
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = 'O'
    return all_valid


def try_to_place_ship(
            row, col, direction, length):
    """Based on direction will use above function to help in trying to place a
        ship on the grid.
    Returns validate_grid_and_place_ship which will either be true or false."""

    global grid_size

    (start_row, end_row, start_col, end_col) = (
        row, row + 1, col, col + 1)
    if direction == 'left':
        if col - length < 0:
            return False
        start_col = col - length + 1
    elif direction == 'right':

        if col + length >= grid_size:
            return False
        end_col = col + length
    elif direction == 'up':

        if row - length < 0:
            return False
        start_row = row - length + 1
    elif direction == 'down':

        if row + length >= grid_size:
            return False
        end_row = row + length

    return validate_grid_and_place_ship(
        start_row, end_row, start_col, end_col)


def create_grid():
    """Will create a 10x10 grid and randomly place down ships
       of different sizes in different directions"""
    global grid
    global grid_size
    global num_ships
    global ship_positions

    random.seed(time.time())

    rows, cols = (grid_size, grid_size)

    grid = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(".")
        grid.append(row)

    num_of_ships_placed = 0

    ship_positions = []

    while num_of_ships_placed != num_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_to_place_ship(
                        random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1


def print_grid():
    # Will print the grid with rows A-J and columns 0-9
    global grid
    global alphabet

    debug_mode = False

    alphabet = alphabet[0: len(grid) + 1]

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")


def valid_bullet_placement():
    """Will get valid row and column to place bullet shot"""
    global alphabet
    global grid

    is_valid_placement = False
    row = -1
    col = -1
    while is_valid_placement is False:
        placement = input("Enter row (A-J) and column (0-9) such as A3:\n")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter only one row and column such as A3")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print(
                "Error: Please enter letter (A-J) for row and (0-9) for column"
                )
            continue
        row = alphabet.find(row)
        if not (-1 < row < grid_size):
            print(
                "Error: Please enter letter (A-J) for row and (0-9) for column"
                )
            continue
        col = int(col)
        if not (-1 < col < grid_size):
            print(
                "Error: Please enter letter (A-J) for row and (0-9) for column"
                )
            continue
        if grid[row][col] == "#" or grid[row][col] == "X":
            print("You have already shot a bullet here, pick somewhere else")
            continue
        if grid[row][col] == "." or grid[row][col] == "O":
            is_valid_placement = True

    return row, col


def check_for_ship_sunk(row, col):
    """ If all parts of a shit have been shot it is sunk
    and we later increment ships sunk"""
    global ship_positions
    global grid

    for position in ship_positions:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            # Ship found, now check if its all sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return False
    return True


def shoot_bullet():
    # Updates grid and ships based on where the bullet was shot
    global grid
    global sunk_ships
    global bullets_left

    row, col = valid_bullet_placement()
    print("")
    print("----------------------------")

    if grid[row][col] == ".":
        print("You missed, no ship was shot")
        grid[row][col] = "#"
    elif grid[row][col] == "O":
        print("You hit!", end=" ")
        grid[row][col] = "X"
        if check_for_ship_sunk(row, col):
            print("A ship was completely sunk!")
            sunk_ships += 1
        else:
            print("A ship was shot")

    bullets_left -= 1


def check_game_over():
    """ when users shots = 0 or all ships are sunk the game is over,
    heres the function to implement this."""
    global sunk_ships
    global num_ships
    global bullets_left
    global game_over

    if num_ships == sunk_ships:
        print("Congrats you won!")
        game_over = True
    elif bullets_left <= 0:
        print("Sorry, you lost! You ran out of bullets, try again next time!")
        game_over = True


def main():
    """Main entry point of application that runs the game loop"""
    global game_over

    print("-----Welcome to Battleships-----")
    print("You have 50 bullets to take down 8 ships, may the battle begin!")

    create_grid()

    while game_over is False:
        print_grid()
        print(
            "Number of ships remaining: " + str(
                num_ships - sunk_ships))
        print("Number of bullets left: " + str(bullets_left))
        shoot_bullet()
        print("----------------------------")
        print("")
        check_game_over()


if __name__ == '__main__':
    # this will only be called when program is run from terminal or an IDE
    main()
