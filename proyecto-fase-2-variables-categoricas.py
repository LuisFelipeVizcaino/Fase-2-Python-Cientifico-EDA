import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("online_shoppers_intention.csv")


def analizar_variables_categoricas(nombre:str):
    variable=df[nombre]
    recurrencia= variable.value_counts()
    porcentaje_cada_categoria=(recurrencia/len(variable))*100
    revenue_true = df[df["Revenue"] == True]
    compras_por_categoria = revenue_true[nombre].value_counts()
    compras_por_categoria = compras_por_categoria.reindex(recurrencia.index, fill_value=0)
    tasa_revenue_true_categoria = (compras_por_categoria / recurrencia) * 100
    revenue_false=df[df["Revenue"]==False]
    nocompraron_por_categoria=revenue_false[nombre].value_counts()
    tasa_revenue_false_categoria=(nocompraron_por_categoria/recurrencia)*100
    return{
        "variable_de_la_que_se_habla": nombre,
        "recurrencia_de_valores": recurrencia,
        "porcentaje_por_categoria": porcentaje_cada_categoria,
        "compras_por_categoria": compras_por_categoria,
        "tasa_revenue_true_categoria": tasa_revenue_true_categoria,
        "tasa_revenue_false_categoria":tasa_revenue_false_categoria
    }

visitor_type = analizar_variables_categoricas("VisitorType") 
month = analizar_variables_categoricas("Month") 
operating_systems = analizar_variables_categoricas("OperatingSystems") 
browser = analizar_variables_categoricas("Browser") 
region = analizar_variables_categoricas("Region") 
traffic_type = analizar_variables_categoricas("TrafficType") 
weekend = analizar_variables_categoricas("Weekend")
