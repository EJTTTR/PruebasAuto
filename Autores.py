from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
from Utils import tomar_captura


class Autores:
    def __init__(self, driver):
        self.driver = driver

    def agregar_autor(self):
        try:
            irAutor = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "nav ul li a[href='autores.php']"))).click()
            tomar_captura(self.driver, "16 pagina_autores")
            time.sleep(2)
            # Agregar un autor
            btnAgregarA = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-outline-primary[data-bs-toggle='modal']"))).click()

            btnGuarda = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div.modal button.btn-outline-primary"))).click()
            time.sleep(2)
            tomar_captura(self.driver, '36 requerimiento_de_no_campos_vacios')
            time.sleep(2)

            tomar_captura(self.driver, '17 modal_agregar_autor')
            nom = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='nombre']")))
            ape = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='apellido']")))
            tel = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='telefono']")))
            dire = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='direccion']")))
            ciu = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='ciudad']")))
            pai = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pais']")))
            img = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='fotografia']")))

            au = 'Antoine Saint-Exupéry'
            nom.clear()
            nom.send_keys('Antoine')

            ape.clear()
            ape.send_keys('Saint-Exupéry')

            tel.clear()
            tel.send_keys('null')

            dire.clear()
            dire.send_keys('desconocido')

            ciu.clear()
            ciu.send_keys('Marsella')

            pai.clear()
            pai.send_keys('Francia')

            img.clear()
            img.send_keys('https://i.pinimg.com/originals/83/3a/89/833a8983b5f5cf47b5989594a8249b89.jpg')

            tomar_captura(self.driver, '18 modal_agregar_autor_lleno')
            btnGuarda = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div.modal button.btn-outline-primary"))).click()
            tomar_captura(self.driver, '19 se_agrego_el_autor')

            xpath_card = f"//h5[contains(text(), '{au}')]/ancestor::div[contains(@class, 'card')]"
            card = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath_card)))

            # Scroll en caso de no verlo
            self.driver.execute_script("arguments[0].scrollIntoView(true);", card)
            time.sleep(1)
            detalle = card.find_element(By.CSS_SELECTOR, "button.btn-outline-dark[data-bs-target='#autorModal']")
            self.driver.execute_script("arguments[0].click();", detalle)
            tomar_captura(self.driver, '20 info_del_autor')

            btnClose = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, "div.modal button.btn-close"))).click()


        except TimeoutException as e:
            print(f"Error al agregar autor: {e}")

    def editar_autor(self, au):
        try:
            # Busco el autor que agregamos para editarlo
            xpath_card = f"//h5[contains(text(), '{au}')]/ancestor::div[contains(@class, 'card')]"
            card = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath_card)))

            # Scroll en caso de no verlo
            self.driver.execute_script("arguments[0].scrollIntoView(true);", card)
            tomar_captura(self.driver, '22 autor_antes_de_modificar')
            time.sleep(1)

            # Busca clickea el btnEditar en card buscada anteriormente
            edit_button = card.find_element(By.CSS_SELECTOR, "button.btn-outline-warning[data-bs-target='#editarAutorModal']")
            tomar_captura(self.driver, '23 modal2_antes_de_modificar')
            self.driver.execute_script("arguments[0].click();", edit_button)

            # Espera que el modal se vea
            modal = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, "editarAutorModal")))

            tip = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, "input#editarDireccion")))

            tip.clear()
            tip.send_keys('Lyon')

            tomar_captura(self.driver, '24 modal2_despues_de_modificar')
            btnGuarda = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(
                (By.CSS_SELECTOR, "#editarAutorModal .modal-footer .btn-outline-primary"))).click()
            tomar_captura(self.driver, '25 autor_despues_de_modificar')

        except Exception as e:
            print(f"Error al editar el libro: {str(e)}")

    def eliminar_autor(self, au):
        try:
            # Busco el autor que editamos para eliminarlo
            xpath_card = f"//h5[contains(text(), '{au}')]/ancestor::div[contains(@class, 'card')]"
            card = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath_card)))

            # Scroll hacia la tarjeta
            self.driver.execute_script("arguments[0].scrollIntoView(true);", card)
            tomar_captura(self.driver, '27 autor_antes_de_eliminar')
            time.sleep(1)

            # Busca clickea el btnEliminar en card buscada anteriormente
            delete_button = card.find_element(By.CSS_SELECTOR, "button.btn-outline-danger")
            self.driver.execute_script("arguments[0].click();", delete_button)
            tomar_captura(self.driver, '28 alerta_de_confirmacion_2')

            # Click en el btn de confirmar eliminar
            confirm_button = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, "button.swal2-confirm"))).click()
            tomar_captura(self.driver, '29 despues_de_confirmar_2')

        except Exception as e:
            print(f"Error al eliminar el libro: {str(e)}")
