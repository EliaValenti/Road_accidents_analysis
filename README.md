# Road Accidents Analysis

> **ATTENZIONE -> Stato del progetto: in fase di revisione**
>
> Il progetto è attualmente sottoposto a una revisione metodologica e tecnica.
> Il processo di data cleaning, l'integrazione dei dati, le analisi statistiche
> e alcune elaborazioni sono in corso di verifica.
>
> Di conseguenza, **analisi, risultati, visualizzazioni e conclusioni presenti
> nella versione attuale potrebbero essere modificati** prima della versione
> definitiva.

## Descrizione

**Road Accidents Analysis** è un progetto di analisi dei dati dedicato agli
incidenti stradali in Italia nel periodo **2001–2024**.

L'analisi combina dati provenienti da **ISTAT** e **SITUAS** con l'obiettivo di
studiare il fenomeno sia dal punto di vista **temporale** sia dal punto di
vista **territoriale**, con particolare attenzione ai comuni italiani.

Il progetto utilizza Python per la raccolta, la pulizia, l'integrazione e
l'analisi dei dati e include una fase di analisi statistica e di clustering.

---

## Obiettivi

Gli obiettivi principali del progetto sono:

- analizzare l'evoluzione degli incidenti stradali in Italia nel periodo
  2001–2024;
- analizzare l'andamento di incidenti, feriti e morti nel tempo;
- studiare le differenze tra i comuni italiani;
- analizzare la relazione tra incidentalità e caratteristiche demografiche;
- analizzare la relazione tra incidentalità e caratteristiche territoriali;
- costruire indicatori di incidentalità normalizzati;
- applicare tecniche di regressione lineare;
- verificare differenze tra gruppi di comuni attraverso test statistici;
- individuare gruppi di comuni con caratteristiche simili attraverso
  clustering K-Means.

---

## Fonti dei dati

Il progetto utilizza principalmente due fonti:

### ISTAT

I dati relativi agli incidenti stradali vengono recuperati tramite
le API SDMX di ISTAT.

### SITUAS

I dati territoriali e comunali vengono raccolti dal sistema SITUAS di ISTAT.

I dati SITUAS vengono scaricati annualmente per il periodo 2001–2024 e
successivamente concatenati in un unico dataset.

Le due fonti vengono successivamente integrate utilizzando il comune e
l'anno come riferimenti per l'integrazione.

---

## Pipeline del progetto

Il progetto segue principalmente questo flusso:

```text
Raccolta dati
     ↓
Data cleaning
     ↓
Integrazione ISTAT + SITUAS
     ↓
Feature engineering
     ↓
Analisi esplorativa
     ↓
Analisi temporale
     ↓
Analisi comunale
     ↓
Analisi statistica
     ↓
Clustering
     ↓
Visualizzazione e dashboard
```

---

## Notebook

### `00_fetching.ipynb`

**Raccolta dei dati**

Il notebook gestisce la fase di acquisizione dei dati.

Le principali attività sono:

- configurazione dello scraping dei dati SITUAS;
- download dei dataset annuali dal 2001 al 2024;
- salvataggio dei file CSV nella cartella `Data/Fetching_data/`;
- concatenazione dei dataset SITUAS annuali;
- aggiunta dell'anno di riferimento (`TIME_PERIOD`);
- acquisizione del dataset ISTAT tramite API;
- salvataggio dei dataset grezzi in `Data/Df_raw/`.

---

### `01cleaning_overview.ipynb`

**Data cleaning e integrazione dei dati**

Il notebook gestisce la preparazione dei dataset grezzi e la loro integrazione.

Le attività principali comprendono:

- caricamento dei dati ISTAT e SITUAS;
- selezione delle colonne di interesse;
- conversione dei tipi di dato;
- standardizzazione dei valori numerici;
- controlli sulla struttura dei dataset;
- verifica dei valori mancanti;
- integrazione dei dataset ISTAT e SITUAS;
- controlli sui codici comunali;
- analisi dei cambiamenti degli identificativi comunali;
- gestione degli identificativi comunali utilizzati nell'analisi;
- verifica delle variazioni della superficie comunale;
- creazione dei dataset finali utilizzati nelle analisi successive.

Vengono inoltre mantenuti gli identificativi comunali originali tramite
`ID_COMUNE_OG`, mentre `ID_COMUNE` viene utilizzato come identificativo
armonizzato per le analisi.

---

### `02a.EDA_&_Temporal_analysis.ipynb`

**EDA e analisi temporale**

Il notebook analizza l'evoluzione del fenomeno a livello nazionale nel
periodo 2001–2024.

Le principali attività comprendono:

- costruzione dei dataset annuali relativi a incidenti, feriti e morti;
- controlli sulla qualità dei dati;
- statistica descrittiva;
- classifiche;
- analisi univariata;
- analisi bivariata;
- analisi del trend temporale;
- variazioni percentuali anno su anno;
- analisi delle correlazioni;
- regressione lineare semplice;
- analisi dei residui e delle metriche del modello;
- regressione lineare multipla;
- analisi dell'andamento degli incidenti all'interno dei cluster
  di profilazione comunale.

---

### `02b_EDA_Municipality_analysis_aggregate_01_24.ipynb`

**EDA a livello comunale**

Il notebook analizza i comuni italiani aggregando le osservazioni relative
al periodo 2001–2024.

Vengono costruiti dataset aggregati per comune e vengono calcolati diversi
indicatori, tra cui:

- incidenti totali;
- incidenti medi annui;
- densità della popolazione;
- densità media degli incidenti;
- incidenti pro capite medi.

I comuni vengono inoltre classificati secondo:

- classe demografica;
- classe di superficie.

Il notebook comprende inoltre:

- statistica descrittiva;
- classifiche;
- analisi delle distribuzioni;
- analisi con scala logaritmica;
- analisi bivariata;
- correlazioni;
- analisi degli outlier.

---

### `03b_Test.ipynb`

**Analisi statistica e clustering**

Il notebook approfondisce le relazioni individuate durante l'analisi
esplorativa a livello comunale.

Sono presenti:

#### Regressioni lineari

Vengono analizzate relazioni tra:

- superficie e incidenti medi annui;
- residenti e incidenti medi annui;
- densità della popolazione e indicatori di incidentalità;
- residenti e incidenti pro capite;
- superficie e incidenti pro capite;
- superficie e densità degli incidenti.

Vengono inoltre utilizzati modelli di regressione lineare multipla.

#### ANOVA e test statistici

Vengono analizzate le differenze tra gruppi di comuni attraverso:

- test di Levene;
- Welch ANOVA;
- ANOVA a una via;
- test post-hoc di Tukey;
- confronti tra gruppi.

Le analisi vengono effettuate considerando sia le classi demografiche sia
le classi di superficie.

#### Clustering

Viene utilizzato **K-Means** per individuare gruppi di comuni con
caratteristiche simili.

Sono considerate due impostazioni:

1. **Rischio puro**
   - incidenti pro capite;
   - densità degli incidenti.

2. **Rischio contestualizzato**
   - incidenti pro capite;
   - densità degli incidenti;
   - numero di residenti trasformato in scala logaritmica.

La scelta del numero di cluster viene supportata da tecniche quali
**Elbow Method** e **Silhouette Score**.

---

## `FUNCTIONS.py`

Il file `FUNCTIONS.py` contiene funzioni riutilizzabili durante le diverse
fasi dell'analisi.

Tra le principali funzioni sono presenti:

- `plot_distribuzione()` per istogrammi e boxplot;
- `plot_bars()` per i grafici relativi alle classi demografiche;
- `plot_distr_logaritmic_scale()` per la visualizzazione delle distribuzioni
  in scala logaritmica;
- `create_municipality_dataset()` per la creazione dei dataset aggregati
  a livello comunale e il calcolo degli indicatori;
- `check_df()` per i controlli generali dei DataFrame;
- `outliers()` per l'individuazione degli outlier tramite IQR;
- `check_class_municipal()` per il conteggio dei comuni appartenenti a una
  determinata classe;
- `simple_linear_regression()` per la regressione lineare semplice.

---

## Principali indicatori

Tra gli indicatori utilizzati nell'analisi sono presenti:

- **Incidenti totali**
- **Incidenti medi annui**
- **Densità della popolazione**
- **Densità media degli incidenti**
- **Incidenti pro capite medi**
- **Numero di residenti**
- **Superficie comunale**

Gli indicatori vengono utilizzati per confrontare comuni con dimensioni
demografiche e territoriali differenti.

---

## Struttura del progetto

```text
Road_accidents_analysis/
│
├── .git/
│
├── Data/
│   ├── Fetching_data/
│   │   └── Dataset SITUAS annuali (2001–2024)
│   │
│   ├── Df_raw/
│   │   ├── df_istat_raw.csv
│   │   └── df_situas_raw.csv
│   │
│   └── Df_clean/
│       ├── df_final_from_01_to_24_clean.csv
│       ├── df_incidenti_from_01_to_24.csv
│       ├── df_feriti_from_01_to_24.csv
│       ├── df_morti_from_01_to_24.csv
│       └── df_accidents_municipality_aggregate_years.csv
│
├── Notebooks/
│   ├── 00_fetching.ipynb
│   ├── 01cleaning_overview.ipynb
│   ├── 02a.EDA_&_Temporal_analysis.ipynb
│   ├── 02b_EDA_Municipality_analysis_aggregate_01_24.ipynb
│   ├── 03b_Test.ipynb
│   └── FUNCTIONS.py
│
├── RAW/
│   ├── Capstone Project README.md
│   ├── Capstone Project README.md.docx
│   ├── copia_env.yml
│   ├── Dashboard.pbix
│   ├── Informazioni utili.txt
│   ├── Presentazione.pptx
│   ├── README.md
│   └── requirements.txt
│
├── Various_doc/
│   └── Elenco-comuni-italiani.csv
│
├── .gitignore
└── README.md
```

---

## Organizzazione dei dati

### `Data/Fetching_data/`

Contiene i file CSV SITUAS scaricati annualmente durante la fase di
raccolta dei dati.

### `Data/Df_raw/`

Contiene i dataset grezzi risultanti dalla fase di acquisizione:

- `df_istat_raw.csv`
- `df_situas_raw.csv`

### `Data/Df_clean/`

Contiene i dataset risultanti dal processo di pulizia e preparazione
utilizzati nelle analisi successive.

### `Notebooks/`

Contiene tutti i notebook Python che costituiscono il flusso principale
dell'analisi.

### `RAW/`

Contiene materiale e documentazione di supporto al progetto, tra cui il
dashboard Power BI, la presentazione, file di configurazione e precedenti
documenti README.

### `Various_doc/`

Contiene documentazione e dataset di supporto, tra cui l'elenco dei comuni
italiani.

---

## Dashboard

Nel progetto è presente anche un dashboard sviluppato con **Power BI**,
conservato nella cartella `RAW/` come:

```text
RAW/Dashboard.pbix
```

Il dashboard costituisce la parte di visualizzazione interattiva dei
risultati dell'analisi.

---

## Tecnologie utilizzate

### Linguaggio

- Python

### Analisi e manipolazione dei dati

- Pandas
- NumPy

### Visualizzazione

- Matplotlib
- Seaborn

### Analisi statistica

- SciPy
- Statsmodels

### Machine Learning

- Scikit-learn
- K-Means

### Business Intelligence

- Power BI

### Versionamento

- Git

---

## Stato attuale del progetto

Il progetto è **in fase di revisione**.

La revisione riguarda in particolare:

- qualità e coerenza dei dati;
- processo di data cleaning;
- integrazione tra ISTAT e SITUAS;
- gestione degli identificativi comunali;
- feature engineering;
- metodologia statistica;
- regressioni;
- test statistici;
- clustering;
- visualizzazioni;
- dashboard.

La versione presente nel repository rappresenta quindi una **versione di
lavoro**.

Prima della pubblicazione della versione definitiva verranno riesaminate
le elaborazioni e, dove necessario, aggiornati codice, dataset, analisi e
documentazione.

---

## Periodo di analisi

**2001–2024**

## Fonti principali

**ISTAT – Istituto Nazionale di Statistica**

**SITUAS – Sistema Informativo Territoriale e Amministrativo**

---

> **Nota:** il README e la struttura del progetto potranno essere aggiornati
> durante la fase di revisione.
