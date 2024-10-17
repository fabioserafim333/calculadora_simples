while True:
  try:
      n1 = int(input('Insira o primeiro número: '))
      n2 = int(input('Insira o segundo número: '))
      operacao = input('Insira o sinal da operação desejada (+, -, *, /): ')

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
              print('Erro: Divisão por zero não é permitida.')
          else:
              resultado = round(n1 / n2, 2)
              print(f'{n1} / {n2} = {resultado}')
      else:
          print('Operação inválida. Use apenas +, -, * ou /.')

  except ValueError:
      print('Erro: Por favor, insira números válidos.')

  continuar = input('Deseja realizar outra operação? (s/n): ')
  if continuar.lower() != 's':
      print('Encerrando calculadora.')
      break
