# Unisa 2023 - Statistical Programming for Data Science; COMP 5070 Assessment Test 1 Battleship
# File in main.py
# Rongtian Guo - 110310135
# Date to start on 26/03/2023
# Due date is 26/03/2023
# I agree to the academic integrity policy and will complete the assignment in accordance with its terms.


import random

def get_ship_positions(ship_types):
    all_ship_positions = []

    for ship in ship_types:
        place_ship = random.choice(["vertically", "horizontally"])
        direction_extend_ship = random.choice(["-", "+"])

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


def check_ship_position_no_same(ships_position, ship_position):
    for existing_ship_position in ships_position:
        for existing_position in existing_ship_position:
            for new_position in ship_position:
                if existing_position == new_position:
                    return True
    return False





def get_ship_position(ship_length, place_ship, direction_extend_ship):
    position_ship = []
    
    while not position_ship:
        position_head_ship = random.randint(1, 10), random.randint(1, 10)
        temp_position_ship = [position_head_ship]
        valid = True

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
        
        if valid:
            position_ship = temp_position_ship

    return position_ship


ship_ready = get_ship_positions(["carrier", "battleship", "cruiser", "submarine", "destroyer"])
print(ship_ready)