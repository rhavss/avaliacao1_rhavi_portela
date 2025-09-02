quant=int(input("Quantos produtos foram vendidos: "))
cmenor=0
cmaior=0
valortotal=0
while quant in range(quant,0,-1):
    valor=float(input(f"Qual o valor do produto: "))
    quant=quant-1
    valortotal=valortotal+valor
    if valor < 50:
        cmenor=cmenor + 1
    if valor > 50:
        cmaior=cmaior + 1
print(f"O valor total dos produtos é: {valortotal}.")
print(f"Há {cmenor} itens abaixo de 50.")
print(f"Há {cmaior} itens acima de 50.")