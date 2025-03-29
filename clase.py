texto=""

with open("archive.txt", "r") as archivo:
    texto= archivo.readlines()

print(texto)

