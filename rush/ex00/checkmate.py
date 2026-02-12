def checkmate(board):
    grid = board.splitlines()
    size = len(grid)

    if size == 0:
        print("Error: Empty board")
        return

    for row in grid:
        if len(row) != size:
            print("Error: Board is not square")
            return

    valid = ["K", "Q", "B", "R", "P", "."]
    king_count = 0
    king_row = -1
    king_col = -1

    for row in range(size):
        for col in range(size):
            current = grid[row][col]

            if current not in valid:
                print("Error: Invalid character")
                return

            if current == "K":
                king_count += 1
                king_row = row
                king_col = col

    if king_count == 0:
        print("Error: No King found")
        return

    if king_count > 1:
        print("Error: More than one King found")
        return

    if king_row + 1 < size:
        if king_col - 1 >= 0:
            if grid[king_row + 1][king_col - 1] == "P":
                print("Success")
                return
        if king_col + 1 < size:
            if grid[king_row + 1][king_col + 1] == "P":
                print("Success")
                return

    straight = [(1,0), (-1,0), (0,1), (0,-1)]

    for i in straight:
        row = king_row + i[0]
        col = king_col + i[1]

        while 0 <= row < size and 0 <= col < size:
            current = grid[row][col]

            if current != ".":
                if current in "RQ":
                    print("Success")
                    return
                break

            row += i[0]
            col += i[1]

    diagonals = [(1,1), (1,-1), (-1,1), (-1,-1)]

    for i in diagonals:
        row = king_row + i[0]
        col = king_col + i[1]

        while 0 <= row < size and 0 <= col < size:
            current = grid[row][col]

            if current != ".":
                if current in "BQ":
                    print("Success")
                    return
                break

            row += i[0]
            col += i[1]

    print("Fail")
