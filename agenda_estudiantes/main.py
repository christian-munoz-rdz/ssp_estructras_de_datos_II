#Agenda de estudiantes version 2.0
import os

def menu():
    print("1. Agregar")
    print("2. Mostrar lista completa")
    print("3. Eliminar")
    print("4. Buscar")
    print("5. Editar")
    print("6. Guardar")
    print("7. Salir")
    opcion = int(input("Ingrese opcion: "))
    return opcion

def cargar():
    try:
        file = open("./file.txt",'r')
        loaded_data = file.read()
        loaded_data = loaded_data.split('*')
        loaded_data.pop()
        for i in range(len(loaded_data)):
            loaded_data[i] = loaded_data[i].split('|')
            loaded_data[i] = dict(codigo=loaded_data[i][0],nombre=loaded_data[i][1],carrera=loaded_data[i][2])
    except IOError:
        loaded_data = []
    finally:
        file.close()
        return loaded_data

def main():
    agenda = cargar()
    opcion = menu()
    os.system('cls')
    while opcion != 7:
        if opcion == 1:
            codigo = input("Ingrese el codigo: ")
            nombre = input("Ingrese el nombre: ")
            carrera = input("Ingrese la carrera: ")
            agenda.append(dict(codigo=codigo,nombre=nombre,carrera=carrera))
            print("Estudiante agregado")
            os.system('pause')
            os.system('cls')
        elif opcion == 2:
            for i in range(len(agenda)):
                for key in agenda[i]:
                    print(key,":",agenda[i][key])
                print("----------------------------")
            os.system('pause')
            os.system('cls')
        elif opcion == 3:
            codigo = input("Ingrese el codigo: ")
            for i in range(len(agenda)):
                if agenda[i]['codigo'] == codigo:
                    agenda.pop(i)
                    print("Estudiante eliminado")
                    break
            os.system('pause')
            os.system('cls')
        elif opcion == 4:
            codigo = input("Ingrese el codigo: ")
            for i in range(len(agenda)):
                if agenda[i]['codigo'] == codigo:
                    for key in agenda[i]:
                        print(key,":",agenda[i][key])
                    break
            os.system('pause')
            os.system('cls')
        elif opcion == 5:
            codigo = input("Ingrese el codigo: ")
            for i in range(len(agenda)):
                if agenda[i]['codigo'] == codigo:
                    agenda[i]['nombre'] = input("Ingrese el nuevo nombre: ")
                    agenda[i]['carrera'] = input("Ingrese la nueva carrera: ")
                    break
            os.system('pause')
            os.system('cls')
        elif opcion == 6:
            try:
                file = open("./file.txt",'w')
                for i in range(len(agenda)):
                    file.write(agenda[i]['codigo']+'|'+agenda[i]['nombre']+'|'+agenda[i]['carrera']+'*')
                print("Guardado exitosamente")
                os.system('pause')
                os.system('cls')
            except IOError:
                print("Error al guardar")
                os.system('pause')
                os.system('cls')
            finally:
                file.close()
        opcion = menu()
        os.system('cls')   

if __name__ == '__main__':
    main()