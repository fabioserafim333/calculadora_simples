while True:
    try:
        # Solicitação dos dados necessários para o usuário.
        n1 = int(input('Insira o primeiro número: '))
        n2 = int(input('Insira o segundo número: '))
        operacao = input('Insira o sinal da operação desejada (+, -, *, /): ')

        # O código executará uma operação diferente para cada sinal digitado e mostrará um resultado personalizado para o usuário.
        if operacao == '+':
            resultado = n1 + n2
            print(f'{n1} + {n2} = {resultado}')
        elif operacao == '-':
            resultado = n1 - n2
            print(f'{n1} - {n2} = {resultado}')
        elif operacao == '*':
            resultado = n1 * n2
            print(f'{n1} * {n2} = {resultado}')
        elif operacao == '/':
            if n2 == 0: 
                print('Erro: Divisão por zero não é permitida.') # Caso o usuário tente dividir por zero.
            else:
                resultado = round(n1 / n2, 2) # O comando 'round' arredondará o resultado para 2 casas decimais.
                print(f'{n1} / {n2} = {resultado}')
        else:
            print('Operação inválida. Use apenas +, -, * ou /.') # Mensagem para operações não reconhecidas.
 
    except ValueError:
        print('Erro: Por favor, insira números válidos.') # Mensagem de erro para entradas inválidas.

    continuar = input('Deseja realizar outra operação? (s/n): ')
    if continuar.lower() != 's':
        print('Encerrando calculadora.')
        break # O loop termina caso o usuário escolha não realizar mais operações.
