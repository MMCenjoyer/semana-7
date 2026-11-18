"""Verifica trazabilidad: SRS <-> matriz <-> pruebas del código."""
import csv, re, sys, pathlib
raiz = pathlib.Path(__file__).resolve().parent.parent
srs = set(re.findall(r"\| (RF-\d+) \|", (raiz / "docs/SRS.md").read_text(encoding="utf-8")))
filas = list(csv.DictReader(open(raiz / "trazabilidad/matriz.csv", encoding="utf-8")))
en_matriz = {f["requisito"] for f in filas}
completos = {f["requisito"] for f in filas if f["caso_de_uso"] and f["clase_metodo"] and f["prueba"]}
codigo = (raiz / "tests/test_biblioteca.py").read_text(encoding="utf-8")
pruebas_codigo = {"PR-" + n for n in re.findall(r"def test_pr(\d+)_", codigo)}
pruebas_matriz = {f["prueba"] for f in filas}
print(f"Requisitos en SRS ........ {len(srs)}")
print(f"Requisitos en matriz ..... {len(en_matriz)}")
print(f"Con CU + clase + prueba .. {len(completos & srs)}")
print(f"Cobertura ................ {100*len(completos & srs)/max(len(srs),1):.0f}%")
huerfanos = sorted(srs - en_matriz); sin_codigo = sorted(pruebas_matriz - pruebas_codigo)
print("Requisitos sin trazar .... " + (", ".join(huerfanos) or "ninguno"))
print("Pruebas sin implementar .. " + (", ".join(sin_codigo) or "ninguna"))
sys.exit(1 if huerfanos or sin_codigo or len(completos & srs) < len(srs) else 0)
