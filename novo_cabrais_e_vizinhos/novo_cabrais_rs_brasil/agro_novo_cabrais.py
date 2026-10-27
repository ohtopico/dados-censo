# ==========================================================================
# Agro de Novo Cabrais (RS): o que mudou
#  - Censo Agropecuário 2006 x 2017 (estabelecimentos, área, agricultura familiar)
#  - Lavouras (PAM, IBGE): 2010 x 2022, cultura por cultura
#  - Rebanhos e produção animal (PPM, IBGE): 2010 x 2022
# Cole tudo numa célula do Colab e rode. Dados da API do SIDRA (IBGE).
# ==========================================================================
import time, requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.float_format', '{:,.1f}'.format)
plt.rcParams.update({'figure.dpi': 110, 'axes.spines.top': False, 'axes.spines.right': False})

LOCAIS = {'Novo Cabrais': 'n6/4313391', 'RS': 'n3/43', 'Brasil': 'n1/1'}
NC = LOCAIS['Novo Cabrais']

def sidra(caminho, tentativas=4):
    url = 'https://apisidra.ibge.gov.br/values/' + caminho.strip('/')
    for i in range(tentativas):
        try:
            r = requests.get(url, timeout=120)
            r.raise_for_status()
            dados = r.json()
            df = pd.DataFrame(dados[1:]).rename(columns=dados[0])
            df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')  # '-' = zero, '..' = não se aplica
            return df
        except Exception as e:
            print(f'  tentativa {i+1} falhou: {e}')
            time.sleep(2 ** (i + 1))
    raise RuntimeError(url)

def num(consulta, nivel):
    return sidra(f'{consulta}/{nivel}')['Valor'].fillna(0).sum()

# Inflação de dez/2010 a dez/2022 (IPCA), para comparar valores em reais de 2022
ipca = sidra('t/1737/v/2266/p/201012,202212/n1/1')['Valor'].values
INFLACAO = ipca[1] / ipca[0]
print(f'R$ 1,00 de 2010 = R$ {INFLACAO:.2f} de 2022\n')

# --------------------------------------------------------------------------
# 1. Censo Agropecuário 2006 x 2017
# --------------------------------------------------------------------------
C06 = 't/1109/p/2006/c218/0'                                   # c12896: 0 total, 119107 familiar
C17 = 't/6880/p/2017/c12517/113601/c12568/113197/c220/110085'  # c829: 46302 total, 46304 familiar
censo = {}
for local, nivel in LOCAIS.items():
    r = {}
    for ano, base, cod_tot, cod_fam, cls in [(2006, C06, '0', '119107', 'c12896'), (2017, C17, '46302', '46304', 'c829')]:
        est = num(f'{base}/v/183/{cls}/{cod_tot}', nivel)
        est_f = num(f'{base}/v/183/{cls}/{cod_fam}', nivel)
        area = num(f'{base}/v/184/{cls}/{cod_tot}', nivel)
        area_f = num(f'{base}/v/184/{cls}/{cod_fam}', nivel)
        r[(ano, 'Estabelecimentos agropecuários')] = est
        r[(ano, 'Estabelecimentos da agricultura familiar')] = est_f
        r[(ano, '% de estabelecimentos familiares')] = 100 * est_f / est
        r[(ano, 'Área total (hectares)')] = area
        r[(ano, '% da área na agricultura familiar')] = 100 * area_f / area
        r[(ano, 'Área média por estabelecimento (ha)')] = area / est
    censo[local] = r
censo = pd.DataFrame(censo).unstack(0)          # linhas: indicador | colunas: (local, ano)
censo = censo[[(l, a) for l in LOCAIS for a in (2006, 2017)]]
print('CENSO AGROPECUÁRIO 2006 x 2017')
print('Obs.: a definição de agricultura familiar mudou um pouco entre os dois Censos (Lei 11.326 x Decreto 9.064).')
display(censo)

# --------------------------------------------------------------------------
# 2. Lavouras de Novo Cabrais, 2010 x 2022 (PAM)
# --------------------------------------------------------------------------
pam = sidra(f't/5457/v/8331,214,215/p/2010,2022/c782/all/{NC}')
pam = pam.rename(columns={'Produto das lavouras temporárias e permanentes': 'cultura'})
pam['var'] = pam['Variável (Código)'].map({'8331': 'area_ha', '214': 'quantidade', '215': 'valor_mil'})
lav = pam.pivot_table(index='cultura', columns=['var', 'Ano'], values='Valor', aggfunc='sum').fillna(0)
lav.columns = [f'{v} {a}' for v, a in lav.columns]
lav['valor_mil 2010 (R$ de 2022)'] = lav['valor_mil 2010'] * INFLACAO
lav = lav[(lav['area_ha 2010'] > 0) | (lav['area_ha 2022'] > 0)].sort_values('valor_mil 2022', ascending=False)
lavouras = lav[['area_ha 2010', 'area_ha 2022', 'quantidade 2010', 'quantidade 2022',
                'valor_mil 2010 (R$ de 2022)', 'valor_mil 2022']]
lavouras.columns = ['Área 2010 (ha)', 'Área 2022 (ha)', 'Produção 2010', 'Produção 2022',
                    'Valor 2010 (mil R$ de 2022)', 'Valor 2022 (mil R$)']
print('\nLAVOURAS DE NOVO CABRAIS (produção em toneladas na maioria das culturas; valor em mil R$)')
display(lavouras)

top = lavouras.drop(index='Total', errors='ignore').head(8)
fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
for ax, (c10, c22, tit) in zip(axes, [('Área 2010 (ha)', 'Área 2022 (ha)', 'Área plantada (hectares)'),
                                      ('Valor 2010 (mil R$ de 2022)', 'Valor 2022 (mil R$)', 'Valor da produção (mil R$ de 2022)')]):
    y = np.arange(len(top))
    ax.barh(y - .2, top[c10], height=.4, color='#b5b5b5', label='2010')
    ax.barh(y + .2, top[c22], height=.4, color='#2e7d32', label='2022')
    ax.set_yticks(y); ax.set_yticklabels(top.index); ax.invert_yaxis()
    ax.set_title(tit); ax.legend()
plt.suptitle('Novo Cabrais: principais lavouras, 2010 x 2022'); plt.tight_layout(); plt.show()

# --------------------------------------------------------------------------
# 3. Rebanhos e produção animal de Novo Cabrais, 2010 x 2022 (PPM)
# --------------------------------------------------------------------------
reb = sidra(f't/3939/v/105/p/2010,2022/c79/all/{NC}')
rebanhos = reb.pivot_table(index='Tipo de rebanho', columns='Ano', values='Valor', aggfunc='sum').fillna(0)
rebanhos = rebanhos[rebanhos.sum(axis=1) > 0]
rebanhos['variação %'] = 100 * (rebanhos['2022'] / rebanhos['2010'].replace(0, np.nan) - 1)
print('\nREBANHOS (cabeças)')
display(rebanhos)

ani = sidra(f't/74/v/106,215/p/2010,2022/c80/all/{NC}')
ani = ani[ani['Tipo de produto de origem animal'] != 'Total']   # o total soma unidades diferentes
ani['var'] = ani['Variável (Código)'].map({'106': 'quantidade', '215': 'valor_mil'})
animal = ani.pivot_table(index=['Tipo de produto de origem animal', 'Unidade de Medida'], columns=['var', 'Ano'],
                         values='Valor', aggfunc='sum')
animal[('valor_mil', '2010 (R$ de 2022)')] = animal[('valor_mil', '2010')] * INFLACAO
animal = animal.dropna(how='all')
print('\nPRODUÇÃO ANIMAL (quantidade e valor em mil R$)')
display(animal)

# --------------------------------------------------------------------------
# 4. Resumo e planilha
# --------------------------------------------------------------------------
tot = lavouras.loc['Total'] if 'Total' in lavouras.index else lavouras.sum()
print('\nRESUMO DE NOVO CABRAIS')
print(f"Área plantada: {tot['Área 2010 (ha)']:,.0f} ha em 2010 -> {tot['Área 2022 (ha)']:,.0f} ha em 2022")
print(f"Valor das lavouras (R$ de 2022): {tot['Valor 2010 (mil R$ de 2022)']/1000:,.1f} mi -> {tot['Valor 2022 (mil R$)']/1000:,.1f} mi")
nc_c = censo['Novo Cabrais']
print(f"Estabelecimentos: {nc_c.loc['Estabelecimentos agropecuários', 2006]:,.0f} em 2006 -> "
      f"{nc_c.loc['Estabelecimentos agropecuários', 2017]:,.0f} em 2017")

with pd.ExcelWriter('agro_novo_cabrais.xlsx') as xls:
    censo.to_excel(xls, sheet_name='Censo Agro 2006x2017')
    lavouras.to_excel(xls, sheet_name='Lavouras 2010x2022')
    rebanhos.to_excel(xls, sheet_name='Rebanhos 2010x2022')
    animal.to_excel(xls, sheet_name='Produção animal')
print('\nPlanilha salva: agro_novo_cabrais.xlsx (pasta à esquerda do Colab)')
