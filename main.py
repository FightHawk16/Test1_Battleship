# Unisa 2023 - Statistical Programming for Data Science; COMP 5070 Assessment Test 1 Battleship
# File in main.py
# Rongtian Guo - 110310135
# Date to start on 26/03/2023
# Due date is 26/03/2023
# I agree to the academic integrity policy and will complete the assignment in accordance with its terms.


import random
import time

# Function to generate a single ship's position
def get_ship_position(ship_length, place_ship, direction_extend_ship):
    position_ship = []
    
    # Keep generating ship positions until a valid one is found
    while not position_ship:
        position_head_ship = random.randint(1, 10), random.randint(1, 10)
        temp_position_ship = [position_head_ship]
        valid = True

        # Extend the ship in the chosen direction, and check if it goes outside the board
        if place_ship == "vertically":
            for length_extend in range(1, ship_length):
                new_position = eval(f"{position_head_ship[0]}{direction_extend_ship}{length_extend}"), position_head_ship[1]
                if new_position[0] < 1 or new_position[0] > 10:
                    valid = False
                    break
                temp_position_ship.append(new_position)
        else:
            for length_extend in range(1, ship_length):
                new_position = position_head_ship[0], eval(f"{position_head_ship[1]}{direction_extend_ship}{length_extend}")
                if new_position[1] < 1 or new_position[1] > 10:
                    valid = False
                    break
                temp_position_ship.append(new_position)

        # If the position is valid, set it as the ship's position
        if valid:
            position_ship = temp_position_ship

    return position_ship

# Function to check if a new ship position overlaps with any existing ships
def check_ship_position_no_same(ships_position, ship_position):
    for existing_ship_position in ships_position:
        for existing_position in existing_ship_position:
            for new_position in ship_position:
                if existing_position == new_position:
                    return True
    return False

# Function to generate positions for all ship types
def get_ship_positions(ship_types):
    all_ship_positions = []

    for ship in ship_types:
        place_ship = random.choice(["vertically", "horizontally"])
        direction_extend_ship = random.choice(["-", "+"])

        # For each ship type, check if the generated position overlaps with existing ships
        # If it does, generate a new position until it doesn't overlap
        if ship == "destroyer":
            similiar_check = True
            while similiar_check:
                ship_position = get_ship_position(2, place_ship, direction_extend_ship)
                if not check_ship_position_no_same(all_ship_positions, ship_position):
                    similiar_check = False
            all_ship_positions.append(ship_position)

        elif ship == "submarine":
            similiar_check = True
            while similiar_check:
                ship_position = get_ship_position(3, place_ship, direction_extend_ship)
                if not check_ship_position_no_same(all_ship_positions, ship_position):
                    similiar_check = False
            all_ship_positions.append(ship_position)

        elif ship == "cruiser":
            similiar_check = True
            while similiar_check:
                ship_position = get_ship_position(3, place_ship, direction_extend_ship)
                if not check_ship_position_no_same(all_ship_positions, ship_position):
                    similiar_check = False
            all_ship_positions.append(ship_position)

        elif ship == "battleship":
            similiar_check = True
            while similiar_check:
                ship_position = get_ship_position(4, place_ship, direction_extend_ship)
                if not check_ship_position_no_same(all_ship_positions, ship_position):
                    similiar_check = False
            all_ship_positions.append(ship_position)

        elif ship == "carrier":
            similiar_check = True
            while similiar_check:
                ship_position = get_ship_position(5, place_ship, direction_extend_ship)
                if not check_ship_position_no_same(all_ship_positions, ship_position):
                    similiar_check = False
            all_ship_positions.append(ship_position)

    return all_ship_positions

# Modified get_attack_on_board to check against history of attack_positions
def get_attack_on_board(attack_history):
    while True:
        attack_position = random.randint(1, 10), random.randint(1, 10)
        if attack_position not in attack_history:
            return attack_position

def check_ship_hit(ships_positions):
    total_point = 17
    attack_history = []

    while total_point > 0:
        attack_position = get_attack_on_board(attack_history)
        attack_history.append(attack_position)
        for ship_positions in ships_positions:
            if attack_position in ship_positions:
                total_point -= 1
                break

    return "All ships been destroyed, Game Finish!"

def get_running_times():
    running_time = None
    while running_time is None:
        try:
            running_time = int(input("Please enter the how many times the game should run: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            running_time = None
    return running_time

def main():
    time_usage = []
    times = get_running_times()

    while times > 0:
        ships_positions = get_ship_positions(["carrier", "battleship", "cruiser", "submarine", "destroyer"])
        start_time = time.time()  # Record start time
        game_stage = check_ship_hit(ships_positions)
        times -= 1
        end_time = time.time()  # Record end time
        time_usage.append(end_time - start_time)
    print(sum(time_usage) / len(time_usage))

if __name__ == "__main__":
    main()