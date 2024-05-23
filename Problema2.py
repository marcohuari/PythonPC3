

fraccion = input("Digite una fracción en formato (X/Y), donde X sea menor o igual a Y (X<Y): ")

largo = 0
for i in fraccion:
    largo += 1

corte = fraccion.find("/")
num = int(fraccion[0:corte])
den = int(fraccion[corte+1:largo])

print(num)
print(den)