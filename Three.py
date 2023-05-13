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


class BinaryTree:
    def __init__(self):
        self.root = Node

    def pretty_print_tree(self, node, prefix="", is_left=True):
        if not node:
            print("Empty Tree")
            return
        if node.right:
            self.pretty_print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        if node.left:
            self.pretty_print_tree(node.left, prefix + ("    " if is_left else "│   "), True)


def system():
    print("Bienvenido al sistema de documento y carpetas")
    while True:

        print("Porfavor, seleccione una opcion:","\n","1. Agregar carpeta","2. Agregar archivo","\n","3. Modificar carpeta","\n","4. modificar archivo","\n","5. Salir")

        Desicion = input()

system()
