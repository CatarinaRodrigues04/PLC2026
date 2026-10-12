# TPC3 - Analisador Léxico

- **Nome:** Catarina Alves Rodrigues
- **ID:** a111491
- **Foto:** 

<img src="foto.JPG" alt="Foto" width="150"/>

## Resumo

O objetivo deste trabalho é construir um analisador léxico em Python para uma linguagem de query (estilo SPARQL) recorrendo a expressões regulares com o módulo `re`.

O analisador processa a string de entrada e identifica as seguintes categorias de tokens:
- **Comentários (`COMMENT`)**: linhas inicidadas por `#`(ignorados no output);
- **Variáveis (`VAR`)**: identificadores iniciados por `?`;
- **Identificador de Língua (`LANG`)**: marcados por `@` seguidos de 2 caracteres (ex: `@en`);
- **Strings (`STRING`)**: sequências de caracteres delimitadas por aspas;
- **Palavras Reservadas (`RESERVED`)**: palavras-chave da linguagem como `LIMIT`, `select`, e `where`;
- **Valores Numéricos (`NUMBER`)**: sequências numérias inteiras;
- **Conceitos (`CONCEPT`)**: identificadores alfanuméricos simples e QNames com prefixos (ex: \`dbo:MusicalArtist\`);
- **Delimitadores (`DELIM`)**: os caracteres `{`, `}`e `.`.

A implementação utiliza uma expressão regular mestre com grupos nomeados e a função `re.finditer()`para percorrer o texto de entrada e gerar a sequência de tokens com identificação da linha correspondente.

## Lista de Resultados

- [Analisador Léxico em Python](tpc3.py)
- [Ficheiro de Teste](exemplo.txt)
