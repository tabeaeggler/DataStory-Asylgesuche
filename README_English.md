# Datastory Asylum Applications in Switzerland

By Hannah-Sarah Kühne & Tabea Eggler

## Goal
With this analysis, we want to find out how asylum applications in Switzerland have developed over the last 25 years. We examine the distribution of asylum applications by gender, the breakdown of decisions over the years, country-specific facts, and the number of applications by nation. In addition, the cantonal distributions of asylum applications have been examined in more detail.

## Result
The analysis with the corresponding graphs can be seen in the following Jupiter Notebook <b>"DataStory_English.ipynb"</b>. This is also available as PDF <b>"Export_DataStory_English.pdf".</b>

## Data basis
The data was collected using a Python script on 10/15/2019. There are 25 tables with information on asylum applications in Switzerland provided by the State Secretariat for Migration (SEM). Each table contains data on a specific year. For each year/table, the data are additionally divided into 30 sub-tables. Three of these 30 sub-tables offer the possibility to view information on asylum applications by canton, by a nation of the asylum seeker, or by gender. The remaining sub-tables provide a more in-depth look at cantonal structures.  

Regarding the scope per table/year: the cantonal overview sub-tables contain 27 data points, for the national sub-tables the number of data points fluctuates around 150 depending on the year, the gender-specific sub-table contains 3 entries per survey year. No general statement can be made regarding the number of data points for the 26 sub-tables, which provide an in-depth insight into the asylum structures per canton. The values vary greatly per year and canton, between 20 and 150 entries. 

The State Secretariat for Migration did not provide any information on the pre-processing or filtering of the data.

Dependencies between variables are relevant for the attributes "Annerkennungsquote" (recognition rate) and "Schutzquote" (protection rate). The recognition rate is dependent on the attributes "Asylgewährungen" (asylum granted), "Ablehnungen" (rejections), "Nichteintreten mit VA" (non-admission with decision) and "Nichteintreten ohne VA" (Non-admission without decision). The protection rate depends on the same variables as the recognition rate, except for the attribute "Nichteintreten ohne VA" (non-entry without VA).

**Description of the attributes**
General note: In principle, the same attributes are used in each sub-table. In three of the 30 tables, the first attribute changes in each case. For simplicity, all attributes are described only once. The unit of the values is guaranteed for all attributes.

Attribute | Translation | Explanation | Data type | Variable type
------------- | -------------  | ------------- | ------------- | -------------
Kanton  | Canton | Swiss Canton.  | string | categorical variable
Total neue Asylgesuche  | Total new asylum applications | Total number of new asylum applications in the corresponding year. | integer | quantitative variable
Mehrfachgesuche nach neuem Asylgesetzt  | Multiple applications under the new Asylum Act | A new asylum application filed within five years of the entry into force of an asylum and removal decision is to be treated as a multiple application under the provisions of Article 111c Asylum Act.  | integer | quantitative variable
Wiederaufnahmen Asylgesuche  | Reopening of asylum applications | An asylum application is reexamined.  | integer | quantitative variable
Totale Erledigungen | Totally done | Gesamtzahl der in diesem Jahr bearbeiteten Asylanträge | integer | quantitative Variable
Asylgewährungen  | Asylum Grants | Number of asylum applications accepted per year  | integer | quantitative variable
Ablehnungen mit VA  | Rejections with VA | Asylum application rejected. Asylum seeker is provisionally admitted.  | integer | quantitative variable
Ablehnung ohne VA  | Rejections without VA | Asylum application rejected. Asylum seeker is not admitted.  | integer | quantitative variable
Nichteintreten mit VA  | No entry with VA | Asylum application is not examined in depth by the authorities. Asylum seeker is provisionally admitted.  | integer | quantitative variable
Nichteintreten ohne VA  | Non-admission without VA | Asylum application is not examined in depth by the authorities. Asylum seeker is not admitted.  | integer | quantitative variable
Andere Erledigungen: Abschreibungen  | Other settlements: Write-offs | In the case of persons who do not cooperate with the authorities' clarifications without good reason (= violation of the duty to cooperate), the asylum procedure is terminated. A procedure can also be terminated if the asylum seeker is not available to the authorities for more than 20 days. Asylum applications are written off informally in these cases. Unfounded or repeated multiple applications with the same grounds are also written off informally.  | integer | quantitative variable
Anerkennungsquote in % | Recognition rate in % | Share of asylum granted in total of all decisions (asylum granted, rejections, and NEE) excluding write-offs at the time of the first-instance decision.  | float | quantitative variable
Schutzquote in %  | Protection rate in % | Share of asylum grants plus temporary admissions in the total of all decisions (asylum grants, rejections, and NEE) excluding write-offs at the time of the first-instance decision.  | float | quantitative variable
Gesuche (Gruppen)  | Applications (groups) | number of applications in the area of asylum for groups.  | integer | quantitative variable
Asylgewährungen (Gruppen)  | Asylum granted (groups) | number of asylum applications accepted for groups.  | integer | quantitative variable
Abschreibungen (Gruppen)  | Depreciations (groups) | Number of depreciations in the area of asylum application for groups.  | integer | quantitative variable
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
