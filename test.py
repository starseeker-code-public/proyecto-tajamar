from tareas import crear_tarea

def test_crear_tarea():
    tarea = crear_tarea("Hacer commit")
    assert tarea["titulo"] == "Hacer commit"
    assert tarea["hecha"] is False