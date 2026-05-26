from ui_text import msg_bienvenida
from tools import bucle_tareas
from ui import UI

print(msg_bienvenida)
tareas = bucle_tareas()
UI.crear_filas(tareas)
UI.mostrar_tabla()