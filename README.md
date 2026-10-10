# 🤖 Automação de Cadastro de Produtos

Projeto desenvolvido em **Python** para automatizar o cadastro de produtos em um sistema web utilizando dados armazenados em um arquivo CSV.

O programa utiliza a biblioteca **PyAutoGUI** para controlar o computador, abrir o navegador, acessar o sistema, realizar o login e cadastrar automaticamente os produtos presentes na planilha.

## 📌 Sobre o projeto

A aplicação foi desenvolvida para praticar conceitos de:

- Automação de tarefas;
- Manipulação de arquivos CSV;
- Leitura de dados com Pandas;
- Controle do mouse e teclado com Python;
- Estruturas de repetição;
- Manipulação de dados de tabelas.

## 🛠️ Tecnologias utilizadas

- 🐍 Python
- 🤖 PyAutoGUI
- 📊 Pandas
- 📄 CSV
- 🌐 Microsoft Edge

## ⚙️ Como funciona

O programa realiza as seguintes etapas:

1. Abre o menu do Windows;
2. Procura e abre o Microsoft Edge;
3. Maximiza o navegador;
4. Acessa o sistema de cadastro;
5. Realiza o login;
6. Lê os produtos presentes no arquivo `produtos.csv`;
7. Percorre cada produto da tabela;
8. Preenche automaticamente os campos:
   - Código;
   - Marca;
   - Tipo;
   - Categoria;
   - Preço unitário;
   - Custo;
   - Observação;
9. Salva o produto;
10. Volta para o início e continua o processo até cadastrar todos os produtos.

## 📂 Estrutura do projeto

```text
📁 automacao-produtos/
├── 📄 codigos.py
├── 📄 produtos.csv
└── 📄 README.md
```

## 📄 Formato do CSV

O arquivo `produtos.csv` deve possuir as seguintes colunas:

```text
codigo
marca
tipo
categoria
preco_unitario
custo
obs
```

Exemplo:

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
001,Marca A,Produto A,Eletrônicos,100,70,Produto novo
002,Marca B,Produto B,Informática,250,180,
```

## 🚀 Como executar

### 1. Instale o Python

Certifique-se de que o Python esteja instalado no computador.

### 2. Instale as bibliotecas

No terminal, execute:

```bash
pip install pyautogui pandas
```

### 3. Configure o arquivo CSV

Coloque o arquivo `produtos.csv` na mesma pasta do programa e certifique-se de que ele possui as colunas esperadas.

### 4. Execute o programa

```bash
python automacao.py
```

Após a execução, o programa realizará o processo de cadastro automaticamente.

## ⚠️ Observações

Este projeto utiliza coordenadas específicas da tela, como:

```python
pyautogui.click(x=674, y=415)
```

Por isso, **as coordenadas podem precisar ser alteradas** caso a resolução, escala ou posição dos elementos na tela sejam diferentes.

Também é necessário que o navegador e a página estejam funcionando conforme esperado para que a automação seja executada corretamente.

## 🎯 Objetivo

O objetivo principal do projeto é demonstrar como o Python pode ser utilizado para **automatizar tarefas repetitivas**, combinando leitura de dados com interação automática com o computador.

## 👨‍💻 Autor

Projeto desenvolvido para estudos de **Python, automação e manipulação de dados**.
