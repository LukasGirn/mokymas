from models.kursas import Kursas
from models.python_kursas import PythonKursas

kursas = Kursas("Geimingas", "Lukas", 20)
pythonkursas = PythonKursas("Programavimas", "Tomas", 370)
kursas2 = PythonKursas("Python", "Jonas", 290)

kursas.destyti()
pythonkursas.destyti()
kursas2.destyti()