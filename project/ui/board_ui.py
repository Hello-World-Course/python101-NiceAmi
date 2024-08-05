def parse_cmd(command: str):
    parts = command.split()
    if not parts:
        return "",[]
    return parts[0], parts[1:]