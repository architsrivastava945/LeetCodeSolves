class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        Columns = [set(range(1,10)) for _ in range(9)]
        rows = [set(range(1,10)) for _ in range(9)]
        grids = [set(range(1,10)) for _ in range(9)]

        for i in range(9):
            for j in range(9):
                grid_no = (3*(i//3))+(j//3)
                element = board[i][j]
                if element == '.':
                    continue
                else:
                    element = int(element)
                if element in Columns[j] and element in rows[i] and element in grids[grid_no]:
                    Columns[j].remove(element)
                    rows[i].remove(element)
                    grids[grid_no].remove(element)
                    continue
                return False
        
        return True

                
            