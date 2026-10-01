# Fase 2 — Python Científico: Análisis Exploratorio de Datos

## Descripción

Proyecto de **Análisis Exploratorio de Datos (EDA)** realizado sobre el dataset **Online Shoppers Purchasing Intention**, con el objetivo de explorar el comportamiento de las sesiones de navegación de usuarios en un sitio web de comercio electrónico y su relación descriptiva con la realización de una compra.

El análisis se desarrolló utilizando principalmente **Pandas, Matplotlib y Seaborn**, trabajando con variables numéricas y categóricas por separado.

> **Importante:** este proyecto realiza análisis descriptivo y exploratorio. Las asociaciones observadas entre variables y `Revenue` no deben interpretarse como relaciones causales.

---

## Dataset

El dataset utilizado es **Online Shoppers Purchasing Intention Dataset**, publicado por la **UCI Machine Learning Repository**.

El conjunto contiene:

* **12.330 sesiones**
* **18 variables**
* Variables numéricas, categóricas y booleanas
* Variable objetivo descriptiva: `Revenue`

Cada fila representa una **sesión de navegación**, no necesariamente un usuario único.

### Variables principales

#### Variables numéricas

* `Administrative`
* `Administrative_Duration`
* `Informational`
* `Informational_Duration`
* `ProductRelated`
* `ProductRelated_Duration`
* `BounceRates`
* `ExitRates`
* `PageValues`
* `SpecialDay`

#### Variables categóricas

* `Month`
* `OperatingSystems`
* `Browser`
* `Region`
* `TrafficType`
* `VisitorType`
* `Weekend`
* `Revenue`

Algunas variables almacenadas como números enteros, como `OperatingSystems`, `Browser`, `Region` y `TrafficType`, fueron tratadas como **códigos categóricos**, no como magnitudes cuantitativas.

---

# 1. Preparación e inspección inicial

Se realizó una inspección inicial del DataFrame utilizando Pandas para conocer:

* Dimensiones del dataset.
* Tipos de datos.
* Nombres de las columnas.
* Primeras observaciones.
* Valores nulos.
* Registros duplicados.

El dataset contiene **12.330 filas y 18 columnas** y no presenta valores nulos.

También se identificaron:

* **125 duplicados adicionales** mediante `df.duplicated().sum()`.
* **201 filas pertenecientes a grupos de registros repetidos**.
* **76 combinaciones completas de filas repetidas**.

Los duplicados no fueron eliminados automáticamente. Debido a que el dataset no contiene un identificador de sesión que permita determinar si dos filas idénticas representan necesariamente un error, se decidió conservarlos y documentar su existencia.

Un dato adicional observado fue que las **201 filas pertenecientes a grupos repetidos tenían `Revenue=False`**.

---

# 2. Análisis de variables numéricas

Para las variables numéricas se desarrolló una función general de análisis que permitió obtener:

* Mínimo.
* Máximo.
* Media.
* Mediana.
* Frecuencia de valores.
* Cuartiles.
* Rango intercuartílico (IQR).
* Límites inferior y superior para detectar posibles outliers.
* Cantidad y porcentaje de observaciones potencialmente atípicas.

La identificación de outliers se realizó mediante el criterio:

**Límite superior = Q3 + 1,5 × IQR**

Estos valores se consideran **posibles outliers estadísticos**, no necesariamente errores de los datos.

---

## 2.1 Administrative

Resultados principales:

* Mínimo: `0`
* Máximo: `27`
* Media: aproximadamente `2,32`
* Mediana: `1`
* Q1: `0`
* Q3: `4`
* IQR: `4`
* Límite superior: `10`
* Posibles outliers: `404`
* Porcentaje: aproximadamente `3,28 %`

La variable presenta concentración de valores bajos y asimetría hacia la derecha.

Al dividir las sesiones según sus cuantiles se observó una tasa de compra de aproximadamente:

* Grupo bajo: `8,91 %`
* Grupo medio: `19,84 %`
* Grupo alto: `23,65 %`

En este dataset, las sesiones con mayor cantidad de páginas administrativas presentan una mayor tasa observada de compra.

---

## 2.2 Administrative_Duration

Resultados principales:

* Mínimo: `0`
* Máximo: `3398,75` segundos
* Media: aproximadamente `80,82` segundos
* Mediana: `7,5` segundos
* Q1: `0`
* Q3: `93,26` segundos
* Límite superior: aproximadamente `233,14` segundos
* Posibles outliers: `1172`
* Porcentaje: aproximadamente `9,51 %`

La diferencia entre media y mediana evidencia una distribución fuertemente sesgada hacia valores altos.

Tasa de compra por grupos:

* Bajo: `9,28 %`
* Medio: `20,36 %`
* Alto: `22,02 %`

El comportamiento observado es similar al de `Administrative`.

---

## 2.3 Informational

Resultados principales:

* Mínimo: `0`
* Máximo: `24`
* Media: aproximadamente `0,50`
* Mediana: `0`
* Q1: `0`
* Q2: `0`
* Q3: `0`

Debido a que los tres cuartiles son `0`, el IQR también es `0`. Por este motivo, utilizar el criterio tradicional de outliers produce que prácticamente todos los valores positivos sean considerados atípicos.

En este caso, la clasificación mediante IQR no resulta especialmente informativa.

Se realizó una comparación más adecuada:

* `Informational = 0`: tasa de compra ≈ `13,35 %`
* `Informational > 0`: tasa de compra ≈ `23,30 %`

La diferencia observada es de aproximadamente **9,95 puntos porcentuales**.

---

## 2.4 Informational_Duration

Resultados principales:

* Mínimo: `0`
* Máximo: `2549,38` segundos
* Media: aproximadamente `34,47` segundos
* Mediana: `0`
* Q1: `0`
* Q2: `0`
* Q3: `0`

Al igual que `Informational`, la concentración de valores en `0` hace que el método del IQR resulte poco útil.

Se compararon las sesiones con y sin duración informativa:

* `Informational_Duration = 0`: tasa de compra ≈ `13,05 %`
* `Informational_Duration > 0`: tasa de compra ≈ `23,49 %`

La diferencia descriptiva es de aproximadamente **10,44 puntos porcentuales**.

---

## 2.5 ProductRelated

Resultados principales:

* Mínimo: `0`
* Máximo: `705`
* Media: aproximadamente `31,73`
* Mediana: `18`
* Q1: `7`
* Q3: `38`
* IQR: `31`
* Límite superior: `84,5`
* Posibles outliers: `987`
* Porcentaje: aproximadamente `8,00 %`

La distribución presenta asimetría positiva.

Tasa de compra por grupos:

* Bajo (`≤ 7`): `5,10 %`
* Medio (`8–38`): `16,79 %`
* Alto (`> 38`): `23,63 %`

La diferencia descriptiva entre el grupo alto y el bajo es de aproximadamente **18,53 puntos porcentuales**.

---

## 2.6 ProductRelated_Duration

Resultados principales:

* Mínimo: `0`
* Máximo: aproximadamente `63.973,52` segundos
* Media: aproximadamente `1.194,75` segundos
* Mediana: aproximadamente `598,94` segundos
* Q1: aproximadamente `184,14` segundos
* Q3: aproximadamente `1.464,16` segundos
* IQR: aproximadamente `1.280,02`
* Límite superior: aproximadamente `3.384,19` segundos
* Posibles outliers: `961`
* Porcentaje: aproximadamente `7,79 %`

La distribución presenta una cola derecha pronunciada.

Tasa de compra:

* Grupo bajo: `4,64 %`
* Grupo medio: `16,79 %`
* Grupo alto: `23,68 %`

Se observa una diferencia descriptiva considerable entre las sesiones con menor y mayor duración relacionada con productos.

---

## 2.7 BounceRates

Resultados principales:

* Mínimo: `0`
* Máximo: `0,2`
* Media: aproximadamente `0,0222`
* Mediana: aproximadamente `0,0031`
* Q1: `0`
* Q3: aproximadamente `0,0168`
* Límite superior: aproximadamente `0,0420`
* Posibles outliers: `1551`
* Porcentaje: aproximadamente `12,58 %`

La diferencia entre media y mediana evidencia una distribución asimétrica.

Los valores considerados outliers mediante IQR no fueron interpretados automáticamente como errores, ya que representan sesiones estadísticamente poco frecuentes, pero posibles dentro del comportamiento del sitio web.

---

## 2.8 ExitRates

Resultados principales:

* Mínimo: `0`
* Máximo: `0,2`
* Q1: aproximadamente `0,0143`
* Q3: `0,05`
* IQR: aproximadamente `0,0357`
* Límite superior: aproximadamente `0,1036`
* Posibles outliers: `1099`
* Porcentaje: aproximadamente `8,91 %`

Los outliers fueron revisados adicionalmente utilizando `Revenue`, `VisitorType` y otras variables.

De las 1.099 sesiones clasificadas como posibles outliers:

* `1093` no terminaron en compra.
* `6` terminaron en compra.

No se encontró evidencia suficiente para considerar estos registros errores y se conservaron.

---

## 2.9 PageValues

`PageValues` presentó uno de los comportamientos más particulares del dataset:

* Mínimo: `0`
* Máximo: aproximadamente `361,76`
* Media: aproximadamente `5,89`
* Mediana: `0`
* Aproximadamente `9.600` sesiones tienen valor `0`.

La variable presenta una fuerte concentración en cero y una cola derecha.

Debido a que sus cuartiles centrales se encuentran en `0`, el análisis mediante grupos de cuantiles no resulta adecuado.

Se realizó una comparación entre:

* `PageValues = 0`
* `PageValues > 0`

Resultados:

* `PageValues = 0`: tasa de compra ≈ `3,85 %`
* `PageValues > 0`: tasa de compra ≈ `56,34 %`

Esta es una de las asociaciones descriptivas más marcadas encontradas durante el análisis.

---

## 2.10 SpecialDay

Resultados principales:

* Mínimo: `0`
* Máximo: `1`
* Media: aproximadamente `0,0614`
* Mediana: `0`
* Q1: `0`
* Q2: `0`
* Q3: `0`

La gran concentración de valores en `0` hace que el IQR sea `0`.

Por ello se compararon directamente las sesiones con `SpecialDay = 0` frente a aquellas con `SpecialDay > 0`.

Resultados:

* `SpecialDay = 0`: tasa de compra ≈ `16,53 %`
* `SpecialDay > 0`: tasa de compra ≈ `6,16 %`

La diferencia descriptiva es de aproximadamente **10,37 puntos porcentuales**.

---

# 3. Análisis de variables categóricas

Se desarrolló una función para analizar cada variable categórica de forma uniforme.

Para cada categoría se obtuvieron:

* Número de sesiones.
* Porcentaje respecto al dataset.
* Número de compras.
* Tasa observada de compra.
* Tasa observada de no compra.

Para evitar valores `NaN` cuando una categoría no aparecía entre las sesiones con `Revenue=True`, se utilizó `reindex(..., fill_value=0)`.

---

## 3.1 VisitorType

Distribución:

* `Returning_Visitor`: 10.551 sesiones
* `New_Visitor`: 1.694 sesiones
* `Other`: 85 sesiones

Tasa observada de compra:

* `Returning_Visitor`: `13,93 %`
* `New_Visitor`: `24,91 %`
* `Other`: `18,82 %`

`Other` representa una cantidad pequeña de observaciones, por lo que su porcentaje debe interpretarse con precaución.

---

## 3.2 Month

La cantidad de sesiones varía considerablemente entre los meses.

Los meses con mayor número de sesiones fueron:

* Mayo: `3.364`
* Noviembre: `2.998`
* Marzo: `1.907`
* Diciembre: `1.727`

Las tasas observadas de compra también presentan diferencias:

* Noviembre: `25,35 %`
* Octubre: `20,95 %`
* Septiembre: `19,20 %`
* Agosto: `17,55 %`
* Julio: `15,28 %`
* Diciembre: `12,51 %`
* Mayo: `10,85 %`
* Marzo: `10,07 %`
* Junio: `10,07 %`
* Febrero: `1,63 %`

Febrero tuvo únicamente 184 sesiones y 3 compras, por lo que su tasa debe interpretarse considerando su menor tamaño de muestra.

---

## 3.3 OperatingSystems

Los valores representan códigos de sistemas operativos.

Los códigos con mayor cantidad de sesiones fueron:

* `2`: 6.601
* `1`: 2.585
* `3`: 2.555

Las tasas observadas de compra variaron entre categorías.

Debido a que estos números son **identificadores de categorías**, no deben interpretarse como una escala numérica donde, por ejemplo, `4` sea "mayor" que `2`.

Las categorías con pocos registros deben interpretarse con precaución.

---

## 3.4 Browser

Los navegadores también están representados mediante códigos.

El código `2` concentró la mayor cantidad de sesiones, con `7.961`.

Las tasas observadas de compra variaron entre categorías.

Algunas categorías tuvieron tamaños de muestra muy pequeños. Por ejemplo:

* Browser `12`: 10 sesiones.
* Browser `13`: 61 sesiones.
* Browser `9`: 1 sesión y ninguna compra.

Por esta razón, porcentajes extremos en categorías pequeñas no deben interpretarse de la misma manera que los porcentajes de categorías con miles de sesiones.

---

## 3.5 Region

La variable `Region` también está representada mediante códigos.

Las regiones con mayor cantidad de sesiones fueron:

* Región `1`: 4.780
* Región `3`: 2.403
* Región `4`: 1.182

Las tasas observadas de compra se mantuvieron relativamente próximas entre categorías, aproximadamente entre:

* `12,90 %`
* `16,83 %`

No se observaron diferencias tan amplias como en algunas otras variables categóricas.

---

## 3.6 TrafficType

`TrafficType` presenta una distribución mucho más desigual.

Las categorías con mayor cantidad de sesiones fueron:

* `2`: 3.913
* `1`: 2.451
* `3`: 2.052
* `4`: 1.069
* `13`: 738

Las tasas observadas de compra presentan una variación considerable.

Sin embargo, varias categorías tienen muy pocas observaciones. Por ejemplo, algunas categorías tienen solamente una, tres o diez sesiones.

Por ello, una tasa de compra elevada en una categoría con muy pocas sesiones no tiene la misma estabilidad descriptiva que una tasa calculada sobre cientos o miles de sesiones.

---

## 3.7 Weekend

La distribución fue:

* `False`: 9.462 sesiones
* `True`: 2.868 sesiones

Tasas observadas de compra:

* Entre semana: `14,89 %`
* Fin de semana: `17,40 %`

La diferencia descriptiva es de aproximadamente **2,51 puntos porcentuales**.

Ambos grupos tienen un tamaño de muestra considerable, por lo que la comparación descriptiva es más estable que la de categorías con muy pocas observaciones.

---

# 4. Visualización

Durante el análisis se utilizaron principalmente:

### Matplotlib

Se utilizó para construir histogramas y apoyar la inspección de la distribución de las variables numéricas.

### Seaborn

Se utilizaron principalmente:

* `boxplot` para visualizar dispersión y posibles valores atípicos.
* `histplot` para estudiar distribuciones.
* Visualizaciones separadas para observar diferencias entre grupos cuando fue pertinente.

Las visualizaciones permitieron complementar las estadísticas calculadas con Pandas.

---

# 5. Principales patrones encontrados

A partir del análisis exploratorio se identificaron varios patrones descriptivos:

### Comportamiento relacionado con productos

`ProductRelated` y `ProductRelated_Duration` mostraron una tendencia descriptiva en la que las sesiones con mayores valores presentaron tasas observadas de compra superiores.

### PageValues

`PageValues` presentó una diferencia especialmente marcada:

* Sesiones con `PageValues = 0`: aproximadamente `3,85 %` de compras.
* Sesiones con `PageValues > 0`: aproximadamente `56,34 %`.

### Información administrativa e informativa

Las sesiones con valores positivos en `Informational` o `Informational_Duration` mostraron tasas observadas de compra superiores a las sesiones con valor cero.

### SpecialDay

Las sesiones con `SpecialDay > 0` presentaron una tasa observada de compra inferior a las sesiones con `SpecialDay = 0`.

### Variables categóricas

`Month`, `VisitorType`, `TrafficType`, `Browser`, `OperatingSystems`, `Region` y `Weekend` mostraron diferentes distribuciones y tasas observadas de compra.

Sin embargo, el tamaño de las categorías debe considerarse antes de interpretar porcentajes extremos.

---

# 6. Consideraciones sobre los outliers

Un punto importante del análisis fue diferenciar entre:

**outlier estadístico ≠ dato incorrecto**

El criterio del IQR permitió identificar observaciones alejadas de la distribución central, pero esto no significa que deban eliminarse.

Por ejemplo, variables como:

* `ProductRelated_Duration`
* `Administrative_Duration`
* `BounceRates`
* `ExitRates`
* `PageValues`

presentan distribuciones asimétricas donde valores extremos pueden representar sesiones reales.

Por esta razón, los posibles outliers fueron utilizados como parte del análisis exploratorio y no eliminados automáticamente.

---

# 7. Limitaciones del análisis

Este proyecto presenta varias limitaciones:

1. El dataset representa **sesiones**, no necesariamente usuarios únicos.
2. No existe un identificador de sesión que permita distinguir todas las observaciones individualmente.
3. La existencia de registros duplicados no permite determinar automáticamente si son errores o sesiones legítimamente idénticas.
4. Algunas variables categóricas están representadas mediante códigos numéricos.
5. Algunas categorías presentan tamaños de muestra muy pequeños.
6. Las diferencias observadas con `Revenue` representan **asociaciones descriptivas**, no causalidad.
7. El análisis no utiliza modelos de Machine Learning ni pretende realizar predicciones.

---

# 8. Herramientas utilizadas

* **Python**
* **Pandas** — manipulación, limpieza y análisis de datos.
* **Matplotlib** — visualización.
* **Seaborn** — visualización estadística.
* **NumPy** — práctica y consolidación de operaciones numéricas dentro de la fase de Python científico.

---

# 9. Estructura del repositorio

```text
Fase-2-Python-Cientifico-EDA/
│
├── online_shoppers_intention.csv
├── proyecto-fase-2-variables-categoricas.py
└── proyecto-fase-2-variables-numericas.py
```

### `proyecto-fase-2-variables-numericas.py`

Contiene el análisis exploratorio de las variables numéricas, incluyendo estadísticas descriptivas, detección de posibles outliers, análisis por grupos y visualizaciones.

### `proyecto-fase-2-variables-categoricas.py`

Contiene el análisis de las variables categóricas, distribución de categorías y tasas observadas de compra según `Revenue`.

---

# 10. Conclusión

El análisis permitió explorar de forma estructurada el comportamiento de las sesiones del dataset **Online Shoppers Purchasing Intention** utilizando herramientas del ecosistema de Python científico.

Se identificaron distribuciones asimétricas, concentraciones importantes de valores en cero, posibles valores atípicos y diferencias en las tasas observadas de compra entre distintos grupos.

Entre los patrones descriptivos más destacados se encuentra la diferencia entre sesiones con `PageValues = 0` y `PageValues > 0`, así como las diferencias observadas según la cantidad y duración de páginas relacionadas con productos, información y administración.

El análisis también mostró la importancia de considerar el tamaño de cada categoría antes de interpretar porcentajes, especialmente en variables como `Browser` y `TrafficType`.

Finalmente, el proyecto permitió aplicar de forma práctica conceptos de **Pandas, visualización con Matplotlib y Seaborn, estadística descriptiva, análisis de distribuciones, detección de outliers y análisis de variables categóricas**, dejando una base para continuar con la siguiente fase de aprendizaje.

---

## Fuente del dataset

**UCI Machine Learning Repository — Online Shoppers Purchasing Intention Dataset**

[Dataset oficial en UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset?utm_source=chatgpt.com)
