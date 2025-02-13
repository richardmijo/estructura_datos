class Contacto:
    """
    Clase que representa un contacto en la agenda.
    """
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
    
    def __str__(self):
        return f"{self.nombre}: {self.telefono}"


class NodoBST:
    """
    Nodo del Árbol Binario de Búsqueda (BST).
    """
    def __init__(self, contacto):
        self.contacto = contacto
        self.izquierda = None
        self.derecha = None


class BST:
    """
    Implementación de un Árbol Binario de Búsqueda (BST) para gestionar contactos.
    """
    def __init__(self):
        self.raiz = None
    
    def insertar(self, contacto):
        """Inserta un nuevo contacto en el BST."""
        if self.raiz is None:
            self.raiz = NodoBST(contacto)
        else:
            self._insertar(self.raiz, contacto)
    
    def _insertar(self, nodo, contacto):
        if contacto.nombre < nodo.contacto.nombre:
            if nodo.izquierda is None:
                nodo.izquierda = NodoBST(contacto)
            else:
                self._insertar(nodo.izquierda, contacto)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoBST(contacto)
            else:
                self._insertar(nodo.derecha, contacto)
    
    def buscar(self, nombre):
        """Busca un contacto por nombre."""
        return self._buscar(self.raiz, nombre)
    
    def _buscar(self, nodo, nombre):
        if nodo is None:
            return None
        if nombre == nodo.contacto.nombre:
            return nodo.contacto
        elif nombre < nodo.contacto.nombre:
            return self._buscar(nodo.izquierda, nombre)
        else:
            return self._buscar(nodo.derecha, nombre)
    
    def eliminar(self, nombre):
        """Elimina un contacto por nombre."""
        self.raiz = self._eliminar(self.raiz, nombre)
    
    def _eliminar(self, nodo, nombre):
        if nodo is None:
            return nodo
        if nombre < nodo.contacto.nombre:
            nodo.izquierda = self._eliminar(nodo.izquierda, nombre)
        elif nombre > nodo.contacto.nombre:
            nodo.derecha = self._eliminar(nodo.derecha, nombre)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            sucesor = self._minimo(nodo.derecha)
            nodo.contacto = sucesor.contacto
            nodo.derecha = self._eliminar(nodo.derecha, sucesor.contacto.nombre)
        return nodo
    
    def _minimo(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo
    
    def inorder(self):
        """Imprime los contactos en orden alfabético."""
        self._inorder(self.raiz)
    
    def _inorder(self, nodo):
        if nodo is not None:
            self._inorder(nodo.izquierda)
            print(nodo.contacto)
            self._inorder(nodo.derecha)


if __name__ == "__main__":
    agenda = BST()
    agenda.insertar(Contacto("Carlos", "0991234567"))
    agenda.insertar(Contacto("Ana", "0999876543"))
    agenda.insertar(Contacto("Luis", "0994567890"))
    
    print("Agenda de contactos en orden alfabético:")
    agenda.inorder()
    
    print("\nBuscando a 'Ana':")
    encontrado = agenda.buscar("Ana")
    print(encontrado if encontrado else "No encontrado")
    
    print("\nEliminando 'Carlos'...")
    agenda.eliminar("Carlos")
    
    print("\nAgenda después de la eliminación:")
    agenda.inorder()
