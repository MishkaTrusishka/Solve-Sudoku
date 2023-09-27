def main():
    solve_sudoku()   

def solve_sudoku(puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]):
 
    for count in range(10):
        for a in range(1):  
            for i in range(9):
                for j in range(9):
                    if puzzle[i][j] == 0:
                        digitals = [1,2,3,4,5,6,7,8,9] 
                        if i<3 and j<3:
                            for m in range(3):
                                for n in range(3):
                                    if puzzle[m][n] in digitals:
                                        digitals.remove(puzzle[m][n])

                        if i<3 and j>2 and j<6:
                            for m in range(3):
                                for n in range(3,6):
                                    if puzzle[m][n] in digitals:
                                        digitals.remove(puzzle[m][n])

                        if i<3 and j>5 and j<9:
                            for m in range(3):
                                for n in range(6,9):
                                    if puzzle[m][n] in digitals:
                                        digitals.remove(puzzle[m][n])

                        if i>2 and i<6 and j<3:
                            for m in range(3,6):
                                for n in range(3):
                                    if puzzle[m][n] in digitals:
                                        digitals.remove(puzzle[m][n])

                        if i>2 and i<6 and j>2 and j<6:
                            for m in range(3,6):
                                for n in range(3,6):
                                    if puzzle[m][n] in digitals:
                                        digitals.remove(puzzle[m][n])

                        if i>2 and i<6 and j>5 and j<9:
                            for m in range(3,6):
                                for n in range(6,9):
                                    if puzzle[m][n] in digitals:
                                        digitals.remove(puzzle[m][n])

                        if i>5 and i<9 and j<3:
                            for m in range(6,9):
                                for n in range(3):
                                    if puzzle[m][n] in digitals:
                                        digitals.remove(puzzle[m][n])

                        if i>5 and i<9 and j>2 and j<6:
                            for m in range(6,9):
                                for n in range(3,6):
                                    if puzzle[m][n] in digitals:
                                        digitals.remove(puzzle[m][n])

                        if i>5 and i<9 and j>5 and j<9:
                            for m in range(6,9):
                                for n in range(6,9):
                                    if puzzle[m][n] in digitals:
                                        digitals.remove(puzzle[m][n])
                        for m in range(9):
                            if puzzle[m][j] in digitals:
                                digitals.remove(puzzle[m][j])
                        for n in range(9):
                            if puzzle[i][n] in digitals:
                                digitals.remove(puzzle[i][n])
                        if len(digitals) == 1:
                            puzzle[i][j] = digitals[0]

    print(puzzle)

if __name__ == "__main__":
    main()
