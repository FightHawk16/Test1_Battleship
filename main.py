# Unisa 2023 - Statistical Programming for Data Science; COMP 5070 Assessment Test 1 Battleship
# File in main.py
# Rongtian Guo - 110310135
# Date to start on 26/03/2023
# Due date is 26/03/2023
# I agree to the academic integrity policy and will complete the assignment in accordance with its terms.

import random
board_vertically=range(1,11)
board_horizontally=range(1,11)
board_size=[board_vertically,board_horizontally]

history=[]

for simulate in range(10):
    vertically_input=random.randint(1,11)
    horizontally_input=random.randint(1,11)
    
    history.append((vertically_input,horizontally_input))


    print(vertically_input in board_size[0], horizontally_input in board_size[1])
    print(history)