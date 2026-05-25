from tareas import crear_tarea, añadir_tarea

def test_crear_tarea(tarea):
    assert tarea["titulo"] == "Hacer commit"
    assert tarea["hecha"] is False
    
def test_añadir_tarea():
    lista_tareas = []
    añadir_tarea(lista_tareas, "Comprar el pan")
    assert len(lista_tareas) > 0
    assert lista_tareas[0] == crear_tarea("Comprar el pan")
    