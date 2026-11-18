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


if __name__ == "__main__":
    unittest.main()
