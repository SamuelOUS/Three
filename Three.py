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
        self.elements = 0
        self.children = [None] * 4

root_folder = Folder("raiz")

class BinaryTree:
    def __init__(self):
        self.root = root_folder

    def pretty_print_tree(self, node, prefix="", is_left=True):
        if not node:
            print("Empty Tree")
            return
        if node.right:
            self.pretty_print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        if node.left:
            self.pretty_print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

    def add_carpet(self, carpet, target: Folder):

        for i in range(4):
            if target.children[i] is None:
                target.children.append(carpet)
            else:
                print("Carpeta llena")



    def add_document(self, document, target):

        for i in range(4):
            if target.children[i] is None:
                target.children.append(document)
            else:
                print("Carpeta llena")

    def modify_carpet(self, carpet):
        pass


    def modify_document(self, document):
        pass



Three = BinaryTree()


def system():
    print("Bienvenido al sistema de documento y carpetas")
    while True:

        print("Porfavor, seleccione una opcion:", "\n", "1. Agregar carpeta", "2. Agregar archivo", "\n",
              "3. modificar carpeta", "\n", "4. modificar archivo", "\n", "5. Salir")

        Desicion = int(input(""))

        if Desicion == 1:
            Three.add_carpet()
            break

        elif Desicion == 2:
            Three.add_document()
            break


        elif Desicion == 3:
            Three.modify_carpet()
            break


        elif Desicion == 4:
            Three.modify_document()
            break


        elif Desicion == 5:
            print("Terminando la aplicacion")
            sys.exit()


system()
