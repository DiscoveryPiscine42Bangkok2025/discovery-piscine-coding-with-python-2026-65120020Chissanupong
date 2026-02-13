def is_check(kr, kc, edge, coordinate, type, direction):
    for v, h in direction:
        for r in range (1, 2 if type == "P" else edge):
            new_r = kr + (v*r)
            new_c = kc + (h*r)

            if not (0 <= new_r < edge and 0 <= new_c < edge):
                break
            
            piece = coordinate.get((new_r, new_c))

            if piece:
                if piece == type:
                    return True
                else:
                    break


def checkmate(board):
    piecetype = {
        "R" : [(0,1), (0,-1), (1,0), (-1,0)], 
        "B" : [(-1,-1), (1,-1), (-1,1), (1,1)], 
        "Q" : [(0,1), (0,-1), (1,0), (-1,0), (-1,-1), (1,-1), (-1,1), (1,1)], 
        "P" : [(1,-1), (1,1)]
        }
    coordinate = {}

    lines = board.strip().split("\n")
    for row, line in enumerate(lines):
        for col, piece in enumerate(line):
            if piece in ("K", "R", "Q", "B", "P"):
                coordinate[(row, col)] = piece
                if piece == "K":
                    kr, kc = row, col
    
    king_count = list(coordinate.values()).count("K")
    if king_count == 0:
        print("There is no King")
        return
    elif king_count > 1:
        print("There must be only one King")
        return

    edge = len(lines)

    for line in lines:
        if not len(line) == edge:
            print("The board isn't a square")
            return
    
    for type, direction in piecetype.items():
        if is_check(kr, kc, edge, coordinate, type, direction):
            print("Success")
            break
    else:
        print("Failed")