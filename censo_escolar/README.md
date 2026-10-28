# Censo Escolar (INEP): municípios das 3 regiões

Escolas, matrículas, turmas, professores e infraestrutura escolar nos 21 municípios dos três recortes deste repositório, em 2010, 2022 e 2025, com RS e Brasil como referência. Matrículas, turmas e professores vão até 2022 (ver Cuidados).

- `dados_censo_escolar_regioes.xlsx`: indicadores por município e ano, tabela com variação, totais dos três recortes e dados longos. A aba **Leia-me** explica as definições.
- `escolas_21_municipios.csv`: uma linha por escola em atividade nos 21 municípios, em cada ano.
- `graficos/`: 9 gráficos (matrículas, creche, ensino médio, escolas, escolas rurais, rede municipal, alunos por turma, internet e etapas por recorte).
- `censo_escolar_regioes.ipynb`: notebook do Google Colab que baixa os microdados do Censo Escolar do INEP (um zip por ano), filtra as escolas em atividade dos 21 municípios e gera a planilha, um CSV escola a escola e os gráficos. Os anos ficam na variável `ANOS` (qualquer ano de 2007 a 2025).

**Indicadores:** escolas em atividade (por rede e rurais); matrículas por etapa (creche, pré-escola, fundamental anos iniciais e finais, médio, profissional, EJA, educação especial); divisão das matrículas entre redes e zona rural; turmas e alunos por turma; professores e alunos por professor; % de escolas com internet, banda larga, biblioteca, laboratórios, quadra, esgoto da rede pública, água potável e alimentação.

**Destaques (microrregião de Santa Cruz do Sul, 16 municípios):**
- As matrículas da educação básica caíram de 70.018 (2010) para 62.859 (2022), −10%. Só Mato Leitão cresceu (+13%); Passa Sete (−46%) e Cerro Branco (−43%) foram os que mais perderam.
- A creche foi na direção contrária: de 4.227 para 7.412 matrículas (+75%). A pré-escola subiu 36%, e a educação especial quase dobrou (1.972 para 3.831).
- A EJA (jovens e adultos) encolheu 56%, e o fundamental anos finais, 27%.
- Havia 431 escolas em atividade em 2010 e 343 em 2025. As rurais caíram de 242 para 108. Sinimbu (26 para 9) e Gramado Xavier (19 para 7) foram os que mais fecharam escolas; Santa Cruz do Sul foi de 96 para 117, puxada pelas escolas privadas.
- Escolas com internet: de 46% em 2010 para 100% em 2025.

**Cuidados:**
- Em 2025 o INEP passou a publicar os microdados em várias tabelas, e a tabela de escolas não traz mais matrículas, turmas e professores. Por isso esses indicadores vão até 2022; escolas e infraestrutura vão até 2025 (coluna "Último ano com dado" na planilha).
- Água potável e "sem nenhum item de acessibilidade" não eram perguntados em 2010.
- Na variação da creche, municípios sem nenhuma matrícula de creche em 2010 (Passa Sete) ficam sem percentual.
- O número de professores é a soma por escola: quem dá aula em duas escolas conta duas vezes.
- Alguns itens de infraestrutura não existiam em todos os anos; nesses casos o valor fica vazio.
- Os três recortes se sobrepõem (Candelária está nos três), então não some os totais entre eles.

Fonte: [INEP, microdados do Censo Escolar](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar).
