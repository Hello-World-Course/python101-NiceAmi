def parse_cmd(coomand: str):
    parts = coomand.split()
    if not parts:
        return "",[]
    return parts[0], parts[1:]

