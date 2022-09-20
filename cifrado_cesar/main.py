def main():
    letters = "bcdefghijklmnopqrstuvwxyza"
    try:
        archivo = open('cancion.txt','r')
        caracter = archivo.read(1)
        nuevo_texto = ""
        while caracter:
            if caracter != caracter.upper():
                try:
                    nuevo_texto += letters[letters.index(caracter)+1]
                except IndexError:
                    nuevo_texto += 'b'
            else:
                nuevo_texto += caracter
            caracter = archivo.read(1)
        print(nuevo_texto)
        nuevo_archivo = open("archivo2.txt",mode="a+",encoding="utf-8")
        nuevo_archivo.write(nuevo_texto)
    except IOError:
        print('No se pudo abrir el archivo')
    finally:
        print('Fin del programa')
        archivo.close()

if __name__ == "__main__":
    main()