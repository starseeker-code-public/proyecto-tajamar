import rich.console as console
import rich.table as table

class UI:
    consola = console.Console()
    tabla = table.Table()
    
    @classmethod
    def mostrar_tabla(cls):
        cls.consola.print(cls.tabla)
        
    @classmethod
    def crear_filas(cls, lista_tareas: list):
        for _ID, tarea in enumerate(lista_tareas):
            cls.tabla.add_row(
                str(_ID + 1),
                "✓" if tarea["completada"] else "ｘ",
                tarea["titulo"]
            )

UI.tabla.add_column("ID")
UI.tabla.add_column("Completada")
UI.tabla.add_column("Tarea")
