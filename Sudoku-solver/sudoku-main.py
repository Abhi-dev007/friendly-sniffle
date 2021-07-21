import tkinter
import solve_sudoku
import display_invalid
import display_sudoku

mainWindow = tkinter.Tk()
mainWindow.title('Sudoku Solver')
mainWindow.geometry('640x480')

label = tkinter.Label(mainWindow, text="Enter the values of Sudoku", font=('Arial', 14, 'bold'))
label.pack(pady=10)
canvas = tkinter.Canvas(mainWindow, width=362, height=362)
canvas.place(x=140, y=60)

entry_sudoku = [[None] * 9 for _ in range(9)]

row_x = 0
col_y = 0
for row in range(9):
    if row % 3 == 0:
        col_y += 1
    for col in range(9):
        entry_sudoku[row][col] = tkinter.Entry(canvas, fg='blue',
                                               font=('Arial', 12, 'bold'), justify='center'
                                               )
        # entry_sudoku[row][col].config(highlightthickness=1, highlightcolor="red", highlightbackground='black')
        if col % 3 == 0:
            row_x += 1
        entry_sudoku[row][col].place(x=row_x, y=col_y, width=40, height=40)
        row_x = row_x + 40

    col_y = col_y + 40
    row_x = 0

canvas.create_line(121, 0, 121, 362, fill='black')
canvas.create_line(242, 0, 242, 362, fill='black')
canvas.create_line(0, 121, 362, 121, fill='black')
canvas.create_line(0, 242, 362, 242, fill='black')


def get_sudoku():
    initial_sudoku = [[None] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            initial_sudoku[i][j] = entry_sudoku[i][j].get()
    mainWindow.destroy()
    if solve_sudoku.valid(initial_sudoku):
        answer = solve_sudoku.solve()
        # print(answer)
        display_sudoku.answer_display(answer, initial_sudoku)
        # print("Y1")
    else:
        display_invalid.display_invalid_window()


button1 = tkinter.Button(mainWindow, text='solve!', width=50, fg='white', background='black',
                         command=get_sudoku)

# button1.place(x=140, y=440)
button1.pack(side='bottom', pady=10)

mainWindow.mainloop()
