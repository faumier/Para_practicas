#Ejercicio para abrir un archivo en python

file = open("sequence.txt", "r")
file.seek(1)
objeto = file.readline(4)
file.close()
z = list(objeto)
print(z)
Cadena_complementaria = []

for nuc in z:
    if nuc == "A":
        Cadena_complementaria.append("T")
    elif nuc == "T":
        Cadena_complementaria.append("A")
    elif nuc == "G":
        Cadena_complementaria.append("C")
    elif nuc == "C":
        Cadena_complementaria.append("G")
    else:
        Cadena_complementaria.append("A")


print(Cadena_complementaria)
print("----------------------------------------------------")
print(z)

