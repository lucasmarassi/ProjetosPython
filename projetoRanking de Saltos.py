resposta = input('Você deseja iniciar o programa?')
while resposta != 's' and resposta != 'n':
    resposta = input('DIGITE APENAS "s" OU "n"')
while resposta == 'n':
    print('??????? não quer começar?')
    resposta = input('Você deseja iniciar o programa?')
media_aux = 1
while resposta == 's':
    competidor = input('Digite o nome do competidor: ')
    while competidor.isnumeric == True:
        competidor = input('DIGITE APENAS LETRAS')
    salto1 = float(input('Digite o primeiro salto: '))
    menor_salto = salto1
    maior_salto = salto1
    salto2 = float(input('Digite o segundo salto: '))
    salto3 = float(input('Digite o terceiro salto: '))
    salto4 = float(input('Digite o quarto salto: '))
    salto5 = float(input('Digite o quinto salto: '))

    if salto2 > maior_salto:
        maior_salto = salto2
    elif salto2 < menor_salto:
        menor_salto = salto2

    if salto3 > maior_salto:
        maior_salto = salto3
    elif salto3 < menor_salto:
        menor_salto = salto3

    if salto4 > maior_salto:
        maior_salto = salto4
    elif salto4 < menor_salto:
        menor_salto = salto4

    if salto5 > maior_salto:
        maior_salto = salto5
    elif salto5 < menor_salto:
        menor_salto = salto5
    vencedor_aux = competidor
    media = (salto1 + salto2 + salto3 + salto4 + salto5 - menor_salto - maior_salto) / 3
    print(f'Atleta: {competidor}')
    print('-------------------------------------')
    print(f'Primeiro salto: {salto1}')
    print(f'Segundo salto: {salto2}')
    print(f'Terceirosalto: {salto3}')
    print(f'Quarto salto: {salto4}')
    print(f'Quinto salto : {salto5}\n\n')
    print('-------------------------------------')
    print(f'Maior salto: {maior_salto}')
    print(f'Menor salto : {menor_salto}')
    print(f'Media dos demais saltos: {media}')
    winner_aux = competidor
    winneraux = str(winner_aux)
    if media >= media_aux:
        winner = competidor
        winner = str(winner)
        media_vencedora = media
        media_aux = media

    print('-------------------------------------')
    print(f'Vencedor ate o momento: {winner}')
    print('--------------------------')
    resposta = input('Deseja continuar? (s/n): ')
    print('-------------------------------------')