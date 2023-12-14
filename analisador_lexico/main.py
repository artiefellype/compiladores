from ply import lex

tokens = (
    'CLASS',
    'INDIVIDUAL',
    'OBJECT_PROPERTY',
    'DATA_PROPERTY',
    'ANNOTATION_PROPERTY',
    'DATATYPE',
    'COMMENT',
    'OPEN_BRACE',
    'CLOSE_BRACE',
    'EQUALS',
    'COLON',
    'COMMA',
    'STRING',
)

t_CLASS = r'Class'
t_INDIVIDUAL = r'Individual'
t_OBJECT_PROPERTY = r'ObjectProperty'
t_DATA_PROPERTY = r'DataProperty'
t_ANNOTATION_PROPERTY = r'AnnotationProperty'
t_DATATYPE = r'Datatype'
t_COMMENT = r'Comment'
t_OPEN_BRACE = r'\('
t_CLOSE_BRACE = r'\)'
t_EQUALS = r'='
t_COLON = r':'
t_COMMA = r','
t_STRING = r'\".*?\"'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def analyze(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        lexer.input(data)
        for token in lexer:
            print(token)

# Use the function like this:
analyze('owl2.txt')
