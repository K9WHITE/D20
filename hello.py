import random
import time


print("A frente você se depara com 3 caminhos diferentes:")
print("1 -Floresta das Almas Perdidas")
print("2 -Desertos dos Sussuros Eternos")
print("3 -Montanha da Aurora Dividida")

opcao = int(input("Qual você deseja seguir?: "))


if opcao == 1:
    print("Você seguiu para A Floresta das Almas Perdidas.")
elif opcao == 2:
    print("Você seguiu para O Deserto dos Sussuros Eternos.")
elif opcao == 3:
    print("Você seguiu para A Montanha da Aurora Dividida.")
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")

time.sleep(4)

if opcao == 1:
    print("Você se depara com Eldralith, o Guardião das Almas Errantes.")
    time.sleep(3)
elif opcao == 2:
    print("Você se depara com Arengoth, Senhor dos Ventos Sibilantes.")
    time.sleep(3)
elif opcao == 3:
    print("Você se depara com Aurorus, o Guardião das Alvoradas.")
    time.sleep(3)




print("Rode o dado para desviar do atk!")
time.sleep(2)
r1 = random.randint(1,20)
print("Você tirou:",r1)

if r1<10:
    print("Você Morreu!")
    exit()
else:
    print("Desviou")

forca=input("Digite seu bonus de força:")
print("Role o dado para realizar o atk!")
time.sleep(2)

r2= random.randint(1,15)
r3=int(r2)+int(forca)

if r3>10:
    print(r3,"Dano critico")
else:
    print(r3,"Dano minimo, Você morrreu!")
    exit()

print("No local do corpo são deixados 2 itens:")
time.sleep(4)
if opcao == 1:
    print("Arco da Redenção Espiritual e a Túnica das Almas Tranquilas")
    time.sleep(3)
elif opcao == 2:
    print("Cajado do Sussurro Zéfiro e o Manto do Véu de Areia")
    time.sleep(3)
elif opcao == 3:
    print("Espada da Aurora Eterna e o Amuleto do Solstício")
    time.sleep(3)
print("Itens adicionados ao inventario")
exit()