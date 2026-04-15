
# Lista inicial
convidados = ['arthur', 'bruno', 'caio', 'diego']

# Alteracao
convidados.remove("arthur")
convidados.append("thiago")


while(len(convidados)>2):
    print(f"Sinto muito, mas voce nao podera vir{convidados.pop()}")  

for name in convidados:
    print(f"Venha para minha festa {name}")
