

# safe-driving
##### Artificial Intelligence to predict accidents on Brazilian highways.
Safe-driving é um software que por meio do uso de redes neurais, busca realizar uma predição probabilística da ocorrência de um acidente em determinada rodovia brasileira.

## Problemática
Segundo a Organização Mundial da Saúde (OMS) os acidentes de trânsito ocupam a nona posição entre as principais causas de morte no mundo. Em torno de 1,25 milhão de pessoas, por ano, morrem em decorrência de acidentes e aproximadamente 50 milhões de pessoas sofrem lesões não fatais. O IPEA aponta ainda em sua pesquisa que em 2014 ocorreram 37,337 acidentes em rodovias federais no país (IPEA e PRF, 2015).

## Solução
Tendo como base toda a problemática dos acidentes e tendo ainda conhecimento dos péssimos estados de conservação das rodovias brasileiras a solução proposta pela equipe é desenvolver uma API que possibilite ao usuário a consulta da probabilidade da ocorrência de um acidente em determinada rodovia, levando em consideração fatores como condições meteorológicas e condições do trecho no momento da ocorrência de acidentes anteriores.

## Arquitetura utilizada
Os dados serão inicialmente treinados por meio de uma LSTM. Quando o usuário entrar com os dados sobre a rodovia que deseja consultar e sua localização, um modelo de ANN simples realizará a filtragem dos dados e retornará a probabilidade de acontecer acidente naquela rodovia.

## Publico alvo
O público alvo do projeto são as pessoas no geral que tenham interesse na consulta da probabilidade de ocorrência de acidente em alguma rodovia.

## Equipe
### Requisitos necessários dos integrantes
Para implementação do projeto sera necessário que:
- Integrantes da equipe possuam conhecimentos em Python e suas bibliotecas;
- Integrantes da equipe possuam conhecimentos a respeito de redes neurais.

### Líder da Equipe
- Maicon Mares @MaiconMares

### Regras de Conduta
Disponível [aqui](https://github.com/deeplearningunb/safe-driving/blob/main/docs/CODE_OF_CONDUCT.md).

### Quantidade de pessoas na equipe
A equipe é composta por 6 integrantes.

### Membros
|Nome	|Matrícula	|GitHub	|E-mail|
|--|--|--|--|
|Amanda Pires	|15/0004796	|pAmanda	|pvieira.amanda@gmail.com|
|Itallo Gravina	|16/0125910	|itallogravina	|Itallo.Gravina@gmail.com|
|Jonathan Jorge	|18/0103580	|Jonathan-Oliveira	|jonathan.jb.oliveira@gmail.com|
|Maicon Mares	|18/0023411	|MaiconMares	|maiconmaresunb@gmail.com|
|Nilo Mendonca	|16/0037522	|nilomendonca	|nilojrmendonca@gmail.com|
|Renan Cristyan	|17/0044386	|RCristyan	|rcristyan9@gmail.com|

### Stakeholders
Professor Diego Dorgam @diegodorgam

## Planejamento
### Objetivo
O objetivo do projeto é disponibilizar informações referentes a periculosidade de determinada rodovia, buscando assim ajudar na redução de acidentes.

### Metas
Construir uma API que permita a consulta da probabilidade de ocorrência de acidente em uma determinada rodovia brasileira.

### Tarefas
Disponível [aqui](https://github.com/deeplearningunb/safe-driving/issues).

## Datasets
Conjunto de dados fornecidos pelos kaggle que foi extraído diretamente do  do site da Polícia Rodoviária Federal disponível por meio deste endereço eletrônico: 
- <https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-acidentes>
- <https://portal.prf.gov.br/dados-abertos-acidentes>
- <https://www.kaggle.com/equeiroz/acidentes-rodovias-federais-brasil-jan07-a-jul19>

Serão utilizados dados de 2017 a 2020 agrupados por ocorrências.

## Bibliografia
- de Lima, Tamires Feitosa, et al. "ANÁLISE EPIDEMIOLÓGICA DOS ACIDENTES DE TRÂNSITO NO BRASIL." Encontro de Extensão, Docência e Iniciação Científica (EEDIC) 5.1 (2019).
