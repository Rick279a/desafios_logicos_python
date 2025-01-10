"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

import json

# Exemplo de JSON com dados de faturamento
faturamento_json = '''
[
    {"dia": 1, "valor": 100.0},
    {"dia": 2, "valor": 200.0},
    {"dia": 3, "valor": 0.0},
    {"dia": 4, "valor": 300.0},
    {"dia": 5, "valor": 150.0},
    {"dia": 6, "valor": 0.0},
    {"dia": 7, "valor": 400.0}
]
'''

faturamento = json.loads(faturamento_json)

valores = [dia["valor"] for dia in faturamento if dia["valor"] > 0]
menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Dias com acima da média: {dias_acima_da_media}")
