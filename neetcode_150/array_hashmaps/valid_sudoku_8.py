def isValidSudoku(board):
    from collections import Counter

    #check rows
    for row in board:
        rowmap=Counter(row)
        for k,v in rowmap.items():
            if k!="." and v>1:
                return False

    #check columns
    for col in zip(*board):
        colmap=Counter(col)
        for k,v in colmap.items():
            if k!="." and v>1:
                return False
            
    #check 3x3 grid
    for r1,r2,r3 in zip(board[0::3],board[1::3],board[2::3]):
        for c in range(0,9,3):
            box = r1[c:c+3] + r2[c:c+3] + r3[c:c+3]
            gridmap = Counter(box)
            for k,v in gridmap.items():
                if k!='.' and v>1:
                    return False
    
    return True
    
