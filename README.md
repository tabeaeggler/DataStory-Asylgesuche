(German below)

# Datastory Asylum applications in Switzerland

By Hannah-Sarah Kühne & Tabea Eggler

## Goal
With this analysis, we want to find out how asylum applications in Switzerland have developed over the last 25 years. We examine the distribution of asylum applications by gender, the breakdown of decisions over the years, country-specific facts, and the number of applications by nation. In addition, the cantonal distributions of asylum applications have been examined in more detail.


## Data basis
The data was collected using a Python script on 10/15/2019. There are 25 tables with information on asylum applications in Switzerland provided by the State Secretariat for Migration (SEM). Each table contains data on a specific year. For each year/table, the data are additionally divided into 30 sub-tables. Three of these 30 sub-tables offer the possibility to view information on asylum applications by canton, by a nation of the asylum seeker, or by gender. The remaining sub-tables provide a more in-depth look at cantonal structures.  

Regarding the scope per table/year: the cantonal overview sub-tables contain 27 data points, for the national sub-tables the number of data points fluctuates around 150 depending on the year, the gender-specific sub-table contains 3 entries per survey year. No general statement can be made regarding the number of data points for the 26 sub-tables, which provide an in-depth insight into the asylum structures per canton. The values vary greatly per year and canton, between 20 and 150 entries. 

The State Secretariat for Migration did not provide any information on the pre-processing or filtering of the data.

Dependencies between variables are relevant for the attributes "Annerkennungsquote" (recognition rate) and "Schutzquote" (protection rate). The recognition rate is dependent on the attributes "Asylgewährungen" (asylum granted), "Ablehnungen" (rejections), "Nichteintreten mit VA" (non-admission with decision) and "Nichteintreten ohne VA" (Non-admission without decision). The protection rate depends on the same variables as the recognition rate, except for the attribute "Nichteintreten ohne VA" (non-entry without VA).

**Description of the attributes**
General note: In principle, the same attributes are used in each sub-table. In three of the 30 tables, the first attribute changes in each case. For simplicity, all attributes are described only once. The unit of the values is guaranteed for all attributes.

Attribute | Translation | Explanation | Data type | Variable type
------------- | -------------  | ------------- | ------------- | -------------
Kanton  | Canton | Swiss Canton.  | String | Categorical variable
Total neue Asylgesuche  | Total new asylum applications | Total number of new asylum applications in the corresponding year. | Integer | quantitative variable
Mehrfachgesuche nach neuem Asylgesetzt  | Multiple applications under the new Asylum Act | A new asylum application filed within five years of the entry into force of an asylum and removal decision is to be treated as a multiple application under the provisions of Article 111c Asylum Act.  | Integer | quantitative variable
Wiederaufnahmen Asylgesuche  | Reopening of asylum applications | An asylum application is reexamined.  | Integer | Quantitative variable
Totale Erledigungen | Gesamtzahl der in diesem Jahr bearbeiteten Asylanträge | Ganze Zahl | Quantitative Variable
Asylgewährungen  | Number of asylum applications accepted per year  | Integer | quantitative variable
Ablehnungen mit VA  | Asylum application rejected. Asylum seeker is provisionally admitted.  | integer | quantitative variable
Ablehnung ohne VA  | Asylum application rejected. Asylum seeker is not admitted.  | integer | quantitative variable
Nichteintreten mit VA  | No entry with VA | Asylum application is not examined in depth by the authorities. Asylum seeker is provisionally admitted.  | Integer | quantitative variable
Nichteintreten ohne VA  | Non-admission without VA | Asylum application is not examined in depth by the authorities. Asylum seeker is not admitted.  | Integer | quantitative variable
Andere Erledigungen: Abschreibungen  | Other settlements: Write-offs | In the case of persons who do not cooperate with the authorities' clarifications without good reason (= violation of the duty to cooperate), the asylum procedure is terminated. A procedure can also be terminated if the asylum seeker is not available to the authorities for more than 20 days. Asylum applications are written off informally in these cases. Unfounded or repeated multiple applications with the same grounds are also written off informally.  | Integer | quantitative variable
Anerkennungsquote in % | Recognition rate in % | Share of asylum granted in total of all decisions (asylum granted, rejections, and NEE) excluding write-offs at the time of the first-instance decision.  | float | quantitative variable
Schutzquote in %  | Protection rate in % | Share of asylum grants plus temporary admissions in the total of all decisions (asylum grants, rejections, and NEE) excluding write-offs at the time of the first-instance decision.  | float | quantitative variable
Gesuche (Gruppen)  | Applications (groups) | number of applications in the area of asylum for groups.  | Integer | quantitative variable
Asylgewährungen (Gruppen)  | Asylum granted (groups) | number of asylum applications accepted for groups.  | integer | quantitative variable
Abschreibungen (Gruppen)  | Depreciations (groups) | Number of depreciations in the area of asylum application for groups.  | Integer | quantitative variable
Kontinent/Nation  | Continent/Nation | Continent of origin or country from which asylum seekers originate.   | string | categorical variable
Geschlecht  | Gender | Gender of asylum seeker.  | string | categorical variable


## Additional data
Two additional data sets were used for the analyses. An automatic data collection script was not used due to time constraints, as a login is required for one data set. Only the relevant attributes are described in each case.

### IP2Location Country Multilingual Database
Since the country names must be given their country abbreviations for the world map, and the countries in the main dataset are described in German, another data source had to be used.
This dataset maps the country codes and countries in different languages and can only be downloaded with a registration (https://www.ip2location.com/free/country-multilingual).


Attribute | Explanation | Data type | Variable type
------------- | -------------  | ------------- | -------------
LANG_NAME | language | string | categorical variable
COUNTRY_NAME | Country (translated into corresponding language) | String | categorical variable
COUNTRY_ALPHA2_CODE | 2-digit country code | String | categorical variable

### Balance of permanent resident population by canton, 1991-2018.
To calculate the ratio of asylum applications distributed among the cantons, this additional dataset from the Swiss Federal Statistical Office was used. (https://www.bfs.admin.ch/bfs/de/home/statistiken/kataloge-datenbanken/tabellen.assetdetail.9486033.html)


Attribute | Translation | Explanation | Data type | Variable type
------------- | -------------  | ------------- | ------------- | -------------
Kantone | Swiss canton | string | categorical variable
Bevölkerungsstand am 1. Jan  | Population on Jan 1 | population from corresponding canton | integer | quantitative variable

## Technology & Libraries
The project was created with Python and related libraries.
For the world map visualization you need two additional installations: `pip install pygal_maps_world` and `pip install pygal`.
Further information: http://www.pygal.org/en/stable/documentation/types/maps/pygal_maps_world.html
http://www.pygal.org/en/stable/

The other visualizations were created with the Altair Library and can be installed as follows: `pip install altair vega_datasets`.
Further information: https://altair-viz.github.io/getting_started/installation.html

For opening Excel files openpyxl has to be installed additionally: `pip install openpyxl`.
Further information: https://openpyxl.readthedocs.io/en/stable/

## Data Fetching & Preprocessing

1. save raw data: The refugee data are stored per year in a separate Excel. In the first step, all these raw data are downloaded from the webpage of the Federal Statistical Office. For this the script "Script_Data_Request.py" must be executed.
2. process the data: Now the data will be cleaned and merged with the script "Script_Data_Clean.py". Thereby all data from each year are added under each other. In addition, the data set is provided with three different columns (nation, gender, canton), which originate from the three different sheets in each Excel. However, only one of the just mentioned columns has a value and the others are empty (nan). This cleaned dataset is saved as "data_cleand.xlsx" and is used for the data analyses and visualizations. 
3. data analysis: For the data analysis the Juptyer notebook "DataStory.ipynb" must be executed. The data, which are still used in addition, are directly loaded, cleaned and used.

Note: for the data clean and fetch process, an executable Jupyter notebook "DataStory_Appendix.ipynb" is available in addition to the scripts.



&nbsp; 
&nbsp; 


# Datastory Asylgesuche in der Schweiz

By Hannah-Sarah Kühne & Tabea Eggler

## Ziel
Mit unserer Analyse möchten wir herausfinden, wie sich die Asylgesuche über die letzten 25 Jahre entwickelt haben. Dabei untersuchen wir die Verteilung der Asylgesuche nach Geschlechtern, die Aufschlüsselung der Entscheide über die Jahre, Länder spezifische Fakten und die Anzahl Gesuche nach Nationen. Zusätzlich sollen die kantonalen Verteilungen der Asylgesuche näher betrachtet werden.


## Datengrundlage
Unsere Daten wurden mit einem Python-Script am 15.10.2019 gesammelt. Es liegen 25 Tabellen mit Informationen zu Asylgesuchen in der Schweiz vor, welche vom Staatssekretariat für Migration (SEM) zur Verfügung gestellt werden. Jede Tabelle enthält Daten zu einem spezifischen Jahr. Pro Jahr/Tabelle sind die Daten zusätzlich in 30 Untertabellen gegliedert. Drei dieser 30 Untertabellen bieten die Möglichkeit, Informationen zu Asylgesuchen nach Kanton, nach Nation des Asylsuchenden oder Geschlecht einzusehen. Die restlichen Untertabellen ermöglichen einen vertieften Einblick in die kantonalen Strukturen. Es werden pro Kanton die Asylgesuche nach Nationalität des Asylsuchenden aufgezeigt. 

Zum Umfang pro Tabelle/Jahr: die kantonalen Übersichts-Untertabellen enthalten 27 Datenpunkte, bei den nationalen Untertabellen schwankt die Anzahl Datenpunkte je nach Jahr um den Wert 150, die geschlechterspezifische Untertabelle enthält pro Erhebungsjahr 3 Einträge. Zu den 26 Untertabellen, welche pro Kanton einen vertieften Einblick in die Asylstrukturen geben, kann keine allgemeingültige Aussage gemacht werden bezüglich der Anzahl Datenpunkte. Die Werte schwanken stark pro Jahr und Kanton, zwischen 20 und 150 Einträge. 

Zur Präprozessierung oder Filterung der Daten wurden keine Informationen Seitens des Staatssekretariats für Migration kundgegeben.

Abhängigkeiten zwischen Variabeln sind für die Attribute "Annerkennungsquote" und "Schutzquote" relevant. Die Annerkennungsquote ist von den Attributen "Asylgewährungen", "Ablehnungen", "Nichteintreten mit VA" und "Nichteintreten ohne VA" abhängig. Die Schutzquote ist, bis auf das Attribut "Nichteintreten ohne VA", von den selben Variabeln abhängig wie die Anerkennungsquote.

Beschreibung der Attribute
Allgemeiner Hinweis: In jeder Untertabelle werden prinzipiell dieselben Attribute verwendet. In drei der 30 Tabellen, ändert sich jeweils das erste Attribut. Einfachheitshalber werden alle Attribute nur einmal beschrieben. Die Einheit der Werte ist bei allen Attributen gewährleistet.

**Eigenschaften der Attribute**

Attribut  | Erklärung  |   Datentyp | Variablentyp
------------- | -------------  | ------------- | -------------
Kanton  | Jeweiliger Schweizer Kanton.  | String | kategorische Variable
Total neue Asylgesuche  | Totale Anzahl neuer Asylgesuche im entsprechenden Jahr. | Integer | quantitative Variable
Mehrfachgesuche nach neuem Asylgesetzt  | Ein neues Asylgesuch, das innerhalb von fünf Jahren nach Eintritt der Rechtskraft eines Asyl- und Wegweisungsentscheides gestellt wird, ist als Mehrfachgesuch unter den Bestimmungen von Artikel 111c AsylG zu behandeln.  | Integer | quantitative Variable
Wiederaufnahmen Asylgesuche  | Ein Asylgesuch wird erneut geprüft.  | Integer | quantitative Variable
Totale Erledigungen  |Anzahl Asylgesuche, die abgearbeitet wurden in diesem Jahr.  | Integer | quantitative Variable
Asylgewährungen  | Anzahl Asylgesuche, welche angenommen wurden pro Jahr.  | Integer | quantitative Variable
Ablehnungen mit VA  | Asylgesuch wurde abgelehnt. Asylsuchender wird vorläufig aufgenommen.  | Integer | quantitative Variable
Ablehnung ohne VA  | Asylgesuch wurde abgelehnt. Asylsuchender wird nicht aufgenommen.  | Integer | quantitative Variable
Nichteintreten mit VA  | Asylgesuch wird von den Behörden nicht vertieft geprüft. Asylsuchender wird vorläufig aufgenommen.  | Integer | quantitative Variable
Nichteintreten ohne VA  | Asylgesuch wird von den Behörden nicht vertieft geprüft. Asylsuchender wird nicht aufgenommen.  | Integer | quantitative Variable
Andere Erledigungen: Abschreibungen  | Bei Personen, die ohne triftigen Grund bei den Abklärungen der Behörden nicht mitwirken (= Verletzung der Mitwirkungspflicht), wird das Asylverfahren abgebrochen. Ein Verfahren kann auch beendet werden, wenn die asylsuchende Person den Behörden während mehr als 20 Tagen nicht zur Verfügung steht. Asylgesuche werden in diesen Fällen formlos abgeschrieben. Unbegründete oder wiederholt gleich begründete Mehrfachgesuche werden ebenfalls formlos abgeschrieben.  | Integer | quantitative Variable
Anerkennungsquote in % | Anteil der Asylgewährungen am Total aller Entscheide (Asylgewährungen, Ablehnungen und NEE) ohne Abschreibungen zum Zeitpunkt des erstinstanzlichen Entscheids.  | Float | quantitative Variable
Schutzquote in %  | Anteil der Asylgewährungen plus vorläufige Aufnahmen am Total aller Entscheide (Asylgewährungen, Ablehnungen und NEE) ohne Abschreibungen zum Zeitpunkt des erstinstanzlichen Entscheids.  | Float | quantitative Variable
Gesuche (Gruppen)  | Anzahl Gesuche im Bereich Asyl für Gruppen.  | Integer | quantitative Variable
Asylgewährungen (Gruppen)  | Anzahl angenommene Asylanträge für Gruppen.  | Integer | quantitative Variable
Abschreibungen (Gruppen)  | Anzahl Abschreibungen im Bereich Asylantrag für Gruppen.  | Integer | quantitative Variable
Kontinent/Nation  | Herkunftskontinent oder Land, aus welchem die Asylbeantragenden stammen.   | String | kategorische Variable
Geschlecht  | Geschlecht der Asylbeantragenden.  | String | kategorische Variable


## Zusätzliche Daten
Für die Analysen wurden zwei weitere Datensätze verwendet. Es wurde aus Zeitgründen auf ein automatisches Datensammlungs-Skript verzichtet, da bei einem Datensatz ein Login erforderlich ist. Es werden jeweils nur die relevanten Attribute beschrieben.

### IP2Location Country Multilingual Database
Da man für die Worldmap die Länder-Namen mit ihren Länderkürzel versehen muss, und die Länder im Hauptdatensatz auf Deutsch beschrieben sind, musste eine weitere Datenquelle benutzt werden.
Dieser Datensatz mappt die Country-Codes und Länder in verschiedenen Sprachen und kann nur mit einer Registrierung heruntergeladen werden (https://www.ip2location.com/free/country-multilingual)


Attribut  | Erklärung  |   Datentyp | Variablentyp
------------- | -------------  | ------------- | -------------
LANG_NAME  | Sprache  | String | kategorische Variable
COUNTRY_NAME  | Land (übersetzt in entsprechender Sprache)  | String | kategorische Variable
COUNTRY_ALPHA2_CODE  | 2-stelliger Länder-Code  | String | kategorische Variable

### Bilanz der ständigen Wohnbevölkerung nach Kanton, 1991-2018
Um das Verhältnis von Asylgesuchen verteilt auf die Kantone zu berechnen, wurde dieser zusätzliche Datensatz vom Bundesamt für Statistik verwendet. (https://www.bfs.admin.ch/bfs/de/home/statistiken/kataloge-datenbanken/tabellen.assetdetail.9486033.html)


Attribut  | Erklärung  |   Datentyp | Variablentyp
------------- | -------------  | ------------- | -------------
Kantone | Jeweiliger Schweizer Kanton  | String | kategorische Variable
Bevölkerungsstand am 1. Jan  | Bevölkerungsstand vom entsprechendem Kanton  | Integer | quantitative Variable

## Technology & Libraries
Das Projekt wurde mit Python und zugehörigen Libraries erstellt.
Für die World Map Visualisierung braucht es zwei zusätzliche Installationen: `pip install pygal_maps_world` und `pip install pygal`
Weitere Informationen: http://www.pygal.org/en/stable/documentation/types/maps/pygal_maps_world.html
http://www.pygal.org/en/stable/

Die weiteren Visualisierungen wurden mit der Altair Library erstellt und kann wie folgt installiert werden: `pip install altair vega_datasets`.
Weitere Informationen: https://altair-viz.github.io/getting_started/installation.html

Für das Öffnen von Excel Datein muss zusätzlich openpyxl installiert werden: `pip install openpyxl`
Weitere Informationen: https://openpyxl.readthedocs.io/en/stable/

## Data Fetching & Preprocessing

1.  Rohdaten abspeichern: Die Flüchtlings-Daten sind pro Jahr in einem eigenen Excel gespeichert. Es werden im ersten Schritt all diese Rohdaten von der Webpage vom Bundesamt für Statistik heruntergeladen. Dafür muss das Skript "Script_Data_Request.py" ausgeführt werden.
2.  Daten aufarbeiten: Nun werden die Daten mit dem Skript "Script_Data_Clean.py" bereinigt und zusammengeführt. Dabei werden alle Daten von jedem Jahr untereinander hinzugefügt. Zusätzlich wird der Datensatz mit drei verschiedenen Spalten (Nation, Geschlecht, Kanton) versehen, welche von den drei unterschiedlichen Sheets in jedem Excel stammen. Dabei hat aber immer nur einer der gerade erwähnten Spalte ein Wert und die anderen sind leer (nan). Dieser bereinigte Datensatz wird als "data_cleand.xlsx" gespeichert und wird für die Datenanalysen und Visualisierungen verwendet. 
3.  Datenanalyse: Für die Datenanalyse muss das Juptyer Notebook "DataStory.ipynb" geöffnet ausgeführt werden. Die Daten, welche noch zusätzlich verwendet werden, werden direkt geladen, gereinigt und benutzt.

Anmerkung: für den Data Clean und Fetch Prozess steht nebst den Scripts auch ein ausführbares Jupyter Notebook "DataStory_Appendix.ipynb" zur Verfügung
