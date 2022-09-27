def encode(nombreArchivo):
    letters = "abcdefghijklmnopqrstuvwxyz"
    try:
        archivo = open(nombreArchivo,'r')
        caracter = archivo.read(1)
        nuevo_texto = ""
        while caracter:
            if caracter != caracter.upper():
                try:
                    nuevo_texto += letters[letters.index(caracter)+1]
                except IndexError:
                    nuevo_texto += 'a'
            else:
                nuevo_texto += caracter
            caracter = archivo.read(1)
    except IOError:
        print('No se pudo abrir el archivo')
    finally:
        archivo.close()
    return nuevo_texto

def decode(archivo1,archivo2,texto):
    letters = "abcdefghijklmnopqrstuvwxyz"
    try:
        codificado = open(archivo1,mode="r+",encoding="utf-8")
        codificado.write(texto)
        decodificado = open(archivo2,mode="r+",encoding="utf-8")
        texto_decodificado = ""
        for i in range(len(texto)):
            caracter = texto[i]
            if caracter != caracter.upper():
                try:
                    texto_decodificado += letters[letters.index(caracter)-1]
                except IndexError:
                    nuevo_texto += 'z'
            else:
                texto_decodificado += caracter
        decodificado.write(texto_decodificado)
    except IOError:
        print('No se pudo abrir el archivo')
    finally:
        codificado.close()
        decodificado.close()

def main():
    texto_encriptado = encode("original.txt")
    decode("codificado.txt","decodificado.txt",texto_encriptado)
    original = open("original.txt",mode="r",encoding="utf-8")
    decodificado = open("decodificado.txt",mode="r",encoding="utf-8")
    if original.read() == decodificado.read():
        print("El archivo se ha decodificado correctamente")

if __name__ == "__main__":
    main()