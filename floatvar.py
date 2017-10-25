class Float(object):
    """Esta clase se usa para implementar variables de tipo entero.
    """

    def __init__(self, id, value):
        """Crear una variable int
        """
        self.id = id
        if(isinstance(value,floats)):
            self.value = value
        return "ASSIGNING TO " + self.id + " A NON-FLOAT VALUE!"

    def getId(self):
        return self.id

    def getValue(self):
        return self.value

    def setValue(self, value):
        if(isinstance(value,floats)):
            self.value = value
        return "ASSIGNING " + self.id + " A NON-FLOAT VALUE!"
