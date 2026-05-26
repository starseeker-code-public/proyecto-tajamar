from tareas import Tarea, añadir_tarea

def test_crear_tarea(tarea):
    assert tarea.titulo == "Hacer commit"
    assert tarea.completada is False
    
def test_añadir_tarea(tarea):
    lista_tareas = []
    añadir_tarea(lista_tareas, "Hacer commit")
    assert len(lista_tareas) > 0
    assert lista_tareas[0].titulo == tarea.titulo
    assert lista_tareas[0].completada == tarea.completada
    assert type(lista_tareas[0]) is type(tarea)
    assert isinstance(lista_tareas[0], Tarea)

def test_formatear_tarea(tarea):
    assert str(tarea) == "[ ] - Hacer commit"
    tarea.completada = True
    assert str(tarea) == "[x] - Hacer commit"