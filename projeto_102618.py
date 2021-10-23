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
        
#print(corrigir_palavra("cCdatabasacCADde"))
#print(corrigir_palavra("abBAx"))
#help(corrigir_palavra)


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

# print(eh_anagrama('caso', 'SaCo'))
# print(eh_anagrama('caso', 'casos'))
# print(eh_anagrama('caso', 'caso'))

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

# print(corrigir_doc('???'))
# doc = 'BuAaXOoxiIKoOkggyrFfhHXxR duJjUTtaCcmMtaAGga eEMmtxXOjUuJQqQHhqoada JlLjbaoOsuUeYy cChgGvValLCwMmWBbclLsNn LyYlMmwmMrRrongTtoOkyYcCK daRfFKkLlhHrtZKqQkkvVKza'
# print(corrigir_doc(doc))


# 2 - DESCOBERTA DO PIN


def obter_posicao(movimento, posicao_atual):
    """Ponto 2.2.1"""
    pass


def obter_digito(movimentos, posicao_inicial):
    """Ponto 2.2.2"""
    pass


def obter_pin(sequencias):
    """
    TEM DE RECEBER UM TUPLO E DEVOLVER OUTRO

    Verificar a validade:
        o tuplo tem de ter entre 4 a 10 "sequencias"
        cada sequencia tem de ter um ou mais carateres `C', `B', `E' ou `D')
        Se nao, gera ValueError ("obter pin: argumento invalido")

    Ponto 2.2.3
    """
    pass


# 3 - VERIFICAÇÃO DE DADOS


def eh_entrada(entrada):
    """Ponto 3.2.1 e 3.2.1"""
    pass


def validar_cifra(cifra, checksum):
    """Ponto 3.2.2"""
    pass


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
