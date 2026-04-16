att 1 
nome = input ("digite sua nome? ")
idade = input("qual a sua idade ? ")
cidade = input("qual cidade voce mora?")

print (f"seu nome é : {nome} tenho {idade} e moro {cidade}");

att 2 
n1 = float(input("digite um numero "))
n2 = float (input( "digite outro numero "))

print (n1 + n2)
print (n1 - n2)
print (n1 / n2 )
print (n1 * n2);

 att 3 
 numero =  int (input ("digite um numero "))

for i in range (1,11):
    resultado = numero*i
    print (f"{numero} x {i} = {resultado}")

   att 4 
   senha = 4

while True:
    numero = int(input ("digite um numero "))
    if numero <4:
        print ("esta abaixo do numero certo ")
    elif numero >4:
        print ("esta acima do numero certo ")
    else:
        print ("voce acertou o numero ");
        break

        ompras = []

 att 5 
 def listadecompras():
    for i in range(5):
        item = input(f"Digite o item {i+1} da sua lista: ")
        compras.append(item)

    print("\nSua lista de compras:")
    for i, item in enumerate(compras, 1):
        print(f"{i}. {item}")

listadecompras()

att 6 
notas = [8,7,6,5,9,8]
maior = max(notas)
menor = min(notas)
media = sum (notas) / len (notas)

print ("maior nota", maior)
print ("menor nota", menor)
print ("media nota", media)

att 7 
def par_ou_impar(n):
    if n % 2 == 0:
        return "par"
    else:
        return "ímpar"

print(par_ou_impar(2))   # par
print(par_ou_impar(7))   # ímpar
print(par_ou_impar(10))  # par