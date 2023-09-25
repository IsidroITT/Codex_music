import ply.lex as lex

# resultado del analisis
resultado_lexema = []

reservada = (
    # Palabras Reservadas
#     'INCLUDE',
#     'USING',
#     'NAMESPACE',
#     'STD',
#     'COUT',
#     'CIN',
#    'GET',
#    'CADENA',
#   'RETURN',
#    'VOID',
#     'INT',
#     'ENDL',
    'inicio','INICIO',
    'fin','FIN',
    'tempo','TEMPO',
    'compas','COMPAS',
    'clave','CLAVE',
    'rep','REP',
    'leds','LEDS',
    'pianoserv','PIANOSERV', 
)
tokens = reservada + (
#     'IDENTIFICADOR',
#     'ENTERO',
#     'ASIGNAR',

#     'SUMA',
#     'RESTA',
#     'MULT',
#     'DIV',
#     'POTENCIA',
#     'MODULO',

#    'MINUSMINUS',
#    'PLUSPLUS',

#     #Condiones
#    'SI',
#     'SINO',
#     #Ciclos
#    'MIENTRAS',
#    'PARA',
#     #logica
#     'AND',
#     'OR',
#     'NOT',
#     'MENORQUE',
#     'MENORIGUAL',
#     'MAYORQUE',
#     'MAYORIGUAL',
#     'IGUAL',
#     'DISTINTO',
#     # Symbolos
#     'NUMERAL',

#     'PARIZQ',
#     'PARDER',
#     'CORIZQ',
#     'CORDER',
#     'LLAIZQ',
#     'LLADER',
    
#     # Otros
#     'PUNTOCOMA',
#     'COMA',
#     'COMDOB',
#     'MAYORDER', #>>
#     'MAYORIZQ', #<<
     'DIGITO',
     'NOTA',
     'PUNTILLO',
     'SOTENIDO',
     'BEMOL',
     'CLAVE_COMPAS',
     'INICIO_PARTITURA',
     'FINAL_PARTITURA',
     'REDONDA',
     'BLANCA',
     'NEGRA',
     'CORCHEA',
     'SEMICORCHEA',
     'FUSA',
     'SEMIFUSA',
     'SILENCIO_REDONDA',
     'SILENCIO_BLANCA',
     'SILENCIO_NEGRA',
     'SILENCIO_CORCHEA',
     'SILENCIO_SEMICORCHEA',
     'SILENCIO_FUSA',
     'SILENCIO_SEMIFUSA',
     'DIVISOR_TEMPO',
     'IDENTIFICADOR',
     'SEPARACION_NOTA',
     'PARENTESIS_ABIERTO',
     'PARENTESIS_CERRADO',
     'CORCHETE_ABIERTO',
     'CORCHETE_CERRADO',
     'LLAVE_ABIERTA',
     'LLAVE_CERRADA',
     'SEPARACION_COMPAS',
     'NUEVA_LINEA',
     'COMENTARIO',
     'ASIGNACION',
     'POTENCIA_CLAVE',
)

# Reglas de Expresiones Regualres para token de Contexto simple
t_ignore = '\t'
#t_NOTA = r'[A-G]|[A-G][1-9]'
t_PUNTILLO = r'\*'
t_SOTENIDO = r'\#'
t_ASIGNACION = r'='
t_SEPARACION_NOTA = r'\.'
t_BEMOL = r'b'
t_CLAVE_COMPAS = r'[A-G]\^[1-4]'
t_INICIO_PARTITURA = r'\\inicio|\\INICIO'
t_FINAL_PARTITURA = r'\\fin|\\FIN'
# t_REDONDA = r'r'
# t_BLANCA = r'b'
# t_NEGRA = r'n'
# t_CORCHEA = r'c'
# t_SEMICORCHEA = r's'
# t_FUSA = r'f'
# t_SEMIFUSA = r'sf'
# t_SILENCIO_REDONDA = r'sir'
# t_SILENCIO_BLANCA = r'sib'
# t_SILENCIO_NEGRA = r'sin'
# t_SILENCIO_CORCHEA = r'sic'
# t_SILENCIO_SEMICORCHEA = r'sis'
# t_SILENCIO_FUSA = r'sif'
# t_SILENCIO_SEMIFUSA = r'sisf'
t_DIVISOR_TEMPO = r'/'
t_PARENTESIS_ABIERTO = r'\('
t_PARENTESIS_CERRADO = r'\)'
t_CORCHETE_ABIERTO = r'\['
t_CORCHETE_CERRADO = r'\]'
t_LLAVE_ABIERTA = r'\{'
t_LLAVE_CERRADA = r'\}'
t_SEPARACION_COMPAS = r','
t_POTENCIA_CLAVE = r'\^'
# t_SUMA = r'\+'
# t_RESTA = r'-'
# t_MINUSMINUS = r'\-\-'
# # t_PUNTO = r'\.'
# t_MULT = r'\*'
# t_DIV = r'/'
# t_MODULO = r'\%'
# t_POTENCIA = r'(\*{2} | \^)'

# t_ASIGNAR = r'='
# # Expresiones Logicas
# t_AND = r'\&\&'
# t_OR = r'\|{2}'
# t_NOT = r'\!'
# t_MENORQUE = r'<'
# t_MAYORQUE = r'>'
# t_PUNTOCOMA = ';'
# t_COMA = r','
# t_PARIZQ = r'\('
# t_PARDER = r'\)'
# t_CORIZQ = r'\['
# t_CORDER = r'\]'
# t_LLAIZQ = r'{'
# t_LLADER = r'}'
# t_COMDOB = r'\"'


# def t_INCLUDE(t):
#     r'include'
#     return t

# def t_USING(t):
#     r'using'
#     return t

# def t_NAMESPACE(t):
#     r'namespace'
#     return t

# def t_STD(t):
#     r'std'
#     return t

# def t_COUT(t):
#     r'cout'
#     return t

# def t_CIN(t):
#     r'cin'
#     return t

# def t_GET(t):
#     r'get'
#     return t

# def t_ENDL(t):
#     r'endl'
#     return t

# def t_SINO(t):
#     r'else'
#     return t

# def t_SI(t):
#     r'if'
#     return t

# def t_RETURN(t):
#    r'return'
#    return t

# def t_VOID(t):
#    r'void'
#    return t

# def t_MIENTRAS(t):
#     r'while'
#     return t

# def t_PARA(t):
#     r'for'
#     return t

# def t_ENTERO(t):
#     r'\d+'
#     t.value = int(t.value)
#     return t


# def t_CADENA(t):
#    r'\"?(\w+ \ *\w*\d* \ *)\"?'
#    return t

# def t_NUMERAL(t):
#     r'\#'
#     return t

# def t_PLUSPLUS(t):
#     r'\+\+'
#     return t

# def t_MENORIGUAL(t):
#     r'<='
#     return t

# def t_MAYORIGUAL(t):
#     r'>='
#     return t

# def t_IGUAL(t):
#     r'=='
#     return t

# def t_MAYORDER(t):
#     r'<<'
#     return t

# def t_MAYORIZQ(t):
#     r'>>'
#     return t

# def t_DISTINTO(t):
#     r'!='
#     return t

def t_INICIO(t):
    r'inicio|INICIO'
    return t

def t_FIN(t):
    r'fin|FIN'
    return t

def t_TEMPO(t):
    r'tempo|TEMPO'
    return t

def t_COMPAS(t):
    r'compas'
    return t

def t_CLAVE(t):
    r'clave|CLAVE'
    return t

def t_REP(t):
    r'rep|REP'
    return t

def t_LEDS(t):
    r'leds|LEDS'
    return t

def t_PIANOSERV(t):
    r'pianoserv|PIANOSERV'
    return t

def t_NOTA(t):
    r'[A-G][1-9]?'
    return t

def t_REDONDA(t):
    r'r'
    return t

def t_BLANCA(t):
    r'b'
    return t

def t_NEGRA(t):
    r'n'
    return t

def t_CORCHEA(t):
    r'c'
    return t

def t_SEMICORCHEA(t):
    r's'
    return t

def t_FUSA(t):
    r'f'
    return t

def t_SEMIFUSA(t):
    r'sf'
    return t

def t_SILENCIO_REDONDA(t):
    r'sir'
    return t

def t_SILENCIO_BLANCA(t):
    r'sib'
    return t

def t_SILENCIO_NEGRA(t):
    r'sin'
    return t

def t_SILENCIO_CORCHEA(t):
    r'sic'
    return t

def t_SILENCIO_SEMICORCHEA(t):
    r'sis'
    return t

def t_SILENCIO_FUSA(t):
    r'sif'
    return t

def t_SILENCIO_SEMIFUSA(t):
    r'sisf'
    return t

def t_DIGITO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")

def t_comments_ONELine(t):
     r'\/\/(.)*\n'
     t.lexer.lineno += 1
     print("Comentario de una linea")
#t_ignore =' \t'

def t_error( t):
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                      str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno),str(tok.type) ,str(tok.value), str(tok.lexpos) )
        resultado_lexema.append(estado)
    return resultado_lexema

 # instanciamos el analizador lexico
analizador = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("ingrese: ")
        prueba(data)
        print(resultado_lexema)