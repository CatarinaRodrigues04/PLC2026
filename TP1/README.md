# TPC1 - Expressão Regular para Linguagem Binária sem "001"

- **Nome:** Catarina Alves Rodrigues
- **ID:** a111491
- **Foto:** 
<img src="foto.JPG" alt="Foto" width="150"/>

## Resumo
O objetivo deste trabalho é construir uma expressão regular capaz de reconhecer a linguagem de strings binárias que não contêm a substring "011".
Para garantir que a sequência "011" nunca é gerada, a palavra dividida em duas fases lógicas. Na primeira parte, representada por "1*", permite-se qualquer combinação de "1"s iniciais antes do surgimento do primeiro "0".
Na segunda parte, representada por "(0|1)*", trata-se do resto da string após o primeiro "0". Nesta fase, qualquer "1" tem de ser imediatamente precedido por um "0" (formando o par "01") e não pode ser seguido por outro "1". Como as opções disponíveis são apenas "0" ou "01" (ambas a começar por "0"), torna-se impossível ter dois "1"s seguidos após um "0", bloqueando definitivamente a criação da sequência proibida "011".

## Lista de Resultados
- [Expressão Regular resultante](er.txt)
