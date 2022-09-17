def write_new_file():

    try:
        archivo = open('archivo.txt','r')
        texto = archivo.readlines()
        nuevo_texto = []
        for i in range(len(texto)):
            nuevo_texto += [texto[i]] + ['*\n']
        nuevo_archivo=open("archivo2.txt",mode="a+",encoding="utf-8")
        nuevo_archivo.writelines(nuevo_texto)
    except IOError:
        print('No se pudo abrir el archivo')
    finally:
        print('Fin del programa')
        archivo.close()

def main():
    try:
        archivo = open('archivo.txt','r')
        print(archivo.read())
    except IOError:
        print('No se pudo abrir el archivo')
    finally:
        print('Fin del programa')

if __name__ == '__main__':
    main()