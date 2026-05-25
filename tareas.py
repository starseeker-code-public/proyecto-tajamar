def crear_tarea(titulo: str):
    return {
        "titulo": titulo,
        "hecha": False
    }
    
def añadir_tarea(lista_tareas: list, titulo_tarea: str):
    tarea = crear_tarea(titulo_tarea)
    lista_tareas.append(tarea)