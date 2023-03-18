# Configuración del módulo

import pathlib
import os
from setuptools import setup, find_packages

# Obtener la ruta del directorio actual
HERE = pathlib.Path(__file__).parent

about = {}

with open(os.path.join(HERE, 'paress2', "__version__.py"), encoding='utf-8') as f:
    exec(f.read(), about)

LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
    'selenium>=4.8.2, <5.0.0',
    'webdriver-manager>=3.8.5, <4.0.0'
]

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=about['__author__'],
    license=about['__license__'],
    author_email=about['__author_email__'],
    requires=["Python (>=3.7)"],
    url=about['__url__'],
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    keywords=['python', 'paress', 'paress2', 'pares2.0', 'archivos históricos', 'historical files', 'historical documents', 'historical images', 'historical photos', 'historical pictures'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ]
)


