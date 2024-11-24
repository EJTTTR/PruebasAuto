from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
from Utils import tomar_captura


class Comentarios:
    def __init__(self, driver):
        self.driver = driver

    def agregar_comentario(self, comen):
        try:
            irContacto = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "nav ul li a[href='contacto.php']"))).click()
            tomar_captura(self.driver, "31 pagina_comentarios")
            time.sleep(2)

            c = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "h2.pb-3")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", c)
            time.sleep(1)

            # Agregar un comentario
            nom = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='nombre']")))
            ape = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='apellido']")))
            cor = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='correo']")))
            asun = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='asunto']")))
            com = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, "textarea[name='comentario']")))

            nom.clear()
            nom.send_keys('bot')

            ape.clear()
            ape.send_keys('selenium')

            cor.clear()
            cor.send_keys('botselenium123@bot.com')

            asun.clear()
            asun.send_keys('prueba automatizada')

            com.clear()
            com.send_keys(comen)

            tomar_captura(self.driver, '32 comentario_lleno')
            btnEnvi = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-outline-dark"))).click()
            time.sleep(2)
            tomar_captura(self.driver, '33 confirmacion_comentario')
            time.sleep(5)

            btnConf = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button.swal-button"))).click()
            c = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "h2.pb-3")))

            # Scroll para ver el comentario
            a = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, f"//p[text()='{comen}']")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", a)
            time.sleep(2)
            tomar_captura(self.driver, '34 comentario')



        except TimeoutException as e:
            print(f"Error al agregar autor: {e}")
