#!/home/linuxbrew/.linuxbrew/bin/python3
"""Hello word Multi Linguas.

Depedendo do ambiente configuarar a linguagem.

Como usar:
Tenha a variável LANG configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ ="0.0.1"
__author__ ="Lucas Telles"
__license__ ="Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, Word!"

if current_language =="pt_BR":
    msg = "Olá, Mundo!"
elif current_language =="it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, MUndo!"
elif current_language =="fr_FR":
    msg = "Bonhour Monde"
    
print(msg)
