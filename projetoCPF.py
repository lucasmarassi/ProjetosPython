print("--" * 10)
lista = list()
dicionario = dict()
qtdd = 0
soma = 0
validos = 0
invalidos = 0
while True:
    # USUÁRIO DIGITA O CPF
    CPF = input("Digite seu CPF: ")
    # VÊ SE O CPF TEM LETRA, SE NÃO TEM NADA OU SE TEM MENOS OU MAIS DE 11 CARACTERES
    while not CPF.isdigit() == True or CPF == '' or len(CPF) != 11:
        CPF = input("DIGITE SEU CPF CORRETAMENTE: ")
    qtdd += 1

    print("-" * 20)
    # CÁLCULO DO PRIMEIRO DIGITO
    for i in range(9):
        num = int(CPF[i])
        soma += num * (10 - i)

    if soma % 11 < 2:
        digitoum = 0
    else:
        digitoum = 11 - (soma % 11)
    soma = 0
    # CÁLCULO DO SEGUNDO DIGITO
    for i in range(9):
        num = int(CPF[i])
        soma += num * (11 - i)

    soma += digitoum * 2
    if soma % 11 < 2:
        digitodois = 0
    else:
        digitodois = 11 - (soma % 11)

    # VERIFICAÇÃO SE É VALIDO OU NÃO
    if int(CPF[9]) == digitoum and int(CPF[10]) == digitodois:
        print('CPF CERTO')
        validacao = 'VÁLIDO'
        validos = validos + 1
    else:
        print('CPF ERRADO')
        validacao = 'INVÁLIDO'
        invalidos = invalidos + 1
    # PASSA PRA UM DICIONÁRIO O CPF COMO INTEIRO E A VALIDAÇÃO
    dicionario = {
        'CPF': [int(CPF)],
        'VALIDACAO': validacao
    }
    lista.append(dicionario)
    # VERIFICA SE O USUÁRIO QUER CONTINUAR OU NÃO
    resposta = input("Deseja continuar? (s/n): ")
    print("--" * 10)
    while resposta == '':
        resposta = input("DIGITE SUA RESPOSTA CORRETAMENTE: ")
    while resposta != 's' and resposta != 'n':
        resposta = input("DIGITE APENAS s/n: ")
        print("--" * 10)
    if resposta == 'n':
        break

print("--" * 10)
porcvalidos = validos * 100 / qtdd
print("--" * 10)
porcinvalidos = invalidos * 100 / qtdd
print(f"CPF'S TESTADOS: {qtdd}")
print("--" * 10)
print(f"CPF'S VÁLDIOS: {validos}")
print("--" * 10)
print(f"CPF'S INVÁLIDOS: {invalidos}")
print("--" * 10)
print(f"PORCENTAGEM DE CPF'S VALIDOS: {porcvalidos}, INVALIDOS: {porcinvalidos}")
print("--" * 10)
print(lista)