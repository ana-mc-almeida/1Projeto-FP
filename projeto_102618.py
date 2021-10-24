'''
https://web.fe.up.pt/~ee96100/projecto/Tabela%20ascii.htm
'''
# 1 - CORREÇÃO DA DOCUMENTAÇÃO


def corrigir_palavra(palavra):
    """
    corrigir palavra: cad. carateres -> cad. carateres

    Recebe uma palavra, potencialmente modificada por um surto de letras.
    Devolve a string correspondente ah aplicação das reduções:
        Remover o par minuscula/maiuscula da mesma letra se estas estiverem juntas
        Não importa a ordem (minuscula/maiuscula ou maiuscula/minuscula)


    Ponto 1.2.1
    """
    i = 0
    while i < len(palavra)-1:  # como vai comparar o indíce i com o índice i+1, o i não chega ao último índice da palavra OU quando só há uma letra nunca vai ser certo
        if (ord(palavra[i]) == ord(palavra[i+1])+ 32) or (ord(palavra[i]) == ord(palavra[i+1]) - 32):  # comparar as letras, usando a tabela ascii
            palavra = palavra[0: i] + palavra[i + 2 : len(palavra)]
            #print(palavra)
            if i != 0:
                i-=1
        else:
            i +=1
    return palavra


def eh_anagrama(palavra, anagrama):
    """
    eh anagrama: (cad. carateres, cad. carateres) -> booleano

    Recebe duas palavras e retorna True or False dependendo se sao anagramas
    É considerado anagrama: as palavras sao constituidas pelas mesmas letras, ignorando diferenças
    entre maiusculas e minusculas e a ordem entre carateres.

    Ponto 1.2.2
    """
    if palavra == anagrama:
        return False
    return sorted(palavra.upper()) == sorted(anagrama.upper())


def validar_corrigir_doc(texto):
    for i in range(len(texto)):
        char_atual = texto[i]
        if char_atual == " " == texto[i+1]: #validar se há dois espaços seguidos
            return False
        elif not (65 <= ord(char_atual) <= 90 or 97 <= ord(char_atual) <= 122 or char_atual == " "): #validar se apenas existem letras e espaços no texto
            return False
    return True


def corrigir_doc(texto):
    """
    corrigir doc: cad. carateres -> cad. carateres


    Recebe o texto com os erros
        Corrige as palavras
        Vê se sao anagramas e soh deixa a primeira ocorrencia de cada
        Verifica se o argumento é valido
            As palavras só podem estar separadas por 1 espaço
            Tem 1 ou mais palavras
            Cada palavra eh formada por pelo menos uma letra
            Cada palavra soh tem letras
            Se nao for, gera um ValueError ("corrigir doc: argumento invalido")

    Ponto 1.2.3
    """
    if not validar_corrigir_doc(texto):
        raise ValueError ("corrigir doc: argumento invalido")

    texto_filtrado = ""
    for palavra in texto.split(" "):
        texto_filtrado += corrigir_palavra(palavra) + " "

    i = 0
    while i < len(texto_filtrado.split(" ")):
        palavras = texto_filtrado.split(" ")
        for j in range(i+1, len(palavras)):
            if eh_anagrama(palavras[i], palavras[j]):
                texto_filtrado = texto_filtrado.replace(palavras[j] + " ", "")
        i += 1

    return texto_filtrado


# 2 - DESCOBERTA DO PIN


def obter_posicao(movimento, digito):
    """
    obter posicao: (cad. carateres, inteiro) -> inteiro

    Ponto 2.2.1"""
    if movimento == "B" and digito < 7: # não entra se digito for 7, 8 ou 9
        digito += 3
    if movimento == "C" and digito > 3: # não entra se digito for 1, 2 ou 3
        digito -= 3
    if movimento == "D" and digito % 3 != 0: # não entra se digito for 7, 8 ou 9
        digito += 1
    if movimento == "E" and digito % 3 != 1: # não entra se digito for 7, 8 ou 9
        digito -= 1
    return digito


def obter_digito(movimentos, digito):
    """
    obter digito: (cad. carateres, inteiro) -> inteiro

    Ponto 2.2.2
    """
    for movimento in movimentos:
        digito = obter_posicao(movimento, digito)
    return digito

def valida_obter_pin(sequencias):
    if not (isinstance(sequencias, tuple) and 4 <= len(sequencias) <= 10):
        return False
    else:
        for sequencia in sequencias:
            for letra in sequencia:
                if letra not in ("B", "C", "E", "D"):
                    return False
    return True


def obter_pin(sequencias):
    """
    obter pin: tuplo -> tuplo

    TEM DE RECEBER UM TUPLO E DEVOLVER OUTRO

    Verificar a validade:
        o tuplo tem de ter entre 4 a 10 "sequencias"
        cada sequencia tem de ter um ou mais carateres `C', `B', `E' ou `D')
        Se nao, gera ValueError ("obter pin: argumento invalido")

    Ponto 2.2.3
    """
    if not valida_obter_pin(sequencias):
        raise ValueError ("obter pin: argumento invalido")

    pin = ()
    for sequencia in sequencias:
        pin += (obter_digito(sequencia, 5),)
    return pin




# 3 - VERIFICAÇÃO DE DADOS

def eh_cifra(cifra):
    '''
    eh_cifra: cad. carateres -> booleano

    Retorna True caso o argumento recebido seja uma cifra.
    Uma cadeira de caracteres eh uma cifra se contiver uma ou mais palavras (só letras minusculas), separadas por traços
    '''
    comprimento = len(cifra)
    if type(cifra) != str or comprimento < 1:  
        return False
    for i in range(comprimento):                                # verifica se o argumento apenas palavras constituidas
        if not 97 <= ord(cifra[i]) <= 122 and cifra[i] != "-":  # por letras minusculas, separedas por -
            return False
    return True

def eh_checksum(checksum):
    '''
    eh_checksum: cad. carateres -> booleano

    Retorna True caso o argumento contenha uma sequência de controlo.
    Uma sequencia de controlo é composta por letras minusculas entre parentesis retos
    '''
    comprimento = len(checksum)
    if type(checksum) != str or comprimento != 7 or checksum[0]!="[" or checksum[6]!="]":
        return False
    for i in range(1, comprimento-1):
        if not 97 <= ord(checksum[i]) <= 122:
            return False
    return True

def eh_seq_seguranca(seq_seguranca):
    '''
    eh_checksum: tuplo -> booleano

    Retorna True caso o argumento contenha uma sequência de seguranca.
    Uma sequencia de seguranca eh um tuplo com dois ou mais numeros inteiros positivos
    '''
    if type(seq_seguranca) != tuple or len(seq_seguranca) < 2:
        return False
    for num in seq_seguranca:
        if type(num) != int or num < 1:
            return False
    return True

def eh_entrada(entrada):
    """
    eh entrada: universal -> booleano
    Ponto 3.2.1 e 3.2.1
    """
    if type(entrada) == tuple and eh_cifra(entrada[0]) and eh_checksum(entrada[1]) and eh_seq_seguranca(entrada[2]):
        return True
    return False

def contar_letras(texto):
    '''
    contar_letras: cad. carateres -> dicionario
    '''
    letra_contagem = {}
    for letra in texto:
        if letra not in letra_contagem.keys():
            if 97 <= ord(letra) <= 122:
                letra_contagem[letra] = texto.count(letra)
    # print(dic)
    # print(sorted(dic, key=dic.get, reverse=True))
    return letra_contagem

def validar_cifra(cifra, checksum):
    """
    validar cifra: (cad. carateres, cad. carateres) -> booleano

    Ponto 3.2.2
    """
    cifra = sorted(cifra)       # ordenar os chars da cifra para ficarem por ordem alfabética no dicionario
    contagem_letras = contar_letras(cifra)
    letras_ordenadas = sorted(contagem_letras, key=contagem_letras.get, reverse=True) #lista com as letras da cifra ordenadas por ordem decrescente do numero de vezes que aparecem

    for i in range(1, len(checksum)-1):
        if letras_ordenadas[i-1] != checksum[i]:
            return False
    return True

def filtrar_bdb(entradas):
    """Ponto 3.2.3"""
    pass


# 4 - DESENCRIPTAÇÃO DE DADOS
"""
Exemplo: q = 133; (133+325)/122 = 3.5... quase 4; 4 + 1 = 5; e é a 5ª letra do abcedário
"""


def obter_num_seguranca(tuplo):
    """
    Mudar nome da variavel
    Ponto 4.2.2
    """
    pass


def decifrar_texto(cifra, numSeguranca):
    """Ponto 4.2.3"""
    pass


def decifrar_bdb(entradas):
    """
    ValueError ("decifrar bdb: argumento invalido")
    Ponto 4.2.4
    """
    pass


# 5 - DEPURACAO DE SENHAS


def eh_utilizador(utilizador):
    """Ponto 5.2.1"""
    pass


def eh_senha_valida(senha, regra):
    """Ponto 5.2.2"""
    pass


def filtrar_senhas(entradas):
    """
    ValueError ("filtrar senhas: argumento invalido")
    Ponto 5.2.3
    """
    pass


# PUBLIC TESTS

def public_tests():

    # print(corrigir_palavra('abBAx'))
    # x

    # print(corrigir_palavra('cCdatabasacCADde'))
    # database

    #print(eh_anagrama('caso', 'SaCo'))
    # True

    #print(eh_anagrama('caso', 'casos'))
    # False

    #print(corrigir_doc('???'))
    # corrigir_doc: argumento invalido

    doc = 'BuAaXOoxiIKoOkggyrFfhHXxR duJjUTtaCcmMtaAGga eEMmtxXOjUuJQqQHhqoada JlLjbaoOsuUeYy cChgGvValLCwMmWBbclLsNn LyYlMmwmMrRrongTtoOkyYcCK daRfFKkLlhHrtZKqQkkvVKza'
    # print(corrigir_doc(doc))
    # Buggy data base has wrong data

    #-----2-----#

    # print(obter_posicao('C', 5))
    # 2

    # print(obter_digito('CEE', 5))
    # 1

    #print(obter_pin(()))
    # obter_pin: argumento invalido

    t = ('CEE', 'DDBBB', 'ECDBE', 'CCCCB')
    # print(obter_pin(t))
    # (1, 9, 8, 5)



    #-----3-----#

    # print(eh_entrada(('a-b-c-d-e-f-g-h', '[abcd]', (950, 300))))
    # False

    # print(eh_entrada(('a-b-c-d-e-f-g-h-2', '[abcde]', (950, 300))))
    # False

    # print(eh_entrada(('a-b-c-d-e-f-g-h', '[xxxxx]', (950, 300))))
    # True

    # print(validar_cifra('a-b-c-d-e-f-g-h', '[xxxxx]'))
    # False

    # print(validar_cifra('a-b-c-d-e-f-g-h', '[abcde]'))
    # True

    #print(filtrar_bdb([]))
    # filtrar_bdb: argumento invalido

    bdb = [('aaaaa-bbb-zx-yz-xy', '[abxyz]', (950, 300)), ('a-b-c-d-e-f-g-h', '[abcde]', (124, 325, 7)), ('entrada-muito-errada', '[abcde]', (50, 404))]
    #print(filtrar_bdb(bdb))
    # [('entrada-muito-errada', '[abcde]', (50, 404))]


    #-----4-----


    # print(eh_entrada(('qgfo-qutdo-s-egoes-wzegsnfmjqz', '[abcde]', (2223,424,1316,99))))
    # True

    #print(obter_num_seguranca((2223,424,1316,99)))
    # 325


    #print(decifrar_texto('qgfo-qutdo-s-egoes-wzegsnfmjqz', 325))
    # esta cifra e quase inquebravel


    #print(decifrar_bdb([('nothing')]))
    # decifrar_bdb: argumento invalido

    bdb = [('qgfo-qutdo-s-egoes-wzegsnfmjqz', '[abcde]', (2223,424,1316,99)), ('lctlgukvzwy-ji-xxwmzgugkgw', '[abxyz]', (2388, 367, 5999)), ('nyccjoj-vfrex-ncalml', '[xxxxx]', (50, 404))]
    #print(decifrar_bdb(bdb))
    # ['esta cifra e quase inquebravel', 'fundamentos da programacao', 'entrada muito errada']

    #----5----

    #print(eh_utilizador({'name': 'john.doe', 'pass': 'aabcde', 'rule': {'vals': (1, 3), 'char': 'a'}}))
    # True

    #print(eh_utilizador({'name': 'john.doe', 'pass': 'aabcde', 'rule': {'vals': 1, 'char': 'a'}}))
    # False


    #print(eh_senha_valida('aabcde', {'vals': (1, 3), 'char': 'a'}))
    # True

    #print(eh_senha_valida('cdefgh', {'vals': (1, 3), 'char': 'b'}))
    # False


    #print(filtrar_senhas([]))
    # filtrar_senhas: argumento invalido

    bdb = [{'name': 'john.doe', 'pass': 'aabcde', 'rule': {'vals': (1, 3), 'char': 'a'}}, {'name': 'jane.doe', 'pass': 'cdefgh', 'rule': {'vals': (1, 3), 'char': 'b'}}, {'name': 'jack.doe', 'pass': 'cccccc', 'rule': {'vals': (2, 9), 'char': 'c'}}]
    #print(filtrar_senhas(bdb))
    # ['jack.doe', 'jane.doe']

    return 0
public_tests()