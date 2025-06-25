import pandas as pd

def renomear_colunas(df: pd.DataFrame):
    """Renomeia colunas do DataFrame para um padrão mais amigável."""
    df.rename(columns={
        'Data': 'data',
        'Dia da Semana': 'dia_da_semana',
        'Gasto (R$)': 'gasto',
        'Impressões': 'impressoes',
        'Alcance': 'alcance',
        'Cliques no Link': 'cliques_no_link',
        'CTR (%)': 'ctr',
        'CPC (R$)': 'cpc',
        'Custo por Visita (R$)': 'custo_por_visita',
        'Custo por Mensagem (R$)': 'custo_por_mensagem',
        'valor_total_vendas': 'valor_total_vendas',
        'ROAS (calculado)': 'roas'}, inplace=True)
    return df

def selecionar_roas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Seleciona apenas as linhas do DataFrame onde o ROAS é maior que 0.
    """
    df_selecionado = df[df['roas'] > 0]
    return df_selecionado