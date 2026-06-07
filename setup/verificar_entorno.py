#!/usr/bin/env python3
"""
Verificador de entorno — Big Data DD283
Universidad Autónoma del Perú — 2026-1

Ejecutar con:
    python setup/verificar_entorno.py

Verifica que todas las librerías y conexiones necesarias para el curso
están correctamente instaladas y configuradas.
"""

import sys
import subprocess

OK    = "✅"
FAIL  = "❌"
WARN  = "⚠️ "
INFO  = "ℹ️ "
SEP   = "─" * 60

def check(nombre, importacion, version_attr=None, min_version=None):
    try:
        mod = __import__(importacion)
        if version_attr:
            ver = getattr(mod, version_attr, "?")
            label = f"{OK}  {nombre:<25} v{ver}"
        else:
            label = f"{OK}  {nombre:<25} instalado"
        print(label)
        return True
    except ImportError:
        print(f"{FAIL}  {nombre:<25} NO INSTALADO — ejecuta: pip install {importacion}")
        return False

def check_java():
    try:
        result = subprocess.run(
            ["java", "-version"], capture_output=True, text=True
        )
        ver_line = (result.stderr or result.stdout).split("\n")[0]
        print(f"{OK}  {'Java':<25} {ver_line.strip()}")
        return True
    except FileNotFoundError:
        print(f"{FAIL}  {'Java':<25} NO INSTALADO — necesario para PySpark")
        print(f"     Descarga: https://adoptium.net/")
        return False

def check_docker():
    try:
        result = subprocess.run(
            ["docker", "info"], capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            print(f"{OK}  {'Docker':<25} corriendo correctamente")
            return True
        else:
            print(f"{WARN} {'Docker':<25} instalado pero NO está corriendo — abre Docker Desktop")
            return False
    except (FileNotFoundError, subprocess.TimeoutExpired):
        print(f"{FAIL}  {'Docker':<25} NO INSTALADO — descarga en docker.com")
        return False

def check_git():
    try:
        result = subprocess.run(["git", "--version"], capture_output=True, text=True)
        print(f"{OK}  {'Git':<25} {result.stdout.strip()}")
        return True
    except FileNotFoundError:
        print(f"{FAIL}  {'Git':<25} NO INSTALADO — descarga en git-scm.com")
        return False

def check_pyspark():
    try:
        import pyspark
        from pyspark.sql import SparkSession
        spark = SparkSession.builder \
            .appName("verificacion_entorno") \
            .master("local[1]") \
            .config("spark.ui.showConsoleProgress", "false") \
            .getOrCreate()
        spark.sparkContext.setLogLevel("ERROR")
        df = spark.createDataFrame([(1, "Big Data UA"), (2, "2026-1")], ["id", "texto"])
        count = df.count()
        spark.stop()
        print(f"{OK}  {'PySpark':<25} v{pyspark.__version__} — SparkSession OK ({count} filas)")
        return True
    except Exception as e:
        print(f"{FAIL}  {'PySpark':<25} Error: {str(e)[:60]}")
        return False

def check_python_version():
    ver = sys.version_info
    ver_str = f"{ver.major}.{ver.minor}.{ver.micro}"
    if ver.major == 3 and ver.minor >= 10:
        print(f"{OK}  {'Python':<25} v{ver_str} ✓")
        return True
    else:
        print(f"{WARN} {'Python':<25} v{ver_str} — se recomienda 3.10+")
        return ver.major == 3

# ─────────────────────────────────────────────────────────────
print()
print("═" * 60)
print("  🐘 BIG DATA DD283 — Verificación de Entorno")
print("  Universidad Autónoma del Perú | Semestre 2026-1")
print("═" * 60)

resultados = []

print(f"\n{SEP}")
print("  🐍 PYTHON Y SISTEMA")
print(SEP)
resultados.append(check_python_version())
resultados.append(check_java())
resultados.append(check_git())
resultados.append(check_docker())

print(f"\n{SEP}")
print("  📦 LIBRERÍAS DE DATOS (Semanas 1-4)")
print(SEP)
resultados.append(check("pandas",        "pandas",      "__version__"))
resultados.append(check("numpy",         "numpy",       "__version__"))
resultados.append(check("pyarrow",       "pyarrow",     "__version__"))
resultados.append(check("matplotlib",    "matplotlib",  "__version__"))
resultados.append(check("seaborn",       "seaborn",     "__version__"))
resultados.append(check("plotly",        "plotly",      "__version__"))

print(f"\n{SEP}")
print("  ⚡ APACHE SPARK (Semanas 5-6)")
print(SEP)
resultados.append(check_pyspark())

print(f"\n{SEP}")
print("  🍃 BASES DE DATOS (Semanas 3-4)")
print(SEP)
resultados.append(check("pymongo",       "pymongo",     "version"))
resultados.append(check("psycopg2",      "psycopg2",    "__version__"))
resultados.append(check("sqlalchemy",    "sqlalchemy",  "__version__"))

print(f"\n{SEP}")
print("  🕷️  WEB SCRAPING (Semana 7)")
print(SEP)
resultados.append(check("requests",      "requests",    "__version__"))
resultados.append(check("BeautifulSoup", "bs4",         None))
resultados.append(check("scrapy",        "scrapy",      "__version__"))
resultados.append(check("lxml",          "lxml",        "__version__"))

print(f"\n{SEP}")
print("  🤖 MACHINE LEARNING (Semana 6)")
print(SEP)
resultados.append(check("scikit-learn",  "sklearn",     "__version__"))
resultados.append(check("imbalanced-learn","imblearn",  "__version__"))

print(f"\n{SEP}")
print("  🔧 UTILIDADES")
print(SEP)
resultados.append(check("python-dotenv", "dotenv",      None))
resultados.append(check("faker",         "faker",       "__version__"))
resultados.append(check("tqdm",          "tqdm",        "__version__"))

# ── RESUMEN ───────────────────────────────────────────────────
total  = len(resultados)
ok     = sum(resultados)
fallos = total - ok

print()
print("═" * 60)
print(f"  RESUMEN: {ok}/{total} componentes OK")
if fallos == 0:
    print(f"  {OK}  ¡Entorno completamente configurado!")
    print(f"  Ya puedes empezar el curso Big Data.")
elif fallos <= 3:
    print(f"  {WARN} Hay {fallos} componente(s) con problemas.")
    print(f"  Revisa los errores arriba e instala lo que falta.")
else:
    print(f"  {FAIL}  Hay {fallos} componentes sin instalar.")
    print(f"  Ejecuta: pip install -r setup/requirements.txt")
print("═" * 60)
print()

# Info del sistema
print(f"{INFO} Sistema: {sys.platform}")
print(f"{INFO} Python:  {sys.executable}")
print(f"{INFO} Ruta:    {sys.path[0]}")
print()
