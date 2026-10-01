import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("online_shoppers_intention.csv")



# FASE DE RECONOCIMIENTO DEL DATASET

info_general = df.info()

columnas = df.columns

head = df.head()


# DUPLICADOS Y DATOS NULOS

cantidad_duplicados = df.duplicated().sum()

datos_nulos = df.isna().sum()

pd.set_option('display.max_columns', None)

duplicados = df[df.duplicated(keep=False)]

conteo_duplicados = duplicados.value_counts()

porcentaje_duplicados = (
    len(duplicados) / len(df)
) * 100


# FUNCIÓN PARA ANALIZAR VARIABLES NUMÉRICAS


def analizar_numerica(nombre_variable: str):

    variable = df[nombre_variable]

    minimo = variable.min()
    maximo = variable.max()
    media = variable.mean()
    mediana = variable.median()

    frecuencia = variable.value_counts()

    q1 = variable.quantile(0.25)
    q2 = variable.quantile(0.50)
    q3 = variable.quantile(0.75)

    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    observaciones_por_encima = (
        variable > limite_superior
    )

    cantidad_outliers = observaciones_por_encima.sum()

    outliers = df[observaciones_por_encima]

    minimo_outliers = outliers[nombre_variable].min()

    maximo_outliers = outliers[nombre_variable].max()

    porcentaje_outliers = (
        cantidad_outliers / len(df)
    ) * 100

    return {
        "variable_analizada": nombre_variable,
        "minimo": minimo,
        "maximo": maximo,
        "media": media,
        "mediana": mediana,
        "frecuencia": frecuencia,
        "q1": q1,
        "q2": q2,
        "q3": q3,
        "iqr": iqr,
        "limite_inferior": limite_inferior,
        "limite_superior": limite_superior,
        "cantidad_outliers": cantidad_outliers,
        "outliers": outliers,
        "minimo_outliers": minimo_outliers,
        "maximo_outliers": maximo_outliers,
        "porcentaje_outliers": porcentaje_outliers
    }


# ANALIZAMOS LAS VARIABLES NUMÉRICAS


administrative = analizar_numerica("Administrative")

administrative_duration = analizar_numerica("Administrative_Duration")

informational = analizar_numerica("Informational")

informational_duration = analizar_numerica("Informational_Duration")

product_related = analizar_numerica("ProductRelated")

product_related_duration = analizar_numerica("ProductRelated_Duration")

bounce_rates = analizar_numerica("BounceRates")

exit_rates = analizar_numerica("ExitRates")

page_values = analizar_numerica("PageValues")

special_day = analizar_numerica("SpecialDay")

# FUNCIÓN PARA ANALIZAR REVENUE POR CUANTILES

def analizar_revenue_por_cuantiles(nombre_variable: str):

    variable = df[nombre_variable]

    q1 = variable.quantile(0.25)
    q3 = variable.quantile(0.75)

    grupo_bajo = df[
        variable <= q1
    ]

    grupo_medio = df[
        (variable > q1) &
        (variable <= q3)
    ]

    grupo_alto = df[
        variable > q3
    ]

    compras_bajo = grupo_bajo[
        grupo_bajo["Revenue"] == True
    ]

    compras_medio = grupo_medio[
        grupo_medio["Revenue"] == True
    ]

    compras_alto = grupo_alto[
        grupo_alto["Revenue"] == True
    ]

    cantidad_bajo = len(grupo_bajo)
    cantidad_medio = len(grupo_medio)
    cantidad_alto = len(grupo_alto)

    tasa_bajo = (
        len(compras_bajo)
        / cantidad_bajo
    ) * 100

    tasa_medio = (
        len(compras_medio)
        / cantidad_medio
    ) * 100

    tasa_alto = (
        len(compras_alto)
        / cantidad_alto
    ) * 100

    return {
        "variable_analisada":nombre_variable,
        "total_grupo_bajo": cantidad_bajo,
        "total_grupo_medio": cantidad_medio,
        "total_grupo_alto": cantidad_alto,
        "grupo_bajo": grupo_bajo,
        "grupo_medio": grupo_medio,
        "grupo_alto": grupo_alto,
        "tasa_bajo": tasa_bajo,
        "tasa_medio": tasa_medio,
        "tasa_alto": tasa_alto
    }



# REVENUE POR CUANTILES
revenue_administrative= analizar_revenue_por_cuantiles("Administrative")

revenue_product_related = analizar_revenue_por_cuantiles("ProductRelated")

revenue_bounce_rates = analizar_revenue_por_cuantiles("BounceRates")

revenue_exit_rates = analizar_revenue_por_cuantiles("ExitRates")

revenue_administrative_duration= analizar_revenue_por_cuantiles("Administrative_Duration")

revenue_product_related_duration= analizar_revenue_por_cuantiles("ProductRelated_Duration")

# analisis especifico de page values 
page_values_mayores_cero = df[df["PageValues"] > 0]

page_values_iguales_cero = df[df["PageValues"] == 0]

revenue_page_values_positivos = (page_values_mayores_cero["Revenue"].value_counts())

revenue_page_values_cero = (page_values_iguales_cero["Revenue"].value_counts())

porcentaje_compra_page_values_positivos = (revenue_page_values_positivos[True]/ len(page_values_mayores_cero)) * 100

porcentaje_compra_page_values_cero = (revenue_page_values_cero[True]/ len(page_values_iguales_cero)) * 100

#analisis especifico de informational
informational_mayores_que_cero=df[df["Informational"]>0]

informational_iguales_a_cero=df[df["Informational"]==0]

revenue_informational_positivos=(informational_mayores_que_cero["Revenue"].value_counts())

revenue_informational_cero=(informational_iguales_a_cero["Revenue"].value_counts())

porcentaje_compra_informational_positivos=(revenue_informational_positivos[True]/len(informational_mayores_que_cero)) * 100

porcentaje_compra_informational_cero=(revenue_informational_cero[True]/len(informational_iguales_a_cero)) * 100

#analisis especifico de informationalduration
informational_duration_positivos=df[df["Informational_Duration"] > 0]

informational_duration_cero=df[df["Informational_Duration"] == 0]

revenue_informational_duration_positivos=(informational_duration_positivos["Revenue"].value_counts())

revenue_informational_duration_cero=(informational_duration_cero["Revenue"].value_counts())

porcentaje_compra_informational_duration_positivos=(revenue_informational_duration_positivos[True]/len(informational_duration_positivos)) * 100

porcentaje_compra_informational_duration_cero=(revenue_informational_duration_cero[True]/len(informational_duration_cero)) * 100

#analisis especifico de specialday
special_day_mayor_cero = df[df["SpecialDay"] > 0]
special_day_igual_cero = df[df["SpecialDay"] == 0]

revenue_special_day_positivos = special_day_mayor_cero["Revenue"].value_counts()
revenue_special_day_cero = special_day_igual_cero["Revenue"].value_counts()

porcentaje_compra_special_day_positivos = (revenue_special_day_positivos[True] /len(special_day_mayor_cero)) * 100

porcentaje_compra_special_day_cero = (revenue_special_day_cero[True] /len(special_day_igual_cero)) * 100

# REVENUE EN LOS OUTLIERS

revenue_outliers_bounce_rates = (bounce_rates["outliers"]["Revenue"].value_counts())

revenue_outliers_exit_rates = (exit_rates["outliers"]["Revenue"].value_counts())

revenue_outliers_page_values = (page_values["outliers"]["Revenue"].value_counts())

revenue_outliers_product_related = (product_related["outliers"]["Revenue"].value_counts())

# VISUALIZACIONES

# BounceRates
sns.boxplot(x=df["BounceRates"])
plt.title("Distribucion de BounceRates")
plt.xlabel("Bounce Rate")
plt.show()

plt.hist(df["BounceRates"], bins="auto")
plt.title("Intervalos BounceRates")
plt.xlabel("Bounce Rate")
plt.show()


# ExitRates
sns.boxplot(x=df["ExitRates"])
plt.title("Distribucion de ExitRates")
plt.xlabel("Exit Rate")
plt.show()

plt.hist(df["ExitRates"], bins="auto")
plt.title("Intervalos ExitRates")
plt.xlabel("Exit Rate")
plt.show()


#PageValues
sns.boxplot(x=df["PageValues"])
plt.title("Distribucion PageValues")
plt.xlabel("PageValues")
plt.show()

plt.hist(df["PageValues"], bins="auto")
plt.title("Intervalos PageValues")
plt.xlabel("PageValues")
plt.show()


# ProductRelated
sns.boxplot(x=df["ProductRelated"])
plt.title("Distribucion ProductRelated")
plt.xlabel("ProductRelated")
plt.show()

plt.hist(df["ProductRelated"], bins="auto")
plt.title("Intervalos ProductRelated")
plt.xlabel("ProductRelated")
plt.show()

# Administrative
sns.boxplot(x=df["Administrative"])
plt.title("Distribución de Administrative")
plt.xlabel("Cantidad de páginas administrativas")
plt.show()

plt.hist(df["Administrative"], bins="auto")
plt.title("Intervalos de Administrative")
plt.xlabel("Cantidad de páginas administrativas")
plt.ylabel("Frecuencia")
plt.show()


# Administrative_Duration
sns.boxplot(x=df["Administrative_Duration"])
plt.title("Distribución de Administrative_Duration")
plt.xlabel("Duración en páginas administrativas (segundos)")
plt.show()

plt.hist(df["Administrative_Duration"], bins="auto")
plt.title("Intervalos de Administrative_Duration")
plt.xlabel("Duración en páginas administrativas (segundos)")
plt.ylabel("Frecuencia")
plt.show()


# Informational
sns.boxplot(x=df["Informational"])
plt.title("Distribución de Informational")
plt.xlabel("Cantidad de páginas informativas")
plt.show()

plt.hist(df["Informational"], bins="auto")
plt.title("Intervalos de Informational")
plt.xlabel("Cantidad de páginas informativas")
plt.ylabel("Frecuencia")
plt.show()


# Informational_Duration
sns.boxplot(x=df["Informational_Duration"])
plt.title("Distribución de Informational_Duration")
plt.xlabel("Duración en páginas informativas (segundos)")
plt.show()

plt.hist(df["Informational_Duration"], bins="auto")
plt.title("Intervalos de Informational_Duration")
plt.xlabel("Duración en páginas informativas (segundos)")
plt.ylabel("Frecuencia")
plt.show()


# ProductRelated_Duration
sns.boxplot(x=df["ProductRelated_Duration"])
plt.title("Distribución de ProductRelated_Duration")
plt.xlabel("Duración en páginas de productos (segundos)")
plt.show()

plt.hist(df["ProductRelated_Duration"], bins="auto")
plt.title("Intervalos de ProductRelated_Duration")
plt.xlabel("Duración en páginas de productos (segundos)")
plt.ylabel("Frecuencia")
plt.show()


# SpecialDay
sns.boxplot(x=df["SpecialDay"])
plt.title("Distribución de SpecialDay")
plt.xlabel("Proximidad a día especial")
plt.show()

plt.hist(df["SpecialDay"], bins="auto")
plt.title("Intervalos de SpecialDay")
plt.xlabel("Proximidad a día especial")
plt.ylabel("Frecuencia")
plt.show()