class Evento:
    def __init__(self, titulo, data, hora, local, registro):
        self.titulo = titulo
        self.data = data
        self.hora = hora
        self.local = local
        self.registro = []
        self.registro = registro

    def str (self):
        print (self.registro[:])