import sys 
import re 

def tokenize(input_string):
    reconhecidos = []
    linha = 1

    regex = (
        r'(?P<COMMENT>#.*)|'
        r'(?P<VAR>\?[a-zA-Z0-9\_]+)|'
        r'(?P<LANG>@[a-zA-Z]{2})|'
        r'(?P<STRING>"[^"]*")|'
        r'(?P<RESERVED>\b(?:LIMIT|select|where)\b)|'
        r'(?P<NUMBER>\d+)|'
        r'(?P<CONCEPT>[a-zA-Z_][a-zA-Z0-9_]*(?::[a-zA-Z_][a-zA-Z0-9_]*)?)|'
        r'(?P<DELIM>[{}.])|'
        r'(?P<SKIP>[ \t]+)|'
        r'(?P<NEWLINE>\n)|'
        r'(?P<ERRO>.)'
    )

    mo = re.finditer(regex, input_string)

    for m in mo:
        dic = m.groupdict()

        if dic['COMMENT']:
            pass
        elif dic['VAR']:
            t = ("VAR", dic['VAR'], linha, m.span())
            reconhecidos.append(t)
        elif dic['LANG']:
            t = ("LANG", dic['LANG'], linha, m.span())
            reconhecidos.append(t)
        elif dic['STRING']:
            t = ("STRING", dic['STRING'], linha, m.span())
            reconhecidos.append(t)
        elif dic['RESERVED']:
            t = ("RESERVED", dic['RESERVED'], linha, m.span())
            reconhecidos.append(t)
        elif dic['NUMBER']:
            t = ("NUMBER", dic['NUMBER'], linha, m.span())
            reconhecidos.append(t)
        elif dic['CONCEPT']:
            t = ("CONCEPT", dic['CONCEPT'], linha, m.span())
            reconhecidos.append(t)
        elif dic['DELIM']:
            t = ("DELIM", dic['DELIM'], linha, m.span())
            reconhecidos.append(t)
        elif dic['SKIP']:
            pass
        elif dic['NEWLINE']:
            linha += 1
        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], linha, m.span())
            reconhecidos.append(t)

    return reconhecidos

if __name__ == "__main__":
    ficheiro = sys.argv[1] if len(sys.argv) > 1 else "exemplo.txt"

    try:
        with open(ficheiro, "r", encoding="utf-8") as f:
            conteudo = f.read()

        for tok in tokenize(conteudo):
            print(tok)

    except FileNotFoundError:
        print(f"Erro: Ficheiro '{ficheiro}' não encontrado.")