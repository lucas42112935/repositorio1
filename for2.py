aprobados = 0
reprobados = 0
for f in range (10):
    nota = int(input("ingrese notas"))
    if nota >=7:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1
print("aprobados:", aprobados)
print("reprobados", reprobados)