# script para normalizar os predicados do usuário encontrados

# -*- coding: utf-8 -*-

import re

# verificar se a linha é um dicionário formatado e não está vazio
def is_non_empty_dict(line):
    # remover espaços extras e verificar se a linha começa e termina com as chaves
    cleaned_line = line.strip()
    if cleaned_line.startswith('{') and cleaned_line.endswith('}'):
        # verificar se o dicionário não está vazio
        content = cleaned_line[1:-1].strip()  # remover as chaves
        return len(content) > 0
    return False

def filter_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        write_lines = False
        for line in infile:
            # ver o início das seções e gravar, se necessário
            if line.startswith('Predicados do diálogo'):
                write_lines = True
                outfile.write(line)
            elif write_lines and is_non_empty_dict(line):
                outfile.write(line)
            elif line.strip() == '':  # ignorar linhas vazias
                outfile.write(line)

filter_lines('user_predicates.txt', 'user_predicates_final.txt')

