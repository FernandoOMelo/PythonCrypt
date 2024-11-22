# Programa com objeto de criptografar um texto simples, a criptografia seguira a seguinte regra: 
# 1. O texto deve conter no máximo 100 caracteres. 
# 2. Toda letra utilizada no texto será substituida pelo seu numero no alfabeto menos 5. 
# 3. Os espaçamento entre as palavras serão conservados. 
# 4. O sistema deve ser capaz de criptografar e descriptografar o texto corretamente.
import random

Caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              '!', '@', '#', '$', '%', '¨', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '^', '~', ',', '<', '.', '>', ';', ':', '/', '?', '\\', '|',
              ' ', ' ',
              '´', '`', '¨', '^', '~',
              'ç', 'Ç',
              'á', 'à', 'â', 'ã', 'é', 'è', 'ê', 'í', 'ì', 'î', 'ó', 'ò', 'ô', 'õ', 'ú', 'ù', 'û',
              'Á', 'À', 'Â', 'Ã', 'É', 'È', 'Ê', 'Í', 'Ì', 'Î', 'Ó', 'Ò', 'Ô', 'Õ', 'Ú', 'Ù', 'Û']



def criptografaTexto():
    Texto = input("Digite um texto para ser criptografado: ")
    if len(Texto) > 100:
        print('Texto muito longo, limite 50 caracteres!')
        return
    arrayTexto = list(Texto)
    arrayCriptografado = []
    for i in range(len(arrayTexto)):
        letra = arrayTexto[i]
        indice = Caracteres.index(letra) - 5
        arrayCriptografado.append(str(indice) + ' ')
    arrayCriptografado = [str(i) for i in arrayCriptografado]
    print("".join(arrayCriptografado))

def descriptografaTexto():
    Texto = input("Digite um texto para ser descriptografado: ")
    arrayTexto = list(map(int, Texto.split()))
    arrayDescriptografado = []
    for i in range(len(arrayTexto)):
        indice = arrayTexto[i] + 5
        letra = Caracteres[indice]
        arrayDescriptografado.append(letra)
    print("".join(arrayDescriptografado))



print("Bem vindo ao Galileo Crypt, por favor digite a opção desejada: ")

metodoSelecionado = int(input("(1) Criptografar texto  - (2) Descriptografar Texto: "))

if metodoSelecionado == 1:
    criptografaTexto()
elif metodoSelecionado == 2:
    descriptografaTexto()







