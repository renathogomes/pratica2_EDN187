# 1 - Conversor de Moeda
reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

dolar = reais / taxa_dolar
euro = reais / taxa_euro

print("Conversor de Moeda")
print(f"Valor em reais: R$ {reais:.2f}")
print(f"Valor em dólares: $ {dolar:.2f}")
print(f"Valor em euros: € {euro:.2f}")

# 2 - Calculadora de Desconto
produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20

valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto

print("Calculadora de Desconto")
print(f"Produto: {produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {desconto_percentual}% (R$ {valor_desconto:.2f})")
print(f"Preço final: R$ {preco_final:.2f}")
print()

# 3 - Calculadora de Média Escolar
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print("Calculadora de Média Escolar")
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")
print(f"Média: {media:.2f}")
print()

# 4 - Calculadora de Consumo de Combustível
distancia = 300
combustivel_gasto = 25

consumo_medio = distancia / combustivel_gasto

print("Calculadora de Consumo de Combustível")
print(f"Distância percorrida: {distancia} km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")