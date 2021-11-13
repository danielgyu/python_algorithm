def draw_board(rows, columns):
    board, count = [], 1

    for _ in range(rows):
        board.append([])
        for _ in range(columns):
            board[-1].append(count)
            count += 1

    return board

def rotate(rows, columns, queries):
    mins = []

    board = draw_board(rows, columns)

    pieces = []
    for q in queries:
        print(f"query: {q}")
        x1, y1, x2, y2 = q[0] - 1, q[1] - 1, q[2] - 1, q[3] - 1

        q_min = board[x1][y1]

        print(f"x1: {x1}, x2: {x2}")
        print(f"y1: {y1}, y2: {y2}")
        for i in range(y1, y2):
            print(f"right: {board[x1][i]}")
            if pieces:
                p = pieces.pop()
                pieces.append(board[x1][i])
                board[x1][i] = p
            else:
                pieces.append(board[x1][i])

            q_min = min(q_min, board[x1][i])

        for i in range(x1, x2):
            print(f"down: {board[i][y2]}")
            if pieces:
                p = pieces.pop()
                pieces.append(board[i][y2])
                board[i][y2] = p
            else:
                pieces.append(board[i][y2])

        for i in range(y2, y1, -1):
            print(f"left: {board[x2][i]}")
            if pieces:
                p = pieces.pop()
                pieces.append(board[x2][i])
                board[x2][i] = p
            else:
                pieces.append(board[x2][i])

        for i in range(x2, x1, - 1):
            print(f"up: {board[i][y1]}")
            if pieces:
                p = pieces.pop()
                pieces.append(board[i][y1])
                board[i][y1] = p
            else:
                pieces.append(board[i][y1])

        mins.append(q_min)

    return mins

if __name__ == "__main__":
    #print(rotate(6, 6, [[2,2,5,4]]))
    print(rotate(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
