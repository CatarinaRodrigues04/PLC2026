# TPC2 - Conversor de MarkDown para HTML

- **Nome:** Catarina Alves Rodrigues
- **ID:** a111491
- **Foto:** 

<img src="foto.JPG" alt="Foto" width="150"/>

## Resumo

O objetivo deste trabalho é criar um conversor simples de MarkDown para HTML em Python utilizando expressões regulares.

O programa processa os elementos básicos de sintaxe: cabeçalhos (`#`, `##`, `###`), texto em negrito (`**`), itálico (`*`), imagens (`[alt](url)`),
links (`[texto](url)`) e listas numeradas. A resolução foca-se na ordem de substituições (imagens antes de links e negrito antes de itálico para evitar conflitos de padrões) e na utilização de `re.sub()`com grupos de captura para gerar as respetivas tags HTML.

## Lista de Resultados
- [Conversor de MarkDown para HTML](tpc2.py)
- [Ficheiro de Teste](exemplo.md)
- [Ficheiro HTML gerado](resultado.html)