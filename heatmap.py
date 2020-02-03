import pandas as pd
import numpy as np
import altair as alt

def get_data_of_year_format1(year):
    """formats data for specific year
    
        Parameters: specific year (int)

        Returns: formatted data for specific year (DataFrame)

       """    
    sheet = year
    df = pd.read_excel('./Data/data_einwohner_kanton_ROW.xlsx', sheet_name = year, skiprows=5, nrows=26)
    df.columns = ["Kanton", "Bewohner", 1, 1, 1, 1, 1, 1, 1, 1]
    df = df.drop(df.columns.difference(["Kanton", "Bewohner"]), axis=1)
    df.insert(0, "Jahr", year)
    return df


def get_data_of_year_format2(year):
    """formats data for specific year (Different excel layout)
    
        Parameters: specific year (int)

        Returns: formatted data for specific year (DataFrame)

       """    
    sheet = year
    df = pd.read_excel('./Data/data_einwohner_kanton_ROW.xlsx', sheet_name = year, skiprows=4, nrows=26)
    df.columns = ["Kanton", "Bewohner", 1, 1, 1, 1, 1, 1, 1, 1]
    df = df.drop(df.columns.difference(["Kanton", "Bewohner"]), axis=1)
    df.insert(0, "Jahr", year)
    return df


def clean_canton_habitant_data():
    """cleans and prepares habitant data for all cantons
    
        Parameters: None

        Returns: cleand canton habitant data (DataFrame)

       """    
    df_kanton = pd.DataFrame()
    
    #layout data
    for i in range(1994, 2011):
        df = get_data_of_year_format1(str(i))
        df_kanton = pd.concat([df_kanton, df], axis = 0, sort = True)
    for i in range(2011, 2019):
        df = get_data_of_year_format2(str(i)) 
        df_kanton = pd.concat([df_kanton, df], axis=0, sort = True) 
        
    #force same naming
    df_kanton['Kanton'].replace(
        to_replace='Appenzell A.Rh.',
        value='Appenzell A. Rh.',
        inplace=True
    )
    df_kanton['Kanton'].replace(
        to_replace='Appenzell I.Rh.',
        value='Appenzell I. Rh.',
        inplace=True
    )
    df_kanton['Kanton'].replace(
        to_replace='Basel-Landschaft',
        value='Basel-Land',
        inplace=True
    )
    df_kanton['Kanton'].replace(
        to_replace='St.Gallen',
        value='St. Gallen',
        inplace=True
    )
    #save to excel
    #df_kanton.to_excel("./Data/data_einwohner_kanton_CLEANED.xlsx")
    
    return df_kanton


def get_canton_list():
    """returns a list with all cantons from canton habitant dataset
    
        Parameters: None

        Returns: list with all cantons

       """   
    df_get_all_Kantone = pd.read_excel('./Data/data_cleaned.xlsx', nrows=26)
    return df_get_all_Kantone['Kanton'].tolist()


def calculate_percentage(habitants, number):
    """calculates the ratio between two numbers
    
        Parameters:
        habitants (int): total habitants of specific canton
        number (int): specific value (For example Asylgesuche, Asylgewährungen...)

        Returns: ratio (int)

       """ 
    return 100 * number / habitants


def calculate_percentage_refugee_data(df_kanton):
    """adds the calculated percentage of "Asylgewährungen" and "Total neue Asylgesuche" to the dataframe
    
        Parameters: cleaned canton dataframe

        Returns: Refugee dataframe with "Bewohner pro Kanton", "Gewährungen in Prozent" and "Neue Gesuche in Prozent"

       """ 
    #import df refugees
    df_refugees = pd.read_excel('./Data/data_cleaned.xlsx')
    #insert new cols
    df_refugees.insert(0, 'Bewohner', np.nan)
    df_refugees.insert(1, 'Gewährungen in Prozent', 0)
    df_refugees.insert(2, 'Neue Gesuche in Prozent', 0)
    
    for j in range(1994, 2019):
        for k in get_canton_list():
            #find values
            bewohner = df_kanton.loc[(df_kanton['Jahr'] == str(j)) &(df_kanton['Kanton'] == str(k))]['Bewohner'].values[0]
            gewährungen = df_refugees.loc[(df_refugees['Jahr'] == j) & (df_refugees['Kanton'] == str(k))]['Asyl-\ngewährungen'].values[0]
            neue_gesuche = df_refugees.loc[(df_refugees['Jahr'] == j) & (df_refugees['Kanton'] == str(k))]['Total\nneue Asyl-\ngesuche\n'].values[0]
            #set values in df
            df_refugees.loc[(df_refugees['Jahr'] == j) & (df_refugees['Kanton'] == str(k)), ['Bewohner']] = bewohner
            df_refugees.loc[(df_refugees['Jahr'] == j) & (df_refugees['Kanton'] == str(k)), ['Gewährungen in Prozent']] = calculate_percentage(bewohner, gewährungen)
            df_refugees.loc[(df_refugees['Jahr'] == j) & (df_refugees['Kanton'] == str(k)), ['Neue Gesuche in Prozent']] = calculate_percentage(bewohner, neue_gesuche)
        
        
    return df_refugees
   
    
def generate_heatmap_gewaehrungen(df_refugees):
    """generates heatmap: "Gewährungen in Prozent"
    
        Parameters: Refugee Dataframe with procent values

        Returns: heatmaps graph

       """ 
    df_refugees = df_refugees.drop(df_refugees[df_refugees.Kanton == 'Ohne Angabe'].index)
    df_refugees = df_refugees.dropna(subset=['Kanton']) 

    source = pd.DataFrame({'Jahre': df_refugees['Jahr'].ravel(),
                     'Kantone': df_refugees['Kanton'].ravel(),
                     'Flüchtlingsanteil': df_refugees['Gewährungen in Prozent'].ravel()})

    chart1 = alt.Chart(source, title="Asylgewährungen pro Kanton im Verhältnis zur Einwohnerzahl").mark_rect().encode(
        x='Jahre:O',
        y='Kantone:O',
        color='Flüchtlingsanteil:Q'
    ).properties(
    width=350,
    height=350
    )
    
    return chart1

def generate_heatmap_neue_gesuche(df_refugees):
    """generates heatmap: "Neue Gesuche un Prozent"
    
        Parameters: Refugee Dataframe with procent values

        Returns: heatmaps graph

       """ 
    df_refugees = df_refugees.drop(df_refugees[df_refugees.Kanton == 'Ohne Angabe'].index)
    df_refugees = df_refugees.dropna(subset=['Kanton']) 

    source = pd.DataFrame({'Jahre': df_refugees['Jahr'].ravel(),
                     'Kantone': df_refugees['Kanton'].ravel(),
                     'Flüchtlingsanteil': df_refugees['Neue Gesuche in Prozent'].ravel()})

    chart2 = alt.Chart(source, title="Verteilung der neuen Flüchtlingsgesuche pro Kanton im Verhältnis zur Einwohnerzahl").mark_rect().encode(
        x='Jahre:O',
        y='Kantone:O',
        color='Flüchtlingsanteil:Q'
    ).properties(
    width=350,
    height=350
    )
    
    return chart2