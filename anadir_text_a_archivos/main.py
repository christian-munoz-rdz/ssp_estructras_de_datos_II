#Agenda de estudiantes version 1
'''
Nombre:
Codigo: 
Carrera:
'''

'''
def main():
    letters = "bcdefghijklmnopqrstuvwxyza"
    archivo_o = open('agenda.txt','r')
    archivo_r = open('agenda_r.txt','w')
    for line in archivo_o:
        archivo_r.write(line)
    archivo_o.close()
    archivo_r.close()
    archivo_r = open('agenda_r.txt','r')
    archivo_o = open('agenda.txt','w')
    for line in archivo_r:
        archivo_o.write(line)
    archivo_o.write("Cadena")
    archivo_r.close()
    archivo_o.close()
'''

def main():
    file = open("./file.txt",'a+')
    curent_record = []
    flag = 'y'
    while(flag=='y'):
        cod = input("Ingrese codigo: ")
        nom = input("Ingrese nombre: ")
        carr = input("Ingrese carrera: ")
        curent_record.append(dict(codigo=cod,nombre=nom,carrera=carr))
        flag = input("Desea agregar otro registro? y/n").lower()
        print(curent_record)
    
    for alumno in curent_record:
        for dato in alumno.values():
            file.write(dato)
            file.write('|')
        file.write('*')

    

if __name__ == '__main__':
    main()