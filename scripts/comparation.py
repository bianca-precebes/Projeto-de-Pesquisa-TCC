# script para comparar os caminhos dos diálogos com os plan traces de Sousa (2024), após normalização

# -*- coding: utf-8 -*-

def read_file(filename):
	# lê um arquivo e retorna uma lista de seções divididas por cabeçalhos (Caminho do diálogo ou Plan trace)
    with open(filename, 'r') as file:
        content = file.read()
    sections = content.split('\n\n')  # separa o conteúdo em seções por linhas em branco
    return sections

def extract_sections(sections, header_prefix):
   # extrai as seções que começam com o cabeçalho específico
    extracted = {}
    for section in sections:
        lines = section.split('\n') # divisão da seção em linhas
        
        lines = [line for line in lines if line.strip() != ''] # remoção das linhas vazias
            
        if lines and lines[0].startswith(header_prefix):
           header = lines[0].strip()
           #print("Header detectado: {}".format(header))
           content = '\n'.join(lines[1:]).strip() # pega o conteúdo depois do cabeçalho
           #print("Conteúdo detectado: {}".format(content))
           extracted[header] = content
           
    return extracted


def compare_sections(sections1, sections2):
    # compara as seções dos dois arquivos e retorna quais seções do primeiro estão presentes no segundo
    matches = []
    for header1, content1 in sections1.items():
    	#print("Header detectado: {}".format(header1))
    	#print("Conteúdo detectado: {}".format(content1))
        for header2, content2 in sections2.items():
        	#print("Header detectado: {}".format(header2))
        	#print("Conteúdo detectado: {}".format(content2))
        	if content1 == content2:
        		matches.append(header1)
                break
    return matches

def main(file1, file2):
    
    sections1 = read_file(file1)
    sections2 = read_file(file2)

    extracted1 = extract_sections(sections1, "Caminho do diálogo")
    extracted2 = extract_sections(sections2, "Plan trace")

    matches = compare_sections(extracted1, extracted2)

    print("Número de 'Caminho do diálogo' que têm correspondentes em 'Plan trace': {}".format(len(matches)))
    print("Seções correspondentes:")
    for match in matches:
        print(match)

if __name__ == '__main__':
    main('input_bianca_final.txt', 'input_fernando.txt')



