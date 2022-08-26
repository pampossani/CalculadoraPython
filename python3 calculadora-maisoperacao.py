#py calculadora.py
#!/usr/bin/env python
# encoding: utf-8
import os
from os import system
from os import sys
while True:

        class Calculadora:
    
            print('*** Calculadora em Python ***')
            print('1 - Soma | 2 - Subtração | 3 - Divisão | 4 - Multiplicação | 5 - Sair')
            operacao = input ('\nQual operação deseja realizar? ')


            if operacao == '1': 
                first_number = int(input('Digite o primeiro número: '))
                second_number = int(input('Digite o segundo número: '))
                resultado = first_number + second_number
                print ( 'O resultado da soma é '+ str(resultado))
                
            elif operacao == '2': 
                first_number = int(input('Digite o primeiro número: '))
                second_number = int(input('Digite o segundo número: '))
                resultado = first_number - second_number
                print ( 'O resultado da subtração é '+ str(resultado))

                
            elif operacao == '3': 
                first_number = float(input('Digite o primeiro número: '))
                second_number = float(input('Digite o segundo número: '))
                resultado = first_number / second_number
                print ( 'O resultado da divisão é '+ str(resultado))
              
              
            elif operacao == '4': 
                first_number = float(input('Digite o primeiro número: '))
                second_number = float(input('Digite o segundo número: '))
                resultado = first_number * second_number
                print ( 'O resultado da multiplicação é '+ str(resultado))
                os.system('clear')
  

            elif operacao == '5':
                sys.exit()

            else :
                print ('Operação inválida!')   
                
        input('Pressione Enter para voltar ao menu!')
        os.system('cls')

if __name__ == '__main__':

    try:
        Calculadora()

    except Exception:
        print (Exception)