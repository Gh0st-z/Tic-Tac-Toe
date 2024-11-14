import socket
from modules.config import Config

class Grid:

    def check_update(grid_list, grid_number, grid_numbers_list, position_map, turn_list):

        grid_number = grid_number.upper()

        if grid_number not in grid_numbers_list:
            print("Please enter a valid grid number as instructed!")
            print("============================================================")

        row, col = position_map[grid_number]

        if grid_list[row][col] != " ":
            print("A symbol has already been placed in the grid! Please re-check and enter and empty grid number!")
            print("============================================================")
            turn_list.pop()

        grid_list[row][col] = turn_list[-1]
        return(grid_list)
        
