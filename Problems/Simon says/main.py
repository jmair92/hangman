def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        return instructions.replace("Simon says", "I")
    elif instructions.endswith("Simon says"):
        return "I " + instructions.replace("Simon says", "")
    else:
        return "I won't do it!"
