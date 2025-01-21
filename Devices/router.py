from Configuration_Terminal.Objects.Terminal import Terminal


def get_router_commands():
    return ["deactivate domain-lookup", "set Banner", ""]

def write_router_command(term: Terminal, command:str):
    term.write_terminal(command)
