import random, math

VAR = 326
X1min = -25
X2min = -15
X3min = -5
X1max = -5
X2max = 35
X3max = 60
XaverageMIN = (X1min+X2min+X3min)/3
XaverageMAX = (X1max+X2max+X3max)/3
Ymin = 200 + XaverageMIN
Ymax = 200 + XaverageMAX
# Оформлення таблиці експерименту
print("y^ = b0 + b1x1 + b2x2 + b3x3")
print("\nМатриця планування експерименту:")
Line = "."
MatrixZ1 = "  N   |  x0  |  x1  |  x2  |  x3  |"
print(MatrixZ1)
numXplan = ["-1","-1","-1","-1","+1","+1","+1","-1","+1","+1","+1","-1"]
It = 0
for i in range(4):
    print(Line*7*5)
    LS = " "*5+"|"
    LF = " "*4+"|"
    print(str(i)+LS+str(1)+LS+numXplan[It]+LF+numXplan[It+1]+LF+numXplan[It+2]+LF)
    It += 3
# Оформлення матриці планування експерименту
X11 = X12 = -25
X13 = X14 = -5
X21 = X23 = -15
X22 = X24 = 35
X31 = X34 = -5
X32 = X33 = 60
# Формування матриці планування експерименту
MatrixZ2 = "N     |  X1  |  X2  |  X3  |  Y1  |  Y2  |  Y3  |"
StrY1 = "1     |  -25  | -15  |  -5  |"
StrY2 = "2     |  -25  |  35  |  60  |"
StrY3 = "3     |   -5  | -15  |  60  |"
StrY4 = "4     |   -5  |  35  |  -5  |"
LstY1 = []
LstY2 = []
LstY3 = []
LstY4 = []

for j1 in range(3):
    numYij1 = random.randrange(int(Ymin),int(Ymax),1)
    LstY1.append(numYij1)
    Z1 = str(float(numYij1))
    StrY1 += Z1+" "*(6-len(Z1))+"|"
for j2 in range(3):
    numYij2 = random.randrange(int(Ymin),int(Ymax),1)
    LstY2.append(numYij2)
    Z2 = str(float(numYij2))
    StrY2 += Z2+" "*(6-len(Z2))+"|"
for j3 in range(3):
    numYij3 = random.randrange(int(Ymin),int(Ymax),1)
    LstY3.append(numYij3)
    Z3 = str(float(numYij3))
    StrY3 += Z3+" "*(6-len(Z3))+"|"
for j4 in range(3):
    numYij4 = random.randrange(int(Ymin),int(Ymax),1)
    LstY4.append(numYij4)
    Z4 = str(float(numYij4))
    StrY4 += Z4+" "*(6-len(Z4))+"|"
# заповнення матриці
print("\n\n"+MatrixZ2+"\n"+Line*49)
print(StrY1+"\n"+Line*49+"\n"+StrY2+"\n"+Line*49+"\n"+StrY3+"\n"+Line*49+"\n"+StrY4)
# Знайдемо середні значення функції відгуку за рядками:
Y1average = (LstY1[0]+LstY1[1]+LstY1[2])/3
Y2average = (LstY2[0]+LstY2[1]+LstY2[2])/3
Y3average = (LstY3[0]+LstY3[1]+LstY3[2])/3
Y4average = (LstY4[0]+LstY4[1]+LstY4[2])/3
mx1 = (X11+X12+X13+X14)/4
mx2 = (X21+X22+X23+X24)/4
mx3 = (X31+X32+X33+X34)/4
my = (Y1average+Y2average+Y3average+Y4average)/4
a1 = (X11*Y1average+X12*Y2average+X13*Y3average+X14*Y4average)/4
a2 = (X21*Y1average+X22*Y2average+X23*Y3average+X24*Y4average)/4
a3 = (X31*Y1average+X32*Y2average+X33*Y3average+X34*Y4average)/4
a11 = (X11*X11+X12*X12+X13*X13+X14*X14)/4
a22 = (X21*X21+X22*X22+X23*X23+X24*X24)/4
a33 = (X31*X31+X32*X32+X33*X33+X34*X34)/4
a12 = a21 = (X11*X21+X12*X22+X13*X23+X14*X24)/4
a13 = a31 = (X11*X31+X12*X32+X13*X33+X14*X34)/4
a23 = a32 = (X21*X31+X22*X32+X23*X33+X24*X34)/4
# Функція розрахунку матриць
def Determinant(a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34,a41,a42,a43,a44):
    D1 = a11*((a22*a33*a44)+(a23*a34*a42)+(a24*a32*a43)-(a24*a33*a42)-(a23*a32*a44)-(a22*a34*a43))
    D2 = a12*((a21*a33*a44)+(a23*a34*a41)+(a24*a31*a43)-(a24*a33*a41)-(a23*a31*a44)-(a21*a34*a43))
    D3 = a13*((a21*a32*a44)+(a22*a34*a41)+(a24*a31*a42)-(a24*a32*a41)-(a31*a22*a44)-(a21*a34*a42))
    D4 = a14*((a21*a32*a43)+(a22*a33*a41)+(a23*a31*a42)-(a23*a32*a41)-(a22*a31*a43)-(a21*a33*a42))
    return D1-D2+D3-D4
# Розрахунок b0,b1,b2,b3
Det1 = Determinant(my,mx1,mx2,mx3,a1,a11,a12,a13,a2,a12,a22,a32,a3,a13,a23,a33)
Det2 = Determinant(1,mx1,mx2,mx3,mx1,a11,a12,a13,mx2,a12,a22,a32,mx3,a13,a23,a33)
Det3 = Determinant(1,my,mx2,mx3,mx1,a1,a12,a13,mx2,a2,a22,a32,mx3,a3,a23,a33)
Det4 = Determinant(1,mx1,mx2,mx3,mx1,a11,a12,a13,mx2,a12,a22,a32,mx3,a13,a23,a33)
Det5 = Determinant(1,mx1,my,mx3,mx1,a11,a1,a13,mx2,a12,a2,a32,mx3,a13,a3,a33)
Det6 = Determinant(1,mx1,mx2,mx3,mx1,a11,a12,a13,mx2,a12,a22,a32,mx3,a13,a23,a33)
Det7 = Determinant(1,mx1,mx2,my,mx1,a11,a12,a1,mx2,a12,a22,a2,mx3,a13,a23,a3)
Det8 = Determinant(1,mx1,mx2,mx3,mx1,a11,a12,a13,mx2,a12,a22,a32,mx3,a13,a23,a33)
b0 = round(Det1/Det2,3);B0 = ""
b1 = round(Det3/Det4,3);B1 = ""
b2 = round(Det5/Det6,3);B2 = ""
b3 = round(Det7/Det8,3);B3 = ""
print("\nРівняння регресії:")
if b0>=0:
    B0 = "+"+str(b0)
else:B0 = str(b0)
if b1>=0:
    B1 = "+"+str(b1)
else:B1 = str(b1)
if b2>=0:
    B2 = "+"+str(b2)
else:B2 = str(b2)
if b3>=0:
    B3 = "+"+str(b3)
else:B3 = str(b3)
print(B0+B1+"*x1"+B2+"*x2"+B3+"*x3")
# Проведення перевірки
Y1averageEX = b0 + b1*X11 + b2*X21 + b3*X31
Y2averageEX = b0 + b1*X12 + b2*X22 + b3*X32
Y3averageEX = b0 + b1*X13 + b2*X23 + b3*X33
Y4averageEX = b0 + b1*X14 + b2*X24 + b3*X34
#критерій Кохрена:
#дисперсії:
S2Y1 = (1/3)*((LstY1[0]-Y1averageEX)**2+(LstY1[1]-Y1averageEX)**2+(LstY1[2]-Y1averageEX)**2)
S2Y2 = (1/3)*((LstY2[0]-Y2averageEX)**2+(LstY2[1]-Y2averageEX)**2+(LstY2[2]-Y2averageEX)**2)
S2Y3 = (1/3)*((LstY3[0]-Y3averageEX)**2+(LstY3[1]-Y3averageEX)**2+(LstY3[2]-Y3averageEX)**2)
S2Y4 = (1/3)*((LstY4[0]-Y4averageEX)**2+(LstY4[1]-Y4averageEX)**2+(LstY4[2]-Y4averageEX)**2)
S2max = [S2Y1,S2Y2,S2Y3,S2Y4]
Gp = (max(S2max)/(S2Y1+S2Y2+S2Y3+S2Y4))
#відповідно до табл:
f1 = 2
f2 = 4
Gt = 0.7679
print("\nПеревірка однорідності дисперсії за критерієм Кохрена:")
if Gp < Gt:
    print("Gp = "+str(round(Gp,4)))
    print("Дисперсія однорідна")
else:
    print("Gp = " + str(round(Gp, 4)))
    print("Дисперсія НЕ однорідна!")
# оцінимо значимість коефіцієнтів регресії згідно  критерію Стьюдента:
print("\nOцінимо значимість коефіцієнтів регресії згідно критерію Стьюдента:")
S2B = (S2Y1+S2Y2+S2Y3+S2Y4)/4
S2Bs = S2B/12
SBs = math.sqrt(S2Bs)
beta0 = 0.25*(Y1averageEX+Y2averageEX+Y3averageEX+Y4averageEX)
beta1 = 0.25*(Y3averageEX+Y4averageEX-Y1averageEX-Y2averageEX)
beta2 = 0.25*(Y2averageEX+Y4averageEX-Y1averageEX-Y3averageEX)
beta3 = 0.25*(Y2averageEX+Y3averageEX-Y1averageEX-Y4averageEX)
def dodatny(a):
    if a > 0:
        return a
    elif a < 0:
        return a*(-1)
    else:
        return 0
t0 = dodatny(beta0)/SBs
t1 = dodatny(beta1)/SBs
t2 = dodatny(beta2)/SBs
t3 = dodatny(beta3)/SBs
tTabl = 2.306
Stiudent = "y = "
Y11 = 0
Y22 = 0
Y33 = 0
Y44 = 0
if t0>tTabl:
    Stiudent += str(round(b0,3))
    Y11 += b0
    Y22 += b0
    Y33 += b0
    Y44 += b0
if t1>tTabl:
    Stiudent += ("+(" + str(round(b1, 3)) + ")*x1")
    Y11 += b1*X11
    Y22 += b1*X12
    Y33 += b1*X13
    Y44 += b1*X14
if t2>tTabl:
    Stiudent += ("+(" + str(round(b2, 3)) + ")*x2")
    Y11 += b2 * X21
    Y22 += b2 * X22
    Y33 += b2 * X23
    Y44 += b2 * X24
if t3>tTabl:
    Stiudent += ("+(" + str(round(b3, 3)) + ")*x3")
    Y11 += b3 * X31
    Y22 += b3 * X32
    Y33 += b3 * X33
    Y44 += b3 * X34
print(Stiudent)
# Крітерій Фішера
print("\nКритерій Фішера:")
f3 = 8
f4 = 2
S2AD = 1.5*((Y11 - Y1averageEX)**2+(Y22 - Y2averageEX)**2+(Y33 - Y3averageEX)**2+(Y44 - Y4averageEX)**2)
Fp = S2AD/S2B
Ft = 4.5
if Fp > Ft:
    print("Fp = "+str(round(Fp,3))+"\nРівняння регресії неадекватно оригіналу при рівні значимості 0.05")
else:
    print("Fp = " + str(round(Fp, 3)) + "\nРівняння регресії адекватно оригіналу при рівні значимості 0.05")
