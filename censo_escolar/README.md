# Censo Escolar (INEP): municípios das 3 regiões

Escolas, matrículas, turmas, professores e infraestrutura escolar nos 21 municípios dos três recortes deste repositório, em 2010, 2022 e 2025, com RS e Brasil como referência.

- `censo_escolar_regioes.ipynb`: notebook do Google Colab que baixa os microdados do Censo Escolar do INEP (um zip por ano), filtra as escolas em atividade dos 21 municípios e gera a planilha, um CSV escola a escola e os gráficos. Os anos ficam na variável `ANOS` (qualquer ano de 2007 a 2025).

**Indicadores:** escolas em atividade (por rede e rurais); matrículas por etapa (creche, pré-escola, fundamental anos iniciais e finais, médio, profissional, EJA, educação especial); divisão das matrículas entre redes e zona rural; turmas e alunos por turma; professores e alunos por professor; % de escolas com internet, banda larga, biblioteca, laboratórios, quadra, esgoto da rede pública, água potável e alimentação.

**Cuidados:**
- O número de professores é a soma por escola: quem dá aula em duas escolas conta duas vezes.
- Alguns itens de infraestrutura não existiam em todos os anos; nesses casos o valor fica vazio.
- Os três recortes se sobrepõem (Candelária está nos três), então não some os totais entre eles.

Fonte: [INEP, microdados do Censo Escolar](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar).
