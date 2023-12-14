import re

# Definindo as expressões regulares para os diferentes tokens
patterns = [
    (r'\b(?:SOME|ALL|VALUE|MIN|MAX|EXACTLY|THAT|NOT|AND|OR|Class|EquivalentTo|Individuals|SubClassOf|DisjointClasses)\b', 'KEYWORD'),
    (r'[A-Z][a-zA-Z_0-9]*', 'CLASS_IDENTIFIER'),  # Identificadores de classes
    (r'has[a-zA-Z_0-9]+', 'PROPERTY_IDENTIFIER'),  # Identificadores de propriedades
    (r'\b(?:[{},\[\]()><])\b', 'SPECIAL_SYMBOL'),  # Símbolos especiais
    (r'[A-Z][a-zA-Z_0-9]*[0-9]+', 'INDIVIDUAL'),  # Nomes de indivíduos
    (r'\b(?:owl:real|rdfs:domain|xsd:string)\b', 'DATA_TYPE'),  # Tipos de dados
    (r'\b(?:[0-9]+)\b', 'CARDINALITY'),  # Cardinalidades
]

# Função para analisar o código e gerar os tokens
def analyze_owl_code(code):
    tokens = []
    for pattern, token_type in patterns:
        regex = re.compile(pattern)
        matches = regex.finditer(code)
        for match in matches:
            tokens.append((token_type, match.group()))

    return tokens

# Exemplo de código OWL2 no formato Manchester Syntax
owl_code = """
Class: Customer

    EquivalentTo:
        Person
         and (purchasedPizza some Pizza)
         and (hasPhone some xsd:string)
    
    Individuals:
        Customer1,
        Customer10,
        Customer2,
        Customer3,
        Customer4,
        Customer5,
        Customer6,
        Customer7,
        Customer8,
        Customer9

Class: Employee

    SubClassOf:
        Person
         and (ssn min 1 xsd:string)
    
    Individuals:
        Chef1,
        Manager1,
        Waiter1,
        Waiter2

Class: Pizza

    SubClassOf:
        hasBase some PizzaBase,
        hasCaloricContent some xsd:integer
    
    DisjointClasses: 
        Pizza, PizzaBase, PizzaTopping
    
    Individuals: 
        CustomPizza1,
        CustomPizza2

Class: CheesyPizza

    EquivalentTo: 
        Pizza
         and (hasTopping some CheeseTopping)
    
    Individuals: 
        CheesyPizza1

Class: HighCaloriePizza

    EquivalentTo: 
        Pizza
         and (hasCaloricContent some xsd:integer[>= 400])

Class: InterestingPizza

    EquivalentTo: 
        Pizza
         and (hasTopping min 3 PizzaTopping)

Class: LowCaloriePizza

    EquivalentTo: 
        Pizza
         and (hasCaloricContent some xsd:integer[< 400])

Class: NamedPizza

    SubClassOf: 
        Pizza

Class: AmericanaHotPizza
   
    SubClassOf:
        NamedPizza,
        hasTopping some JalapenoPepperTopping,
        hasTopping some MozzarellaTopping,
        hasTopping some PepperoniTopping,
        hasTopping some TomatoTopping
    
    DisjointClasses:
        AmericanaHotPizza, AmericanaPizza, MargheritaPizza, SohoPizza
    
    Individuals: 
        AmericanaHotPizza1,
        AmericanaHotPizza2,
        AmericanaHotPizza3,
        ChicagoAmericanaHotPizza1

Class: AmericanaPizza
   
    SubClassOf: 
        NamedPizza,
        hasTopping some MozzarellaTopping,
        hasTopping some PepperoniTopping,
        hasTopping some TomatoTopping
    
    DisjointClasses: 
        AmericanaHotPizza, AmericanaPizza, MargheritaPizza, SohoPizza
    
    Individuals: 
        AmericanaPizza1,
        AmericanaPizza2

Class: MargheritaPizza
   
    SubClassOf:
        NamedPizza,
        hasTopping some MozzarellaTopping,
        hasTopping some TomatoTopping,
        hasTopping only 
            (MozzarellaTopping or TomatoTopping)
    
    DisjointClasses:
        AmericanaHotPizza, AmericanaPizza, MargheritaPizza, SohoPizza
    
    Individuals: 
        MargheritaPizza1,
        MargheritaPizza2

Class: SohoPizza
   
    SubClassOf: 
        NamedPizza,
        hasTopping some MozzarellaTopping,
        hasTopping some OliveTopping,
        hasTopping some ParmesanTopping,
        hasTopping some TomatoTopping,
        hasTopping only 
            (MozzarellaTopping or OliveTopping or ParmesanTopping or TomatoTopping)
    
    DisjointClasses:
        AmericanaHotPizza, AmericanaPizza, MargheritaPizza, SohoPizza
    
    Individuals:
        SohoPizza1,
        SohoPizza2

Class: SpicyPizza

    EquivalentTo:
        Pizza
         and (hasTopping some (hasSpiciness value Hot))

Class: VegetarianPizza

    EquivalentTo:
        Pizza
         and (hasTopping only 
            (CheeseTopping or VegetableTopping))

Class: PizzaBase

    DisjointClasses:
        Pizza, PizzaBase, PizzaTopping

Class: PizzaTopping

    DisjointClasses:
        Pizza, PizzaBase, PizzaTopping

Class: Spiciness

    EquivalentTo:
        {Hot , Medium , Mild}
    

"""

# Obtendo os tokens
tokens = analyze_owl_code(owl_code)

# Imprimindo os tokens
for token_type, value in tokens:
    print(f'{token_type}: {value}')
