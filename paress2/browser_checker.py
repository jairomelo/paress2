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
# Licencia: GNU GPLv3                                                                                      #
############################################################################################################

import platform
import subprocess
import os


def is_browser_installed(browser_name: str) -> bool:
    """ Revisa si el usuario tiene instalado el navegador especificado.

    Parámetros:
    -----------
    browser_name: str
        Nombre del navegador a revisar.
        Ej: "chrome", "firefox"

    Devuelve:
    ---------
    bool
        True si el navegador está instalado, False en caso contrario.

    """
    system_name = platform.system()
    if system_name == "Windows":
        if browser_name == "chrome":
            return os.path.exists(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        elif browser_name == "firefox":
            return os.path.exists(r"C:\Program Files\Mozilla Firefox\firefox.exe")
        else:
            return False
    elif system_name == 'Darwin' or system_name == 'Linux':
        try:
            result = subprocess.run(
                ['which', browser_name], capture_output=True, check=True, text=True)
            return True
        except subprocess.CalledProcessError:
            return False


if __name__ == "__main__":
    print(is_browser_installed("chrome"))
