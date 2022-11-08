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