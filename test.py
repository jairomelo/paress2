## Testing module for Paress class
import unittest
from paress2 import Paress

class TestParess(unittest.TestCase):
    def setUp(self):
        self.paress = Paress("http://pares.mcu.es/ParesBusquedas20/catalogo/show/4223090?nm", destino="descargas", velocidad=1)

    def test_descargar_imgs(self):
        self.paress.descargar_imagenes()

if __name__ == '__main__':
    unittest.main()