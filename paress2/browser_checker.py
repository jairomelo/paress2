import platform
import subprocess
import os

def is_browser_installed(browser_name):
    system_name = platform.system()
    if system_name == "Windows":
        if browser_name == "chrome":
            return os.path.exists(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        elif browser_name == "firefox":
            return os.path.exists(r"C:\Program Files\Mozilla Firefox\firefox.exe")
        else:
            raise ValueError("Browser name not supported")
    elif system_name == 'Darwin' or system_name == 'Linux':
        try:
            result = subprocess.run(['which', browser_name], capture_output=True, check=True, text=True)
            return True
        except subprocess.CalledProcessError:
            return False

if __name__ == "__main__":
    print(is_browser_installed("chrome"))
    