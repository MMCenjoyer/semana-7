"""CL-01 Biblioteca, CL-02 Libro, CL-03 Prestamo (v1.0)."""
from dataclasses import dataclass


class BibliotecaError(Exception):
    pass


@dataclass
class Libro:                      # CL-02
    id: int
    titulo: str
    disponible: bool = True


@dataclass
class Prestamo:                   # CL-03
    estudiante_id: str
    libro_id: int
    activo: bool = True


class Biblioteca:                 # CL-01
    def __init__(self, libros):
        self.libros = {l.id: l for l in libros}
        self.prestamos = []

    def buscar(self, texto):                                   # RF-01
        return [l for l in self.libros.values() if texto.lower() in l.titulo.lower()]

    def prestar(self, estudiante_id, libro_id):                # RF-02
        libro = self.libros[libro_id]
        if not libro.disponible:
            raise BibliotecaError("Libro no disponible")
        libro.disponible = False
        p = Prestamo(estudiante_id, libro_id)
        self.prestamos.append(p)
        return p

    def devolver(self, estudiante_id, libro_id):               # RF-03
        for p in self.prestamos:
            if p.estudiante_id == estudiante_id and p.libro_id == libro_id and p.activo:
                p.activo = False
                self.libros[libro_id].disponible = True
                return p
        raise BibliotecaError("No existe un préstamo activo")

    def consultar(self, estudiante_id):                        # RF-04
        return [p for p in self.prestamos if p.estudiante_id == estudiante_id and p.activo]
