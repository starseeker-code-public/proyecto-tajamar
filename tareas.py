
class Tarea:
    def __init__(self, titulo: str):
            self.titulo = titulo
            self.completada = False
        
    def __str__(self) -> str:
        completada = "[x]" if self.completada else "[ ]"
        return f"{completada} - {self.titulo}"
    
def añadir_tarea(lista_tareas: list, titulo_tarea: str):
    tarea = Tarea(titulo_tarea)
    lista_tareas.append(tarea)
