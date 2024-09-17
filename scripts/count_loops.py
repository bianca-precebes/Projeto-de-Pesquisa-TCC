# script para contabilizar os caminhos dos diálogos com loops

# -*- coding: utf-8 -*-

def count_dialog_paths_with_error_treatment(file_path):
    
    error_treatment_count = 0
    in_dialog_section = False
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            
            # vê se a linha é uma nova seção de diálogo
            if line.startswith('Caminho do diálogo'):
                in_dialog_section = True
                has_error_treatment = False
            elif line == '':
                # termina a seção atual se encontrar uma linha em branco
                if in_dialog_section and has_error_treatment:
                    error_treatment_count += 1
                in_dialog_section = False
            elif in_dialog_section:
                # verifica se a linha contém "error-treatment"
                if 'error-treatment' in line:
                    has_error_treatment = True

        # verifica a última seção se não terminar com uma linha em branco
        if in_dialog_section and has_error_treatment:
            error_treatment_count += 1

    return error_treatment_count

file_path = 'input_bianca_final.txt'
count = count_dialog_paths_with_error_treatment(file_path)
print("Número de seções que contêm error-treatment: {}".format(count))

