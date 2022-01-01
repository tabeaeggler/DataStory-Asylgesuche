(Datastory Asylum Applications in Switzerland: english translation in "README_English.md")

# Datastory Asylgesuche in der Schweiz

By Hannah-Sarah Kühne & Tabea Eggler

## Ziel
Mit unserer Analyse möchten wir herausfinden, wie sich die Asylgesuche über die letzten 25 Jahre entwickelt haben. Dabei untersuchen wir die Verteilung der Asylgesuche nach Geschlechtern, die Aufschlüsselung der Entscheide über die Jahre, Länder spezifische Fakten und die Anzahl Gesuche nach Nationen. Zusätzlich sollen die kantonalen Verteilungen der Asylgesuche näher betrachtet werden.

## Ergebnis
Die Analyse mit den zugehörigen Grafiken ist im folgenden Jupiter Notebook ersichtlich "DataStory_German.ipynb". Dies ist auch als PDF "Export_DataStory_German.pdf" verfügbar.

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
