import unittest
import cambiatext

class ProbarCambiaTexto(unittest.TestCase):
    def test_mayusculas(self):
        palabra = "buen dia"
        resultado = cambiatext.todo_mayuscula(palabra)
        self.assertEqual(resultado, "buen dia")

if __name__ == "__main__":
    unittest.main()