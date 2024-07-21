def validar_fidelidad(cliente: dict) -> bool:
    if len(cliente) >= 5:
        return True
    return False