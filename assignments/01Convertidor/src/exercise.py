# Escribe tus funciones abajo de esta línea

def main():
    # Escribe tu código abajo de esta línea
    print("1. pies a cm, 2. pulgadas a cm, 3. yardas a cm")
    x = int(input("Introduce una opcion: "))
    y = int(input("Introduce la cantidad: "))
    if x == 1:
        f = y*30.48
        print(f)
        return
    elif x == 2:
        f = y*2.54
        print(f)
        return
    elif x == 3:
        f = y*91.44
        print(f)
        return
    else:
        print("Error")
        return
        


if __name__ == '__main__':
    main()
