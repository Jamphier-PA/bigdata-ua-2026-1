# 🐙 GUÍA COMPLETA DE GITHUB — Big Data DD283
## Paso a Paso: Docente + Estudiantes

---

# PARTE 1 — EL DOCENTE CREA EL REPOSITORIO BASE

## Paso 1: Crear la cuenta y el repositorio en GitHub

```bash
# 1. Ir a github.com → Sign Up (si no tienes cuenta)
# 2. Crear repositorio:
#    - Name: bigdata-ua-2026-1
#    - Description: "Curso Big Data DD283 - Universidad Autónoma del Perú - 2026-1"
#    - Visibility: PUBLIC (para que estudiantes puedan verlo sin login)
#    - ✅ Add README
#    - ✅ Add .gitignore → Python
#    - License: MIT
```

## Paso 2: Clonar y subir todos los archivos preparados

```bash
# En tu laptop (docente):
git clone https://github.com/TU_USUARIO_DOCENTE/bigdata-ua-2026-1.git
cd bigdata-ua-2026-1

# Copiar todos los archivos de este repositorio preparado:
# (ya tienes la estructura lista en tu Google Drive)
cp -r /ruta/a/GitHub_Repo/bigdata-ua-2026-1/* .

# Subir al repositorio:
git add .
git commit -m "chore: estructura inicial del curso Big Data 2026-1"
git push origin main

# ✅ Verificar que todo subió en: github.com/TU_USUARIO/bigdata-ua-2026-1
```

## Paso 3: Configurar protección de la rama main

```
GitHub → Repositorio → Settings → Branches → Add rule
  - Branch name pattern: main
  - ✅ Require a pull request before merging
  - ✅ Require review from Code Owners
  - ✅ Do not allow bypassing the above settings
→ Guardar
```

> **¿Por qué?** Esto impide que los estudiantes committeen directamente a main.
> Deben hacer PR, y tú revisas antes de mergear.

## Paso 4: Crear GitHub Classroom (OPCIONAL pero recomendado)

```
1. Ir a: classroom.github.com
2. New classroom → Link to this organization
3. New assignment:
   - Title: "Big Data 2026-1 — Semana {N}"
   - Repository visibility: Private (cada estudiante tiene su repo)
   - Template repository: bigdata-ua-2026-1
   - Enable feedback pull requests: ✅
4. Copiar el link de invitación → compartir con estudiantes
```

> **Con GitHub Classroom**: Cada estudiante obtiene automáticamente una copia
> del repositorio template en su cuenta. Tú puedes ver todos los repos desde
> el dashboard de Classroom.

---

# PARTE 2 — LOS ESTUDIANTES CONFIGURAN SU REPOSITORIO

GUIA DEFINITIVA — Estudiantes (paso a paso completo)
FASE 1: Configuración inicial (solo UNA VEZ en todo el semestre)
En la web — github.com:


1. Ir a: github.com/RubenCarty/bigdata-ua-2026-1
2. Clic en el botón "Fork" (arriba a la derecha)
3. Clic "Create fork"
   → Ahora tienen su propia copia: github.com/SU-USUARIO/bigdata-ua-2026-1
En su laptop — Terminal:


# Paso 1: Clonar SU fork a su laptop
git clone https://github.com/SU-USUARIO/bigdata-ua-2026-1.git
# ¿Para qué? Descarga todos los archivos del repo a su computadora

# Paso 2: Entrar a la carpeta
cd bigdata-ua-2026-1
# ¿Para qué? Posicionarse dentro del repo para que Git funcione

# Paso 3: Conectar con el repo del DOCENTE
git remote add upstream https://github.com/RubenCarty/bigdata-ua-2026-1.git
# ¿Para qué? Crear un "canal" para recibir actualizaciones del docente cada semana

# Paso 4: Verificar que quedó bien
git remote -v
# Debe mostrar:
# origin   → su fork (donde ellos suben sus tareas)
# upstream → repo del docente (de donde descargan materiales nuevos)

# Paso 5: Configurar su identidad
git config user.name "Juan Perez"
git config user.email "juan.perez@gmail.com"
FASE 2: Inicio de cada semana (descargar material nuevo del docente)

# Volver a la rama principal
git checkout main
# ¿Para qué? Asegurarse de estar en la base antes de sincronizar

# Descargar los materiales nuevos del docente
git pull upstream main
# ¿Para qué? Traer a su laptop todo lo que el docente publicó
# (guías de trabajo, labs, slides de la semana)

# Actualizar también su fork en GitHub
git push origin main
# ¿Para qué? Su copia en GitHub también queda actualizada
FASE 3: Trabajar y entregar la tarea

# Crear su rama personal para la semana
git checkout -b semana-01-lopez-maria
# ¿Para qué? Crear una "línea de trabajo" solo para ellos
# FORMATO: semana-NN-apellido-nombre (sin espacios, sin tildes)
# NUNCA trabajar directamente en main

# --- Aquí el estudiante trabaja ---
# Abre Jupyter, completa el lab, responde las preguntas teóricas
# Guarda sus archivos con el formato correcto:
#   semana_01/Solucion_S1/lopez_maria/GUIA_TRABAJO_S1_lopez.md
#   semana_01/Solucion_S1/lopez_maria/LABORATORIO_S1_lopez.ipynb

# Ver qué archivos modificó
git status

# Agregar sus archivos de solución
git add semana_01/Solucion_S1/lopez_maria/
# ¿Para qué? Preparar SOLO sus archivos (no tocar los de otros)

# Guardar con mensaje claro
git commit -m "[S01] entrego guia de trabajo y lab completado - Lopez Maria"
# ¿Para qué? Registrar en el historial que entregó su tarea

# Subir su rama a GitHub (a su fork)
git push origin semana-01-lopez-maria
# ¿Para qué? Sus archivos ahora están en internet, en su fork personal
FASE 4: Crear el Pull Request (la "entrega oficial")

1. Ir a: github.com/SU-USUARIO/bigdata-ua-2026-1
2. Aparece banner amarillo: "Compare & pull request" → clic
3. Verificar que dice:
   base repository: RubenCarty/bigdata-ua-2026-1   base: main    ← repo del docente
   head repository: SU-USUARIO/bigdata-ua-2026-1   compare: semana-01-lopez-maria
4. Completar el formulario automático:
   - Nombre completo
   - Semana entregada
   - Qué aprendió
   - Conexión con su trabajo actual
5. Clic "Create pull request"

FASE 5: Docente revisa y apruebas 

github.com/RubenCarty/bigdata-ua-2026-1 → Pull requests
Acción	Cómo
Ver la tarea	Tab "Files changed"
Comentar líneas	Clic en el "+" de cada línea
Aprobar	"Review changes" → Approve
Pedir corrección	"Review changes" → Request changes
Hacer merge (aprobar entrega final)	"Merge pull request"
Resumen visual del flujo completo

                    
---

# PARTE 3 — FLUJO SEMANAL (repetir cada semana)

## CADA SEMANA — Flujo de trabajo

```
┌────────────────────────────────────────────────────────────┐
│                 FLUJO SEMANAL DE TRABAJO                    │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  1. SINCRONIZAR con el docente                             │
│     git pull upstream main                                  │
│                                                            │
│  2. CREAR RAMA para esta semana                            │
│     git checkout -b semana-N-tu-nombre                      │
│                                                            │
│  3. TRABAJAR en el laboratorio                             │
│     (editar notebooks, ejecutar código)                     │
│                                                            │
│  4. GUARDAR AVANCE (cada vez que terminas algo)            │
│     git add .                                              │
│     git commit -m "[S0N] descripción - Tu Nombre"          │
│                                                            │
│  5. SUBIR al repositorio en GitHub                         │
│     git push origin semana-N-tu-nombre                      │
│                                                            │
│  6. CREAR PULL REQUEST en GitHub                           │
│     (GitHub detecta la rama y sugiere crear PR)            │
│                                                            │
│  7. ESPERAR FEEDBACK del docente                           │
│     (el docente deja comentarios en el PR)                  │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## PASO A PASO DETALLADO — Semana 1 (Lab S1)

### Paso 1: Sincronizar con el repositorio del docente

```bash
# ¡Siempre hacer esto PRIMERO al comenzar una nueva semana!
git checkout main              # Asegurarte de estar en main
git pull upstream main         # Traer cambios del docente
git push origin main           # Actualizar tu fork en GitHub

echo "✅ Repo sincronizado con los materiales del docente"
```

### Paso 2: Crear tu rama para la semana

```bash
# Nomenclatura: semana-N-apellido (sin acentos, sin espacios)
git checkout -b semana-01-quispe

# Verificar que estás en la nueva rama
git branch
# Debe mostrar: * semana-01-quispe
```

### Paso 3: Trabajar en el laboratorio

```bash
# Abrir Jupyter Lab
jupyter lab

# O abrir el notebook directamente
jupyter notebook semana_01/notebooks/lab_s1_estudiante.ipynb

# Trabajar en el notebook:
# - Ejecutar todas las celdas (Shift+Enter)
# - Completar donde dice "📝 TU CÓDIGO AQUÍ"
# - Escribir la reflexión final
# - Guardar el notebook con outputs
```

### Paso 4: Hacer commits mientras trabajas

```bash
# Guardar progreso después de cada parte completada:

# Después de terminar Parte 1:
git add semana_01/notebooks/lab_s1_estudiante.ipynb
git commit -m "[S01] Parte 1 completada: análisis datos estructurados - Quispe"

# Después de terminar el lab completo:
git add .
git commit -m "[S01] Lab S1 completo: tipos de datos + arquitectura - Quispe"

# Ver historial de commits
git log --oneline
```

### Paso 5: Subir a GitHub

```bash
git push origin semana-01-quispe
```

### Paso 6: Crear el Pull Request

```
1. Ir a: github.com/TU_USUARIO/bigdata-ua-2026-1
2. GitHub muestra un banner: "semana-01-quispe had recent pushes"
3. Clic en "Compare & pull request"
4. Completar el formulario:
   
   Title: [S01] Lab Semana 1 - Juan Quispe
   
   Base repository: [DOCENTE]/bigdata-ua-2026-1  ← hacia el docente
   Base: main
   Head repository: TU_USUARIO/bigdata-ua-2026-1
   Compare: semana-01-quispe
   
5. Completar el template del PR:
   - Nombre completo
   - Grupo de proyecto
   - ✅ Checklist de entregables
   - Reflexión sobre qué aprendí
   
6. Clic: "Create Pull Request"
7. Copiar el link del PR y compartirlo con el docente
```

---

## SEMANA 2 en adelante — Flujo simplificado

```bash
# Al inicio de cada semana:
git checkout main
git pull upstream main          # Sincronizar materiales del docente
git push origin main
git checkout -b semana-02-quispe

# Trabajar...

# Al finalizar:
git add .
git commit -m "[S02] Lab S2: WordCount PySpark + Hadoop - Quispe"
git push origin semana-02-quispe
# Crear PR en GitHub
```

---

# PARTE 4 — EL DOCENTE REVISA LOS PULL REQUESTS

## Cómo revisar un PR de estudiante

```
1. Ir a: github.com/TU_USUARIO/bigdata-ua-2026-1 → Pull Requests
2. Seleccionar el PR del estudiante
3. Tab "Files changed" → ver todos los cambios
4. Dejar comentarios inline:
   - Clic en el "+" al lado de una línea
   - Escribir el feedback específico
5. Tab "Review changes":
   - Comment: feedback sin aprobar/rechazar
   - Approve: trabajo correcto ✅
   - Request changes: hay que corregir ❌
```

## Tipos de comentarios de feedback

```markdown
# Feedback positivo:
✅ Excelente análisis! Las 5 V's están bien identificadas para tu proyecto.

# Feedback de mejora:
⚠️ La reflexión es muy corta. Necesito ver la conexión con tu empresa actual.
Por favor expande la celda de reflexión con al menos 3 oraciones por pregunta.

# Feedback técnico:
💡 Hay una forma más eficiente de hacer este cálculo con Pandas:
   df.groupby('categoria')['monto'].agg(['sum', 'mean', 'count'])
   Esto es más Pythónico que el loop que usaste.

# Error crítico:
❌ Tu notebook tiene errores de ejecución en las celdas 7 y 8.
   Necesito ver el notebook ejecutado completamente antes de dar feedback.
   Por favor corrige y pushea de nuevo.
```

---

# PARTE 5 — PROYECTO GRUPAL EN GITHUB

## Crear el repositorio del proyecto del grupo

```bash
# El líder del grupo crea un NUEVO repositorio:
# github.com → New repository
# Name: bigdata-ua-2026-1-[nombre-proyecto]
# Description: "Proyecto Big Data: [descripción]"
# Visibility: Public
# ✅ Add README

# Invitar a los compañeros como colaboradores:
# Settings → Collaborators → Add people → (username de cada integrante)
```

## Estructura del repo del proyecto

```
tu-proyecto-bigdata/
├── README.md                    ← OBLIGATORIO: descripción completa
│   ├── Problema
│   ├── Objetivo
│   ├── Arquitectura (imagen)
│   ├── Stack tecnológico
│   ├── Cómo ejecutar
│   └── Integrantes
├── notebooks/
│   ├── 01_exploracion_EDA.ipynb      ← Semana 1-2
│   ├── 02_pipeline_hadoop.ipynb      ← Semana 2-3
│   ├── 03_nosql_mongodb.ipynb        ← Semana 3-4
│   ├── 04_spark_processing.ipynb     ← Semana 5
│   ├── 05_ml_modelo.ipynb            ← Semana 6
│   ├── 06_scraping_datos.ipynb       ← Semana 7
│   └── 07_dashboard_final.ipynb      ← Semana 8
├── src/
│   ├── pipeline_ingesta.py
│   ├── transformaciones.py
│   └── modelo_ml.py
├── data/
│   ├── README_datos.md              ← Explicación de los datos (no subir datos grandes)
│   └── sample/                      ← Solo muestra pequeña (< 5MB)
├── docs/
│   ├── arquitectura.drawio
│   ├── presentacion_ep_semana4.pdf
│   └── presentacion_ef_semana8.pdf
├── .gitignore
└── requirements.txt
```

## Flujo de trabajo del grupo

```bash
# Cada integrante trabaja en su propia rama:
git checkout -b feature/modelo-ml-quispe
git checkout -b feature/pipeline-ingesta-torres
git checkout -b feature/dashboard-mamani

# Cuando terminas tu parte → PR al repo del proyecto:
git push origin feature/modelo-ml-quispe
# Crear PR → otro integrante revisa → merge

# El líder es responsable de:
# - Revisar y mergear los PRs del equipo
# - Mantener el README actualizado
# - Crear las releases para las sustentaciones
```

---

# PARTE 6 — COMANDOS GIT ESENCIALES

## Comandos que usarás todos los días

```bash
# ── Ver estado del repositorio ────────────────────────────────
git status                      # ¿Qué cambié?
git diff                        # ¿Qué líneas cambié exactamente?
git log --oneline               # Historial de commits

# ── Ramas ────────────────────────────────────────────────────
git branch                      # Ver todas las ramas
git checkout -b nueva-rama      # Crear y cambiar a nueva rama
git checkout main               # Volver a main
git branch -d rama-vieja        # Borrar rama local ya mergeada

# ── Guardar cambios ───────────────────────────────────────────
git add archivo.ipynb           # Agregar archivo específico
git add .                       # Agregar todos los cambios
git commit -m "mensaje"         # Guardar con mensaje
git push origin mi-rama         # Subir a GitHub

# ── Sincronizar ───────────────────────────────────────────────
git pull upstream main          # Traer cambios del docente
git fetch upstream              # Solo ver cambios (sin aplicar)

# ── Deshacer ─────────────────────────────────────────────────
git restore archivo.py          # Deshacer cambios en un archivo (NO committed)
git revert HEAD                 # Deshacer el último commit (SAFE)
# NUNCA usar: git reset --hard (borra trabajo sin aviso)
```

## Solución de problemas comunes

### Problema: "Your branch is behind"
```bash
git pull upstream main
git push origin main
```

### Problema: Merge conflict
```bash
# Git marca los conflictos en el archivo:
# <<<<<<< HEAD
# Tu versión
# =======
# Versión del repo original
# >>>>>>> upstream/main

# Editar el archivo manualmente, elegir qué conservar
# Luego:
git add archivo_con_conflicto.py
git commit -m "fix: resolver conflicto en archivo"
```

### Problema: "Nothing to commit"
```bash
# Verificar que guardaste el notebook:
# Jupyter → File → Save (Ctrl+S)
# Luego:
git status   # debe mostrar los archivos modificados
```

### Problema: Subí información sensible (contraseña, API key)
```bash
# URGENTE: notificar al docente y:
# 1. Cambiar la contraseña/key inmediatamente
# 2. Agregar al .gitignore
# 3. Hacer commit del .gitignore
# NUNCA dejar credenciales en el repo
```

---

# PARTE 7 — CONVENCIONES Y ESTÁNDARES

## Nombres de ramas
```
semana-01-apellido          ← Lab semanal individual
feature/nombre-feature      ← Feature del proyecto grupal
fix/descripcion-bug         ← Corrección de errores
hotfix/nombre               ← Corrección urgente
```

## Mensajes de commit
```
Formato: [TIPO][SEMANA] descripción breve - Apellido

Tipos:
  [S01]  → Lab de la semana
  feat   → Nueva funcionalidad
  fix    → Corrección de error
  docs   → Documentación
  style  → Formato (no lógica)
  chore  → Mantenimiento

Ejemplos correctos:
  [S01] análisis tipos de datos completado - Quispe
  [S03] feat: implementar CRUD MongoDB con índices - Torres
  [S06] fix: corregir desbalance de clases en modelo ML - Mamani
  docs: actualizar README con instrucciones de instalación

Ejemplos INCORRECTOS:
  cambios                    ← demasiado vago
  TRABAJO SEMANA 3           ← sin formato
  fix                        ← qué fijaste?
  asdfjkl                    ← no describe nada
```

## Estructura de un notebook profesional
```python
# ── Celda 1: Encabezado Markdown ──────────────────────────────
"""
# Título del Notebook
## Semana N — Tema
### Nombre | Fecha | Proyecto
"""

# ── Celda 2: Imports ──────────────────────────────────────────
import pandas as pd
# ... todos los imports juntos al inicio

# ── Celda 3-N: Código por secciones ───────────────────────────
# Cada sección con título Markdown explicando QUÉ y POR QUÉ

# ── Última celda: Reflexión Markdown ──────────────────────────
"""
## Reflexión
...
"""
```

---

# RESUMEN VISUAL — Una página para imprimir

```
╔══════════════════════════════════════════════════════════════╗
║           FLUJO GIT SEMANAL — BIG DATA DD283                 ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  INICIO DE SEMANA:                                           ║
║  $ git checkout main                                         ║
║  $ git pull upstream main        ← actualizar del docente    ║
║  $ git checkout -b semana-N-tu-apellido  ← crear tu rama     ║
║                                                              ║
║  MIENTRAS TRABAJAS (hacer frecuentemente):                   ║
║  $ git add .                                                 ║
║  $ git commit -m "[S0N] lo que hiciste - Apellido"           ║
║                                                              ║
║  AL TERMINAR EL LAB:                                         ║
║  $ git push origin semana-N-tu-apellido                      ║
║  → Abrir github.com → "Compare & pull request"               ║
║  → Completar el formulario del PR                            ║
║  → Compartir el link con el docente                          ║
║                                                              ║
║  EL DOCENTE REVISA Y DA FEEDBACK EN EL PR                    ║
║  → Leer los comentarios                                      ║
║  → Corregir si pide cambios → git push (el PR se actualiza)  ║
║  → El docente mergea cuando está OK ✅                        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

*Universidad Autónoma del Perú | Big Data DD283 | 2026-1*  
*Cualquier duda: abrir un Issue en el repositorio del curso*
