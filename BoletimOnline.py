import pandas as pd

matricula = list()
aluno = list()
pvb = list()
paw = list()
bd = list()
pooi=list()
media=list()

i=0
while True:
        try:
            matricula_atual=int(input("digite sua matricula: "))
            if matricula_atual > 99999999 or matricula_atual< 1:
                continue
            matricula.append(matricula_atual)
            aluno_atual=input("digite seu nome: ")
            if len(aluno_atual) < 3 or aluno_atual == "":
                continue
            aluno.append(aluno_atual)

            pvb_atual=float(input("digite nota em pvb:"))
            if pvb_atual < 0 or pvb_atual >10:
                continue
            pvb.append(pvb_atual)

            paw_atual = float(input("digite nota em paw:"))
            if paw_atual < 0 or paw_atual > 10:
                continue
            paw.append(paw_atual)

            bd_atual = float(input("digite nota em bd:"))
            if bd_atual < 0 or bd_atual > 10:
                continue
            bd.append(bd_atual)

            pooi_atual = float(input("digite nota em pooi:"))
            if pooi_atual < 0 or pooi_atual > 10:
                continue
            pooi.append(pooi_atual)
            media.append((pvb[i]+paw[i]+bd[i]+pooi[i])/4)
            i+=1

        except Exception as erro:
            print(erro)
            continue

        if input("Deja continuar adicionando?nao-parar: ") == "nao" or "não":
                break;


dicionario = {
    'Matricula': matricula,
    'Aluno': aluno,
    'PVB': pvb,
    'PAW': paw,
    'BD': bd,
    'POOI': pooi,
    'Média': media
}

print(dicionario)
df=pd.DataFrame(dicionario)
print(df)
df.to_excel('c:/PROJETO4BIMESTRE/notasfinais.xlsx',sheet_name='Planilha1', na_rep='#N/A', header=True, index=False)

if input("Deseja gerar um arquivo HTML?  sim - gerar: ") == "sim":
    titulo = "Boletim do Aluno"  # Título fixo da página

    # Percorrer cada aluno pelo índice
    for i in range(len(matricula)):
        # Nome do arquivo HTML usando a matrícula
        nome_arquivo = f"c:/PROJETO4BIMESTRE/{matricula[i]}.html"

        # Abrir o arquivo para escrita
        with open(nome_arquivo, 'w') as arquivo:
            # Escrever a estrutura básica do HTML
            arquivo.write("<!DOCTYPE html>\n")
            arquivo.write("<html lang='pt-BR'>\n")
            arquivo.write("<head>\n")
            arquivo.write("<meta charset='UTF-8'>\n")
            arquivo.write("<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
            arquivo.write(f"<title>{titulo}</title>\n")
            arquivo.write("<style>\n")
            arquivo.write("body { font-family: Arial, sans-serif; text-align: center; }\n")
            arquivo.write("h1 { font-size: 24px; }\n")
            arquivo.write("table { width: 50%; margin: 20px auto; border-collapse: collapse; }\n")

            # Adição da classe .label para cor preta
            arquivo.write(".label { color: black; font-weight: bold; }\n")  # Define a cor preta para "MATRÍCULA" e "ALUNO"

            # Definir cores e status conforme a média
            if media[i] >= 6:
                status = "APROVADO"
                arquivo.write("th, td { padding: 10px; border: 1px solid black; background-color: #add8e6; }\n")
                arquivo.write(".status { color: blue; font-weight: bold; margin-top: 20px; }\n")
            elif media[i] >= 3.75:
                status = "REPROVADO"
                arquivo.write("th, td { padding: 10px; border: 1px solid black; background-color: #FFFF00; }\n")
                arquivo.write(".status { color: yellow; font-weight: bold; margin-top: 20px; }\n")
            else:
                status = "RETIDO"
                arquivo.write("th, td { padding: 10px; border: 1px solid black; background-color: #FF0000; }\n")
                arquivo.write(".status { color: red; font-weight: bold; margin-top: 20px; }\n")

            arquivo.write("th { font-weight: bold; }\n")
            arquivo.write("</style>\n")
            arquivo.write("</head>\n")
            arquivo.write("<body>\n")

            # Título do aluno com "MATRÍCULA" e "ALUNO" em preto
            arquivo.write(f"<h1><span class='label'>RESULTADO FINAL ANUAL DO ALUNO </h1>\n")
            arquivo.write(f"<h1><span class='label'>MATRÍCULA:</span> {matricula[i]}</h1>\n")  # Mudança feita aqui
            arquivo.write(f"<h1><span class='label'>ALUNO:</span> {aluno[i]}</h1>\n")            # Mudança feita aqui

            # Tabela com as notas
            arquivo.write("<table>\n")
            arquivo.write("<tr><th>PVB</th><th>PAW</th><th>BD</th><th>POOI</th><th>MÉDIA</th></tr>\n")
            arquivo.write(f"<tr><td>{pvb[i]}</td><td>{paw[i]}</td><td>{bd[i]}</td><td>{pooi[i]}</td><td>{media[i]:.1f}</td></tr>\n")
            arquivo.write("</table>\n")

            # Status de aprovação
            arquivo.write(f"<p class='status'>{status}</p>\n")

            # Fechar as tags
            arquivo.write("</body>\n")
            arquivo.write("</html>\n")

        print(f"Arquivo '{nome_arquivo}' criado com sucesso!")




