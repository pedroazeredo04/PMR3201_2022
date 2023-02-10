# 💻 PMR3201 - Computação pra Automação

## ✨ Introdução

Este repositório se refere à entrega do Exercício Programa da disciplina PMR3201 para engenharia mecatrônica, ministrada no primeiro semestre de 2022.

## 📂 Arquivos

O repositório foi brevemente arquiteturado da seguinte maneira:

- __.gitignore__
- __src/__ - Pasta contendo as funções usadas no EP.
  - __encoding_functions.py__ - Funções de codificação e decodificação de texto.
  - __tree_functions.py__ - Funções relacionadas às árvores binárias.
  - __utils.py__ - Funções de utilidade geral.
- __docs/__
  - __Alice1.txt__ - Texto contendo o primeiro capítulo de Alice in Wonderland.
  - __abracadabra.txt__ - Texto contendo a palavra "ABRACADABRA".
  - __dickens.txt__ - Texto contendo a frase "it was the best of times it was the worst of times".
  - __enunciado.pdf__ - Enunciado do exercício.
- __test.py__
- __main.py__
- __README.md__

### _main.py_

Função principal do exercício.
Nela, você pode escolher entre duas opções:

1. __Codificar mensagem:__ lê um texto e o codifica de acordo com o algorítmo de huffman, escrevendo-o em outro arquivo, na forma de _bytes_.
2. __Decodificar mensagem:__ lê um arquivo codificado, na forma de _bytes_, e o traduz; escrevendo-o num arquivo de texto.

Dentro dessas ações, tanto os arquivos a serem lidos quanto os arquivos a serem escritos são determinados pelo usuário.

Ao digitar o nome do arquivo, precisa-se colocar a extensão (.txt para textos decodificados e .huf para textos codificados). Além disso, todos os arquivos a serem lidos e escritos estarão dentro da pasta ```/docs``` do repositório.

### _test.py_

Função de teste, que permite o usuário checar a codificação e decodificação da mensagem sem escrever ela em nenhum arquivo. Nela, você pode escolher entre três mensagens:

1. abracadabra.txt
2. dickens.txt
3. Alice1.txt

Ao escolher, o programa printará o texto, sua codificação em binário e a tradução dessa codificação no terminal.

## 🚀 Execução

Para executar a função principal do projeto, basta rodar o comando:

```console
python3 main.py 
```

Já para executar os testes, basta rodar o comando:

```console
python3 test.py
```
