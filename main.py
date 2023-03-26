# Unisa 2023 - Statistical Programming for Data Science; COMP 5070 Assessment Test 1 Battleship
# File in main.py
# Rongtian Guo - 110310135
# Date to start on 26/03/2023
# Due date is 26/03/2023
# I agree to the academic integrity policy and will complete the assignment in accordance with its terms.


import random

def get_ship_position(ship_lenght, place_ship, direction_extend_ship):
    position_ship = []
    position_head_ship = random.randint(1, 3), random.randint(1, 3)
    position_ship.append(position_head_ship)

    if place_ship=="vertically":
        for lenght_extend in range(1, ship_lenght):
            position_ship.append((eval(f"{position_head_ship[0]}{direction_extend_ship}{lenght_extend}"), position_head_ship[1]))
    else:
        for lenght_extend in range(1, ship_lenght):
            position_ship.append((position_head_ship[0], eval(f"{position_head_ship[1]}{direction_extend_ship}{lenght_extend}")))

    return position_ship

def check_ship_position_no_same(ships_position,ship_position):
    ship_position in ships_position
    for i in ship_position:
        for b in ships_position:
            for c in i:
                for h in b:
                    print(c)
                    print(h)
                    print(c==h)

a1=check_ship_position_no_same([[(2, 1), (2, 0), (2, -1), (2, -2), (2, -3),(3,1)]],[[(3, 1), (3, 2), (3, 3), (3, 4)]])


# def get_ship_positions(ship_types):
#     all_ship_positions = []

#     for ship in ship_types:
#         place_ship = random.choice(["vertically", "horizontally"])
#         direction_extend_ship = random.choice(["-", "+"])

#         if ship == "destroyer":
#             ship_position=get_ship_position(2, place_ship, direction_extend_ship)
            
#         elif ship == "submarine":
#             all_ship_positions.append(get_ship_position(3, place_ship, direction_extend_ship))
#         elif ship == "cruiser":
#             all_ship_positions.append(get_ship_position(3, place_ship, direction_extend_ship))
#         elif ship == "battleship":
#             all_ship_positions.append(get_ship_position(4, place_ship, direction_extend_ship))
#         elif ship == "carrier":
#             all_ship_positions.append(get_ship_position(5, place_ship, direction_extend_ship))

#     return all_ship_positions

# ship_ready = get_ship_positions(["carrier", "battleship", "cruiser", "submarine", "destroyer"])
# print(ship_ready)

# history=[]

# for simulate in range(10):
#     vertically_input=random.randint(1,11)
#     horizontally_input=random.randint(1,11)
    
#     history.append((vertically_input,horizontally_input))


#     print(vertically_input in board_size[0], horizontally_input in board_size[1])
#     print(history)