import sys, unittest
sys.path.insert(0, "src")
from biblioteca import Biblioteca, Libro, BibliotecaError


def nueva():
    return Biblioteca([Libro(i, f"Libro {i}") for i in range(1, 7)])


class TestBiblioteca(unittest.TestCase):
    def test_pr01_buscar(self):                                  # RF-01
        self.assertEqual(len(nueva().buscar("libro 2")), 1)

    def test_pr02_prestar(self):                                 # RF-02
        b = nueva(); b.prestar("E1", 1)
        self.assertFalse(b.libros[1].disponible)
        with self.assertRaises(BibliotecaError):
            b.prestar("E2", 1)

    def test_pr03_devolver(self):                                # RF-03
        b = nueva(); b.prestar("E1", 1); b.devolver("E1", 1)
        self.assertTrue(b.libros[1].disponible)

    def test_pr04_consultar(self):                               # RF-04
        b = nueva(); b.prestar("E1", 1); b.prestar("E1", 2)
        self.assertEqual(len(b.consultar("E1")), 2)

    def test_pr05_limite_tres(self):                             # RF-05 (CR-001)
        b = nueva()
        for i in (1, 2, 3):
            b.prestar("E1", i)
        with self.assertRaises(BibliotecaError):
            b.prestar("E1", 4)
        self.assertTrue(b.libros[4].disponible)                  # inventario intacto
        b.devolver("E1", 1)
        b.prestar("E1", 4)                                       # tras devolver, se acepta
        self.assertEqual(len(b.consultar("E1")), 3)


if __name__ == "__main__":
    unittest.main()
