from ui_text import msg_input, msg_salida_bucle_eventos
from tareas import añadir_tarea

condiciones_stop = ("STOP", "PARA", "PARAR", "S")

def bucle_tareas() -> list:
    lista_tareas = []
    while True:
        print(msg_salida_bucle_eventos)
        titulo_tarea = input(msg_input)
        if titulo_tarea.upper() in condiciones_stop:
            break
        añadir_tarea(lista_tareas, titulo_tarea.title())
    return lista_tareas