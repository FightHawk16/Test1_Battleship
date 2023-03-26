# Unisa 2023 - Statistical Programming for Data Science; COMP 5070 Assessment Test 1 Battleship
# File in main.py
# Rongtian Guo - 110310135
# Date to start on 26/03/2023
# Due date is 26/03/2023
# I agree to the academic integrity policy and will complete the assignment in accordance with its terms.

import random
# board_vertically=range(1,11)
# board_horizontally=range(1,11)
# board_size=[board_vertically,board_horizontally]
# ship_carrier=[(1,5),(5,1)]
# ship_battleship=[(1,4),(4,1)]
# ship_destroyer=(random.choice(1,2))
# if ship_destroyer[0] == 1:
#     pass

def get_ship_position(ship_type,ship_lenght):
    place_ship=random.choice(["vertically","horizontally"])
    direction_extend_ship=random.choice(["-","+"])
    if ship_type == "destoryer":
        position_destroyer=[]
        position_head_ship=random.randint(1,10),random.randint(1,10)
        position_destroyer.append(position_head_ship)
        if place_ship == "vertically":
            for lenght_extend in range(1,ship_lenght):
                position_destroyer.append((eval(f"{position_head_ship[0]}{direction_extend_ship}{lenght_extend}"),position_head_ship[1]))
        else:
            for lenght_extend in range(1,ship_lenght):
                position_destroyer.append((position_head_ship[0],eval(f"{position_head_ship[1]}{direction_extend_ship}{lenght_extend}")))
                
    
        return position_destroyer
    
ship_ready=get_ship_position("destoryer",2)
print(ship_ready)

# save= "+"
# print(eval(f"1{save}2"))

# print(random.choice(board_size[0]),random.choice(board_size[1]))

# print(random.choice(ship_carrier))

# history=[]

# for simulate in range(10):
#     vertically_input=random.randint(1,11)
#     horizontally_input=random.randint(1,11)
    
#     history.append((vertically_input,horizontally_input))


#     print(vertically_input in board_size[0], horizontally_input in board_size[1])
#     print(history)