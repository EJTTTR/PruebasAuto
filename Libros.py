from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
from Utils import tomar_captura


class Libros:
    def __init__(self, driver):
        self.driver = driver


    def agregar_libro(self):
        try:
            # Agregar un libro
            btnAgregarL = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-outline-primary[data-bs-toggle='modal']"))).click()
            tomar_captura(self.driver, '2 modal_agregar_libro')

            btnGuarda = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div.modal button.btn-outline-primary"))).click()
            time.sleep(2)
            tomar_captura(self.driver, '35 requerimiento_de_no_campos_vacios')
            time.sleep(2)

            titu = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='titulo']")))
            tip = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='tipo']")))
            pre = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='precio']")))
            nota = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, "textarea[name='notas']")))
            img = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='imagen']")))

            til = 'El principito'
            titu.clear()
            titu.send_keys(til)

            tip.clear()
            tip.send_keys('Cuento')

            pre.clear()
            pre.send_keys('60')

            nota.clear()
            nota.send_keys(
                'El narrador cuenta que una vez, cuando era un niño, hizo un dibujo de una boa que digería a un elefante; sin embargo, todos los adultos que veían el dibujo lo interpretaban erróneamente como un sombrero.')

            img.clear()
            img.send_keys('https://www.elidealgallego.com/images/showid2/5880035?w=1200&zc=4')

            tomar_captura(self.driver, '3 modal_agregar_libro_lleno')
            btnGuarda = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div.modal button.btn-outline-primary"))).click()
            tomar_captura(self.driver, '4 se_agrego_el_libro')

            xpath_card = f"//h5[contains(text(), '{til}')]/ancestor::div[contains(@class, 'card')]"
            card = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath_card)))

            # Scroll en caso de no verlo
            self.driver.execute_script("arguments[0].scrollIntoView(true);", card)
            time.sleep(1)
            detalle = card.find_element(By.CSS_SELECTOR, "button.btn-outline-dark[data-bs-target='#libroModal']")
            self.driver.execute_script("arguments[0].click();", detalle)
            tomar_captura(self.driver, '5 info_del_libro')

            btnClose = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, "div.modal button.btn-close"))).click()


        except TimeoutException as e:
            print(f"Error al agregar libro: {str(e)}")

    def editar_libro(self, til):
        try:
            # Busco el libro que agregamos para editarlo
            xpath_card = f"//h5[contains(text(), '{til}')]/ancestor::div[contains(@class, 'card')]"
            card = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath_card)))

            # Scroll en caso de no verlo
            self.driver.execute_script("arguments[0].scrollIntoView(true);", card)
            tomar_captura(self.driver, '7 libro_antes_de_modificar')
            time.sleep(1)

            tomar_captura(self.driver, '8 modal_antes_de_modificar')
            # Busca clickea el btnEditar en card buscada anteriormente
            edit_button = card.find_element(By.CSS_SELECTOR, "button.btn-outline-warning[data-bs-target='#editarLibroModal']")
            self.driver.execute_script("arguments[0].click();", edit_button)

            # Espera que el modal se vea
            modal = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, "editarLibroModal")))

            tip = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input#editarTipo")))

            tip.clear()
            tip.send_keys('Novela')

            tomar_captura(self.driver, '9 modal_despues_de_modificar')
            btnGuarda = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(
                (By.CSS_SELECTOR, "#editarLibroModal .modal-footer .btn-outline-primary"))).click()
            tomar_captura(self.driver, '10 libro_despues_de_modificar')

        except Exception as e:
            print(f"Error al editar el libro: {str(e)}")

    def eliminar_libro(self, til):
        try:
            # Busco el libro que editamos para eliminarlo
            xpath_card = f"//h5[contains(text(), '{til}')]/ancestor::div[contains(@class, 'card')]"
            card = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath_card)))

            # Scroll hacia la tarjeta
            self.driver.execute_script("arguments[0].scrollIntoView(true);", card)
            tomar_captura(self.driver, '12 libro_antes_de_eliminar')
            time.sleep(1)

            # Busca clickea el btnEliminar en card buscada anteriormente
            delete_button = card.find_element(By.CSS_SELECTOR, "button.btn-outline-danger")
            self.driver.execute_script("arguments[0].click();", delete_button)
            tomar_captura(self.driver, '13 alerta_de_confirmacion')

            # Click en el btn de confirmar eliminar
            confirm_button = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, "button.swal2-confirm"))).click()
            tomar_captura(self.driver, '14 despues_de_confirmar')

        except Exception as e:
            print(f"Error al eliminar el libro: {str(e)}")
