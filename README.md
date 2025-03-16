# Teste Backend - Análise e Recomendação de Filmes

Este repositório contém dois scripts Python que utilizam a API do TMDb para analisar dados de filmes e recomendar filmes similares. Foi desenvolvido como parte de um teste técnico para a vaga de Backend.

## Pré-requisitos

Antes de executar os scripts, você precisa ter:

- **Python 3.x** instalado na sua máquina.
- A biblioteca **`requests`** instalada. Ela é usada para fazer as requisições à API do TMDb.


# Como Executar os Scripts
## 1. **Análise de Dados de Filmes (teste_1.py)**
Este script analisa a participação de atores, a frequência de gêneros e a bilheteria dos filmes com base em uma lista de IDs fornecida pelo usuário.

## Passos para Executar:
1. Abra o terminal na pasta onde o arquivo **teste_1.py** está localizado.
2. Execute o comando: **python teste_1.py**

3. **Quando solicitado, insira os IDs dos filmes que deseja analisar, separados por vírgula. Por exemplo:**
  Digite os IDs dos filmes separados por vírgula (ex: 550, 155, 27205): 550, 155, 27205

4. **O script exibirá os seguintes resultados**:

  * **Participação dos Atores**: Quantos filmes cada ator participou.

  * **Frequência dos Gêneros**: Quantos filmes de cada gênero foram analisados.

  * **Top 5 Atores com Maior Bilheteria**: Os atores que geraram mais receita nos filmes analisados.