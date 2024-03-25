from enum import Enum
# KATE:: нужно изменить в соответсвии с нашей грамматикой

# не трогать
class Terminal(Enum):
    number = "number"
    name = "name"
    string = "string"
    code = "code"
    char_key = "char_key"


tokenRegularExpressions = [
    (Terminal.number, r"[0-9]+(.[0-9]*)?"),
    (Terminal.name, r"[\w^\d][\w]*"),
    (Terminal.string, r'"(\\.|[^\\"]+)"'),
    (Terminal.code, r"\{[^\}]*\}"),
    (Terminal.char_key, r"/|\(|\)|,|;|\.|:|=|\->|\[|\]|\|"),
]


keys = [
    ("VAR", Terminal.name),
    ("EFFECT", Terminal.name),
    ("EVENT", Terminal.name),
    ("STATE", Terminal.name),
    ("else", Terminal.name),
    ("true", Terminal.name),
    ("false", Terminal.name),
    ("=", Terminal.char_key),
    ("->", Terminal.char_key),
    ("/", Terminal.char_key),
    ("(", Terminal.char_key),
    (")", Terminal.char_key),
    (",", Terminal.char_key),
    (".", Terminal.char_key),
    (":", Terminal.char_key),
    (";", Terminal.char_key),
    ("[", Terminal.char_key),
    ("]", Terminal.char_key),
    ("|", Terminal.char_key),
    ("provided", Terminal.name),
    ("in", Terminal.name),
    ("out", Terminal.name),
    ("var", Terminal.name),
    ("const", Terminal.name),
    ("integer", Terminal.name),
    ("string", Terminal.name),
    ("bool", Terminal.name),
    ("REQUIRED_CONDITION", Terminal.name),
    ("PROVIDED_CONDITION", Terminal.name),
]


class Nonterminal(Enum):
    CIAO = "CIAO"
    AUTOMATA_OBJECT_1 = "AUTOMATA_OBJECT_1"
    VAR_BLOCK = "VAR_BLOCK"
    EFFECT_BLOCK = "EFFECT_BLOCK"
    EVENT_BLOCK = "EVENT_BLOCK"
    FUNCTION = "FUNCTION"
    STATE_BLOCK = "STATE_BLOCK"
    TRANSITION_DESCRIPTION = "TRANSITION_DESCRIPTION"
    REQUIRED_CONDITION_BLOCK = "REQUIRED_CONDITION_BLOCK"
    PROVIDED_CONDITION_BLOCK = "PROVIDED_CONDITION_BLOCK"



axiom = Nonterminal.CIAO
