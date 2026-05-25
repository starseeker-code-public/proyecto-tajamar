def crear_tarea(titulo: str):
    return {
        "titulo": titulo,
        "completada": False
    }
    
def añadir_tarea(lista_tareas: list, titulo_tarea: str):
    tarea = crear_tarea(titulo_tarea)
    lista_tareas.append(tarea)
    
def formatear_tarea(tarea):
    completada = "[x]" if tarea["completada"] else "[ ]"
    return f"{completada} - {tarea["titulo"]}"