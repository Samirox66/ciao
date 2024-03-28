from dsl_info import Nonterminal
from syntax.core import NodeType

def translate_ast_to_ciao(ast):
    code = ""
    stack_of_nodes = [ast]
    while stack_of_nodes:
        current_node = stack_of_nodes.pop()
        if not hasattr(current_node, "childs"):
            if hasattr(current_node, "token"):
                code += " " + current_node.token.str
            continue
        if current_node.nonterminalType != Nonterminal.EXPRESSION and current_node.nonterminalType != Nonterminal.TYPE:
            code += "\n"
        new_childs = []
        for child in current_node.childs:
            new_childs.append(child)

        new_childs.reverse()
        stack_of_nodes.extend(new_childs)
    with open(f"_debug/retranslate.ciao", 'w') as codeFile:
        codeFile.write(code)