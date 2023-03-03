# PARESS2 :: Descargador automatizado de archivos del Portal de Archivos Españoles PARES2.0

Esta librería permite realizar descargas automatizadas de archivos del Portal de Archivos Españoles PARES2.0. Debido a que el portal no cuenta con una API, se ha desarrollado esta librería para realizar un Web Scrapping de la página web del portal.

## Requisitos

Este programa ha sido probado y configurado para funcionar con Google Chrome a través de la librería [webdriver-manager](https://pypi.org/project/webdriver-manager/). Para su correcto funcionamiento es necesario tener instalado Google Chrome en el equipo. En caso de no tenerlo instalado, se puede descargar desde [aquí](https://www.google.com/intl/es/chrome/).

Se planea en una actualización posterior incluir soporte para Firefox y Chromium con el propósito de facilitar su uso en distribuciones Linux.

## Instalación

Este módulo está disponible en [PyPI](https://pypi.org/project/pypares2/). Para instalarlo, se debe ejecutar el siguiente comando:

```bash
pip install paress2
```

## Uso

En esta versión, solamente está disponible la opción de guardar imágenes de un legajo. En próximas versiones se incluirán más opciones.

Este módulo está diseñado para ser usado en un script de Python, por lo que no se incluye una interfaz gráfica. Para su uso, se debe importar el módulo y crear una instancia de la clase `Paress`:

```python
from paress2 import Paress
```

El objeto `Paress` se inicializa con mínimo un parámetro, que es el enlace al legajo que se quiera descargar. Por ejemplo:

```python
Paress("http://pares.mcu.es/ParesBusquedas20/catalogo/show/7255960?nm")
```

También existen tres parámetros opcionales:

- `destino`: Ruta de destino donde se guardarán los archivos. Por defecto, se guardan en un subdirectorio construido a partir del numero de catálogo del legajo (ej: 7255960). Si la ruta no es absoluta (ej: "C:\Users\usuario\descargas\images"), se guardará en el directorio donde se ejecute el script. Si la ruta no existe, se creará.
- `headless`: Si es `True`, se ejecutará el navegador en modo headless. Por defecto, es `False`. En este modo no es posible descargar imágenes, así que se debe entender como un modo de pruebas.
- `velocidad`: Tiempo en segundos (acepta valores decimales, p. ej: 0.5) que se espera entre cada proceso. El valor predeterminado es `10`, lo cual es aceptable para una cantidad de imágenes moderada (menor a 50 imágenes). Puede modificar este valor si se desea que el proceso sea más rápido o más lento. No obstante, tenga en cuenta que si el valor es muy bajo, se pueden presentar errores de conexión e incluso repetición en la descarga de imágenes.

Una vez creado el objeto, se debe llamar al método `descargar_imagenes()` para iniciar la descarga de las imágenes. Este método no recibe parámetros.

```python
Paress("http://pares.mcu.es/ParesBusquedas20/catalogo/show/7255960?nm", destino="C:\Users\usuario\descargas\images", velocidad=1).descargar_imagenes()
```

A menos que esté en modo headless, se abrirá una ventana de Google Chrome y se iniciará la descarga de las imágenes. El proceso puede tardar varios minutos, dependiendo de la velocidad de conexión a Internet y de la cantidad de imágenes que tenga el legajo.

## Licencia

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)

## Contribuciones

Las contribuciones son bienvenidas. Para solicitar cambios o reportar errores, por favor, cree un [issue](https://github.com/jairomelo/paress2/issues/new) en el repositorio de GitHub. Para reportar errores por favor compartir el número de catálogo del legajo y el mensaje de error que se muestra en la consola.

Si desea contribuir con el código, por favor, cree un pull request y se revisará o aceptará lo antes posible.

## TODO

- [ ] Añadir un registro del legajo descargado para identificar el documento.
- [ ] Incluir soporte para Firefox y Chromium
- [ ] Incluir opción para descargar el archivo como PDF
- [ ] Construir una interfaz gráfica para facilitar su uso
- [ ] Añadir la opción de descargar metadatos y conjuntos de búsquedas (por ejemplo, para descargar una lista de mapas)

## Patrocinio

Este proyecto ha sido elaborado de manera independiente por el autor. Si desea apoyar el desarrollo de este y otros proyectos, puede considerar patrocinarme a través de [GitHub Sponsors](https://github.com/sponsors/jairomelo)
