texto=input("Ingrese texto para agregar al archivo.")

with open("archive.txt", "w") as f:
    
    print(texto, file= f)

