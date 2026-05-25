from ui import msg_bienvenida, msg_salida_bucle_eventos, msg_input
from tareas import añadir_tarea
from tabulate import tabulate

print(msg_bienvenida)

tareas = []

while True:
    print(msg_salida_bucle_eventos)
    titulo_tarea = input(msg_input)
    if titulo_tarea.upper() in ("STOP", "PARA", "PARAR", "S"):
        break
    añadir_tarea(tareas, titulo_tarea.title())
    tabla_bonita = tabulate([(tarea["hecha"], tarea["titulo"]) for tarea in tareas],
                            headers=["COMPLETADA", "TITULO"], tablefmt="rounded_grid")
    print(f"\n{tabla_bonita}\n")