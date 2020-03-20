from random import randrange
from tkinter import *


root = Tk()
root.title("Lab №1")
Label(root, text='№', font='Arial 10').grid(column=0, row=0)
for i in range(1, 9):
    Label(root, text=str(i), font='Arial 10').grid(column=0, row=i)

Label(root, text='Xo', font='Arial 10').grid(column=0, row=9)
Label(root, text='dx', font='Arial 10').grid(column=0, row=10)
for j in range(1, 4):
    Label(root, text='X{}'.format(j), font='Arial 10').grid(column=j, row=0)
    Label(root, text='Xн{}'.format(j), font='Arial 10').grid(column=j+4, row=0)

Label(root, text='Y', font='Arial 10').grid(column=4, row=0)

M, N = 3, 8
matrix = [[randrange(0, 20) for y in range(M)] for x in range(N)]
a0, a1, a2, a3 = 1, 2, 3, 4
lst_y = []
lst_x0 = []
lst_dx = []
for i in range(3):
    lst = []
    for j in range(8):
        lst.append(matrix[j][i])
    x_min = min(lst)
    x_max = max(lst)
    x_0 = (x_max + x_min) / 2
    dx = x_0 - x_min
    lst_x0.append(x_0)
    lst_dx.append(dx)
    lst.clear()

matrix.append(lst_x0)
matrix.append(lst_dx)

for i in range(10):
    lst = matrix[i]
    y = a0 + a1*lst[0] + a2*lst[1] + a3*lst[2]
    lst.append(y)
    lst_y.append(y)

for i in range(3):
    for j in range(9):
        x_n = (matrix[j][i] - lst_x0[i]) / lst_dx[i]
        matrix[j].append(x_n)

for i in range(3):
    matrix[9].append(0)

for i in range(10):
    for j in range(7):
        Button(root, text=str('{:.1f}'.format(matrix[i][j])), font='Arial 10',
               width=5, height=2).grid(column=j+1, row=i+1)


lst_with_criterion = []
for i in range(8):
    lst_with_criterion.append((lst_y[i]-lst_y[8])**2)

lst_with_factors = matrix[lst_with_criterion.index(max(lst_with_criterion))]
Label(root, text='Max (Y - Y(ref))**2: {}'.format(max(lst_with_criterion)), font='Arial 10',
      fg='red').grid(row=11, column=0, columnspan=8)
Label(root, text='Reference Y: {}'.format(lst_y[8]), font='Arial 10', fg='red').grid(row=12, column=0, columnspan=8)
Label(root, text='Factor value: {}, {}, {}'.format(lst_with_factors[0], lst_with_factors[1], lst_with_factors[2]),
      font='Arial 10', fg='red').grid(row=13, column=0, columnspan=8)

root.mainloop()
