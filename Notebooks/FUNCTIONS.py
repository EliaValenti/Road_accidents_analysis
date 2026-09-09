import pandas as pd
import os
import numpy as np

#grafici
import seaborn as sns
import matplotlib 
import matplotlib.pyplot as plt

#per test anova
import scipy.stats as stats
#simple linear regression
import statsmodels.api as sm

#=====================================================================================
#FUNZIONE PER ISTOGRAMMI E BOXPLOT
#=====================================================================================
def plot_distribuzione(df, column):
    fig, ax = plt.subplots(1, 2, figsize=(8, 4))

    sns.histplot(data=df,x=column,ax=ax[0]).set_title(f"Istogramma - {column}")

    sns.boxplot(x=df[column],ax=ax[1]).set_title(f"Boxplot - {column}")

    plt.tight_layout()
    plt.show()


#=====================================================================================
#FUNZIONE PER BARPLOT CLASSE DEMOGRAFICA
#=====================================================================================
def plot_bars(df, var1, var2):
    # fig, ax = plt.subplots(1, 2, figsize=(8, 4))

    ordine=["Molto piccolo","Piccolo","Medio","Grande"]

    sns.barplot(data=df,x=var1,y=var2,order=ordine, estimator = "mean").set_title(f"Boxplot - {var1} x {var2}")

    plt.xlabel({var1})
    plt.ylabel({var2})

    plt.show()
#=====================================================================================
#FUNZIONE PER ISTOGRAMMI E BOXPLOT CON SCALA LOGARITMICA
#=====================================================================================
def plot_distr_logaritmic_scale(df, column):
    fig, ax = plt.subplots(1, 2, figsize=(8, 4))

    sns.histplot(data=df,x=column,ax=ax[0],log_scale=10).set_title(f"Histplot  - LOG SCALE") #ho messo la scala logaritmica in maniera tale che la scala mostrasse tutti i dati nel grafico 
                                                                                                #N.B. se non specifico, la scala log di solito è in base 10
                                                                                                # kde=True mi fa la curva sulle barre

    sns.boxplot(x=df[column],ax=ax[1],log_scale=10).set_title(f"Boxplot  - LOG SCALE")

    plt.tight_layout()
    plt.show()

    #N.B. LA SCALA LOGARITMICA AIUTA A VEDERE LA DISTRIBUZIONE MA FALSA GLI OUTLIER

#=====================================================================================
#CREAZIONE DATASET PER OSSERVAZIONE CON VARIABILE (segnata incidenti, ma creando nuovo df posso usarne un' altra in sostituzione) E AGGIUNTA NUOVE FEATURE 
#=====================================================================================

def create_municipality_dataset(df, value_col="OBS_VALUE", value_name="INCIDENTI"): #i nomi delle colonne nei parametri vengono utilizzati solo e unicamente
                                                                                    #se non se ne passa uno differente
    # Numero totale di anni del periodo di studio
    tot_period_years = df["TIME_PERIOD"].nunique()

    # Numero di anni effettivamente disponibili per ogni comune
    years_recorded_per_municipality = (
        df.groupby(["ID_COMUNE"])["TIME_PERIOD"]
          .nunique()
          .reset_index(name="N_ANNI")
    )

    # Ordinamento cronologico per ottenere l'ID_COMUNE più recente
    df = df.sort_values(["ID_COMUNE", "TIME_PERIOD"])

    # Aggregazione per comune
    df_municipality = (
        df.groupby(["ID_COMUNE"], as_index=False)
          .agg({
              "COMUNE": "last",
              value_col: "sum",
              "RESIDENTI": "mean",
              "SUPERFICIE (KMQ)": "mean",
              "ID_REGIONE": "first",
            "REGIONE": "first"
          })
    )

    # Aggiunta del numero di anni osservati
    df_municipality = df_municipality.merge(
        years_recorded_per_municipality,
        on=["ID_COMUNE"],
        how="left",
        validate="one_to_one"
    )

    # Rinomina
    df_municipality.rename(
        columns={value_col: f"{value_name}_TOTALI"},
        inplace=True
    )

    # Media annuale sul periodo complessivo
    df_municipality[f"{value_name}_MEDI_ANNUI"] = (
        df_municipality[f"{value_name}_TOTALI"] / tot_period_years
    )

    # Densità popolazione
    df_municipality["DENSITA_POPOLAZIONE"] = (
        df_municipality["RESIDENTI"] /
        df_municipality["SUPERFICIE (KMQ)"]
    )

    # Densità dell'osservazione
    df_municipality[f"DENSITA_{value_name}_MEDIA"] = (
        df_municipality[f"{value_name}_MEDI_ANNUI"] /
        df_municipality["SUPERFICIE (KMQ)"]
    )

    # Osservazione pro capite
    df_municipality[f"{value_name}_PRO_CAPITE(1000)_MEDIA"] = (
        df_municipality[f"{value_name}_MEDI_ANNUI"] /
        df_municipality["RESIDENTI"]
    ) * 1000

    return df_municipality

#=====================================================================================
#FUNZIONE CHECK GENERALE DF
#=====================================================================================

def check_df (df):
    print(df.info())
    print("-"*40)
    print("Dati duplicati:",df.duplicated().sum())
    print("-"*40)
    print("Dati nulli: \n", df.isna().sum())
    print("-"*40)
    return df.head()



#=====================================================================================
#RICERCA OUTLIER
#=====================================================================================
def outliers(df, column):

    # Calcolo dei quartili
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    # Intervallo interquartile
    IQR = Q3 - Q1

    # Limiti per gli outlier
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    # DataFrame degli outlier inferiori
    outliers_lower = (df[df[column] < lower].sort_values(by=column))

    # DataFrame degli outlier superiori
    outliers_upper = (df[df[column] > upper].sort_values(by=column, ascending=False))

    #Totale dei recordo del df
    totale = len(df)

    print(f"ANALISI OUTLIER - {column}")
    print("=" * 70)
    print(f"Q1: {Q1:.3f}")
    print(f"Q3: {Q3:.3f}")
    print(f"IQR: {IQR:.3f}")
    print(f"Limite inferiore: {lower:.3f}")
    print(f"Limite superiore: {upper:.3f}")
    print("-" * 70)
    print("-OUTLIER INFERIORI")
    print(f"Numero di comuni: {len(outliers_lower)}")
    print(f"Percentuale sul totale: {(len(outliers_lower)/totale)*100:.3f}%")
    display(outliers_lower)

    print("-OUTLIER SUPERIORI")
    print(f"Numero di comuni: {len(outliers_upper)}")
    print(f"Percentuale sul totale: {(len(outliers_upper)/totale)*100:.3f}%")
    display(outliers_upper)

    return outliers_lower, outliers_upper  #return permette di utilizzare anche queste cose che inserisco al di là della funzione


#=====================================================================================
#CONTEGGIO PER CLASSE E QUANTO OGNI CLASSE PESA SUL TOTALE DEI COMUNI REGISTRATI NEL DF
#=====================================================================================
def check_class_municipal(df, column, size):
    tot_df = len(df)
    num_for_class = (df[column] == size).sum()
    perc = round(num_for_class / tot_df * 100, 2)

    print(f"Comuni '{size}': {num_for_class} ({perc}%)")


#=====================================================================================
# FUNZIONE DI REGRESSIONE LINEARE SEMPLICE
#=====================================================================================
def simple_linear_regression(df, indep_var, dep_var, model_n):
    
    X = df[indep_var] #variabile indipendente-predittore
    y = df[dep_var] #variabile dipendente, quella che si vorrebbe predirre in base all' x

    X = sm.add_constant(X)

    model_n = sm.OLS(y, X).fit()
    print(model_n.summary())


    # future = pd.DataFrame({
    #     indep_var: [2025, 2026, 2027, 2028, 2029, 2030]}) 

    # future=sm.add_constant(future) #devo aggiungere la costante a tutti i valori di future poichè non è più semplicemente un array in cui aggiungevo io a mano 1 per avere anche la seconda dimensione

    # print(X.head())
    # print(X.columns)
    # print(future.head())
    # print(future.columns) #con queste ultime 4 righe vedo che i miei due df hanno tutte e due la stessa dimensione (cioè 2)


    # future["Predicted"] = model1.predict(future)

    # print(future)

    model_n.params

    #Grafico della retta di regressione

    #Coefficienti della retta
    intercept=model_n.params["const"]
    slope=model_n.params[indep_var]

    sns.scatterplot(x=indep_var,y=dep_var,
                    data=df)
    plt.xlabel(indep_var)
    plt.ylabel(dep_var)
    plt.title(f"SIMPLE LINEAR REGRESSION: {indep_var} x {dep_var}")


    #Limiti asse X
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())

    #Eq della retta
    y_vals = intercept + slope * x_vals

    #Plot della retta di regressione
    plt.plot(x_vals, y_vals, "--", color="r")

    # #Plot della previsione
    # plt.plot(future["TIME_PERIOD"], future["Predicted"], "ro")

    plt.tight_layout() #per uniformare gli spazi
    plt.show()