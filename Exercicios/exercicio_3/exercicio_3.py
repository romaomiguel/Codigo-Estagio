import json

# Função para processar os dados de faturamento
def processar_faturamento(caminho_arquivo):

    # Abra/fecha e leia o arquivo JSON
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    
    # Extrair valores de faturamento ignorando dias sem faturamento
    faturamentos = [float(dia['valor']) for dia in dados if float(dia['valor']) > 0] #Se valor for menor que 0 ele vira um "float" e é adicionado em faturamentos
    
    # Se não houver faturamento, retornamos valores nulos e zero
    if not faturamentos:
        return None, None, 0 
    
    #Divisão das variaveis menor, maior, media extraindo do arquivo dados.json
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_faturamento = sum(faturamentos) / len(faturamentos)
    
    dias_acima_da_media = len([f for f in faturamentos if f > media_faturamento])
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

caminho_arquivo = r'C:\Users\amand\Desktop\Trabalho\Teste-de-Codigo-Estagio\exercicio_3\dados.json'  # O caminho completo para o arquivo JSON
menor, maior, dias_acima = processar_faturamento(caminho_arquivo)

if menor is not None and maior is not None:
    print(f'Menor valor de faturamento: R${menor:.2f}')
    print(f'Maior valor de faturamento: R${maior:.2f}')
    print(f'Número de dias com faturamento acima da média: {dias_acima}')
else:
    print('Não há faturamento disponível para processamento.')