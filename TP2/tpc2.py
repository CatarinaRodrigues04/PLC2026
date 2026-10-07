import re

def markdown_to_html(markdown_text):

    # Cabeçalhos
    markdown_text = re.sub(r'^### (.*)$', r'<h3>\1</h3>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^## (.*)$', r'<h2>\1</h2>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^# (.*)$', r'<h1>\1</h1>', markdown_text, flags=re.MULTILINE)

    # Imagem
    markdown_text = re.sub(r'!\\[(.*?)\\]\\((.*?)\\)', r'<img src="\2" alt="\1"/>', markdown_text)

    # Link
    markdown_text = re.sub(r'\\[(.*?)\\]\\((.*?)\\)', r'<a href="\2">\1</a>', markdown_text)

    # Bold
    markdown_text = re.sub(r'\\\*\\\*(.\*?)\\\*\\\*', r'<b>\\1</b>', markdown_text)

    # Itálico
    markdown_text = re.sub(r'\\\*(.\*?)\\\*', r'<i>\\1</i>', markdown_text)

    # Lista Numerada
    # cada linha "1. item" passa a ser "<li>item</li>"
    markdown_text = re.sub(r'^\\d+\\.\\s+(.\*)$', r'<li>\\1</li>', markdown_text, flags=re.MULTILINE)

    # envolve linhas consecutivas de <li> em <ol>...<ol>
    markdown_text = re.sub(r'((?:<li>.\*</li>\\n?)+)', r'<ol>\\n\\1</ol>', markdown_text)

    return markdown_text

if __name__ == "__main__":
    with open("exemplo.md", "r", encoding="utf-8") as f:
        conteudo_md = f.read()

    resultado_html = markdown_to_html(conteudo_md)

    with open("resultado.html", "w", encoding="utf-8") as f:
        f.write(resultado_html)

    print("Conversão convertida com sucesso!")