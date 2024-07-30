def partida():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato')
    escolha = int(input('Digite sua escolha: '))
    if escolha == 1:
        print('Você escolheu uma partida isolada!')
        print('**** Começa o Jogo ****')
        n = int(input('Digite o número de peças: '))
        m = int(input('Digite o número máximo de peças que podem ser retiradas: '))
        while n > 0:
            n = usuario_escolhe_jogada(n, m)
            if n == 0:
                print('Você ganhou!')
                return
            n = computador_escolhe_jogada(n, m)
            if n == 0:
                print('Computador ganhou!')
                return
    elif escolha == 2:
        campeonato()

def computador_escolhe_jogada(n, m):
    jogada = 1
    while jogada != m:
        if (n - jogada) % (m + 1) == 0:
            break
        else:
            jogada += 1
    if jogada == 0:
        jogada = 1
    print('Computador tirou', jogada, 'peças.')
    return n - jogada

def usuario_escolhe_jogada(n, m):
    jogada = int(input('Escolha quantas peças deseja retirar: '))
    while jogada > m or jogada < 1:
        print('Jogada inválida! Tente novamente.')
        jogada = int(input('Escolha quantas peças deseja retirar: '))
    return n - jogada

def campeonato():
    print('Você escolheu um campeonato!')
    for i in range(1, 4):
        print(f'**** Rodada {i} ****')
        n = int(input('Digite o número de peças: '))
        m = int(input('Digite o número máximo de peças que podem ser retiradas: '))
        while n > 0:
            if n % (m + 1) != 0:
                print('Computador começa!')
                while n > 0:
                    n = computador_escolhe_jogada(n, m)
                    if n == 0:
                        print('Computador ganhou!')
                        break
                    n = usuario_escolhe_jogada(n, m)
                    if n == 0:
                        print('Você ganhou!')
                        break
            else:
                print('Você começa!')
                while n > 0:
                    n = usuario_escolhe_jogada(n, m)
                    if n == 0:
                        print('Você ganhou!')
                        break
                    n = computador_escolhe_jogada(n, m)
                    if n == 0:
                        print('Computador ganhou!')
                        break

partida()
