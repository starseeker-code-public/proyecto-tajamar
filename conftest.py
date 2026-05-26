from pytest import fixture
from tareas import Tarea

@fixture
def tarea():
    return Tarea("Hacer commit")