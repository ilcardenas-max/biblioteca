biblioteca = {}

while True:
    print("\====SISTEMA DE BIBLIOTECA====")
    print("1.- Registrar Libro")
    print("2.- Buscar Libro ")
    print("3.- Actualizar Stock")
    print("4.- Prestar Libro")
    print("5.- Eliminar Libro")
    print("6.- Mostrar Catálogo")
    print("7.- Salir")

    opcion = input("Seleecione una opción: ")

    try:
        opcion = int(opcion)

        if opcion == 1:
            codigo = input("Ingrese código del Libro: ")

            if codigo in biblioteca:
                print("Error: El código ya existe")
                continue

            titulo = input("Ingrese Título: ")
            autor = input("Ingrese Autor: ")

            while True:
                try:
                    stock = int(input("Ingrese Cantidad de ejemplares: "))

                    if stock < 0:
                        raise ValueError("El stock no puede ser negativo")
                    
                    break
                except ValueError as error:
                    print("Error: ", error)

            biblioteca[codigo] = {"titulo": titulo,
                                  "autor": autor,
                                  "stock": stock}
            
            print("Libro registrado correctamente")

        elif opcion == 2:

                codigo = input("Ingrese Código a buscar: ")

                if codigo in biblioteca:
                    print("\nInformación de Libro")
                    print("Titulo : ", biblioteca[codigo]["titulo"])
                    print("Autor  : ", biblioteca[codigo]["autor"])
                    print("Sotck  : ", biblioteca[codigo]["stock"])
                
                else:
                    print("Libro no encontrado")

        elif opcion == 3:

            codigo = input("Ingrese código del Libro: ")

            if codigo not in biblioteca:
                print("Libro no existe")
                continue

            while True:
                try:
                    nuevo_stock = int(input("Ingrese nuevo stock: "))

                    if nuevo_stock < 0:
                        raise ValueError("El stock no puede ser negativo")
                    
                    biblioteca[codigo]["stock"] = nuevo_stock
                    print("Stock actualizado correctamente")
                    break

                except ValueError as error:
                    print("Error: ",error)

        elif opcion == 4:
            codigo = input("Ingrese codigo del Libro: ")

            if codigo not in biblioteca:
                print("Libro no existe")
                continue

            if biblioteca[codigo]["stock"] > 0:

                biblioteca[codigo]["stock"] -= 1

                print("Préstamo realizado correctamente")
                print("Stock restante: ",
                      biblioteca[codigo]["stock"])
                
            else:
                print("No hay ejemplares Disponibles")

        elif opcion == 5:
            codigo = input("Ingrese código a eliminar: ")

            if codigo in biblioteca:
                del biblioteca[codigo]
                print("Libro Eliminado correctamente")

            else:
                print("Libro No encontrado")

        elif opcion == 6:
            if len(biblioteca) == 0:
                print("No existen libros registrados")
            else:
                print("\n====CATÁLOGO DE LIBROS====")

                for codigo, datos in biblioteca.items():
                    print(f"""
                           Código : {codigo}
                           Título : {datos["titulo"]}
                           Autor  : {datos["autor"]}
                           Stock  : {datos["stock"]}
                           ----------------------------
                            """)
        elif opcion == 7:
            print("Programa Finalizado")
            break

        else:
            print("Debe Seleccionar una opción entre 1 y 7.")

    except ValueError:
        print("Debe Ingresar un número válido")            