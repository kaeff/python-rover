

def launch_mission(input_string):
    rovers = parse_rovers(input_string)
    final_positions = map(execute_mission, rovers)
    return format_output(final_positions)


def parse_rovers(input_string):
    rover_lines = input_string.splitlines()[1:]
    rovers = [(commands, initial_position.split(' ')) for commands, initial_position in pairs(rover_lines)]
    return rovers


def pairs(a_list):
    result = []
    while a_list:
        result.insert(0, (a_list.pop(), a_list.pop()))
    return result


def format_output(final_positions):
    return '\n'.join(["%s %s %s" % final_position for final_position in final_positions])


def execute_mission(rover):
    commands, (x, y, heading) = rover
    for command in commands:
        x, y, heading = execute_command(x, y, heading, command)
    return x, y, heading


def execute_command(x, y, heading, command):
    x, y = int(x), int(y)

    if command is 'M':
        x, y = execute_move(heading, x, y)
    else:
        heading = execute_turn(heading, command)

    return x, y, heading


def execute_move(heading, x, y):
    y = y + 1 if heading is 'N' else y
    y = y - 1 if heading is 'S' else y
    x = x + 1 if heading is 'E' else x
    x = x - 1 if heading is 'W' else x
    return x, y


HEADINGS = ['N', 'E', 'S', 'W']
LEFT_RIGHT = {'L': -1, 'R': 1}


def execute_turn(heading, command):
    return HEADINGS[(HEADINGS.index(heading) + LEFT_RIGHT[command]) % 4]
