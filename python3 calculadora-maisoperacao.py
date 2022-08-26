#py calculadora.py
#!/usr/bin/env python
# encoding: utf-8
from os import system
from os import sys 

class Calculadora:
    
            print('*** Calculadora em Python ***')
            print('1 - Soma | 2 - Subtração | 3 - Divisão | 4 - Multiplicação | 5 - Sair')
            operacao = input ('\nQual operação deseja realizar? ')


            if operacao == '1': 
                first_number = int(input('Digite o primeiro número: '))
                second_number = int(input('Digite o segundo número: '))
                resultado = first_number + second_number
                print ( 'O resultado da soma é '+ str(resultado))
                
            if operacao == '2': 
                first_number = int(input('Digite o primeiro número: '))
                second_number = int(input('Digite o segundo número: '))
                resultado = first_number - second_number
                print ( 'O resultado da subtração é '+ str(resultado))
                
   

            if operacao == 5:
                sys.exit()


if __name__ == '__main__':

    try:
        Calculadora()

    except Exception:
        print (Exception)