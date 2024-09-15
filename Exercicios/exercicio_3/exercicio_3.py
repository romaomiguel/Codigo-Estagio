import json
import os

# Função para processar os dados de faturamento
def processar_faturamento(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    faturamentos = [float(dia['valor']) for dia in dados if float(dia['valor']) > 0]

    if not faturamentos:
        return None, None, 0 

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_faturamento = sum(faturamentos) / len(faturamentos)

    dias_acima_da_media = len([f for f in faturamentos if f > media_faturamento])

    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Construir o caminho do arquivo relativo ao diretório do script
caminho_arquivo = os.path.join(os.path.dirname(__file__), 'dados.json')  # Assume que o arquivo JSON está no mesmo diretório que o script
menor, maior, dias_acima = processar_faturamento(caminho_arquivo)

if menor is not None and maior is not None:
    print(f'Menor valor de faturamento: R${menor:.2f}')
    print(f'Maior valor de faturamento: R${maior:.2f}')
    print(f'Número de dias com faturamento acima da média: {dias_acima}')
else:
    print('Não há faturamento disponível para processamento.')
