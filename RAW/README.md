ANALISI DEGLI INCIDENTI STRADALI IN ITALIA (2020-2024)
---------------------------------------------------------

Panoramica
----------

Utilizzando dati ufficialmente emessi da ISTAT, il progetto ha l' obiettivo di analizzare l' andamento degli incidenti 
su territorio italiano nel periodo 2020-2024 evidenziandone i comuni a maggior rischio, 
in maniera tale da essere utilizzato come possibile supporto decisionale in caso di investimenti nell' ambito della sicurezza stradale.

Il processo analitico è partito dall' acquisizione dei dati con conseguente pulizia e aggregazione, fino alla realizzazione di 
una dashboard interattiva tramite Power BI, fornendo supporto all' analisi.

Il progetto comprende:

-Pulizia e integrazione dei dataset

-Analisi esplorativa dei dati

-Analisi statistica

-Clustering dei comuni

-Dashboard creata in Power BI


Obiettivi
---------

L' analisi è stata sviluppata con i seguenti obiettivi:

-Analizzare l' evoluzione degli incidenti stradali in Italia (2020-2024)

-Osservare il fenomeno a livello nazionale, regionale e comunale.

-Individuare comuni con maggior numero di incidenti in termini assoluti e pro capite

-Analizzare la relazione tra variabili demografiche e territoriali

-Creare una profilazione di comuni che presentano affinità tramite clustering

-Realizzare una dashboard interattiva che aiuti nella comprensione dei risultati e sia da supporto per eventuali decisioni


Dataset e Strumenti utilizzati
------------------------------

E' stato utilizzato:

-Linguaggio --> Python 

-Dipendenze presenti nel file "requirements.txt"

-Editor --> Visual Studio Code (VSCode)

-Visualizzazione --> Power BI

Dataset:

I dataset utilizzati sono stati recuperati dal sito ufficiale ISTAT dai seguenti link:

-ISTAT [https://esploradati.istat.it/SDMXWS/rest/data/41_983](url) --> contentente i dati informativi sul numero di incidenti e il periodo di registrazione


-SITUAS [https://situas.istat.it/web/#/territorio/body?id=74&dateFrom=2020-12-31](url) --> contenente informazioni tra cui i codici regionali, provinciali e comunali, i nomi dei comuni, la loro superficie e la popolazione residenti

I dataset sono stati successivamente integrati in maniera tale da ottenere una base unica utilizzata nelle analisi.


Struttura del progetto
------------------------

Notebook Jupyter:

-00_fetching.ipynb --> Download dei dati

-01_overview_e_cleaning.ipynb --> Pulizia e integrazione

-02_EDA.ipynb --> Analisi esplorativa

-03_Analysis.ipynb --> Analisi statistiche e clustering


Dataset classificati in:

-fetching_data --> Dataset recuperati

-raw_data --> Dataset grezzi

-df_clean --> Dataset opportunamente puliti e integrati


Dashboard.pbix --> Dashboard Power BI

Presentazione.pptx --> Presentazione finale

requirements.txt

Cartella di documenti contenente file informativi e link utili (es. quelli usati per le classificazioni) 


README.md

copia_env.yml --> copia dell' ambiente di lavoro

Processo di analisi
-----------------------

Il progetto è stato sviluppato seguendo le seguenti fasi:

1. Raccolta dei dati

Download dei dati ISTAT tramite API

Recupero dei dati territoriali dal portale SITUAS tramite scraping

--------------------------
2. Pulizia dei dati

Gestione dei valori mancanti

Controllo della qualità dei dati

Uniformazione degli identificativi comunali

Integrazione dei dataset

----------------------------------------------------
3. Creazione nuovi indicatori utili all'analisi

Incidenti per 1000 abitanti

Densità degli incidenti

Densità della popolazione

Classe demografica

Classe di superficie

------------------------------
4. Analisi esplorativa (EDA)

Andamento degli incidenti nel tempo

Distribuzione regionale

Distribuzione comunale

Classificazione dei comuni per classe demografica

Classificazione dei comuni per superficie

-------------------------------
5. Analisi statistica

L'analisi comprende:

Studio delle correlazioni

Regressione lineare

Clustering tramite K-Means, realizzato utilizzando: residenti, densità degli incidenti, incidenti per 1000 abitanti.

-------------------
6. Dashboard

È stata sviluppata una dashboard interattiva in Power BI composta da tre sezioni:

Panoramica nazionale

Analisi dei comuni

Approfondimenti statistici


La dashboard
------------------

La dashboard è composta da tre pagine:

1. Incidenti Stradali

Andamento temporale

Indicatori principali

Confronto tra regioni

Filtri per anno, regione e comune

--------------------------------
2. Analisi dei Comuni

Distribuzione per classe demografica

Distribuzione per superficie

Comuni con maggiore incidentalità pro capite

Comuni con il maggior numero di incidenti

-----------------------------------
3. Approfondimenti

Analisi delle correlazioni con annessi scatter plot

Clustering dei comuni

Individuazione cluster dei comuni con maggiore densità di incidenti

Risultati principali
--------------------

L'analisi ha evidenziato alcuni risultati di particolare interesse:

-Gli incidenti stradali mostrano un trend crescente nel periodo 2020–2024

-Circa il 70% dei comuni italiani appartiene alle classi demografiche Piccolo o Molto piccolo

-I grandi comuni registrano il maggior numero assoluto di incidenti

-I piccoli comuni presentano spesso valori più elevati di incidentalità pro capite

-Esiste una forte correlazione tra numero di residenti e numero di incidenti

-La densità della popolazione è correlata con la densità degli incidenti

-Non emerge una relazione significativa tra densità della popolazione e incidentalità pro capite

-Il clustering ha individuato gruppi di comuni con caratteristiche simili, evidenziando aree che potrebbero rappresentare priorità per eventuali interventi in materia di sicurezza stradale




