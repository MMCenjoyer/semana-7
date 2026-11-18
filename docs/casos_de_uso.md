# Casos de uso (v1.1)
- CU-01 Buscar libro [RF-01]
- CU-02 Registrar préstamo [RF-02, RF-05]: el estudiante elige un libro disponible; el sistema lo marca como no disponible y registra el préstamo.
  - Flujo alterno (CR-001, RF-05): si el estudiante ya tiene 3 préstamos activos, el sistema rechaza con «Máximo tres préstamos activos» y no modifica el libro.
- CU-03 Devolver libro [RF-03]
- CU-04 Consultar préstamos [RF-04]
