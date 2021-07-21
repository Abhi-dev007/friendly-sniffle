row_vals = [[0] * 9 for _ in range(9)]
col_vals = [[0] * 9 for _ in range(9)]
grp_three = [[0] * 9 for _ in range(9)]
grp_three_mp = [[0] * 9 for _ in range(9)]
sudoku_s = [[0] * 9 for _ in range(9)]


def valid(initial_sudoku: list[list[str]]) -> bool:
    for i in range(9):
        for j in range(9):
            if initial_sudoku[i][j]:
                if initial_sudoku[i][j].isnumeric():
                    if 9 >= int(initial_sudoku[i][j]) >= 1:
                        sudoku_s[i][j] = int(initial_sudoku[i][j])
                    else:
                        return False
                else:
                    return False
            else:
                sudoku_s[i][j] = -1
    # rows
    for i in range(9):
        for j in range(9):
            if sudoku_s[i][j] != -1:
                row_vals[i][sudoku_s[i][j] - 1] += 1
                if row_vals[i][sudoku_s[i][j] - 1] > 1:
                    return False
    # cols
    for i in range(9):
        for j in range(9):
            if sudoku_s[j][i] != -1:
                col_vals[i][sudoku_s[j][i] - 1] += 1
                if col_vals[i][sudoku_s[j][i] - 1] > 1:
                    return False

    # grp_three
    mp = 0
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    if sudoku_s[k][l] != -1:
                        grp_three[mp][sudoku_s[k][l] - 1] += 1
                        if grp_three[mp][sudoku_s[k][l] - 1] > 1:
                            return False
            mp += 1

    # grp_three_mp
    grp_three_mp[0][0] = 0
    grp_three_mp[0][6] = 2
    grp_three_mp[1][3] = 4
    grp_three_mp[2][0] = 6
    grp_three_mp[2][6] = 8
    grp_three_mp[0][3] = 1
    grp_three_mp[1][0] = 3
    grp_three_mp[1][6] = 5
    grp_three_mp[2][3] = 7

    return True


def backtrack(sudoku_s: list[list[int]], blank_pos: list[list[int]], cur: int) -> bool:
    if cur >= len(blank_pos):
        return True

    row = blank_pos[cur][0]
    col = blank_pos[cur][1]

    for i in range(9):
        xs = row // 3
        ys = (col // 3) * 3
        if row_vals[row][i] == 0 and col_vals[col][i] == 0 and grp_three[grp_three_mp[xs][ys]][i] == 0:
            sudoku_s[row][col] = i + 1
            row_vals[row][i] += 1
            col_vals[col][i] += 1
            grp_three[grp_three_mp[xs][ys]][i] += 1

            if backtrack(sudoku_s, blank_pos, cur + 1):
                return True

            sudoku_s[row][col] = -1
            row_vals[row][i] -= 1
            col_vals[col][i] -= 1
            grp_three[grp_three_mp[xs][ys]][i] -= 1

    return False


def solve() -> list[list[str]]:
    for l in range(9):
        for k in range(9):  # k is row
            for i in range(9):
                if row_vals[k][i] == 0:
                    cnt = 0
                    pos = 0
                    for j in range(9):  # j is col
                        if sudoku_s[k][j] == -1:
                            x = k // 3
                            y = (j // 3) * 3
                            if col_vals[j][i] == 0 and grp_three[grp_three_mp[x][y]][i] == 0:
                                pos = j
                                cnt += 1

                    if cnt == 1:
                        sudoku_s[k][pos] = i + 1
                        row_vals[k][i] += 1
                        col_vals[pos][i] += 1
                        x = k // 3
                        y = (pos // 3) * 3
                        grp_three[grp_three_mp[x][y]][i] += 1

        for k in range(9):  # k is col
            for i in range(9):
                if col_vals[k][i] == 0:
                    cnt = 0
                    pos = 0
                    for j in range(9):  # j is row
                        if sudoku_s[j][k] == -1:
                            x = j // 3
                            y = (k // 3) * 3
                            if row_vals[j][i] == 0 and grp_three[grp_three_mp[x][y]][i] == 0:
                                pos = j
                                cnt += 1

                    if cnt == 1:
                        sudoku_s[pos][k] = i + 1
                        row_vals[pos][i] += 1
                        col_vals[k][i] += 1
                        x = pos // 3
                        y = (k // 3) * 3
                        grp_three[grp_three_mp[x][y]][i] += 1

    blank_pos = []
    for i in range(9):
        for j in range(9):
            if sudoku_s[i][j] == -1:
                t = [i, j]
                blank_pos.append(t)
    backtrack(sudoku_s, blank_pos, 0)

    answer = [[None] * 9 for _ in range(9)]

    for row in range(9):
        for col in range(9):
            if sudoku_s[row][col] != -1:
                answer[row][col] = str(sudoku_s[row][col])

    return answer
