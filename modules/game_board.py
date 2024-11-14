class Board:

    def create_board(grid_list):

        i = 0
        print("     " + "A" + "   " + "|" + "   " + "B" + "   " + "|" + "   " + "C")
        print("--------------------------")

        for row in grid_list:
            i = i + 1
            print(str(i)  + "|" +"   " + row[0] + "   " + row[1] + "   " + row[2] + "   " + row[3] + "   " + row[4])
            print("--------------------------")