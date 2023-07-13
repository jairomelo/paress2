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
import winreg


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
        """
        Este código intenta leer la ruta de instalación del navegador desde el registro de Windows.
        Fue contruido en conjunto con ChatGPT https://chat.openai.com/share/1c018a56-7cd4-4ea3-a186-91d774d84ff8
        """
        if browser_name == "chrome":
            try:
                reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe"
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_READ) as key:
                    value, _ = winreg.QueryValueEx(key, None)
                    return os.path.exists(value)
            except WindowsError:
                return False

        elif browser_name == "firefox":
            try:
                reg_path = r"SOFTWARE\Mozilla\Mozilla Firefox"
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_READ) as key:
                    subkey_count = winreg.QueryInfoKey(key)[0]
                    for i in range(subkey_count):
                        subkey_name = winreg.EnumKey(key, i)
                        subkey_path = os.path.join(reg_path, subkey_name, "Main")
                        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path, 0, winreg.KEY_READ) as subkey:
                            value, _ = winreg.QueryValueEx(subkey, "PathToExe")
                            if os.path.exists(value):
                                return True
                    return False
            except WindowsError:
                return False

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
