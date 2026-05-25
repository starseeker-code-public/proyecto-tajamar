from pytest import fixture
from tareas import crear_tarea

@fixture
def tarea():
    return crear_tarea("Hacer commit")