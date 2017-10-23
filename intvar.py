class Int(object):
    """Esta clase se usa para implementar variables de tipo entero.
    """

    def __init__(self, id, value):
        """Crear una variable int
        """
        self.id = id
        if(isinstance(value,int)):
            self.value = value
        else:
            print("ASSIGNING " + self.id + " A NON-INT VALUE!")
            exit()

    def getId(self):
        return self.id

    def getValue(self):
        return self.value

    def setValue(self, value):
        if(isinstance(value,int)):
            self.value = value
        else:
            print("ASSIGNING " + self.id + " A NON-INT VALUE!")
            exit()
