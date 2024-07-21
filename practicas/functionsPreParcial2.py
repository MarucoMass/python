def validar_numero_documento(medicos: list, nro_doc:str) -> bool:
    dni_encontrado = any(x["dni"] == nro_doc for x in medicos)
    return dni_encontrado