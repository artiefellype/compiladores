import ply.lex as lex

# Define the token names
tokens = (
    'CLASS', 'EQUIVALENTTO', 'AND', 'SOME', 'MIN', 'XSD', 'INDIVIDUALS',
    'SUBCLASSOF', 'DISJOINTCLASSES', 'HASBASE', 'HASCALORICCONTENT', 'HASPHONE',
    'CUSTOMER', 'EMPLOYEE', 'PIZZA', 'CHEESYPIZZA', 'HIGHCALORIEPIZZA',
    'INTERESTINGPIZZA', 'LOWCALORIEPIZZA', 'NAMEDPIZZA', 'AMERICANAHOTPIZZA',
    'AMERICANAPIZZA', 'MARGHERITAPIZZA', 'SOHOPIZZA', 'SPICYPIZZA',
    'VEGETARIANPIZZA', 'PIZZABASE', 'PIZZATOPPING', 'SPICINESS',
    'IDENTIFIER', 'INTEGER', 'STRING', 'VALUE', 'LPAREN', 'RPAREN', 
    'LBRACKET', 'RBRACKET', 'LCURLY', 'RCURLY', 'COMMA', 'COLON', 'GT', 'EQ', 'LT'
)

# Define regular expressions for simple tokens
t_CLASS = r'Class'
t_EQUIVALENTTO = r'EquivalentTo'
t_AND = r'and'
t_SOME = r'some'
t_MIN = r'min'
t_XSD = r'xsd'
t_INDIVIDUALS = r'Individuals'
t_SUBCLASSOF = r'SubClassOf'
t_DISJOINTCLASSES = r'DisjointClasses'
t_HASBASE = r'hasBase'
t_HASCALORICCONTENT = r'hasCaloricContent'
t_HASPHONE = r'hasPhone'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_INTEGER = r'\d+'
t_STRING = r'"[^"]*"'
t_VALUE = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_COMMA = r','
t_COLON = r':'
t_GT = r'>'
t_EQ = r'='
t_LT = r'<'
t_ignore_COMMENT = r'\#.*'

# Ignored characters
t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

print("Analisando o arquivo owl2.txt...")
# Abra o arquivo e leia o conteúdo
with open('owl2.txt', 'r') as file:
    data = file.read()

# Dê ao lexer alguns dados de entrada
lexer.input(data)


print("Gerando o arquivo analisador_lexico_output.txt...")

# Abra o arquivo de saída
with open('analisador_lexico_output.txt', 'w') as output_file:
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # Não há mais entrada
        output_file.write(str(tok) + '\n')  # Escreva o token no arquivo de saída
        
print("Análise léxica concluída!")