from ui import msg_bienvenida, msg_salida_bucle_eventos, msg_input
from tareas import añadir_tarea
import rich.console as console
import rich.table as table

print(msg_bienvenida)

consola = console.Console()
tabla = table.Table()
tareas = []

tabla.add_column("ID")
tabla.add_column("Completada")
tabla.add_column("Tarea")

while True:
    print(msg_salida_bucle_eventos)
    titulo_tarea = input(msg_input)
    if titulo_tarea.upper() in ("STOP", "PARA", "PARAR", "S"):
        break
    añadir_tarea(tareas, titulo_tarea.title())
    
for _ID, tarea in enumerate(tareas):
    tabla.add_row(
        str(_ID + 1),
        "✓" if tarea["completada"] else "ｘ",
        tarea["titulo"]
    )

consola.print(tabla)