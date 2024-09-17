# script para normalizar os dados dos plan traces de Sousa (2024)

# -*- coding: utf-8 -*-

def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                # verificar se a linha é uma linha de cabeçalho (começa com "Plan trace")
                if line.startswith('Plan trace'):
                    # manter a linha de cabeçalho
                    outfile.write('\n' + line)
                else:
                    # verificar se a linha tem pelo menos dois dois pontos
                    if ':' in line:
                        # separar a linha na parte antes e depois do primeiro dois pontos
                        parts = line.split(':', 2)
                        # verificar se tem pelo menos três partes
                        if len(parts) > 2:
                            # manter apenas a parte após o segundo dois pontos e remover espaços em excesso
                            cleaned_line = parts[2].strip()
                            # escrever a linha processada no arquivo
                            outfile.write(cleaned_line + '\n')
    except Exception as e:
        print 'Erro ao processar o arquivo: {}'.format(e)

if __name__ == "__main__":
    input_filename = 'plan-traces-only-with-actions.txt'
    output_filename = 'input_fernando.txt'
    process_file(input_filename, output_filename)
    print 'Arquivo processado e salvo como {}'.format(output_filename)



