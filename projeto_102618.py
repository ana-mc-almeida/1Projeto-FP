# 1 - CORREÇÃO DA DOCUMENTAÇÃO


def corrigir_palavra(palavra):
    """
    Recebe uma palavra, potencialmente modificada por um surto de letras.
    Devolve a string correspondente ah aplicação das reduções:
        Remover o par minuscula/maiuscula da mesma letra se estas estiverem juntas
        Não importa a ordem (minuscula/maiuscula ou maiuscula/minuscula)


    Ponto 1.2.1
    """
    pass


def eh_anagrama(palavra, anagrama):
    """
    Recebe duas palavras e retorna True or False dependendo se sao anagramas
    É considerado anagrama: as palavras sao constituidas pelas mesmas letras, ignorando diferenças
    entre maiusculas e minusculas e a ordem entre carateres.

    Ponto 1.2.2
    """
    pass


def corrigir_doc(texto):
    """
    Recebe o texto com os erros
        Corrige as palavras
        Vê se sao anagramas e soh deixa a primeira ocorrencia de cada
        Verifica se o argumento é valido
            As palavras só podem estar separadas por 1 espaço
            Tem 1 ou mais palavras
            Cada palavra eh formada por pelo menos uma letra
            Se nao for, gera um ValueError ("corrigir doc: argumento invalido")

    Ponto 1.2.3
    """
    pass


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
