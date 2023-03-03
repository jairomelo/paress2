# Configuración del módulo

import pathlib
from setuptools import setup, find_packages

# Obtener la ruta del directorio actual
HERE = pathlib.Path(__file__).parent

# El texto de la descripción se obtiene del archivo README.md
VERSION = '0.1.3'
PACKAGE_NAME = 'paress2'
AUTHOR = 'Jairo Antonio Melo'
AUTHOR_EMAIL = 'jairoantoniomelo@gmail.com'
URL = 'https://github.com/jairomelo/paress2'

LICENSE = 'GNU General Public License v3.0'
DESCRIPTION = 'Paquete para la descarga automatizada de documentos desde el Portal de Archivos Españoles'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
    'selenium>=4.8.2, <5.0.0',
    'webdriver-manager>=3.8.5, <4.0.0'
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    requires=["Python (>=3.7)"],
    url=URL,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    keywords=['python', 'paress', 'paress2', 'pares2.0'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ]
)


