asignaturas=["Matematica", "Fisica", "Quimica", "Historia", "Lengua"]
notas=[]
reprobadas=[]
for asignatura in asignaturas:
    nota=input("Que nota sacaste en: "+asignatura+"?")
    notas.append(nota)
    if int(nota)<10:
        reprobadas.append(asignatura)
print("\n")
for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " has sacado " + notas[i])

print("\n")
for i in range(len(reprobadas)):
        print("Debes repetir " + reprobadas[i])
