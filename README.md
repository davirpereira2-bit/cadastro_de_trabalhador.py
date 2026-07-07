# cadastro_de_trabalhador.py

# Cadastro de Trabalhador

Programa em Python que cadastra dados básicos de um trabalhador e, caso ele possua carteira de trabalho assinada, calcula automaticamente informações adicionais como salário e previsão do ano de aposentadoria.

## 📋 Funcionalidades

- Cadastro de nome e ano de nascimento, com cálculo automático da idade atual
- Verificação se o trabalhador possui carteira de trabalho (CTPS)
- Caso possua, coleta o ano de contratação e o salário
- Cálculo estimado da idade de aposentadoria, com base no ano de contratação (considerando 35 anos de contribuição)
- Exibição de todos os dados cadastrados de forma organizada, percorrendo o dicionário

## 🛠️ Tecnologias utilizadas

- Python 3
- Módulo `datetime` (para obter o ano atual dinamicamente)
- Dicionários (`dict`)
- Estruturas condicionais (`if`)
- Formatação de strings com f-strings

## 💻 Conceitos praticados

- Uso de dicionários para armazenar dados heterogêneos de forma nomeada (chave-valor)
- Obtenção de dados dinâmicos com `datetime.now().year`, evitando valores fixos no código
- Lógica condicional para tratar cadastros com informações opcionais
- Iteração sobre dicionários com `.items()` para exibição dos dados
- Cálculo com base em regras de negócio simples (estimativa de aposentadoria)

## ▶️ Como executar

```bash
python cadastro_trabalhador.py
```

O programa pede nome, ano de nascimento e se o trabalhador possui carteira assinada. Se a resposta for diferente de 0, também pergunta o ano de contratação e o salário.

## 📄 Exemplo de uso

```
Nome: Carlos Eduardo
Nasc: 1990
Carteira de Trabalho: (0 não tem ) 1
Ano da contratação:2015
Salario: R$3500
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  - Nome tem o valor Carlos Eduardo:
  - idade tem o valor 36:
  - ctps tem o valor 1:
  - contratação tem o valor 2015:
  - Salario tem o valor 3500.0:
  - Aposentadoria tem o valor 71:
```

## 🔍 Possíveis melhorias futuras

- Tratamento de exceções para entradas inválidas (`try/except`), como letras no lugar de números
- Validação de ano de nascimento e ano de contratação (evitar anos futuros ou inconsistentes)
- Deixar a regra de anos de contribuição (35) como uma variável configurável, em vez de valor fixo no código
- Adicionar opção de cadastrar múltiplos trabalhadores em uma lista

## 👤 Autor

Projeto desenvolvido por DAVI RAPOSO PEREIRA como parte dos estudos de lógica de programação em Python, com foco em dicionários e no módulo `datetime`.
