from evento import Evento
from AgendaEventos import Agenda
titulo = ''
data = ''
hora = ''
local = ''
cod = 0

a = Agenda(titulo, data, hora, local, cod)
e = Evento(titulo, data, hora, local, cod)

opt = ''
while opt != 5:
    print ("1 - Criar")
    print ("2 - Editar")
    print ("3 - Deletar")
    print ("4 - Listar")
    print ("5 - Sair")
    print ("Escolha uma das opções acima.")
    opt = int(input("-> "))

    if opt == 1:
        Agenda.criar(a)

    if opt == 2:
       pass 

    if opt == 3:
        pass
    if opt == 4:
        pass
    if opt == 5:
        print ("Fechando programa. ")
    else:
        print ("Erro")