import random, math, numpy

# Вхідні дані за варінтом
m = 2
NomVar = 326
X1min = -20
X2min = 25
X3min = 10
X1max = 15
X2max = 45
X3max = 20
X1LIST = [-20,15]
X2LIST = [25,45]
X3LIST = [10,20]
XaverMIN = (X1min + X2min + X3min)/3
XaverMAX = (X1max + X2max + X3max)/3
Yimin = 200 + XaverMIN
Yimax = 200 + XaverMAX
X0line = "1"
X1line = ["-1","-1","-1","-1","+1","+1","+1","+1"]
X2line = ["-1","-1","+1","+1","-1","-1","+1","+1"]
X3line = ["-1","+1","-1","+1","-1","+1","-1","+1"]
X1X2line = []
X1X3line = []
X2X3line = []
X1X2X3line = []
Yij = []
Yiaverage = []
S2y = []
print("\nрівняння регресії з ефектом взаємодії:")
print("ŷ = b0 + b1*x1 + b2*x2 + b3*x3 + b12*x1*x2 + b13*x1*x3 + b23*x2*x3 + b123*x1*x2*x3")

work = True
while work:
    m += 1
    # формування таблиці
    linepodch = "------+"
    def tabl10():
        namestring = "|"
        name = ["i", "x0", "x1", "x2", "x3", "x1x2", "x1x3", "x2x3", "x1x2x3","Yi1","Yi2","Yi3","Yaver","S2y"]
        nametabl = "\nМатриця ПФЕ:"
        for i in range(len(name)):
            namestring += (name[i] + " " * (6 - len(name[i])) + "|")
        return nametabl + "\n" + namestring + "\n+" + linepodch * 14

    def ZNAK(a):
        if a > 0:
            b = "+"+str(a)
        else:
            b = str(a)
        return b
    TABLznach = []
    def tabl11():
        nameznach = "|"
        count1 = 0
        for i in range(8):
            nameznach += (str(i+1) + " " * (6 - len(str(i+1))) + "|")
            nameznach += (X0line + " " * (6 - len(str(X0line))) + "|")
            nameznach += (X1line[i] + " " * (6 - len(str(X1line[i]))) + "|")
            nameznach += (X2line[i] + " " * (6 - len(str(X2line[i]))) + "|")
            nameznach += (X3line[i] + " " * (6 - len(str(X3line[i]))) + "|")
            nameznach += (ZNAK(int(X1line[i]) * int(X2line[i])) + " " * (6 - len(ZNAK(int(X1line[i]) * int(X2line[i])))) + "|")
            nameznach += (ZNAK(int(X1line[i]) * int(X3line[i])) + " " * (6 - len(ZNAK(int(X1line[i]) * int(X3line[i])))) + "|")
            nameznach += (ZNAK(int(X2line[i]) * int(X3line[i])) + " " * (6 - len(ZNAK(int(X2line[i]) * int(X3line[i])))) + "|")
            nameznach += (ZNAK(int(X1line[i]) * int(X2line[i]) * int(X3line[i])) + " " * (6 - len(ZNAK(int(X1line[i]) * int(X2line[i]) * int(X3line[i])))) + "|")
            X1X2line.append(ZNAK(int(X1line[i])*int(X2line[i])))
            X1X3line.append(ZNAK(int(X1line[i]) * int(X2line[i])))
            X2X3line.append(ZNAK(int(X1line[i]) * int(X2line[i])))
            X1X2X3line.append(ZNAK(int(X1line[i]) * int(X2line[i])))
            SUM1 = 0
            for j in range(m):
                A = random.randrange(int(Yimin),int(Yimax),1)
                nameznach += (str(A) + " " * (6 - len(str(A))) + "|")
                Yij.append(A)
                SUM1 += A
            Yiaverage.append(round(float(SUM1/m),2))
            nameznach += (str(Yiaverage[i]) + " " * (6 - len(str(Yiaverage[i]))) + "|")
            SUM2 = 0
            for k in range(m):
                SUM2 += (Yij[count1+k] - Yiaverage[i]) ** 2
            count1 += 3
            nameznach += (str(round(SUM2/m,2)) + " " * (6 - len(str(round(SUM2/m,2)))) + "|")
            S2y.append(round(SUM2/m,2))
            print(nameznach)
            print("+"+linepodch * 14)
            nameznach = "|"
        return " "
    print(tabl10())
    print(tabl11())
    # розрахунок коефіціентів
    m0i = [8]
    m1i = [0]
    m2i = [0]
    m3i = [0]
    m4i = [0]
    m5i = [0]
    m6i = [0]
    m7i = [0]
    k = [0]
    for i in range(7):
        m0i.append(0)
        m1i.append(0)
        m2i.append(0)
        m3i.append(0)
        m4i.append(0)
        m5i.append(0)
        m6i.append(0)
        m7i.append(0)
        k.append(0)
    def Module(a):
        if int(a) < 0:
            return a*(-1)
        else:
            return a
    def REAL(a,b):
        if int(b) > 0:
            return a[1]
        else:
            return a[0]
    S = 0
    for i in range(8):
        m0i[1] += REAL(X1LIST, X1line[i])
        m0i[2] += REAL(X2LIST, X2line[i])
        m0i[3] += REAL(X3LIST, X3line[i])
        m0i[4] += (REAL(X1LIST, X1line[i]) * REAL(X2LIST, X2line[i]))
        m0i[5] += (REAL(X1LIST, X1line[i]) * REAL(X3LIST, X3line[i]))
        m0i[6] += (REAL(X2LIST, X2line[i]) * REAL(X3LIST, X3line[i]))
        m0i[7] += (REAL(X1LIST, X1line[i]) * REAL(X2LIST, X2line[i]) * REAL(X3LIST, X3line[i]))
        m1i[0] += REAL(X1LIST, X1line[i])
        m1i[1] += (REAL(X1LIST, X1line[i])) ** 2
        m1i[2] += (REAL(X1LIST, X1line[i]) * REAL(X2LIST, X2line[i]))
        m1i[3] += (REAL(X1LIST, X1line[i]) * REAL(X3LIST, X3line[i]))
        m1i[4] += (((REAL(X1LIST, X1line[i])) ** 2) * REAL(X2LIST, X2line[i]))
        m1i[5] += (((REAL(X1LIST, X1line[i])) ** 2) * REAL(X3LIST, X3line[i]))
        m1i[6] += (REAL(X1LIST, X1line[i]) * REAL(X2LIST, X2line[i]) * REAL(X3LIST, X3line[i]))
        m1i[7] += (((REAL(X1LIST, X1line[i])) ** 2) * REAL(X2LIST, X2line[i]) * REAL(X3LIST, X3line[i]))
        m2i[0] += REAL(X2LIST, X2line[i])
        m2i[1] += (REAL(X1LIST, X1line[i]) * REAL(X2LIST, X2line[i]))
        m2i[2] += (REAL(X2LIST, X2line[i])) ** 2
        m2i[3] += (REAL(X2LIST, X2line[i]) * REAL(X3LIST, X3line[i]))
        m2i[4] += (REAL(X1LIST, X1line[i]) * ((REAL(X2LIST, X2line[i])) ** 2))
        m2i[5] += (REAL(X1LIST, X1line[i]) * REAL(X2LIST, X2line[i]) * REAL(X3LIST, X3line[i]))
        m2i[6] += (((REAL(X2LIST, X2line[i])) ** 2) * REAL(X3LIST, X3line[i]))
        m2i[7] += (REAL(X1LIST, X1line[i]) * ((REAL(X2LIST, X2line[i])) ** 2) * REAL(X3LIST, X3line[i]))
        m3i[0] += REAL(X3LIST, X3line[i])
        m3i[1] += (REAL(X1LIST, X1line[i]) * REAL(X3LIST, X3line[i]))
        m3i[2] += (REAL(X2LIST, X2line[i]) * REAL(X3LIST, X3line[i]))
        m3i[3] += (REAL(X3LIST, X3line[i])) ** 2
        m3i[4] += (REAL(X1LIST, X1line[i]) * REAL(X2LIST, X2line[i]) * REAL(X3LIST, X3line[i]))
        m3i[5] += (REAL(X1LIST, X1line[i]) * ((REAL(X3LIST, X3line[i])) ** 2))
        m3i[6] += (REAL(X2LIST, X2line[i]) * ((REAL(X3LIST, X3line[i])) ** 2))
        m3i[7] += (REAL(X1LIST, X1line[i]) * REAL(X2LIST, X2line[i]) * ((REAL(X3LIST, X3line[i])) ** 2))
        m4i[0] += (REAL(X1LIST, X1line[i]) * REAL(X2LIST, X2line[i]))
        m4i[1] += (((REAL(X1LIST, X1line[i])) ** 2) * REAL(X2LIST, X2line[i]))
        m4i[2] += (REAL(X1LIST, X1line[i]) * ((REAL(X2LIST, X2line[i])) ** 2))
        m4i[3] += (REAL(X1LIST, X1line[i]) * REAL(X2LIST, X2line[i]) * REAL(X3LIST, X3line[i]))
        m4i[4] += (((REAL(X1LIST, X1line[i])) ** 2) * ((REAL(X2LIST, X2line[i])) ** 2))
        m4i[5] += (((REAL(X1LIST, X1line[i])) ** 2) * REAL(X2LIST, X2line[i]) * REAL(X3LIST, X3line[i]))
        m4i[6] += (REAL(X1LIST, X1line[i]) * ((REAL(X2LIST, X2line[i])) ** 2) * REAL(X3LIST, X3line[i]))
        m4i[7] += (((REAL(X1LIST, X1line[i])) ** 2) * ((REAL(X2LIST, X2line[i])) ** 2) * REAL(X3LIST, X3line[i]))
        m5i[0] += (REAL(X1LIST, X1line[i]) * REAL(X3LIST, X3line[i]))
        m5i[1] += (((REAL(X1LIST, X1line[i])) ** 2) * REAL(X3LIST, X3line[i]))
        m5i[2] += (REAL(X1LIST, X1line[i]) * REAL(X2LIST, X2line[i]) * REAL(X3LIST, X3line[i]))
        m5i[3] += (REAL(X1LIST, X1line[i]) * ((REAL(X3LIST, X3line[i])) ** 2))
        m5i[4] += (((REAL(X1LIST, X1line[i])) ** 2) * REAL(X2LIST, X2line[i]) * REAL(X3LIST, X3line[i]))
        m5i[5] += (((REAL(X1LIST, X1line[i])) ** 2) * ((REAL(X3LIST, X3line[i])) ** 2))
        m5i[6] += (REAL(X1LIST, X1line[i]) * REAL(X2LIST, X2line[i]) * ((REAL(X3LIST, X3line[i])) ** 2))
        m5i[7] += (((REAL(X1LIST, X1line[i])) ** 2) * REAL(X2LIST, X2line[i]) * ((REAL(X3LIST, X3line[i])) ** 2))
        m6i[0] += (REAL(X2LIST, X2line[i]) * REAL(X3LIST, X3line[i]))
        m6i[1] += (REAL(X1LIST, X1line[i]) * REAL(X2LIST, X2line[i]) * REAL(X3LIST, X3line[i]))
        m6i[2] += (((REAL(X2LIST, X2line[i])) ** 2) * REAL(X3LIST, X3line[i]))
        m6i[3] += (REAL(X2LIST, X2line[i]) * ((REAL(X3LIST, X3line[i])) ** 2))
        m6i[4] += (REAL(X1LIST, X1line[i]) * ((REAL(X2LIST, X2line[i])) ** 2) * REAL(X3LIST, X3line[i]))
        m6i[5] += (REAL(X1LIST, X1line[i]) * REAL(X2LIST, X2line[i]) * ((REAL(X3LIST, X3line[i])) ** 2))
        m6i[6] += (((REAL(X2LIST, X2line[i])) ** 2) * ((REAL(X3LIST, X3line[i])) ** 2))
        m6i[7] += (REAL(X1LIST, X1line[i]) * ((REAL(X2LIST, X2line[i])) ** 2) * ((REAL(X3LIST, X3line[i])) ** 2))
        m7i[0] += (REAL(X1LIST, X1line[i]) * REAL(X2LIST, X2line[i]) * REAL(X3LIST, X3line[i]))
        m7i[1] += (((REAL(X1LIST, X1line[i])) ** 2) * REAL(X2LIST, X2line[i]) * REAL(X3LIST, X3line[i]))
        m7i[2] += (REAL(X1LIST, X1line[i]) * ((REAL(X2LIST, X2line[i])) ** 2) * REAL(X3LIST, X3line[i]))
        m7i[3] += (REAL(X1LIST, X1line[i]) * REAL(X2LIST, X2line[i]) * ((REAL(X3LIST, X3line[i])) ** 2))
        m7i[4] += (((REAL(X1LIST, X1line[i])) ** 2) * ((REAL(X2LIST, X2line[i])) ** 2) * REAL(X3LIST, X3line[i]))
        m7i[5] += (((REAL(X1LIST, X1line[i])) ** 2) * REAL(X2LIST, X2line[i]) * ((REAL(X3LIST, X3line[i])) ** 2))
        m7i[6] += (REAL(X1LIST, X1line[i]) * ((REAL(X2LIST, X2line[i])) ** 2) * ((REAL(X3LIST, X3line[i])) ** 2))
        m7i[7] += (((REAL(X1LIST, X1line[i])) ** 2) * ((REAL(X2LIST, X2line[i])) ** 2) * ((REAL(X3LIST, X3line[i])) ** 2))
        k[0] += Yiaverage[i]
        k[1] += Yiaverage[i] * (REAL(X1LIST, X1line[i]))
        k[2] += Yiaverage[i] * (REAL(X2LIST, X2line[i]))
        k[3] += Yiaverage[i] * (REAL(X3LIST, X3line[i]))
        k[4] += Yiaverage[i] * (REAL(X1LIST, X1line[i])) * (REAL(X2LIST, X2line[i]))
        k[5] += Yiaverage[i] * (REAL(X1LIST, X1line[i])) * (REAL(X3LIST, X3line[i]))
        k[6] += Yiaverage[i] * (REAL(X2LIST, X2line[i])) * (REAL(X3LIST, X3line[i]))
        k[7] += Yiaverage[i] * (REAL(X1LIST, X1line[i])) * (REAL(X2LIST, X2line[i])) * (REAL(X3LIST, X3line[i]))
    ### розрахунок детермінантів
    Matrix = [[m0i[0], m1i[0], m2i[0], m3i[0], m4i[0], m5i[0], m6i[0], m7i[0]],
              [m0i[1], m1i[1], m2i[1], m3i[1], m4i[1], m5i[1], m6i[1], m7i[1]],
              [m0i[2], m1i[2], m2i[2], m3i[2], m4i[2], m5i[2], m6i[2], m7i[2]],
              [m0i[3], m1i[3], m2i[3], m3i[3], m4i[3], m5i[3], m6i[3], m7i[3]],
              [m0i[4], m1i[4], m2i[4], m3i[4], m4i[4], m5i[4], m6i[4], m7i[4]],
              [m0i[5], m1i[5], m2i[5], m3i[5], m4i[5], m5i[5], m6i[5], m7i[5]],
              [m0i[6], m1i[6], m2i[6], m3i[6], m4i[6], m5i[6], m6i[6], m7i[6]],
              [m0i[7], m1i[7], m2i[7], m3i[7], m4i[7], m5i[7], m6i[7], m7i[7]]]
    B0det =  [[k[0], m1i[0], m2i[0], m3i[0], m4i[0], m5i[0], m6i[0], m7i[0]],
              [k[1], m1i[1], m2i[1], m3i[1], m4i[1], m5i[1], m6i[1], m7i[1]],
              [k[2], m1i[2], m2i[2], m3i[2], m4i[2], m5i[2], m6i[2], m7i[2]],
              [k[3], m1i[3], m2i[3], m3i[3], m4i[3], m5i[3], m6i[3], m7i[3]],
              [k[4], m1i[4], m2i[4], m3i[4], m4i[4], m5i[4], m6i[4], m7i[4]],
              [k[5], m1i[5], m2i[5], m3i[5], m4i[5], m5i[5], m6i[5], m7i[5]],
              [k[6], m1i[6], m2i[6], m3i[6], m4i[6], m5i[6], m6i[6], m7i[6]],
              [k[7], m1i[7], m2i[7], m3i[7], m4i[7], m5i[7], m6i[7], m7i[7]]]
    B1det =  [[m0i[0], k[0], m2i[0], m3i[0], m4i[0], m5i[0], m6i[0], m7i[0]],
              [m0i[1], k[1], m2i[1], m3i[1], m4i[1], m5i[1], m6i[1], m7i[1]],
              [m0i[2], k[2], m2i[2], m3i[2], m4i[2], m5i[2], m6i[2], m7i[2]],
              [m0i[3], k[3], m2i[3], m3i[3], m4i[3], m5i[3], m6i[3], m7i[3]],
              [m0i[4], k[4], m2i[4], m3i[4], m4i[4], m5i[4], m6i[4], m7i[4]],
              [m0i[5], k[5], m2i[5], m3i[5], m4i[5], m5i[5], m6i[5], m7i[5]],
              [m0i[6], k[6], m2i[6], m3i[6], m4i[6], m5i[6], m6i[6], m7i[6]],
              [m0i[7], k[7], m2i[7], m3i[7], m4i[7], m5i[7], m6i[7], m7i[7]]]
    B2det =  [[m0i[0], m1i[0], k[0], m3i[0], m4i[0], m5i[0], m6i[0], m7i[0]],
              [m0i[1], m1i[1], k[1], m3i[1], m4i[1], m5i[1], m6i[1], m7i[1]],
              [m0i[2], m1i[2], k[2], m3i[2], m4i[2], m5i[2], m6i[2], m7i[2]],
              [m0i[3], m1i[3], k[3], m3i[3], m4i[3], m5i[3], m6i[3], m7i[3]],
              [m0i[4], m1i[4], k[4], m3i[4], m4i[4], m5i[4], m6i[4], m7i[4]],
              [m0i[5], m1i[5], k[5], m3i[5], m4i[5], m5i[5], m6i[5], m7i[5]],
              [m0i[6], m1i[6], k[6], m3i[6], m4i[6], m5i[6], m6i[6], m7i[6]],
              [m0i[7], m1i[7], k[7], m3i[7], m4i[7], m5i[7], m6i[7], m7i[7]]]
    B3det =  [[m0i[0], m1i[0], m2i[0], k[0], m4i[0], m5i[0], m6i[0], m7i[0]],
              [m0i[1], m1i[1], m2i[1], k[1], m4i[1], m5i[1], m6i[1], m7i[1]],
              [m0i[2], m1i[2], m2i[2], k[2], m4i[2], m5i[2], m6i[2], m7i[2]],
              [m0i[3], m1i[3], m2i[3], k[3], m4i[3], m5i[3], m6i[3], m7i[3]],
              [m0i[4], m1i[4], m2i[4], k[4], m4i[4], m5i[4], m6i[4], m7i[4]],
              [m0i[5], m1i[5], m2i[5], k[5], m4i[5], m5i[5], m6i[5], m7i[5]],
              [m0i[6], m1i[6], m2i[6], k[6], m4i[6], m5i[6], m6i[6], m7i[6]],
              [m0i[7], m1i[7], m2i[7], k[7], m4i[7], m5i[7], m6i[7], m7i[7]]]
    B12det = [[m0i[0], m1i[0], m2i[0], m3i[0], k[0], m5i[0], m6i[0], m7i[0]],
              [m0i[1], m1i[1], m2i[1], m3i[1], k[1], m5i[1], m6i[1], m7i[1]],
              [m0i[2], m1i[2], m2i[2], m3i[2], k[2], m5i[2], m6i[2], m7i[2]],
              [m0i[3], m1i[3], m2i[3], m3i[3], k[3], m5i[3], m6i[3], m7i[3]],
              [m0i[4], m1i[4], m2i[4], m3i[4], k[4], m5i[4], m6i[4], m7i[4]],
              [m0i[5], m1i[5], m2i[5], m3i[5], k[5], m5i[5], m6i[5], m7i[5]],
              [m0i[6], m1i[6], m2i[6], m3i[6], k[6], m5i[6], m6i[6], m7i[6]],
              [m0i[7], m1i[7], m2i[7], m3i[7], k[7], m5i[7], m6i[7], m7i[7]]]
    B13det = [[m0i[0], m1i[0], m2i[0], m3i[0], m4i[0], k[0], m6i[0], m7i[0]],
              [m0i[1], m1i[1], m2i[1], m3i[1], m4i[1], k[1], m6i[1], m7i[1]],
              [m0i[2], m1i[2], m2i[2], m3i[2], m4i[2], k[2], m6i[2], m7i[2]],
              [m0i[3], m1i[3], m2i[3], m3i[3], m4i[3], k[3], m6i[3], m7i[3]],
              [m0i[4], m1i[4], m2i[4], m3i[4], m4i[4], k[4], m6i[4], m7i[4]],
              [m0i[5], m1i[5], m2i[5], m3i[5], m4i[5], k[5], m6i[5], m7i[5]],
              [m0i[6], m1i[6], m2i[6], m3i[6], m4i[6], k[6], m6i[6], m7i[6]],
              [m0i[7], m1i[7], m2i[7], m3i[7], m4i[7], k[7], m6i[7], m7i[7]]]
    B23det = [[m0i[0], m1i[0], m2i[0], m3i[0], m4i[0], m5i[0], k[0], m7i[0]],
              [m0i[1], m1i[1], m2i[1], m3i[1], m4i[1], m5i[1], k[1], m7i[1]],
              [m0i[2], m1i[2], m2i[2], m3i[2], m4i[2], m5i[2], k[2], m7i[2]],
              [m0i[3], m1i[3], m2i[3], m3i[3], m4i[3], m5i[3], k[3], m7i[3]],
              [m0i[4], m1i[4], m2i[4], m3i[4], m4i[4], m5i[4], k[4], m7i[4]],
              [m0i[5], m1i[5], m2i[5], m3i[5], m4i[5], m5i[5], k[5], m7i[5]],
              [m0i[6], m1i[6], m2i[6], m3i[6], m4i[6], m5i[6], k[6], m7i[6]],
              [m0i[7], m1i[7], m2i[7], m3i[7], m4i[7], m5i[7], k[7], m7i[7]]]
    B123det = [[m0i[0], m1i[0], m2i[0], m3i[0], m4i[0], m5i[0], m6i[0], k[0]],
              [m0i[1], m1i[1], m2i[1], m3i[1], m4i[1], m5i[1], m6i[1], k[1]],
              [m0i[2], m1i[2], m2i[2], m3i[2], m4i[2], m5i[2], m6i[2], k[2]],
              [m0i[3], m1i[3], m2i[3], m3i[3], m4i[3], m5i[3], m6i[3], k[3]],
              [m0i[4], m1i[4], m2i[4], m3i[4], m4i[4], m5i[4], m6i[4], k[4]],
              [m0i[5], m1i[5], m2i[5], m3i[5], m4i[5], m5i[5], m6i[5], k[5]],
              [m0i[6], m1i[6], m2i[6], m3i[6], m4i[6], m5i[6], m6i[6], k[6]],
              [m0i[7], m1i[7], m2i[7], m3i[7], m4i[7], m5i[7], m6i[7], k[7]]]
    B0new = round((numpy.linalg.det(B0det)/numpy.linalg.det(Matrix)), 3)
    B1new = round((numpy.linalg.det(B1det)/numpy.linalg.det(Matrix)), 3)
    B2new = round((numpy.linalg.det(B2det)/numpy.linalg.det(Matrix)), 3)
    B3new = round((numpy.linalg.det(B3det)/numpy.linalg.det(Matrix)), 3)
    B12new = round((numpy.linalg.det(B12det)/numpy.linalg.det(Matrix)), 3)
    B13new = round((numpy.linalg.det(B13det)/numpy.linalg.det(Matrix)), 3)
    B23new = round((numpy.linalg.det(B23det)/numpy.linalg.det(Matrix)), 3)
    B123new = round((numpy.linalg.det(B123det)/numpy.linalg.det(Matrix)), 3)
    Ya1 = str(B0new)+"+("+str(B1new)+")*x1+("+str(B2new)+")*x2+("+str(B3new)+")*x3+("
    Ya2 = str(B12new)+")*x1x2+("+str(B13new)+")*x1x3+("+str(B23new)+")*x2x3+("
    Ya3 = str(B123new)+")*x1x2x3"
    print("рівняння дня натуральних значень факторів:")
    print("Y = "+Ya1+Ya2+Ya3)
    #print(B0new+B1new*(15)+B2new*(-35)+B3new*(-35)+B12new*(-525)+B13new*(-525)+B23new*(1225)+B123new*(91875))

    # Знаходження коефіцієнтів регресії для нормованих значень факторів ПФЕ
    b0new = 0
    b1new = 0
    b2new = 0
    b3new = 0
    b12new = 0
    b13new = 0
    b23new = 0
    b123new = 0
    for i in range(8):
        b0new += Yiaverage[i]
        b1new += Yiaverage[i] * int(X1line[i])
        b2new += Yiaverage[i] * int(X2line[i])
        b3new += Yiaverage[i] * int(X3line[i])
        b12new += Yiaverage[i] * int(X1line[i]) * int(X2line[i])
        b13new += Yiaverage[i] * int(X1line[i]) * int(X3line[i])
        b23new += Yiaverage[i] * int(X2line[i]) * int(X3line[i])
        b123new += Yiaverage[i] * int(X1line[i]) * int(X2line[i]) * int(X3line[i])
    Yb1 = str(round(b0new,3))+"+("+str(round(b1new,3))+")*x1+("+str(round(b2new,3))+")*x2+("+str(round(b3new,3))+")*x3+("
    Yb2 = str(round(b12new,3))+")*x1x2+("+str(round(b13new,3))+")*x1x3+("+str(round(b23new,3))+")*x2x3+("
    Yb3 = str(round(b123new,3))+")*x1x2x3"
    print("рівняння дня нормованих значень факторів:")
    print("Y = "+Yb1+Yb2+Yb3)
    #print((b0new+b1new*(-1)+b2new*(-1)+b3new*(-1)+b12new*(1)+b13new*(1)+b23new*(1)+b123new*(-1))/8)

    # Перевірка однорідності дисперсії за критерієм Кохрена:
    GrK = [0.6798, 0.5157, 0.4377, 0.391, 0.3595, 0.3362, 0.3185, 0.3043, 0.2926, 0.2829]
    S2yMAX = max(S2y)
    Gp = S2yMAX/sum(S2y)
    f1 = m - 1
    f2 = 8
    RZ = 0.05
    if Gp < GrK[f1-1]:
        print("дисперсія однорідна")
        #####  оцінимо значимість коефіцієнтів регресії згідно критерію Стьюдента
        S2B = (1/8)*sum(S2y)
        S2betaS = S2B / (8 * m)
        SbetaS = math.sqrt(S2betaS)
        beta0 = 0
        beta1 = 0
        beta2 = 0
        beta3 = 0
        beta12 = 0
        beta13 = 0
        beta23 = 0
        beta123 = 0
        for i in range(8):
            beta0 += (1 / 8) * (Yiaverage[i] * int(X0line))
            beta1 += (1 / 8) * (Yiaverage[i] * int(X1line[i]))
            beta2 += (1 / 8) * (Yiaverage[i] * int(X2line[i]))
            beta3 += (1 / 8) * (Yiaverage[i] * int(X3line[i]))
            beta12 += (1 / 8) * (Yiaverage[i] * int(X1X2line[i]))
            beta13 += (1 / 8) * (Yiaverage[i] * int(X1X3line[i]))
            beta23 += (1 / 8) * (Yiaverage[i] * int(X2X3line[i]))
            beta123 += (1 / 8) * (Yiaverage[i] * int(X1X2X3line[i]))
        t0new = Module(beta0) / SbetaS
        t1new = Module(beta1) / SbetaS
        t2new = Module(beta2) / SbetaS
        t3new = Module(beta3) / SbetaS
        t12new = Module(beta12) / SbetaS
        t13new = Module(beta13) / SbetaS
        t23new = Module(beta23) / SbetaS
        t123new = Module(beta123) / SbetaS
        f3 = f1 * f2
        d = 0
        ZkSt = [2.12, 2.11, 2.101, 2.093, 2.086, 2.08, 2.074, 2.069, 2.064]
        rivnyannya = "Y = "
        YyFIGNYA1 = 0
        YyFIGNYA2 = 0
        YyFIGNYA3 = 0
        YyFIGNYA4 = 0
        YyFIGNYA5 = 0
        YyFIGNYA6 = 0
        YyFIGNYA7 = 0
        YyFIGNYA8 = 0
        if t0new > ZkSt[f3 - 16]:
            rivnyannya += (str(B0new))
            d += 1
            YyFIGNYA1 += B0new
            YyFIGNYA2 += B0new
            YyFIGNYA3 += B0new
            YyFIGNYA4 += B0new
            YyFIGNYA5 += B0new
            YyFIGNYA6 += B0new
            YyFIGNYA7 += B0new
            YyFIGNYA8 += B0new
        if t1new > ZkSt[f3 - 16]:
            rivnyannya += ("+(" + str(B1new) + ")*x1")
            d += 1
            YyFIGNYA1 += (B1new * (REAL(X1LIST, X1line[0])))
            YyFIGNYA2 += (B1new * (REAL(X1LIST, X1line[1])))
            YyFIGNYA3 += (B1new * (REAL(X1LIST, X1line[2])))
            YyFIGNYA4 += (B1new * (REAL(X1LIST, X1line[3])))
            YyFIGNYA5 += (B1new * (REAL(X1LIST, X1line[4])))
            YyFIGNYA6 += (B1new * (REAL(X1LIST, X1line[5])))
            YyFIGNYA7 += (B1new * (REAL(X1LIST, X1line[6])))
            YyFIGNYA8 += (B1new * (REAL(X1LIST, X1line[7])))
        if t2new > ZkSt[f3 - 16]:
            rivnyannya += ("+(" + str(B2new) + ")*x2")
            d += 1
            YyFIGNYA1 += (B2new * (REAL(X2LIST, X2line[0])))
            YyFIGNYA2 += (B2new * (REAL(X2LIST, X2line[1])))
            YyFIGNYA3 += (B2new * (REAL(X2LIST, X2line[2])))
            YyFIGNYA4 += (B2new * (REAL(X2LIST, X2line[3])))
            YyFIGNYA5 += (B2new * (REAL(X2LIST, X2line[4])))
            YyFIGNYA6 += (B2new * (REAL(X2LIST, X2line[5])))
            YyFIGNYA7 += (B2new * (REAL(X2LIST, X2line[6])))
            YyFIGNYA8 += (B2new * (REAL(X2LIST, X2line[7])))
        if t3new > ZkSt[f3 - 16]:
            rivnyannya += ("+(" + str(B3new) + ")*x3")
            d += 1
            YyFIGNYA1 += (B3new * (REAL(X3LIST, X3line[0])))
            YyFIGNYA2 += (B3new * (REAL(X3LIST, X3line[1])))
            YyFIGNYA3 += (B3new * (REAL(X3LIST, X3line[2])))
            YyFIGNYA4 += (B3new * (REAL(X3LIST, X3line[3])))
            YyFIGNYA5 += (B3new * (REAL(X3LIST, X3line[4])))
            YyFIGNYA6 += (B3new * (REAL(X3LIST, X3line[5])))
            YyFIGNYA7 += (B3new * (REAL(X3LIST, X3line[6])))
            YyFIGNYA8 += (B3new * (REAL(X3LIST, X3line[7])))
        if t12new > ZkSt[f3 - 16]:
            rivnyannya += ("+(" + str(B12new) + ")*x1x2")
            d += 1
            YyFIGNYA1 += (B12new * (REAL(X1LIST, X1line[0])) * (REAL(X2LIST, X2line[0])))
            YyFIGNYA2 += (B12new * (REAL(X1LIST, X1line[1])) * (REAL(X2LIST, X2line[1])))
            YyFIGNYA3 += (B12new * (REAL(X1LIST, X1line[2])) * (REAL(X2LIST, X2line[2])))
            YyFIGNYA4 += (B12new * (REAL(X1LIST, X1line[3])) * (REAL(X2LIST, X2line[3])))
            YyFIGNYA5 += (B12new * (REAL(X1LIST, X1line[4])) * (REAL(X2LIST, X2line[4])))
            YyFIGNYA6 += (B12new * (REAL(X1LIST, X1line[5])) * (REAL(X2LIST, X2line[5])))
            YyFIGNYA7 += (B12new * (REAL(X1LIST, X1line[6])) * (REAL(X2LIST, X2line[6])))
            YyFIGNYA8 += (B12new * (REAL(X1LIST, X1line[7])) * (REAL(X2LIST, X2line[7])))
        if t13new > ZkSt[f3 - 16]:
            rivnyannya += ("+(" + str(B13new) + ")*x1x3")
            d += 1
            YyFIGNYA1 += (B13new * (REAL(X1LIST, X1line[0])) * (REAL(X3LIST, X3line[0])))
            YyFIGNYA2 += (B13new * (REAL(X1LIST, X1line[1])) * (REAL(X3LIST, X3line[1])))
            YyFIGNYA3 += (B13new * (REAL(X1LIST, X1line[2])) * (REAL(X3LIST, X3line[2])))
            YyFIGNYA4 += (B13new * (REAL(X1LIST, X1line[3])) * (REAL(X3LIST, X3line[3])))
            YyFIGNYA5 += (B13new * (REAL(X1LIST, X1line[4])) * (REAL(X3LIST, X3line[4])))
            YyFIGNYA6 += (B13new * (REAL(X1LIST, X1line[5])) * (REAL(X3LIST, X3line[5])))
            YyFIGNYA7 += (B13new * (REAL(X1LIST, X1line[6])) * (REAL(X3LIST, X3line[6])))
            YyFIGNYA8 += (B13new * (REAL(X1LIST, X1line[7])) * (REAL(X3LIST, X3line[7])))
        if t23new > ZkSt[f3 - 16]:
            rivnyannya += ("+(" + str(B23new) + ")*x2x3+(")
            d += 1
            YyFIGNYA1 += (B23new * (REAL(X2LIST, X2line[0])) * (REAL(X3LIST, X3line[0])))
            YyFIGNYA2 += (B23new * (REAL(X2LIST, X2line[1])) * (REAL(X3LIST, X3line[1])))
            YyFIGNYA3 += (B23new * (REAL(X2LIST, X2line[2])) * (REAL(X3LIST, X3line[2])))
            YyFIGNYA4 += (B23new * (REAL(X2LIST, X2line[3])) * (REAL(X3LIST, X3line[3])))
            YyFIGNYA5 += (B23new * (REAL(X2LIST, X2line[4])) * (REAL(X3LIST, X3line[4])))
            YyFIGNYA6 += (B23new * (REAL(X2LIST, X2line[5])) * (REAL(X3LIST, X3line[5])))
            YyFIGNYA7 += (B23new * (REAL(X2LIST, X2line[6])) * (REAL(X3LIST, X3line[6])))
            YyFIGNYA8 += (B23new * (REAL(X2LIST, X2line[7])) * (REAL(X3LIST, X3line[7])))
        if t123new > ZkSt[f3 - 16]:
            rivnyannya += ("+(" + str(B123new) + ")*x1x2x3")
            d += 1
            YyFIGNYA1 += (B123new * (REAL(X1LIST, X1line[0])) * (REAL(X2LIST, X2line[0])) * (REAL(X3LIST, X3line[0])))
            YyFIGNYA2 += (B123new * (REAL(X1LIST, X1line[1])) * (REAL(X2LIST, X2line[1])) * (REAL(X3LIST, X3line[1])))
            YyFIGNYA3 += (B123new * (REAL(X1LIST, X1line[2])) * (REAL(X2LIST, X2line[2])) * (REAL(X3LIST, X3line[2])))
            YyFIGNYA4 += (B123new * (REAL(X1LIST, X1line[3])) * (REAL(X2LIST, X2line[3])) * (REAL(X3LIST, X3line[3])))
            YyFIGNYA5 += (B123new * (REAL(X1LIST, X1line[4])) * (REAL(X2LIST, X2line[4])) * (REAL(X3LIST, X3line[4])))
            YyFIGNYA6 += (B123new * (REAL(X1LIST, X1line[5])) * (REAL(X2LIST, X2line[5])) * (REAL(X3LIST, X3line[5])))
            YyFIGNYA7 += (B123new * (REAL(X1LIST, X1line[6])) * (REAL(X2LIST, X2line[6])) * (REAL(X3LIST, X3line[6])))
            YyFIGNYA8 += (B123new * (REAL(X1LIST, X1line[7])) * (REAL(X2LIST, X2line[7])) * (REAL(X3LIST, X3line[7])))
        print("\n" + rivnyannya)
        ### Критерій Фішера:2
        YyFIGNYA = []
        YyFIGNYA.append(YyFIGNYA1)
        YyFIGNYA.append(YyFIGNYA2)
        YyFIGNYA.append(YyFIGNYA3)
        YyFIGNYA.append(YyFIGNYA4)
        YyFIGNYA.append(YyFIGNYA5)
        YyFIGNYA.append(YyFIGNYA6)
        YyFIGNYA.append(YyFIGNYA7)
        YyFIGNYA.append(YyFIGNYA8)
        f4 = 8 - d
        S2ad = 0
        for i in range(8):
            S2ad += ((m/f4) * ((YyFIGNYA[i] - Yiaverage[i]) ** 2))
        Fp = S2ad / S2B
        print("значення Fp: " + str(Fp))
        print("значення f3: " + str(f3))
        print("значення f4: " + str(f4))
        Z = str(input("Адекватне"))
        if Z == "+":
            print("експеримент закінчено")
            work = False
        else:
            print("Не вийшло")
    else:
        pass
