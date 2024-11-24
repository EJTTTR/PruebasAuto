import os

def tomar_captura(driver, nombre_archivo):
    nombre_archivo = f"{nombre_archivo}.png"
    driver.save_screenshot(os.path.join("results", nombre_archivo))