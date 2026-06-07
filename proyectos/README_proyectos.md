# 🚀 10 PROYECTOS INNOVADORES — Big Data DD283
## Universidad Autónoma del Perú | Semestre 2026-1

> **Cada grupo elige UN proyecto.** Los proyectos son de implementación real —
> se esperan datos reales, código funcional y resultados de negocio concretos.

---

## 📋 REGLAS GENERALES

- **Grupos**: 3-4 estudiantes (máximo)
- **Datos**: Deben ser reales o altamente realistas (no datos de Kaggle genéricos)
- **Código**: Todo en GitHub desde la Semana 1
- **Entregables**: EP (Semana 4) + EF (Semana 8)
- **Lenguaje principal**: Python + PySpark

---

## P1 — Sistema de Detección de Fraude Bancario en Tiempo Real

| Atributo | Detalle |
|---------|---------|
| **Sector** | Finanzas / Banca |
| **Empresa objetivo** | Yape, BCP, Interbank, o Fintech peruana |
| **Dificultad** | ⭐⭐⭐⭐ |

### El Problema
Las entidades financieras peruanas pierden millones de soles anualmente por fraude en transacciones digitales. El sistema actual tarda minutos en detectar transacciones fraudulentas, tiempo en el que el daño ya está hecho.

### Objetivo
Construir un pipeline Big Data que detecte transacciones fraudulentas en tiempo real (< 500ms por transacción) con una tasa de detección > 85% y < 5% de falsos positivos.

### Arquitectura propuesta
```
Transacciones → Kafka → Spark Streaming → Modelo ML → MongoDB (alertas) → Dashboard
```

### Stack tecnológico
- **Ingesta**: Apache Kafka (o simulación con Python)
- **Procesamiento**: PySpark Structured Streaming
- **Modelo ML**: PySpark MLlib (Random Forest / GBT)
- **Almacenamiento**: MongoDB Atlas
- **Visualización**: Power BI o Streamlit

### Dataset sugerido
- Generar con Faker + patrones de fraude reales
- Referencia: [Credit Card Fraud Detection (IEEE)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Enriquecer con variables peruanas (hora, geolocalización Lima, método de pago)

### Recursos GitHub
- https://github.com/gauravtayal0/Credit-Card-Fraud-Detection
- https://github.com/elastic/examples/tree/master/fraud-detection

### KPIs esperados del proyecto
- Precision > 85% en detección de fraude
- Recall > 80%
- Tiempo de respuesta < 500ms por transacción
- Dashboard con alertas en tiempo real

---

## P2 — Predicción de Churn en Telecomunicaciones

| Atributo | Detalle |
|---------|---------|
| **Sector** | Telecomunicaciones |
| **Empresa objetivo** | Claro Perú, Movistar, Entel |
| **Dificultad** | ⭐⭐⭐ |

### El Problema
Las empresas de telecom peruanas pierden clientes valiosos sin anticiparse a la baja. Adquirir un cliente nuevo cuesta 5-7x más que retener uno existente.

### Objetivo
Predecir con 30 días de anticipación qué clientes cancelarán su servicio, con suficiente precisión para que el equipo de retención actúe proactivamente.

### Dataset sugerido
- Generar con historial de llamadas, datos de uso, quejas, pagos tardíos
- Referencia: [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- Enriquecer con: zona geográfica peruana, tipo de contrato, ARPU

### Recursos GitHub
- https://github.com/dssg/telco-churn
- https://github.com/IBM/telco-customer-churn-on-icp4d

---

## P3 — Plataforma de Análisis de Sentimiento en Redes Sociales

| Atributo | Detalle |
|---------|---------|
| **Sector** | Marketing Digital / Retail |
| **Empresa objetivo** | InRetail, Falabella, o marca peruana |
| **Dificultad** | ⭐⭐⭐ |

### El Problema
Las marcas peruanas no tienen visibilidad en tiempo real sobre cómo habla la gente de ellas en redes sociales. Una crisis de reputación puede costar millones antes de ser detectada.

### Objetivo
Pipeline que scrape comentarios de Twitter/X, Facebook y Google Reviews sobre una marca peruana, los analice emocionalmente y genere alertas cuando el sentimiento se deteriora.

### Stack
- **Scraping**: Scrapy + BeautifulSoup + APIs sociales
- **Procesamiento**: PySpark + NLTK/SpaCy en español
- **Almacenamiento**: MongoDB (texto crudo + resultados)
- **Visualización**: Dashboard con Power BI

### Recursos GitHub
- https://github.com/cjhutto/vaderSentiment
- https://github.com/davebulaval/SpaCy-Spanish

---

## P4 — Motor de Recomendación para E-commerce Peruano

| Atributo | Detalle |
|---------|---------|
| **Sector** | Retail / E-commerce |
| **Empresa objetivo** | Falabella.pe, Ripley, Saga, MercadoLibre Perú |
| **Dificultad** | ⭐⭐⭐⭐ |

### El Problema
El 70% de los productos en e-commerce peruanos no son descubiertos por los clientes. Un motor de recomendación podría aumentar el ticket promedio 20-35%.

### Objetivo
Implementar un sistema de recomendación colaborativo y basado en contenido que sugiera productos relevantes a cada usuario.

### Algoritmos
- **ALS (Alternating Least Squares)** de PySpark MLlib para filtrado colaborativo
- **TF-IDF** para similitud de contenido
- **Híbrido**: combinar ambos

### Recursos GitHub
- https://github.com/recommenders-team/recommenders (Microsoft)
- https://github.com/benfred/implicit

---

## P5 — Predicción de Demanda Hospitalaria (EsSalud)

| Atributo | Detalle |
|---------|---------|
| **Sector** | Salud Pública |
| **Empresa objetivo** | EsSalud, MINSA, Clínicas privadas |
| **Dificultad** | ⭐⭐⭐ |

### El Problema
Los hospitales peruanos tienen problemas crónicos de gestión de camas, especialmente en temporadas de gripe y dengue. EsSalud tiene datos históricos pero no los usa predictivamente.

### Objetivo
Predecir la demanda de camas por especialidad con 7 días de anticipación, para optimizar la asignación de recursos médicos.

### Dataset
- Datos sintéticos basados en estadísticas reales del MINSA
- SUSALUD publica estadísticas en data.gob.pe
- Datos climáticos (correlación dengue-temperatura)

### Recursos GitHub
- https://github.com/drivendataorg/flu-shot-learning
- https://data.gob.pe/ (datos abiertos MINSA)

---

## P6 — Detección de Evasión Fiscal con Big Data (SUNAT)

| Atributo | Detalle |
|---------|---------|
| **Sector** | Gobierno / Finanzas Públicas |
| **Empresa objetivo** | SUNAT |
| **Dificultad** | ⭐⭐⭐⭐⭐ |

### El Problema
La evasión tributaria en Perú alcanza el 35-40% del IGV. SUNAT tiene datos de declaraciones juradas pero no los cruza eficientemente para detectar inconsistencias.

### Objetivo
Modelo que detecte contribuyentes con alta probabilidad de evasión cruzando: ingresos declarados vs. movimientos bancarios vs. patrimonio visible vs. gasto social.

### Consideración Ética
⚠️ Este proyecto debe incluir un análisis ético detallado:
privacidad de datos, sesgos del modelo, y cumplimiento de la Ley 29733.

### Dataset
- Datos sintéticos que simulen declaraciones de IGV e IR
- Datos públicos del BCRP sobre recaudación
- Datos catastrales de COFOPRI (disponibles en data.gob.pe)

---

## P7 — Análisis de Tráfico Urbano Lima con Datos GPS

| Atributo | Detalle |
|---------|---------|
| **Sector** | Smart City / Transporte |
| **Empresa objetivo** | MTC, Municipalidad Lima, Uber, InDrive |
| **Dificultad** | ⭐⭐⭐ |

### El Problema
Lima es la 5ta ciudad más congestionada de Latinoamérica. Los datos de tráfico existen (GPS de taxis, app de tráfico) pero no se procesan para optimización.

### Objetivo
Analizar patrones de tráfico en Lima usando datos GPS, predecir congestión con 30 minutos de anticipación y sugerir rutas alternativas.

### Dataset
- Datos GPS sintéticos de 50,000 vehículos en Lima
- OpenStreetMap para el grafo de calles
- Datos de lluvia SENAMHI (correlación tráfico-clima)

### Recursos GitHub
- https://github.com/gboeing/osmnx (OpenStreetMap para Python)
- https://github.com/pgrosse/spark-traffic

---

## P8 — Plataforma de Análisis de Calidad Ambiental IoT

| Atributo | Detalle |
|---------|---------|
| **Sector** | Medio Ambiente / IoT |
| **Empresa objetivo** | MINAM, OEFA, Municipalidades |
| **Dificultad** | ⭐⭐⭐ |

### El Problema
Lima tiene niveles de contaminación del aire que superan estándares OMS. Los datos de calidad existen (sensores IoT) pero no se procesan en tiempo real para alertas ciudadanas.

### Objetivo
Pipeline de datos IoT que ingesta lecturas de sensores de calidad de aire en tiempo real, detecta anomalías y genera alertas para ciudadanos y autoridades.

### Stack
- **Simulación IoT**: Python generando lecturas de sensores
- **Ingesta streaming**: Apache Kafka
- **Procesamiento**: PySpark Streaming
- **Alertas**: MongoDB + API REST

### Dataset
- Datos reales del SENAMHI/DIGESA en data.gob.pe
- Simular red de 100 sensores en Lima Metropolitana

---

## P9 — Sistema de Crédito Alternativo para Microempresas

| Atributo | Detalle |
|---------|---------|
| **Sector** | Fintech / Inclusión Financiera |
| **Empresa objetivo** | MiBanco, CrediScotia, Fintech startups |
| **Dificultad** | ⭐⭐⭐⭐ |

### El Problema
El 70% de las microempresas en Perú no tienen acceso al sistema financiero formal porque no tienen historial crediticio. Las fintechs usan datos alternativos pero no a escala.

### Objetivo
Modelo de credit scoring alternativo que use datos no-tradicionales (historial de pagos de servicios, comportamiento móvil, datos sociales) para evaluar la solvencia de microempresarios.

### Consideración Ética
⚠️ Análisis obligatorio de sesgo algorítmico:
¿El modelo discrimina por género, zona geográfica o etnia?

### Dataset
- Datos sintéticos de 500,000 microempresarios con historial alternativo
- Incluir variables: pagos de Yape/Plin, uso de apps bancarias, historial Sunat

### Recursos GitHub
- https://github.com/dssg/early_warning_system
- https://github.com/ml-for-good/financial-inclusion

---

## P10 — Análisis de Deserción Estudiantil Universitaria

| Atributo | Detalle |
|---------|---------|
| **Sector** | Educación / EdTech |
| **Empresa objetivo** | Universidad Autónoma del Perú (u otra) |
| **Dificultad** | ⭐⭐⭐ |

### El Problema
Las universidades peruanas tienen tasas de deserción del 30-40%. La deserción se detecta cuando ya es demasiado tarde — cuando el estudiante ya dejó de asistir.

### Objetivo
Sistema de alerta temprana que prediga qué estudiantes tienen riesgo de desertar con 4 semanas de anticipación, para que la universidad intervenga proactivamente.

### Dataset
- Datos sintéticos de 10,000 estudiantes: asistencia, notas, pagos, actividad en campus virtual
- Variables críticas: irregularidad en pagos, baja actividad en plataforma, notas en descenso

### Recursos GitHub
- https://github.com/dssg/student-intervention
- https://github.com/learning-analytics-group/dropout-prediction

---

## 📁 TEMPLATE DEL PROYECTO

Todos los grupos deben estructurar su repositorio así:

```
tu-proyecto-bigdata/
├── README.md              ← Descripción, problema, objetivos, arquitectura
├── notebooks/
│   ├── 01_exploracion.ipynb    ← EDA inicial
│   ├── 02_procesamiento.ipynb  ← ETL con Spark
│   ├── 03_modelo.ipynb         ← ML / análisis
│   └── 04_visualizacion.ipynb  ← Dashboard
├── data/
│   ├── raw/               ← Datos crudos (o links a datos)
│   └── processed/         ← Datos limpios
├── src/
│   ├── ingesta.py         ← Pipeline de ingesta
│   ├── transformacion.py  ← Transformaciones Spark
│   └── modelo.py          ← Código del modelo ML
├── docs/
│   ├── arquitectura.drawio ← Diagrama de arquitectura
│   └── presentacion_ep.pdf ← Slides semana 4
└── requirements.txt
```

Ver template completo en [proyectos/template_proyecto/](./template_proyecto/)

---

*Universidad Autónoma del Perú | Big Data DD283 | 2026-1*
