from evento import Evento

class Agenda(Evento):
    def __init__ (self, titulo, data, hora, local, registro):
        self.titulo = titulo
        self.data = data
        self.hora = hora
        self.local = local
        self.registro = []
        self.registro = registro

    def criar (self):
        self.titulo = input("Dê um título para o registro: ")
        self.data = input("Adicione uma data para o registro (dd/mm/aa) ")
        self.hora = input("Adicione um horário para o registro (hh:mm): ")
        self.local = input("Adicione o local do registro: ")
        self.registro.append(f'{self.titulo}\n'
                        f'{self.data}\n'
                        f'{self.hora}\n'
                        f'{self.local}')
    def editar (self, pesquisa, a):
        pesquisa = input("Diga o título da agenda que procura: ")
        a = self.registro.find(pesquisa)
        if a >= 0:
            pass
        else:
            print ("Não há um evento com esse título. ")

    def deletar (self):
        self.cod = int("Diga o código do evento que quer deletar. ")
        pass