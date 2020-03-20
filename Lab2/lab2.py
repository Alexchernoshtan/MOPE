import random
import math
M = 5
R = 2
X1min = -25
X1max = -5
X2min = -15
X2max = 35
print("***Варіант = 326***")
print("|  Ymin=0 Ymax=100 | X1min=-25  X1max=-5 | X2min=-15 X2max=35  |")
print("\nЛінійне рівняння регрессії:\nY^= b0 - 15*b1 +  10*b2")
work = True
while work:
    print("\nНормована матриця планування експерименту:")
    LineIS = "*******"*(3+M)
    Matrix = "  N   |X1    |X2    |"
    for i in range(M):
        Matrix += "Y"+str(i+1)+"    |"
    print(Matrix+"\n"+LineIS)
    StrY1 = "  1   |-1.0  |-1.0  |"
    StrY2 = "  2   |-1.0  |+1.0  |"
    StrY3 = "  3   |+1.0  |-1.0  |"
    LstY1 = []
    LstY2 = []
    LstY3 = []
    SumY1 = 0
    SumY2 = 0
    SumY3 = 0
    for j1 in range(M):
        numYij1 = random.randrange(0,100,1)
        LstY1.append(numYij1)
        Z1 = str(float(numYij1))
        StrY1 += Z1+" "*(6-len(Z1))+"|"
        SumY1 += float(numYij1)
    for j2 in range(M):
        numYij2 = random.randrange(0,100,1)
        LstY2.append(numYij2)
        Z2 = str(float(numYij2))
        StrY2 += Z2+" "*(6-len(Z2))+"|"
        SumY2 += float(numYij2)
    for j3 in range(M):
        numYij3 = random.randrange(0,100,1)
        LstY3.append(numYij3)
        Z3 = str(float(numYij3))
        StrY3 += Z3+" "*(6-len(Z3))+"|"
        SumY3 += float(numYij3)
    # заповнення матриці
    print(StrY1+"\n"+LineIS+"\n"+StrY2+"\n"+LineIS+"\n"+StrY3)
    # перевірка однорідності дисперсії за критерієм Романовського
    Y1average = round(float(SumY1/M),2)
    Y2average = round(float(SumY2/M),2)
    Y3average = round(float(SumY3/M),2)
    # 2) розрахунок дисперсії
    dispersion1 = 0
    dispersion2 = 0
    dispersion3 = 0
    for i in range(M):
        dispersion1 += ((LstY1[i] - Y1average) ** 2) / M
        dispersion2 += ((LstY2[i] - Y2average) ** 2) / M
        dispersion3 += ((LstY3[i] - Y3average) ** 2) / M
    # 3) обчислення основного відхилення
    deviation = math.sqrt((2*(2*M-2))/(M*(M-4)))
    # 4) розрахунок Fuv
    Fuv1 = dispersion1/dispersion2
    Fuv2 = dispersion3/dispersion1
    Fuv3 = dispersion3/dispersion2
    # 5) розрахунок θuv
    Our1 = ((M - 2)/M)*Fuv1
    Our2 = ((M - 2)/M)*Fuv2
    Our3 = ((M - 2)/M)*Fuv3
    # 6) розрахунок Ruv
    Ruv1 = math.fabs(Our1-1)/deviation
    Ruv2 = math.fabs(Our2-1)/deviation
    Ruv3 = math.fabs(Our3-1)/deviation
    if Ruv1 < R and Ruv2 < R and Ruv3 < R:
        print("\nДисперсія однорідна")
        # розрахунок нормованих коефіцієнтів рів-ня регресії
        X11 = -1.0
        X12 = -1.0
        X13 = 1.0
        X21 = -1.0
        X22 = 1.0
        X23 = -1.0
        mx1 = (X11 + X12 + X13)/3
        mx2 = (X21 + X22 + X23)/3
        my = (Y1average + Y2average + Y3average) / 3
        a1 = (X11**2 + X12**2 + X13**3)/3
        a2 = (X11*X21 + X12*X22 + X13*X23)/3
        a3 = (X21**2 + X22**2 + X23**2)/3
        a11 = (X11*Y1average + X12*Y2average + X13*Y3average)/3
        a22 = (X21*Y1average + X22*Y2average + X23*Y3average)/3
        det11 = (my*a1*a3) + (mx1*a2*a22) + (mx2*a11*a2) - (a22*a1*mx2) - (my*a2*a2) - (mx1*a11*a3)
        det12 = (1*a1*a3) + (mx1*a2*mx2) + (mx2*mx1*a2) - (mx2*mx2*a1) - (mx1*mx1*a3) - (1*a2*a2)
        b0 = det11/det12
        det21 = (1*a11*a3) + (my*a2*mx2) + (mx1*a22*mx2) - (mx2*a11*mx2) - (mx1*my*a3) - (1*a22*a2)
        det22 = (1*a1*a3) + (mx1*a2*mx2) + (mx2*mx1*a2) - (mx2*mx2*a1) - (mx1*mx1*a3) - (a2*a2*1)
        b1 = det21/det22
        det31 = (1*a1*a22) + (mx1*a11*mx2) + (mx1*a2*my) - (mx2*a1*my) - (mx1*mx1*a22) - (1*a2*a11)
        det32 = (1*a1*a3) + (mx1*a2*mx2) + (mx1*a2*mx2) - (mx2*a1*mx2) - (mx1*mx1*a3) - (a2*a2*1)
        b2 = det31/det32
        print("\nНормоване рівняння регресії:")
        if b1 <0:
            STRX1 = str(round(b1,2))+"*x1"
        else:
            STRX1 = "+"+str(round(b1,2))+"*x1"
        if b2 <0:
            STRX2 = str(round(b2,2))+"*x2"
        else:
            STRX2 = "+"+str(round(b2,2))+"*x2"
        print("Y = "+str(round(b0,1))+STRX1+STRX2)
        print("Перевірка:")
        Pro1 = round((b0 + (X11 * b1) + (X21 * b2)),2)
        Pro2 = round((b0 + (X12 * b1) + (X22 * b2)),2)
        Pro3 = round((b0 + (X13 * b1) + (X23 * b2)),2)
        if Pro1 == Y1average and Pro2 == Y2average and Pro3 == Y3average:
            print("Результат ЗБІГАЄТЬСЯ")
        else:
            print("Результат НЕ ЗБІГАЄТЬСЯ")
        # проведення натуралізації коефіцієнтів
        deltaX1 = (math.fabs(X1max - X1min)) / 2
        deltaX2 = (math.fabs(X2max - X2min)) / 2
        X10 = (X1max + X1min) / 2
        X20 = (X2max + X2min) / 2
        A0 = b0 - b1*(X10/deltaX1) - b2*(X20/deltaX2)
        A1 = b1/deltaX1
        A2 = b2/deltaX2
        print("\nНатуралізоване рів-ня регресії:")
        if A1 <0:
            STRA1 = str(round(A1,3))+"*x1"
        else:
            STRA1 = "+"+str(round(A1,3))+"*x1"
        if A2 <0:
            STRA2 = str(round(A2,3))+"*x2"
        else:
            STRA2 = "+"+str(round(A2,3))+"*x2"
        print("Y = "+str(round(A0,1))+STRA1+STRA2)
        FinPro1 = round((A0 + (A1 * X1min) + (A2 * X2min)),2)
        FinPro2 = round((A0 + (A1 * X1min) + (A2 * X2max)),2)
        FinPro3 = round((A0 + (A1 * X1max) + (A2 * X2min)),2)
        if FinPro1 == Y1average and FinPro2 == Y2average and FinPro3 == Y3average:
            print("коефіцієнти ВІРНІ")
        else:
            print("ПОМИЛКА!")
        work = False
    else:
        M += 1
        print("\n!!!Збільшення М=М+1\n")
