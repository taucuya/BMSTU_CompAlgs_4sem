from polynom import *
from spline import *
from readData import *

pointTable = readTable("./data.txt")
printTable(pointTable)

n = 3
x = float(input("Введите значение аргумента x: "))

start1 = 0
end1 = 0
start2 = 0
end2 = 0
start3 = 0
end3 = 0

yValues = [list(), list(), list(), list()]
if n < len(pointTable):
    print("Ньютон 3-й степени: ", newtonPolynom(pointTable, n + 1, x))

    end2 = findDerivativeNewtonPolynom(pointTable, n + 1, pointTable[-1].x)

    start3 = findDerivativeNewtonPolynom(pointTable, n + 1, pointTable[0].x)
    end3 = findDerivativeNewtonPolynom(pointTable, n + 1, pointTable[-1].x)
else:
    print("Ньютон 3-й степени нельзя посчитать стпени", n, ", так как точек всего", len(pointTable))

print("Cплайн 0 и 0 - краевые случаи: ", spline(pointTable, x, start1, end1))
printSplineFunct(pointTable, x, start1, end1)
print()
print("Cплайн 0 и P''(xn) - краевые случаи: ", spline(pointTable, x, start2, end2))
printSplineFunct(pointTable, x, start2, end2)
print()
print("Cплайн P''(x0) и P''(xn) - краевые случаи: ", spline(pointTable, x, start3, end3))
printSplineFunct(pointTable, x, start3, end3)