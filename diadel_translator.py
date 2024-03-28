import re
from parse_states import *

def parse_state_transition(code):
    transitions = []
    state_id_map = {}
    next_state_id = 1

    func_pat = r'((?:\w+\([^()]*\))|(?:\w+))'
    state_pattern = re.compile(r'STATE:(.*?)\.', re.DOTALL)
    trans_pattern_simple = re.compile(r'(\w+) -> ((?:\w+\([^()]*\))|(?:\w+)) -> (\w+)')
    trans_pattern_base = re.compile(r'(\w+) -> ((?:\w+\([^()]*\))|(?:\w+)) / ((?:\w+\([^()]*\))|(?:\w+)) -> (\w+)')
    trans_pattern_cond = re.compile(rf'(\w+) -> ({func_pat}) \[?({func_pat})?\]? / ({func_pat}) -> (\w+)(?: \| (\w+) / ({func_pat}) -> (\w+))?')

    start_state = None
    event = None
    condition = None
    effect = None
    end_state = None
    action_else = None
    end_else_state = None

    state_blocks = state_pattern.findall(code)
    for state_block in state_blocks:
        lines = state_block.strip().split('\n')
        for line in lines:
            tmp_line = line.split()
            line = ' '.join(tmp_line)
            # Извлечение информации о переходе из каждой строки блока состояний
            match = trans_pattern_simple.search(line)
            if match:
                start_state = match.group(1).strip()
                event = match.group(2).strip()
                end_state = match.group(3).strip()

                condition = None
                effect = None
                action_else = None
                end_else_state =None


            match2 = trans_pattern_base.search(line)
            if match2:
                start_state = match2.group(1)
                event = match2.group(2)
                effect = match2.group(3)
                end_state = match2.group(4)

                condition = None
                action_else = None
                end_else_state = None

            match3 = trans_pattern_cond.search(line)
            if match3:
                start_state = match3.group(1)
                event = match3.group(2)
                condition = match3.group(4)
                effect = match3.group(6)
                end_state = match3.group(8)
                action_else = match3.group(10)
                end_else_state = match3.group(12) if match3.group(12) else None


            elif not match and not match2 and not match3:
                print("NO MATCH FOUND")
                return None

            if start_state not in state_id_map:
                state_id_map[start_state] = next_state_id
                next_state_id += 1

            if end_state not in state_id_map:
                state_id_map[end_state] = next_state_id
                next_state_id += 1
            if end_else_state is not None and end_else_state not in state_id_map:
                state_id_map[end_else_state] = next_state_id
                next_state_id += 1

            if match:
                transition = f"state{{id={state_id_map[start_state]}, text='{start_state}'}} arrow{{text='{event}'}} state{{id={state_id_map[end_state]}, text='{end_state}'}}"
                transitions.append(transition)
            elif match2:
                transition = f"state{{id={state_id_map[start_state]}, text='{start_state}'}} arrow{{text='{event} ; {effect}'}} state{{id={state_id_map[end_state]}, text='{end_state}'}}"
                transitions.append(transition)
            elif match3:
                transition1 = f"state{{id={state_id_map[start_state]}, text='{start_state}'}} arrow{{text='[{condition}] {event} {effect}'}} state{{id={state_id_map[end_state]}, text='{end_state}'}}"
                transition2 = f"state{{id={state_id_map[start_state]}, text='{start_state}'}} arrow{{text='else / {action_else} '}} state{{id={state_id_map[end_else_state]}, text='{end_else_state}'}}"
                transitions.append(transition1)
                transitions.append(transition2)
    return transitions, state_id_map

def parse_blocks(code):
    var_block_pattern = re.compile(r'VAR:(.*?)\.', re.DOTALL)
    event_block_pattern = re.compile(r'EVENT:(.*?)\.', re.DOTALL)
    effect_block_pattern = re.compile(r'EFFECT:(.*?)\.', re.DOTALL)
    reqired_cond_block_pattern = re.compile(r'REQUIRED_CONDITION:(.*?)\.', re.DOTALL)
    provided_cond_block_pattern = re.compile(r'PROVIDED_CONDITION:(.*?)\.', re.DOTALL)
    state_block_pattern = re.compile(r'STATE:(.*?)\.', re.DOTALL)

    var_code = var_block_pattern.findall(code)
    for var in var_code:
        print(var)
    event_code = event_block_pattern.findall(code)
    effect_code = effect_block_pattern.findall(code)
    reqired_cond_code = reqired_cond_block_pattern.findall(code)
    provided_cond_code = provided_cond_block_pattern.findall(code)
    state_block_code = state_block_pattern.findall(code)
    for state in state_block_code:
        print(state)


    return var_code, event_code, effect_code, reqired_cond_code, provided_cond_code, state_block_code

def include_states(automata_name, state_map):
    lines = []
    for _text, _id in state_map.items():
        line =f"automata{{id=1, text='{automata_name}'}} include{{}} state{{id={_id}, text='{_text}'}}\n"
        lines.append(line)
    return lines

def include_vars(automata_name, vars):
    var_lines = vars[0].split("\n")
    vars_included = []
    for var in var_lines :
        if var != "":
            vars_included.append(f"automata{{id=1, text='{automata_name}'}} include{{}} variables{{ text='{var}'}}\n")
    return vars_included



ciao_file = "ciao.txt"

with open(ciao_file) as f:
    code = f.read()
automata_name = code.split("\n")[0]

# change . in floats to ,
code = re.sub(r'\.(?!\n)', ',', code)

# read blocks
var_code, event_code, effect_code, reqired_cond_code, provided_cond_code, state_block_code = parse_blocks(code)

diadel_file = "diadel_code.txt"
with open(diadel_file, "w") as f:
    # parse state block
    transitions, state_map = parse_state_transition(code)
    for line in transitions:
        print(line, file=f)

    print("\n", file=f)

    # get lines with included states
    included_states = include_states(automata_name, state_map)
    for line in included_states:
        print(line, end="", file=f)

    print("\n", file=f)

    if len(var_code) != 0:
        included_vars = include_vars(automata_name, var_code)
        for line in included_vars:
            print(line, end="", file=f)







