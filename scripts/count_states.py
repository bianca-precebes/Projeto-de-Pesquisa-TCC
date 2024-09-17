# script para contabilizar os predicados com configurações únicas

# -*- coding: utf-8 -*-

import ast

# analisa e conta dicionários únicos em um arquivo
def count_unique_dicts(file_path):
    unique_dicts = set()
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('{') and line.endswith('}'):
                try:
                    # converte a linha para um dicionário
                    dict_obj = ast.literal_eval(line)
                    # adiciona o dicionário ao conjunto de dicionários únicos
                    unique_dicts.add(frozenset(dict_obj.items()))
                except (ValueError, SyntaxError):
                    # falha da conversão
                    continue
    
    return unique_dicts

file_path = 'output.txt'
uniques = count_unique_dicts(file_path)
quant = len(uniques)
print("Número de dicionários únicos: {}".format(quant))
print('\n')
print(uniques)

