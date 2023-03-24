############################################################################################################
# Utilidad para realizar Web Scraping desde el sitio web del Portal de Archivos Españoles                  #
#                                                                                                          #
# https://pypi.org/project/paress2/                                                                        #
#                                                                                                          #
# Creada por Jairo Antonio Melo                                                                            #
# https://jairomelo.com                                                                                    #
#                                                                                                          #
# Repositorio en GitHub: https://github.com/jairomelo/paress2                                              #
#                                                                                                          #
# Licencia: GNU GPLv3                                                                                   #
############################################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions as se
from urllib.parse import urlparse, parse_qs

from .browser_checker import is_browser_installed
import os
import time

detectar_navegador = is_browser_installed("chrome")

if detectar_navegador:
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    navegador = "chrome"
elif is_browser_installed("firefox"):
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager
    navegador = "firefox"
else:
    raise Exception("Ningún navegador compatible instalado")


class Paress:

    def __init__(self, url: str, destino=None, headless=False, velocidad=10):
        """
        Parámetros:
        url: str
            URL del documento a descargar (http://)
        destino: str, path object o None
            Directorio donde se guardarán las imágenes
            Cualquier ruta en forma de cadena es válida.
            El objeto de ruta (path object) acepta cualquier `os.PathLike` object que dirija a un directorio.
            Si no se especifica una ruta absoluta, se guardará en el directorio donde se ejecute el script de Python o Jupyter Notebook (idéntico a os.getcwd())
        headless: bool
            Si es True, se ejecutará el navegador en modo headless (sin interfaz gráfica)
            **Este modo no descarga las imágenes**, así que debe entenderse como un modo de prueba.
            Default: False
        velocidad: float
            Tiempo de espera en segundos para que cargue la página web y la pausa entre descargas.
            Default: 10

        Ejemplo:
        paress = Paress("http://pares.mcu.es/ParesBusquedas20/catalogo/show/384442", destino="C:/Users/usuario/Downloads")

        """
        self.url = url
        self.destino = destino
        self.headless = headless
        self.velocidad = velocidad

        self.navegador = navegador

        directorio_legajo = self.url.split("/")[-1].split("?")[0]

        if self.destino:
            # ruta absoluta al directorio self.destino + directorio_legajo
            self.directorio_destino = os.path.join(
                os.path.abspath(self.destino), directorio_legajo)
        else:
            # ruta absoluta al directorio donde se ejecuta el script + directorio_legajo
            self.directorio_destino = os.path.join(
                os.getcwd(), directorio_legajo)

        self.driver = self.iniciar_driver()

    def iniciar_driver(self):
        """
        # inicializar el driver como un servicio
        """
        if self.navegador == "chrome":
            service = Service(ChromeDriverManager().install())

            # opciones para evitar que se muestre advertencia USB
            options = webdriver.ChromeOptions()
            options.add_experimental_option(
                'excludeSwitches', ['enable-logging'])

            # no abrir una ventana nueva
            if self.headless:
                print("Cargando en modo headless...")
                options.add_argument("--headless")

            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_experimental_option(
                'excludeSwitches', ['enable-logging'])

            options.add_experimental_option("prefs", {
                "download.default_directory": self.directorio_destino,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True
            })

            # inicializar el driver
            driver = webdriver.Chrome(service=service, options=options)
            driver.get(self.url)
            driver.implicitly_wait(self.velocidad)

            return driver

        elif self.navegador == "firefox":
            service = Service(GeckoDriverManager().install())

            # opciones para evitar que se muestre advertencia USB
            options = webdriver.FirefoxOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            # no abrir una ventana nueva
            if self.headless:
                print("Cargando en modo headless...")
                options.add_argument("--headless")

            options.set_preference("browser.download.folderList", 2)
            options.set_preference(
                "browser.download.manager.showWhenStarting", False)
            options.set_preference(
                "browser.download.dir", self.directorio_destino)
            options.set_preference(
                "browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

            # inicializar el driver
            driver = webdriver.Firefox(service=service, options=options)
            driver.get(self.url)
            driver.implicitly_wait(self.velocidad)

            return driver

    def get_elemento_descarga(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="saveImageLink"]')) and
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="saveImageLink"]'))
        )

        elemento_descarga = self.driver.find_element(
            By.XPATH, '//*[@id="saveImageLink"]')

        nombre_elemento = elemento_descarga.get_attribute("href")

        # get dbCode from href
        parsed_url = urlparse(nombre_elemento)
        querydict = parse_qs(parsed_url.query)
        try:
            dbCode = querydict["dbCode"][0]
        except KeyError:
            dbCode = None

        return elemento_descarga, dbCode

    def descargar_imagenes(self):
        # Mensaje de inicio
        os.makedirs(self.directorio_destino, exist_ok=True)
        print(
            f"Preparando la descarga de imágenes en el directorio: {self.directorio_destino}")

        # obtener número desde esta etiqueta <label id="lblVerImgs" for="chkVerImgs" class="nm" title="Ver Imágenes">308 imgs</label>
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#lblOcultarImgs")) and
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#lblOcultarImgs"), "imgs"))

        num_imgs = self.driver.find_element(
            By.CSS_SELECTOR, "#lblOcultarImgs").text.split(" ")[0]
        num_imgs = int(num_imgs)

        # iterar por el número de imágenes
        for i in range(num_imgs):

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#viewer > img")) and
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#viewer > img"))
            )

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="saveImageLink"]/img')) and
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="saveImageLink"]/img'))
            )

            # obtener el nombre del archivo
            elemento_descarga, nombre_archivo = self.get_elemento_descarga()
            try:
                nombre_archivo = nombre_archivo + ".jpg"
            except TypeError:
                nombre_archivo = "imagensindbCode.jpg"
            ruta_archivo = os.path.join(
                self.directorio_destino, nombre_archivo)

            # verificar si el archivo ya existe
            if os.path.exists(ruta_archivo):
                print(
                    f"El archivo {ruta_archivo} ya existe, omitiendo descarga...")
            else:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//*[@id="saveImageLink"]/img'))
                )

                # desplazarse al botón de descarga
                self.driver.execute_script(
                    "arguments[0].scrollIntoView();", elemento_descarga)

                # click en el elemento de descarga
                elemento_descarga.click()

            # click en la siguiente imagen y esperar a que desaparezca la clase iviewer_loading
            self.driver.find_element(By.XPATH, '//*[@id="botonMasPeq-2"]')\
                .click()
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element_located((By.CSS_SELECTOR, ".iviewer_loading")) and
                    EC.invisibility_of_element_located((By.CSS_SELECTOR, ".loader"))
                )
                print(f"Descargada la imagen {i+1} de {num_imgs}...", end="\r")
            except se.TimeoutException:
                print("TimeoutException: No se pudo cargar la siguiente imagen")

            # pausar para evitar que el servidor se sobrecargue
            time.sleep(self.velocidad)

        print(f"""
              REPORTE
                -------
                Directorio de destino: {self.directorio_destino}
                Número de imágenes: {num_imgs}
                Tamaño total: {round(sum(os.path.getsize(os.path.join(self.directorio_destino, f)) for f in os.listdir(self.directorio_destino)) / 1024 / 1024, 2)} MB
        """)

        self.close()

    def close(self):
        self.driver.close()


if __name__ == "__main__":
    pass
