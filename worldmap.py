import pandas as pd
import numpy as np
import altair as alt
import pygal
from pygal_maps_world.maps import World
from pygal_maps_world.maps import COUNTRIES
from pygal.style import Style
from IPython.display import display, HTML

def get_country_code(country_name, country_dict):
    """returns the country code of specific country
    
        Parameters:
        country_name: Name of the country in english (String)
        country_dict: Dictionary with country - country code mapping (Dictionary)

        Returns: country code if found, otherwise original country name (String)

       """    
    for key, value in country_dict.get('COUNTRY_ALPHA2_CODE').items():
        if key in country_name:
            return str(value).lower()
    return country_name


def replace_manual_country_code(country_name, code, df_nation_counts):
    """replaces a manuel set country code in given dataframe
    
        Parameters:
        country_name: Name of the country in english (String)
        code: Country Code of specific country-name (String)
        df_nation_counts: DataFrame in which the country-name should be replaced

        Returns: modified DataFrame

       """    
    df_nation_counts.loc[df_nation_counts['Nation'] == country_name, ['Nation']] = code
    return df_nation_counts
    
    
def replace_nation_code():
    """imports refugee data and replaces countries with its country code. Since the countrie names must be in english, an external dataset which provides the countries and its code in several languages is needed. Some must be handled separately.
    
        Parameters: None

        Returns: prepared DataFrame for vizualisation

       """   
    #import data
    df_refugees = pd.read_excel('./Data/data_cleaned.xlsx')
    
    #filter df_refugees by nation & asylgesuche
    df_map = df_refugees[['Total\nneue Asyl-\ngesuche\n', 'Nation']]
    df_map = df_map.dropna(subset=['Nation'])

    #sum all asylgesuche for all years by nation
    series_nation_counts = df_map.groupby('Nation')['Total\nneue Asyl-\ngesuche\n'].sum()
    df_nation_counts = pd.DataFrame({'Nation':series_nation_counts.index, 'Anzahl Gesuche':series_nation_counts.values})

    #replace country with its code
    df_country_code = pd.read_csv('./Data/country_codes_RAW.CSV', index_col=5)
    df_country_code = df_country_code.drop(['LANG', 'LANG_NAME', 'COUNTRY_ALPHA3_CODE', 'COUNTRY_NUMERIC_CODE'], 1)
    country_dict = df_country_code.to_dict('dict')
    
    #replace country by its code from country data set
    df_nation_counts['Nation'] = df_nation_counts['Nation'].apply(lambda x: get_country_code(x, country_dict))
    
    #Replace not found countries
    manual_country_codes = {'Bosnien u. Herzegowina':'ba',
                            'Korea (Nord)':'kp',
                            'Korea (Süd)':'kr',
                            'Sao Tomé u. Principe':'st',
                            'Slowakische Republik':'sk',
                            'Tschechische Republik':'cz',
                            'V. A. Emirate':'ae',
                            'Zentralafr. Republik':'cf',
                            'Grossbritannien':'gb',
                            'Kapverden':'cv'}

    for key, value in manual_country_codes.items():
        df_nation_counts = replace_manual_country_code(key, value, df_nation_counts)
        
    #Add Kosovo to Serbia
    kosovo_value = df_nation_counts.loc[(df_nation_counts.Nation == 'Kosovo'), 'Anzahl Gesuche']
    serbia_value = df_nation_counts.loc[(df_nation_counts.Nation == 'rs'), 'Anzahl Gesuche']
    sum_kosovo_serbia = kosovo_value.values[0] + serbia_value.values[0]
    df_nation_counts.loc[df_nation_counts['Nation'] == 'rs', ['Anzahl Gesuche']] = sum_kosovo_serbia

    #df_nation_counts.to_excel("./Data/country_codes_CLEANED.xlsx")
    return df_nation_counts
    
    
def generate_worldmap(df_nation_counts):
    """displays a worldmap coded with the pygal-library in HTML format (interactive Chart)
    
        Parameters: Nations Count Dataframe

        Returns: HTML worldmap

       """ 
    total_dict = df_nation_counts.set_index('Nation').to_dict('dict').get('Anzahl Gesuche')
    dict_1_5000 = dict(filter(lambda elem: elem[1] <= 5000, total_dict.items()))
    dict_5000_20000 = dict(filter(lambda elem: (elem[1] > 5000 and elem[1] <= 20000), total_dict.items()))
    dict_20000_plus = dict(filter(lambda elem: (elem[1] > 20000), total_dict.items()))
    
    base_html = """
    <!DOCTYPE html>
    <html>
      <head>
      <script type="text/javascript" src="https://kozea.github.io/pygal.js/2.0.x/pygal-tooltips.min.js"></script>
      <script type="text/javascript" src="http://kozea.github.com/pygal.js/javascripts/pygal-tooltips.js"></script>
      </head>
      <body>
        <figure>
          {rendered_chart}
        </figure>
      </body>
    </html>
    """
    #styles
    custom_style = Style(
        colors=('#e4ed80', '#7dccbc', '#63192e'),
        tooltip_font_size=8,
        legend_font_size=7,
        title_font_size=10,
        background='#ffffff')

    #define chart
    worldmap_chart = World(style=custom_style)
    worldmap_chart.title = 'Anzahl Asylgesuche nach Nation'
    worldmap_chart.add('1-5000 Gesuche', dict_1_5000)
    worldmap_chart.add('5000-20000 Gesuche', dict_5000_20000)
    worldmap_chart.add('20000+ Gesuche', dict_20000_plus)

    #render
    rendered_chart = worldmap_chart.render(is_unicode=True)
    plot_html = base_html.format(rendered_chart=rendered_chart)
    return display(HTML(plot_html))

    
def get_worldmap():
    """main-function to plot worldmap
    
        Parameters: None

        Returns: worldmap graph

       """ 
    df_nation_counts = replace_nation_code()
    return generate_worldmap(df_nation_counts)