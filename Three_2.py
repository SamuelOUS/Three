import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.children = [None] * 4
        self.is_folder = True


class File:
    def __init__(self, name, extension, size):
        self.name = name
        self.extension = extension
        self.size = size


class Folder:
    def __init__(self, name):
        self.name = name
        self.children = [Node, Node, Node, Node]


folder = Folder("raiz")
root_folder = Node(folder)


class BinaryTree:
    def __init__(self):
        self.root = root_folder

    # ---------------------------------------------------------------------------------------

    def print_tree(self, root, level=0):
        if root is not None:
            print("  " * level + str(root.key))
            for child in root.children:
                self.print_tree(child, level + 1)

    # ---------------------------------------------------------------------------------------
    def add_folder(self, folder, target: Folder):

        for i in range(4):
            if target.children[i] is None:
                target.children[i] = folder
            else:
                print("Carpeta llena, desea salir o elegir otra carpeta")
                decision = int(input(""))
                if decision != "salir":
                    new = str(input("Introduzca el nombre de la carpeta:"))
                    self.add_folder(folder, new)

                else:
                    print("Saliendo de la app")
                    sys.exit()

    # ---------------------------------------------------------------------------------------

    def add_file(self, file, target: Folder):
        for i in range(4):
            if target.children[i] is None:
                target.children[i] = file
                break
            elif i == 3:
                print("Carpeta llena")

    # ---------------------------------------------------------------------------------------

    def modify_folder(self, old_name, new_name):
        target_folder = None
        for child in self.root.children:
            if child and isinstance(child, Folder) and child.name == old_name:
                target_folder = child
                break

        if target_folder:
            target_folder.name = new_name
            print(f"El nombre de la carpeta '{old_name}' ha sido cambiado a '{new_name}'.")
        else:
            print(f"No se encontró la carpeta con el nombre '{old_name}'.")

    # ---------------------------------------------------------------------------------------

    def modify_file(self, old_name, new_name, new_extension, new_size):
        target_file = None
        for child in self.root.children:
            if child and isinstance(child, File) and child.name == old_name:
                target_file = child
                break

        if target_file:
            target_file.name = new_name
            target_file.extension = new_extension
            target_file.size = new_size
            print(f"El archivo '{old_name}' ha sido modificado.")
        else:
            print(f"No se encontró el archivo con el nombre '{old_name}'.")


tree = BinaryTree()


# ---------------------------------------------------------------------------------------

def system():
    print("Bienvenido al sistema de documento y carpetas")

    while True:
        print("Porfavor, seleccione una opcion:", "\n", "1. Agregar carpeta", "\n", "2. Agregar archivo", "\n",
              "3. modificar carpeta", "\n", "4. modificar archivo", "\n", "5. Imprimir árbol")

        decision = int(input(""))

        if decision == 1:
            folder_name = input("Ingrese el nombre de la carpeta: ")
            new_folder = Folder(folder_name)
            tree.add_folder(new_folder, tree.root)

        elif decision == 2:
            file_name = input("Ingrese el nombre del archivo: ")
            file_extension = input("Ingrese la extension del archivo: ")
            file_size = int(input("Ingrese el tamaño del archivo: "))
            new_file = File(file_name, file_extension, file_size)
            tree.add_file(new_file, tree.root)

        elif decision == 3:
            old_folder_name = input("Ingrese el nombre actual de la carpeta: ")
            new_folder_name = input("Ingrese el nuevo nombre de la carpeta: ")
            tree.modify_folder(old_folder_name, new_folder_name)


        elif decision == 4:
            old_file_name = input("Ingrese el nombre actual del archivo: ")
            new_file_name = input("Ingrese el nuevo nombre del archivo: ")
            new_file_extension = input("Ingrese la nueva extensión del archivo: ")
            new_file_size = int(input("Ingrese el nuevo tamaño del archivo: "))
            tree.modify_file(old_file_name, new_file_name, new_file_extension, new_file_size)


        elif decision == 5:
            tree.print_tree(tree.root)
            sys.exit()


system()
