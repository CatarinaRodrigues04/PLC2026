# TPC1 - Expressão Regular para Linguagem Binária sem "001"

- **Nome:** Catarina Alves Rodrigues
- **ID:** a111491
- **Foto:** 
<img src="foto.JPG" alt="Foto" width="150"/>

## Resumo
O objetivo deste trabalho é construir uma expressão regular capaz de reconhecer a linguagem de strings binárias que não contêm a substring "001".
Para garantir que a sequência "001" nunca é gerada, a palavra dividida em duas fases lógicas. Na primeira parte, representada por '(1|01)*', permite-se qualquer combinação de '1's isolados ou do par '01'. Como casa '0' nesta fase vem obrigatoriamente seguido de um ´1´, é impossível formar dois zeros seguidos ('00') antes de um '1'.
Na segunda parte, representada por '0*', permite-se que a string termine com zero ou mai szeros no final ('0', '00', '000', ...). Assim que a palavra passa a ter dois zeros seguidos, entra nesta fase final e já não pode conter nenhum '1', bloqueando definitivamente a criação da sequênci proibida "001".

## Lista de Resultados
- [Expressão Regular resultante](er.txt)