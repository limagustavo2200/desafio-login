import pandas as pd


def agrupar_boletos(df):
    boleto_agrupado = {
        'ID_CONDOMINIO': df['ID_CONDOMINIO'].iloc[0],
        'ID_UNIDADE': df['ID_UNIDADE'].iloc[0],
        'VENCIMENTO': df['VENCIMENTO'].iloc[0],
        'DATA_DE_COMPETENCIA': df['DATA_DE_COMPETENCIA'].iloc[0],
        'CONTA_BANCARIA': df['CONTA_BANCARIA'].iloc[0],
        'NOSSO_NUMERO': df['NOSSO_NUMERO'].iloc[0],
        'TOKEN-FACILITADOR': df['TOKEN-FACILITADOR'].iloc[0],
        'TOKEN-CONTA': df['TOKEN-CONTA'].iloc[0],
    }

    for idx, row in enumerate(df.itertuples(index=False), start=1):
        boleto_agrupado[f'RECEITA_APROPRIACAO{idx}[CONTA_CATEGORIA]'] = row.CONTA_CATEGORIA
        boleto_agrupado[f'RECEITA_APROPRIACAO{idx}[COMPLEMENTO]'] = row.COMPLEMENTO
        boleto_agrupado[f'RECEITA_APROPRIACAO{idx}[VALOR]'] = row.VALOR

    total_apropriacoes = 15
    for i in range(1, total_apropriacoes + 1):
        if f'RECEITA_APROPRIACAO{i}[CONTA_CATEGORIA]' not in boleto_agrupado:
            boleto_agrupado[f'RECEITA_APROPRIACAO{i}[CONTA_CATEGORIA]'] = None
        if f'RECEITA_APROPRIACAO{i}[COMPLEMENTO]' not in boleto_agrupado:
            boleto_agrupado[f'RECEITA_APROPRIACAO{i}[COMPLEMENTO]'] = None
        if f'RECEITA_APROPRIACAO{i}[VALOR]' not in boleto_agrupado:
            boleto_agrupado[f'RECEITA_APROPRIACAO{i}[VALOR]'] = None

    boleto_agrupado.update({
        'TAXA_DE_JUROS': df['TAXA_DE_JUROS'].iloc[0],
        'TAXA_DE_MULTA': df['TAXA_DE_MULTA'].iloc[0],
        'TAXA_DE_DESCONTO': df['TAXA_DE_DESCONTO'].iloc[0],
        'COBRANCA_EXTRAORDINARIA': None})
    return boleto_agrupado


def transformar_planilha(planilha_original):
    boletos_agrupados = []

    grupos = planilha_original.groupby('NOSSO_NUMERO')
    for _, grupo in grupos:
        boletos_agrupados.append(agrupar_boletos(grupo))

    planilha_agrupada = pd.DataFrame(boletos_agrupados)

    return planilha_agrupada


def gerar_arquivo(f):
    file_path = '/tmp/original.csv'
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path
