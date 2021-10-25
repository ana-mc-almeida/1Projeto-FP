'''
https://web.fe.up.pt/~ee96100/projecto/Tabela%20ascii.htm
'''
# 1 - CORREÇÃO DA DOCUMENTAÇÃO


def corrigir_palavra(palavra):
    """
    corrigir palavra: string -> string

    Retorna uma string correspondente à aplicação de reduções na palavra inicial.
    Sempre que existirem duas letras iguais seguidas (uma minúscula e outra maiúscula), a palavra irá sofrer uma redução, pois estas letras serão removidas.
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
    eh anagrama: (string, string) -> bool

    Retorna True or False, dependendo se os argumentos dados são anagramas ou não.
    São consideradas anagramas duas palavras constituídas pelas mesmas letras, ignorando diferenças entre maiúsculas e minúsculas e a ordem entre carateres.
    """
    return sorted(palavra.upper()) == sorted(anagrama.upper())


def validar_corrigir_doc(texto):
    '''
    validar_corrigir_doc: string -> bool

    Retorna True ou False caso o argumento seja válido ou não.
    Para isso, o texto deve estar formado por uma ou mais palavras em que as palavras apenas podem estar separadas por um único espaço e tem de ser apenas por, pelo menos, uma letra.
    '''
    comprimento = len(texto)
    for i in range(comprimento):
        char_atual = texto[i]
        if comprimento < 1 or (comprimento == 1 and not (65 <= ord(char_atual) <= 90 or 97 <= ord(char_atual) <= 122)):
            return False
        if char_atual == " " == texto[i+1]: #validar se há dois espaços seguidos
            return False
        elif not (65 <= ord(char_atual) <= 90 or 97 <= ord(char_atual) <= 122 or char_atual == " "): #validar se apenas existem letras e espaços no texto
            return False
    return True


def corrigir_doc(texto):
    """
    corrigir doc: string -> string

    Retorna o texto recebido sem erros, isto é, as palavras são corrigidas e os anagramas retirados, ficando apenas a sua primeira ocorrência.
    """
    if not validar_corrigir_doc(texto):
        raise ValueError ("corrigir_doc: argumento invalido")

    texto_filtrado = ""
    for palavra in texto.split(" "):
        texto_filtrado += corrigir_palavra(palavra) + " "

    i = 0
    while i < len(texto_filtrado.split(" ")):
        palavras = texto_filtrado.split(" ")
        for j in range(i+1, len(palavras)):
            if eh_anagrama(palavras[i], palavras[j]) and palavras[i] != palavras [j]:
                texto_filtrado = texto_filtrado.replace(palavras[j] + " ", "")
        i += 1

    return texto_filtrado


# 2 - DESCOBERTA DO PIN


def obter_posicao(movimento, digito):
    """
    obter posicao: (string, inteiro) -> inteiro

    Retorna o dígito correspondente à nova posição, após o movimento recebido.
    """
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
    obter digito: (string, inteiro) -> inteiro

    Retorna o dígito a marcar após finalizar todos os movimentos recebidos.
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

    Retorna os dígitos que constituem o PIN codificado de acordo com movimentos recebidos.
    """
    if not valida_obter_pin(sequencias):
        raise ValueError ("obter_pin: argumento invalido")

    pin = ()
    digito = 5
    for sequencia in sequencias:
        digito = obter_digito(sequencia, digito)
        pin += (digito,)
    return pin




# 3 - VERIFICAÇÃO DE DADOS

def eh_cifra(cifra):
    '''
    eh_cifra: string -> booleano

    Retorna True caso o argumento recebido seja uma cifra.
    Uma cadeira de caracteres é uma cifra se contiver uma ou mais palavras (só letras minúsculas), separadas por traços.
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
    eh_checksum: string -> booleano

    Retorna True caso o argumento contenha uma sequência de controlo.
    Uma sequência de controlo é composta por letras minúsculas entre parêntesis retos.
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
    Uma sequência de segurança é um tuplo com dois ou mais númeors inteiros positivos.
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

    Retorna True caso o argumento seja uma entrada da BDB, isto é, se é um tuplo que contém uma cifra, uma sequência de controlo e uma sequência de segurança.
    """
    if type(entrada) == tuple and eh_cifra(entrada[0]) and eh_checksum(entrada[1]) and eh_seq_seguranca(entrada[2]):
        return True
    return False


def contar_letras(texto):
    '''
    contar_letras: string -> dict

    Retorna um dicionário em que cada chave corresponde a uma letra e o seu valor corresponde ao número de vezes que essa letra se encontra no argumento recebido.
    '''
    letra_contagem = {}
    for letra in texto:
        if letra not in letra_contagem.keys():
            if 97 <= ord(letra) <= 122:
                letra_contagem[letra] = texto.count(letra)
    return letra_contagem

def validar_cifra(cifra, checksum):
    """
    validar cifra: (string, string) -> booleano

    Retorna True caso a sequência de controlo seja coerente com a cifra.
    Para isso a sequência de controlo tem de ser formada pelas cinco letras mais comuns na cifra, por ordem inversa de ocorrências, com empates decididos por ordem alfabética.
    """
    cifra = sorted(cifra)       # ordenar os chars da cifra para ficarem por ordem alfabética em letras_ordenadas
    contagem_letras = contar_letras(cifra)
    letras_ordenadas = sorted(contagem_letras, key=contagem_letras.get, reverse=True) #lista com as letras da cifra ordenadas por ordem decrescente do numero de vezes que aparecem

    for i in range(1, len(checksum)-1):
        if letras_ordenadas[i-1] != checksum[i]:
            return False
    return True


def filtrar_bdb(entradas):
    """
    filtrar_bdb: lista -> lista

    Retorna uma lista com as entradas em o checksum não seja coerente com a cifra correspondente.
    """
    cifra_nao_corresponde = []
    if type(entradas) != list or len(entradas) < 1:
        raise ValueError ("filtrar_bdb: argumento invalido")
    for entrada in entradas:
        if eh_entrada(entrada):
            if not validar_cifra(entrada[0], entrada[1]):
                cifra_nao_corresponde.append(entrada)
        else:
            raise ValueError ("filtrar_bdb: argumento invalido")
    return cifra_nao_corresponde



# 4 - DESENCRIPTAÇÃO DE DADOS

def obter_num_seguranca(nums):
    """
    obter num seguranca: tuplo -> inteiro
    
    Retorna a menor diferença positiva entre qualquer par dos números recebidos.
    """
    comprimento = len(nums)
    for i in range(comprimento-1):
        for j in range(i+1, comprimento):
            diferenca = abs(nums[i]-nums[j])
            if (i == 0 and j == 1) or diferenca < num_seguranca: # (i == 0 and j == 1) faz com que a primeira diferença seja automaticamente o numero de seguranca, para começar
                num_seguranca = diferenca    
    return num_seguranca


def decifrar_texto(cifra, numSeguranca):
    """
    decifrar texto: (string, inteiro) -> string
    
    Retorna o texto decifrado conforme a cifra e o número de segurança.
    """
    texto_decifrado = ""
    numSeguranca = numSeguranca % 26 # para só percorrer o alfabeto uma vez 
    for i in range(len(cifra)):
        if cifra[i] == "-":
            texto_decifrado += " "
        else:
            nova_letra = ord(cifra[i]) + numSeguranca
            if i % 2 == 0:
                nova_letra += 1
            else: 
                nova_letra -= 1
            if nova_letra > 122:
                nova_letra -= 26    # voltar ao inicio do alfabeto
            texto_decifrado += chr(nova_letra)
    return texto_decifrado


def decifrar_bdb(entradas):
    """
    decifrar_bdb: lista -> lista

    Retorna uma lista com o texto das entradas recebidas, já decifradas.
    """
    entradas_decifradas = []
    if type(entradas) != list or len(entradas) < 1:
        raise ValueError ("decifrar_bdb: argumento invalido")
    for entrada in entradas:
        if eh_entrada(entrada):
            entradas_decifradas.append(decifrar_texto(entrada[0], obter_num_seguranca(entrada[2])))
        else:
            raise ValueError ("decifrar_bdb: argumento invalido")
    return entradas_decifradas


# 5 - DEPURACAO DE SENHAS

def valida_nome_ou_senha(utilizador, informacao):
    '''
    valida_nome_ou_senha: (dict, string) -> bool

    Retorna True caso a informação desejada cumpra aos requesitos (ter tamanho mínimo 1 e podem conter qualquer caráter).
    '''
    informacao = utilizador.get(informacao)
    if type(informacao) == str and len(informacao) > 0:
        return True
    return False


def valida_valor(rule):
    '''
    valida_valor: dict -> bool

    Retorna True caso o valor 'vals' da regra indivual seja um tuplo de dois inteiros positivos em que o primeiro tem de ser menor que o segundo.
    '''
    valor = rule.get("vals")
    if type(valor) == tuple and len(valor) == 2:
        return True
    elif type(tuple[0]) == type(tuple[1]) == int and tuple[0] <= tuple[1]:
        return True
    return False

def valida_char(rule):
    '''
    valida_char: dict -> bool

    Retorna True caso o valor 'char' da regra indivual corresponda a uma letra minúscula.
    '''
    char = rule.get("char")
    if type(char) == str and len(char) == 1 and 96 < ord(char) < 122:
        return True
    return False

def valida_regra_individual(utilizador):
    '''
    valida_regra_individual: dict -> bool

    Retorna True caso a regra individual seja válida.
    '''
    rule = utilizador.get("rule")
    if type(rule) == dict and valida_valor(rule) and valida_char(rule):
        return True
    return False

def eh_utilizador(utilizador):
    """
    eh utilizador: universal -> booleano

    Retorna True caso o argumento recebido contenha a informação de utilizador relevante da BDB, isto é, nome, senha e regra individual.
    """
    if type(utilizador) is dict and valida_nome_ou_senha(utilizador, "name") and valida_nome_ou_senha(utilizador, "pass") and valida_regra_individual(utilizador):
        return True
    return False


def valida_regras_gerais(senha):
    '''
    valida_regras_gerais: string -> bool

    Retorna True caso o argumento recebido corresponda regras gerais, sendo estas:
    - Conter pelo menos 3 vogais minúsculas;
    - Conter pelo menos 1 caracter que apareça duas vezes consecutivas
    '''
    count_vogais = seguidas = 0
    comprimento = len(senha)
    for i in range(comprimento):
        if senha[i] in ('a', 'e', 'i', 'o', 'u'):
            count_vogais += 1
        if i !=comprimento-1 and senha[i] == senha[i+1]:
            seguidas = 1

    if count_vogais >= 3 and seguidas:
        return True
    return False

def valida_regras_individuais(senha, regra):
    '''
    valida_regras_individuais: (string, dict) -> bool

    Retorna True caso a senha corresponda às regras individuais.
    '''
    valor = regra.get("vals")
    min = valor[0]
    max = valor[1]
    char = regra.get("char")
    count = 0

    for letra in senha:
        if letra == char:
            count += 1

    if min <= count <= max:
        return True
    return False

def eh_senha_valida(senha, regra_individual):
    """
    eh senha valida: (string, dicionario) -> booleano

    Retorna True se a senha cumpre tanto as regras gerais como as individuais.
    """
    if valida_regras_individuais(senha, regra_individual) and valida_regras_gerais(senha):
        return True
    return False


def filtrar_senhas(entradas):
    """
    filtrar senhas: lista -> lista

    Retorna, ordenado alfabeticamente, os nomes dos utilizadores com senhas erradas.
    """
    senhas_erradas = []
    if type(entradas) != list or len(entradas) < 1:
        raise ValueError ("filtrar_senhas: argumento invalido")
    for entrada in entradas:
        if eh_utilizador(entrada):
            if not eh_senha_valida(entrada["pass"], entrada["rule"]):
                senhas_erradas.append(entrada["name"])
        else:
            raise ValueError ("filtrar_senhas: argumento invalido")
    return sorted(senhas_erradas)



# PUBLIC TESTS

def public_tests():

    # print(corrigir_palavra('abBAx'))
    # x

    # print(corrigir_palavra('cCdatabasacCADde'))
    # database

    # print(eh_anagrama('caso', 'SaCo'))
    # True

    # print(eh_anagrama('caso', 'casos'))
    # False

    # print(corrigir_doc('???'))
    # corrigir_doc: argumento invalido

    doc = 'BuAaXOoxiIKoOkggyrFfhHXxR duJjUTtaCcmMtaAGga eEMmtxXOjUuJQqQHhqoada JlLjbaoOsuUeYy cChgGvValLCwMmWBbclLsNn LyYlMmwmMrRrongTtoOkyYcCK daRfFKkLlhHrtZKqQkkvVKza'
    # print(corrigir_doc(doc))
    # Buggy data base has wrong data

    #-----2-----#

    # print(obter_posicao('C', 5))
    # 2

    # print(obter_digito('CEE', 5))
    # 1

    # print(obter_pin(()))
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

    # print(filtrar_bdb([]))
    # filtrar_bdb: argumento invalido

    bdb = [('aaaaa-bbb-zx-yz-xy', '[abxyz]', (950, 300)), ('a-b-c-d-e-f-g-h', '[abcde]', (124, 325, 7)), ('entrada-muito-errada', '[abcde]', (50, 404))]
    # print(filtrar_bdb(bdb))
    # [('entrada-muito-errada', '[abcde]', (50, 404))]


    #-----4-----


    # print(eh_entrada(('qgfo-qutdo-s-egoes-wzegsnfmjqz', '[abcde]', (2223,424,1316,99))))
    # True

    # print(obter_num_seguranca((2223,424,1316,99)))
    # 325


    # print(decifrar_texto('qgfo-qutdo-s-egoes-wzegsnfmjqz', 325))
    # esta cifra e quase inquebravel


    # print(decifrar_bdb([('nothing')]))
    # decifrar_bdb: argumento invalido

    bdb = [('qgfo-qutdo-s-egoes-wzegsnfmjqz', '[abcde]', (2223,424,1316,99)), ('lctlgukvzwy-ji-xxwmzgugkgw', '[abxyz]', (2388, 367, 5999)), ('nyccjoj-vfrex-ncalml', '[xxxxx]', (50, 404))]
    # print(decifrar_bdb(bdb))
    # ['esta cifra e quase inquebravel', 'fundamentos da programacao', 'entrada muito errada']

    #----5----

    # print(eh_utilizador({'name': 'john.doe', 'pass': 'aabcde', 'rule': {'vals': (1, 3), 'char': 'a'}}))
    # True

    # print(eh_utilizador({'name': 'john.doe', 'pass': 'aabcde', 'rule': {'vals': 1, 'char': 'a'}}))
    # False


    # print(eh_senha_valida('aabcde', {'vals': (1, 3), 'char': 'a'}))
    # True

    # print(eh_senha_valida('cdefgh', {'vals': (1, 3), 'char': 'b'}))
    # False


    # print(filtrar_senhas([]))
    # filtrar_senhas: argumento invalido

    # bdb = [{'name': 'john.doe', 'pass': 'aabcde', 'rule': {'vals': (1, 3), 'char': 'a'}}, {'name': 'jane.doe', 'pass': 'cdefgh', 'rule': {'vals': (1, 3), 'char': 'b'}}, {'name': 'jack.doe', 'pass': 'cccccc', 'rule': {'vals': (2, 9), 'char': 'c'}}]
    # print(filtrar_senhas(bdb))
    # ['jack.doe', 'jane.doe']

    
    # bdb2 = [{'name': 'bbb', 'pass': 'aabcde', 'rule': {'vals': (1, 3), 'char': 'a'}}, {'name': 'gagagagahj', 'pass': 'cdefgh', 'rule': {'vals': (1, 3), 'char': 'b'}}, {'name': 'fafafaf', 'pass': 'cccccc', 'rule': {'vals': (2, 9), 'char': 'c'}}]
    # print(filtrar_senhas(bdb2))

    return 0
public_tests()