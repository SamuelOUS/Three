import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.children = [None] * 4
        self.is_folder = True


# -----------------------------------------------------------------

class File:
    def __init__(self, name, extension, size):
        self.name = name
        self.extension = extension
        self.size = size


# -----------------------------------------------------------------

class Folder:
    def __init__(self, name):
        self.name = name
        self.cantidad_elementos = 0
        self.children = [None] * 4


root_folder = Folder("raiz")


# -----------------------------------------------------------------

class BinaryTree:
    def __init__(self):
        self.root = root_folder

    # -----------------------------------------------------------------

    def pretty_print_tree(self, node, prefix="", is_folder=True):
        if not node:
            print("Empty Tree")
            return

        if is_folder:
            for i in range(len(node.children) - 1, -1, -1):
                child = node.children[i]
                if child:
                    new_prefix = prefix + "    "
                    self.pretty_print_tree(child, new_prefix, isinstance(child, Folder))

        if isinstance(node, Folder):
            print(prefix + "📁 " + node.name + " (" + str(node.cantidad_elementos) + " elementos)")
        else:
            print(prefix + "📄 " + node.name + "." + node.extension + " (" + str(node.size) + " KB)")

    # -----------------------------------------------------------------

    def add_folder(self, folder, target: Folder):
        if self.search_node(folder.name, True, target):
            print(f"Ya existe una carpeta con el nombre '{folder.name}' en el mismo nivel del árbol.")
            return

        for i in range(4):
            if target.children[i] is None:
                target.children[i] = folder
                target.cantidad_elementos += 1
                break
            else:
                if target.cantidad_elementos == 4:
                    print("Carpeta llena, desea salir o elegir otra carpeta")
                    decision = (input(""))
                    if decision == "elegir":
                        new = str(input("Introduzca el nombre de la carpeta:"))

                        self.add_folder(folder, new)

                    elif decision == "salir":
                        print("Saliendo de la app")
                        sys.exit()

        print_tree()

    # -----------------------------------------------------------------

    def add_file(self, file, target: Folder):
        if self.search_node(file.name, False, target):
            print(
                f"Ya existe un archivo con el nombre '{file.name}' y la extensión '{file.extension}' en la misma carpeta.")
            return

        for i in range(4):
            if target.children[i] is None:
                target.children[i] = file
                target.cantidad_elementos += 1
                break
            else:
                if target.cantidad_elementos == 4:
                    print("Carpeta llena, desea salir o elegir otra carpeta")
                    decision = (input(""))
                    if decision == "elegir":
                        new = str(input("Introduzca el nombre de la carpeta:"))

                        self.add_file(file, new)

                    elif decision == "salir":
                        print("Saliendo de la app")
                        sys.exit()
        print_tree()

    # -----------------------------------------------------------------

    def modify_folder(self, old_name, new_name):
        target_folder = self.search_node(old_name, True, self.root)
        if not target_folder:
            print(f"No se encontró la carpeta con el nombre '{old_name}'.")
            return

        if self.search_node(new_name, True, self.root):
            print(f"Ya existe una carpeta con el nombre '{new_name}' en el mismo nivel del árbol.")
            return

        target_folder.name = new_name
        print(f"El nombre de la carpeta '{old_name}' ha sido cambiado a '{new_name}'.")
        print_tree()

    # -----------------------------------------------------------------

    def modify_file(self, old_name, new_name, new_extension, new_size):
        target_file = self.search_node(old_name, False, self.root)
        if not target_file:
            print(f"No se encontró el archivo con el nombre '{old_name}'.")
            return

        if self.search_node(new_name, False, target_file.parent):
            print(
                f"Ya existe un archivo con el nombre '{new_name}' y la extensión '{new_extension}' en la misma carpeta.")
            return

        target_file.name = new_name
        target_file.extension = new_extension
        target_file.size = new_size
        print(f"El archivo '{old_name}' ha sido modificado.")
        print_tree()

    # -----------------------------------------------------------------
    def search_node(self, name, is_folder, node):
        if isinstance(node, Folder) and node.name == name:
            if isinstance(node, File) and not is_folder:
                return node
            elif isinstance(node, Folder) and is_folder:
                return node

        for child in node.children:
            if child:
                result = self.search_node(name, is_folder, child)
                if result:
                    return result

        return None


tree = BinaryTree()


def print_menu():
    print("Por favor, seleccione una opción:")
    print("1. Agregar carpeta")
    print("2. Agregar archivo")
    print("3. Modificar carpeta")
    print("4. Modificar archivo")
    print("5. Imprimir árbol")
    print("6. Salir")


def print_tree():
    print("Estructura del árbol:")
    tree.pretty_print_tree(tree.root, is_folder=True)


def system():
    print("Bienvenido al sistema de documentos y carpetas")
    while True:
        print_menu()

        decision = int(input(""))

        if decision == 1:
            folder_name = input("Ingrese el nombre de la carpeta: ")
            new_folder = Folder(folder_name)
            folder_target = input("Ingrese la carpeta de destino")
            new_target = Folder(folder_target)
            if folder_target == tree.root.name:
                tree.add_folder(new_folder, tree.root)
            else:
                tree.add_folder(new_folder, new_target)

        elif decision == 2:
            file_name = input("Ingrese el nombre del archivo: ")
            file_extension = input("Ingrese la extensión del archivo: ")
            file_size = int(input("Ingrese el tamaño del archivo: "))
            folder_name = input("Ingrese el nombre de la carpeta donde quiere alojar el archivo: ")
            target_folder = tree.search_node(folder_name, True, tree.root)
            new_file = File(file_name, file_extension, file_size)
            tree.add_file(new_file, target_folder)

        elif decision == 3:
            old_folder_name = input("Ingrese el nombre actual de la carpeta: ")
            new_folder_name = input("Ingrese el nuevo nombre de la carpeta: ")
            tree.modify_folder(old_folder_name, new_folder_name)

        elif decision == 4:
            old_file_name = input("Ingrese el nombre actual del archivo: ")
            new_file_name = input("Ingrese el nuevo nombre del archivo: ")
            new_file_extension = input("Ingrese la nueva extensión del archivo: ")
            new_file_size = int(input("Ingrese el nuevo tamaño del archivo: "))
            target_file = tree.search_node(old_file_name, False, tree.root)
            if not target_file:
                print(f"No se encontró el archivo con el nombre '{old_file_name}'.")
                continue
            tree.modify_file(old_file_name, new_file_name, new_file_extension, new_file_size)

        elif decision == 5:
            print_tree()

        elif decision == 6:
            print("Terminando la aplicación")
            sys.exit()


system()
