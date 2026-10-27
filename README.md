# Dados dos Censos 2010 e 2022: Candelária, Novo Cabrais e região de Santa Cruz do Sul

Comparações entre os Censos Demográficos do IBGE de 2010 e 2022 para três recortes de municípios do Vale do Rio Pardo (RS), sempre com o Rio Grande do Sul e o Brasil como referência. Cada pasta traz a planilha com os números, o notebook do Google Colab que baixa tudo do IBGE, os gráficos e o infográfico.

| Pasta | Recorte | Municípios |
|---|---|---|
| [`candelaria_e_vizinhos/`](candelaria_e_vizinhos/) | Candelária e os 8 municípios que fazem divisa com ela | 9 |
| [`novo_cabrais_e_vizinhos/`](novo_cabrais_e_vizinhos/) | Novo Cabrais e os 4 municípios que fazem divisa com ela | 5 |
| [`alfabetizacao_microrregiao_santa_cruz/`](alfabetizacao_microrregiao_santa_cruz/) | Alfabetização na microrregião IBGE de Santa Cruz do Sul (43020) | 16 |

## Fonte

Todos os números vêm do IBGE, pela API do SIDRA (`apisidra.ibge.gov.br`), extraídos em 27/10/2026. Valores em reais de 2010 foram corrigidos pelo IPCA para reais de julho de 2022 (fator 2,061; tabela 1737).

| Tema | 2010 | 2022 |
|---|---|---|
| População, idade e sexo | 1378 | 9514 |
| Zona urbana | 1378 | 9923 |
| Cor ou raça | 3175 | 9605 |
| Domicílios | 3451 | 4712 |
| Água, esgoto, lixo | 3218 | 6803, 6805, 6892 |
| Alfabetização | 3213 (+ 1378 para a população) | 9542 |
| Renda do trabalho | 3577 | 10291 |
| PIB dos Municípios | 5938 | 5938 |
| Agropecuária | Censo Agro 2006 (1109) | Censo Agro 2017 (6880), PAM 5457, PPM 3939 e 74 |

## 1. Candelária e vizinhos

Municípios (código IBGE): Candelária (4304200), Cachoeira do Sul (4303004), Cerro Branco (4305132), Lagoa Bonita do Sul (4311239), Novo Cabrais (4313391), Passa Sete (4314068), Rio Pardo (4315701), Vale do Sol (4322533) e Vera Cruz (4322707).

- `dados_candelaria_vizinhos_2010_2022.xlsx`: 30 indicadores em 2010 e 2022, variação, ranking de avanços e agropecuária. A aba **Leia-me** explica fontes e cuidados.
- `candelaria_vizinhos_2010_2022.ipynb`: notebook que gera a planilha e os gráficos.
- `graficos/`, `infografico_candelaria_vizinhos.{png,pdf}`, `materia_candelaria_vizinhos.{pdf,docx}` (matéria de jornal) e `resumo_destaques.txt`.

Destaques: Candelária passou de 30.171 para 28.906 habitantes (−4,2%), e só Vera Cruz cresceu entre os 9. No ranking de avanços, Novo Cabrais ficou em 1º, Passa Sete em 2º e Candelária e Vale do Sol empatadas em 3º. Na região, a área de fumo caiu 35% e a de soja multiplicou por 2,4.

## 2. Novo Cabrais e vizinhos

Municípios: Novo Cabrais (4313391), Cachoeira do Sul (4303004), Candelária (4304200), Cerro Branco (4305132) e Paraíso do Sul (4314027).

- `dados_novo_cabrais_vizinhos_2010_2022.xlsx`: valores de 2010 e 2022, variação, avanço, ranking, idade e agropecuária.
- `novo_cabrais_vizinhos_2010_2022.ipynb`, `graficos/` e `infografico_novo_cabrais.{png,pdf}`.
- `novo_cabrais_rs_brasil/`: notebook só de Novo Cabrais x RS x Brasil (30 indicadores) e o script da agropecuária (`agro_novo_cabrais.py`).

Destaques: Novo Cabrais foi o município que mais avançou entre os 5 (posição média 1,7), à frente de Candelária (2,8), Cachoeira do Sul (3,3), Paraíso do Sul (3,5) e Cerro Branco (3,7). Esgoto adequado subiu 39,4 pontos e a alfabetização de 15+ subiu 3,5 pontos.

> **Pendência:** nas abas "Valores 2010" e "Valores 2022" ainda faltam os números absolutos de Paraíso do Sul (as demais abas já o incluem). Rodar o notebook completa a planilha. Os gráficos desta pasta estão em resolução de tela.

## 3. Alfabetização na microrregião de Santa Cruz do Sul

Os 16 municípios da microrregião IBGE 43020: Arroio do Tigre, Candelária, Estrela Velha, Gramado Xavier, Herveiras, Ibarama, Lagoa Bonita do Sul, Mato Leitão, Passa Sete, Santa Cruz do Sul, Segredo, Sinimbu, Sobradinho, Vale do Sol, Venâncio Aires e Vera Cruz.

- `dados_alfabetizacao_santa_cruz_2010_2022.xlsx`: taxa de alfabetização e pessoas que não sabem ler e escrever (15+), por faixa de idade, e por sexo e cor ou raça (2022).
- `alfabetizacao_santa_cruz_2010_2022.ipynb`, `graficos/` e `infografico_alfabetizacao_santa_cruz.{png,pdf}`.

Destaques: a taxa da região subiu de 94,6% para 96,3%, e o número de pessoas de 15+ que não sabem ler e escrever caiu de 13.886 para 10.398. Todos os 16 municípios melhoraram; os maiores avanços foram Estrela Velha (+4,4 pontos), Passa Sete (+4,0) e Candelária (+3,6).

> **Correção:** a primeira versão desta planilha tinha o grupo de 65 anos ou mais zerado em 2010, o que deixava a taxa de 2010 alta demais. A planilha e o gráfico `01_taxa.png` aqui já estão corrigidos, e o notebook também.

## Como reproduzir

Abra o notebook da pasta no [Google Colab](https://colab.research.google.com/) e rode todas as células. Cada um baixa os dados do SIDRA (alguns minutos) e no fim gera um `.zip` com a planilha e os gráficos.

## Cuidados na comparação

- As perguntas sobre água e esgoto mudaram em 2022; a comparação com 2010 é aproximada.
- "Pessoas ocupadas" não é comparável: 2010 conta todos os ocupados, 2022 só os com rendimento.
- Nos municípios pequenos, a razão de renda entre negros e brancos se baseia em poucas centenas de pessoas.
- A divisão do PIB por setor vai só até 2021, o último ano publicado.
