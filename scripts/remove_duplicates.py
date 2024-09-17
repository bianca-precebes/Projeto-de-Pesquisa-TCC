# script para remover as linhas duplicadas dos caminhos dos diálogos adquiridos
# processo necessário para fins de comparação com Sousa (2024)

# -*- coding: utf-8 -*-

import sys
import codecs

def remove_consecutive_duplicates(input_file, output_file):
    try:
        infile = codecs.open(input_file, 'r')
        outfile = codecs.open(output_file, 'w')

        with infile as f_in, outfile as f_out:
            current_header = None
            previous_line = None
            
            for line in f_in:
                line = line.strip()
                
                # verificar se a linha é um cabeçalho
                if line.startswith('Caminho do diálogo'):
                    if current_header:
                        f_out.write('\n')  # adicionar uma linha em branco para separar as seções
                    current_header = line
                    f_out.write(current_header + '\n')
                    previous_line = None  # reiniciar o rastreamento de linhas anteriores para um novo cabeçalho
                else:
                    if line != previous_line:
                        f_out.write(line + '\n')
                        previous_line = line  # atualizar a linha anterior para a linha atual
    except UnicodeDecodeError as e:
        print('Erro de decodificação Unicode ao processar o arquivo: {}'.format(e))
    except Exception as e:
        print('Erro ao processar o arquivo: {}'.format(e))

if __name__ == "__main__":
    input_filename = 'input_bianca.txt'
    output_filename = 'input_bianca_final.txt'
    remove_consecutive_duplicates(input_filename, output_filename)
    print('Arquivo processado e salvo como {}'.format(output_filename))





