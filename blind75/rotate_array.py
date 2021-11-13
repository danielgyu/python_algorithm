def print_array(array):
    for a in array:
        print(a)

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

    for q in queries:
        x1, y1, x2, y2 = q[0] - 1, q[1] - 1, q[2] - 1, q[3] - 1

        q_min = board[x1][y1]
        pieces = [q_min]

        for i in range(y1, y2):
            tmp = board[x1][i]
            board[x1][i] = pieces.pop()
            pieces.append(tmp)
            q_min = min(q_min, tmp)

        for i in range(x1, x2):
            tmp = board[i][y2]
            board[i][y2] = pieces.pop()
            pieces.append(tmp)
            q_min = min(q_min, tmp)

        for i in range(y2, y1, -1):
            tmp = board[x2][i]
            board[x2][i] = pieces.pop()
            pieces.append(tmp)
            q_min = min(q_min, tmp)

        for i in range(x2, x1, - 1):
            tmp = board[i][y1]
            board[i][y1] = pieces.pop()
            pieces.append(tmp)
            q_min = min(q_min, tmp)

        board[x1][y1] = pieces.pop()
        mins.append(q_min)

    print_array(board)

    return mins

if __name__ == "__main__":
    print(rotate(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
    #print(rotate(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
    #print(rotate(100, 97, [[1,1,100,97]]))
