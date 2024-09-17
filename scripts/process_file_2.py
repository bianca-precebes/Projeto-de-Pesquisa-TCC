# script para normalizar os dados dos caminhos de diálogos

# -*- coding: utf-8 -*-

import re
import sys

def process_file(input_file, output_file):
    try:
        if sys.version_info[0] < 3:
            import codecs
            infile = codecs.open(input_file, 'r', 'utf-8')
            outfile = codecs.open(output_file, 'w', 'utf-8')
        else:
            infile = open(input_file, 'r', encoding='utf-8')
            outfile = open(output_file, 'w', encoding='utf-8')

        with infile as f_in, outfile as f_out:
            for line in f_in:
                # remover a linha de troca de turno
                if line.strip() == "----- troca de turno entre bot e humano -----":
                    continue
                
                # remover sufixos como "-v1", "-v2", "-v3"
                cleaned_line = re.sub(r'-v\d+', '', line).strip()
                
                # escrever a linha processada no arquivo
                f_out.write(cleaned_line + '\n')
    except Exception as e:
        print('Erro ao processar o arquivo: {}'.format(e))

if __name__ == "__main__":
    input_filename = 'dialogs_path.txt'
    output_filename = 'input_bianca.txt'
    process_file(input_filename, output_filename)
    print('Arquivo processado e salvo como {}'.format(output_filename))


