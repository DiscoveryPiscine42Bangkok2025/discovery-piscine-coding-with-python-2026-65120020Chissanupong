valid_pieces = {"K", "P", "B", "R", "Q"}

def print_board(board_grid):
    if board_grid is None:
        return None
    
    for row in board_grid:
        print(row)

def parse_board(board_text):
    if not board_text:
        return None
    rows = board_text.splitlines()
    if not rows:
        return None
    board_grid = []
    size = len(rows)

    for row in rows:
        if len(row) != size:
            print("It is not a square!")
            return None
        else:
            board_grid.append(list(row))        

    return board_grid

def normalize_board(board_grid):
    if board_grid is None:
        return None
    
    n = len(board_grid)

    for r in range(n):
        for c in range(n):
            board_grid[r][c] = board_grid[r][c].upper()
            if board_grid[r][c] not in valid_pieces:
                board_grid[r][c] = "."

    return board_grid

def find_pieces(board_grid, pieces=None):
    if board_grid is None:
        return []
    if pieces is None:
        print("Piece argument is required")
        return []
    
    n = len(board_grid)
    pos = []
    for r in range(n):
        for c in range(n):
            if board_grid[r][c] == pieces:
                pos.append((r, c))
    if pieces == "K" and len(pos) != 1:
        print("There can only be one king.")
        return []
    return pos

def pawn_check(pawn_positions, kr, kc):
    for pr, pc in pawn_positions:
        if pr == kr + 1 and pc in (kc - 1, kc + 1):
            return True
    return False

def rook_check(board_grid, kr, kc):
    n = len(board_grid)

    # UP
    r = kr - 1
    while r >= 0:
        if board_grid[r][kc] != ".":
            return board_grid[r][kc] == "R"
        r -= 1

    # DOWN
    r = kr + 1
    while r < n:
        if board_grid[r][kc] != ".":
            return board_grid[r][kc] == "R"
        r += 1

    # LEFT
    c = kc - 1
    while c >= 0:
        if board_grid[kr][c] != ".":
            return board_grid[kr][c] == "R"
        c -= 1

    # RIGHT
    c = kc + 1
    while c < n:
        if board_grid[kr][c] != ".":
            return board_grid[kr][c] == "R"
        c += 1

    return False

def bishop_check(board_grid, kr, kc):
    n = len(board_grid)

    directions = [(-1, -1), (-1,  1), (1, -1), (1,  1)]

    for dr, dc in directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            if board_grid[r][c] != ".":
                if board_grid[r][c] == "B":
                    return True
                else:
                    break
            else:
                r += dr
                c += dc

    return False

def queen_check(board_grid, kr, kc):
    n = len(board_grid)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dr, dc in directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            if board_grid[r][c] != ".":
                if board_grid[r][c] == "Q":
                    return True
                break
            r += dr
            c += dc

    return False

def checkmate(board_text):
    raw_parse = parse_board(board_text)
    if raw_parse is None:
        return
    board_grid = normalize_board(raw_parse)
    print_board(board_grid)

    king_pos = find_pieces(board_grid,"K")
    pawn_pos = find_pieces(board_grid,"P")
    bishop_pos = find_pieces(board_grid,"B")
    rook_pos = find_pieces(board_grid,"R")
    queen_pos = find_pieces(board_grid,"Q")

    #score
    checkmate = 0

    # King
    if not king_pos:
        return
    kr,kc = king_pos[0]
    # print(f"King position: {king_pos}")

    #Pawn
    # print(f"Pawn position: {pawn_pos}")
    if pawn_check(pawn_pos, kr, kc):
        checkmate += 1
        # print("Pawn Checkmate")
    
    #Bishop
    # print(f"Bishop position: {bishop_pos}")
    if bishop_check(board_grid, kr, kc):
        checkmate += 1
        # print("Bishop Checkmate")

    #Rook
    # print(f"Rook position: {rook_pos}")
    if rook_check(board_grid, kr, kc):
        checkmate += 1
        # print("Rook Checkmate")

    #Queen
    # print(f"Queen position: {queen_pos}")
    if queen_check(board_grid, kr, kc):
        checkmate += 1
        # print("Queen Checkmate")

    if checkmate > 0:
        # print(checkmate)
        print("Success")
    else:
        print("Fail")
