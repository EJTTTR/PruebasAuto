import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
from Libros import Libros
from Autores import Autores
from Comentarios import Comentarios
from Utils import tomar_captura
import pytest


@pytest.fixture(scope="module")
def setup_driver():
    edge_options = Options()
    service = Service('C:/edgedriver/msedgedriver.exe')
    driver = webdriver.Edge(service=service, options=edge_options)
    driver.get('http://bonfirebooks.free.nf/')
    driver.maximize_window()
    yield driver
    driver.quit()

if not os.path.exists("results"):
    os.makedirs("results")

if not os.path.exists("reporte"):
    os.makedirs("reporte")

def test_agregar_libro(setup_driver):
    driver = setup_driver
    lib = Libros(driver)
    try:
        tomar_captura(driver, "1 pagina_principal")
        lib.agregar_libro()
        tomar_captura(driver, '6 estado_final_despues_de_agregar_libro')
    except Exception as e:
        tomar_captura(driver, 'error_agregar_libro')
        pytest.fail(f"Error al agregar libro: {str(e)}")

def test_editar_libro(setup_driver):
    driver = setup_driver
    lib = Libros(driver)
    try:
        lib.editar_libro("El principito")
        tomar_captura(driver, '11 estado_final_despues_de_editar_libro')
    except Exception as e:
        tomar_captura(driver, 'error_editar_libro')
        pytest.fail(f"Error al editar libro: {str(e)}")

def test_eliminar_libro(setup_driver):
    driver = setup_driver
    lib = Libros(driver)
    try:
        lib.eliminar_libro('El principito')
        tomar_captura(driver, '15 estado_final_despues_de_eliminar_libro')
    except Exception as e:
        tomar_captura(driver, 'error_eliminar_libro')
        pytest.fail(f"Error al eliminar libro: {str(e)}")

def test_agregar_autor(setup_driver):
    driver = setup_driver
    autor = Autores(driver)
    try:
        time.sleep(3)
        autor.agregar_autor()
        tomar_captura(driver, '21 estado_final_despues_de_agregar_autor')
    except Exception as e:
        tomar_captura(driver, 'error_agregar_autor')
        pytest.fail(f"Error al agregar autor: {str(e)}")


def test_editar_autor(setup_driver):
    driver = setup_driver
    autor = Autores(driver)
    try:
        autor.editar_autor("Antoine Saint-Exupéry")
        tomar_captura(driver, '26 estado_final_despues_de_editar_autor')
    except Exception as e:
        tomar_captura(driver, 'error_editar_autor')
        pytest.fail(f"Error al editar autor: {str(e)}")


def test_eliminar_autor(setup_driver):
    driver = setup_driver
    autor = Autores(driver)
    try:
        autor.eliminar_autor("Antoine Saint-Exupéry")
        tomar_captura(driver, '30 estado_final_despues_de_eliminar_autor')
    except Exception as e:
        tomar_captura(driver, 'error_eliminar_autor')
        pytest.fail(f"Error al eliminar autor: {str(e)}")

def test_agregar_comentario(setup_driver):
    driver = setup_driver
    comentario = Comentarios(driver)
    try:
        time.sleep(4)
        comentario.agregar_comentario("prueba automatizada de comentario ihoi558")

    except Exception as e:
        tomar_captura(driver, 'error_agregar_comentario')
        pytest.fail(f"Error al agregar comentario: {str(e)}")

