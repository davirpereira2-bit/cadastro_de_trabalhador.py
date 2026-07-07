from datetime import datetime

dados = dict()

dados['Nome'] = str(input("Nome: "))
nasc = int(input("Nasc: "))
dados ['idade'] = datetime.now().year - nasc
dados ['ctps'] = int(input("Carteira de Trabalho: (0 não tem ) "))

if dados['ctps'] != 0:
        dados ['contratação'] = int(input('Ano da contratação:'))
        dados ['Salario'] = float(input('Salario: R$'))
        dados ['Aposentadoria'] = dados ['idade']+ ((dados ['contratação'] + 35) - datetime.now().year)

print("-="*30)
for k, v in dados.items():
    print(f"  - {k} tem o valor {v}:")
