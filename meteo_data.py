meses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
    ]

temp_max = []

for mes in meses:
    while True:
        try:
            temperatura = float(input(f"Digite a temperatura máxima de {mes} (deve estar em °C, para décimos usar '.'): "))
            if -10 <= temperatura <= 55:
                temp_max.append(temperatura)
                break
            print("Temperatura deve estar entre -10°C e 55°C, digite novamente.")
        except ValueError:
            print("Digite um número válido.")

media_anual = sum(temp_max)/12

meses_escaldantes = []
for i, temp in enumerate(temp_max):
    if temp > 33:
        meses_escaldantes.append(meses[i])

mais_quente = meses[temp_max.index(max(temp_max))]
menos_quente = meses[temp_max.index(min(temp_max))]

print(f"Temperatura média máxima anual: {media_anual:.1f}°C")
print(f"Quantidade de meses escaldantes: {len(meses_escaldantes)}")
print(f"Mês mais escaldante: {mais_quente}")
print(f"Mês menos quente: {menos_quente}")