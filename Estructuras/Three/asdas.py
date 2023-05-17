import time


class ElementoNoEncontrado(Exception):
    pass


class EspacioNoDisponible(Exception):
    pass


class NombreInvalido(Exception):
    pass


class EntradaInvalida(Exception):
    pass


class Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = [None, None, None, None]
        self.simbolo = "📁 "


class Archivo:
    def __init__(self, nombre, extension, peso):
        self.nombre = nombre
        self.extension = extension
        self.peso = peso
        self.simbolo = "📄 "


def buscar_carpeta(carpeta, nombre):
    if carpeta.nombre == nombre:
        return carpeta
    for elemento in carpeta.elementos:
        if elemento and isinstance(elemento, Carpeta):
            resultado = buscar_carpeta(elemento, nombre)
            if resultado:
                return resultado
    return None


def agregar_carpeta(carpeta_madre, nombre_nueva_carpeta):
    if not carpeta_madre:
        raise ElementoNoEncontrado("Carpeta madre no encontrada.")
    for elemento in carpeta_madre.elementos:
        if elemento and elemento.nombre == nombre_nueva_carpeta:
            raise NombreInvalido("Ya existe una carpeta con el mismo nombre.")
    for i, elemento in enumerate(carpeta_madre.elementos):
        if not elemento:
            carpeta_madre.elementos[i] = Carpeta(nombre_nueva_carpeta)
            return
    raise EspacioNoDisponible("No hay espacio disponible en la carpeta madre.")


def agregar_archivo(carpeta_madre, nombre_archivo, extension, peso):
    if not carpeta_madre:
        raise ElementoNoEncontrado("Carpeta madre no encontrada.")
    for elemento in carpeta_madre.elementos:
        if elemento and isinstance(elemento, Archivo) and elemento.nombre == nombre_archivo:
            raise NombreInvalido("Ya existe un archivo con el mismo nombre y extensión.")
    for i, elemento in enumerate(carpeta_madre.elementos):
        if not elemento:
            carpeta_madre.elementos[i] = Archivo(nombre_archivo, extension, peso)
            return
    raise EspacioNoDisponible("No hay espacio disponible en la carpeta madre.")


def modificar_carpeta(carpeta_raiz, nombre_actual, nuevo_nombre):
    carpeta = buscar_carpeta(carpeta_raiz, nombre_actual)
    if not carpeta:
        raise ElementoNoEncontrado("Carpeta no encontrada.")
    carpeta.nombre = nuevo_nombre


def modificar_archivo(carpeta_raiz, nombre_carpeta, nombre_archivo, nueva_extension, nuevo_peso):
    carpeta = buscar_carpeta(carpeta_raiz, nombre_carpeta)
    if not carpeta:
        raise ElementoNoEncontrado("Carpeta madre no encontrada.")
    archivo_modificado = False
    for elemento in carpeta.elementos:
        if elemento and isinstance(elemento, Archivo) and elemento.nombre == nombre_archivo:
            elemento.extension = nueva_extension
            elemento.peso = nuevo_peso
            archivo_modificado = True
            break
        else:
            raise ElementoNoEncontrado("Archivo no encontrado.")


def imprimir_arbol(carpeta, nivel=0):
    print("  " * nivel + carpeta.nombre + carpeta.simbolo)
    for elemento in carpeta.elementos:
        if elemento:
            if isinstance(elemento, Carpeta):
                imprimir_arbol(elemento, nivel + 1)
            else:
                print("  " * (nivel + 1) + elemento.nombre + "." + "📄 " + elemento.extension + " (" + str(
                    elemento.peso) + ")")


def main():
    carpeta_raiz = Carpeta("raiz")

    while True:
        print("Porfavor, seleccione una opcion:", "\n", "1. Agregar carpeta", "\n", "2. Agregar archivo", "\n",
              "3. modificar carpeta", "\n", "4. modificar archivo", "\n", "5. salir")
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre_carpeta_madre = input("Ingrese el nombre de la carpeta madre: ")
                nombre_nueva_carpeta = input("Ingrese el nombre de la nueva carpeta: ")
                agregar_carpeta(buscar_carpeta(carpeta_raiz, nombre_carpeta_madre), nombre_nueva_carpeta)
                print("Carpeta agregada.")

                # ------------------------------------------------------------------------------------------

            elif opcion == "2":
                nombre_carpeta_madre = input("Ingrese el nombre de la carpeta madre: ")
                entrada = input("Ingrese el nombre del archivo, extensión y peso (ejemplo: archivo.txt 56): ")
                if len(entrada.split()) != 3:
                    raise EntradaInvalida("Por favor, ingrese el nombre del archivo, extensión y peso correctamente.")
                nombre_archivo, extension, peso = entrada.split()
                peso = int(peso)
                agregar_archivo(buscar_carpeta(carpeta_raiz, nombre_carpeta_madre), nombre_archivo, extension, peso)
                print("Archivo agregado.")

                # ------------------------------------------------------------------------------------------

            elif opcion == "3":
                nombre_actual = input("Ingrese el nombre actual de la carpeta: ")
                nuevo_nombre = input("Ingrese el nuevo nombre de la carpeta: ")
                modificar_carpeta(carpeta_raiz, nombre_actual, nuevo_nombre)
                print("Carpeta modificada.")

                # ------------------------------------------------------------------------------------------

            elif opcion == "4":
                nombre_carpeta = input("Ingrese el nombre de la carpeta madre: ")
                nombre_archivo = input("Ingrese el nombre actual del archivo: ")
                nueva_extension = input("Ingrese la nueva extensión del archivo: ")
                nuevo_peso = int(input("Ingrese el nuevo peso del archivo: "))
                modificar_archivo(carpeta_raiz, nombre_carpeta, nombre_archivo, nueva_extension, nuevo_peso)
                print("Archivo modificado.")

                # ------------------------------------------------------------------------------------------

            elif opcion == "5":
                print("terminando..")
                time.sleep(2)
                break

                # ------------------------------------------------------------------------------------------

            else:
                print("Opción no válida.")

                # ------------------------------------------------------------------------------------------

        except (ElementoNoEncontrado, EspacioNoDisponible, NombreInvalido, EntradaInvalida) as e:
            print(str(e))

        print("\nÁrbol de carpetas y archivos:")
        imprimir_arbol(carpeta_raiz)


if __name__ == "__main__":
    main()
