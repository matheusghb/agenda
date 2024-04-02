from evento import Evento

class Agenda(Evento):
    def criar (self):
        global registro
        titulo = input("Dê um título para o registro: ")
        data = input("Adicione uma data para o registro (dd/mm/aa) ")
        hora = input("Adicione um horário para o registro (hh:mm): ")
        local = input("Adicione o local do registro: ")
        cod = (len(registro))+1
        registro.append([titulo, data, hora, local, cod])

    def editar (self):
        pass

    def deletar (self):
        cod = int("Diga o código do evento que quer deletar. ")
        pass