import pandas as pd
import numpy as np
import altair as alt

#import data
dataset = pd.read_excel("./Data/data_cleaned.xlsx")

def get_year_gender_df(gender):
    """returns df grouped by year with new asylum soughts for each gender
    
       Parameters: specific gender as text (String)

       Returns: DataFrame
       
    """    
    group = dataset.groupby('Jahr')
    s_gender = group.apply(lambda x: dataset['Total\nneue Asyl-\ngesuche\n'].loc[x[x['Geschlecht'] == gender].index])
    s_gender = s_gender.reset_index(drop=True)
    df_gender = s_gender.to_frame()
    
    df_gender.rename(columns = {df_gender.columns[0]: 'Total'}, inplace=True)
    s_year_total = group.apply(lambda x: x[x['Kanton'].isnull() == False]['Total\nneue Asyl-\ngesuche\n'].sum())
    df_year_total = s_year_total.to_frame()
    df_year_total.rename(columns = {df_year_total.columns[0]: 'End'}, inplace=True)
    df_year_total.reset_index(inplace=True)
    
    if(gender == 'Frauen'):
        df_year_total['End'] = df_gender['Total']
    df_year_total['Gender'] = gender
    
    return df_year_total

def get_year_gender_status_df(gender):
    """returns df grouped by year with shelter and recognition data for each gender
    
       Parameters: specific gender as text (String)

       Returns: DataFrame

    """    
    group_status = dataset.groupby('Jahr')
    s_gender_status = group_status.apply(lambda x: dataset['Schutz-\nquote\nin % *\n'].loc[x[x['Geschlecht'] == gender].index])
    df_gender_status = s_gender_status.to_frame()
    df_gender_status.rename(columns = {df_gender_status.columns[0]: 'Schutzquote'}, inplace=True)
    
    df_gender_status['Gender'] = gender
    df_gender_status['Anerkennungsquote'] = group_status.apply(lambda x: dataset['Aner-\nkennungs-\nquote\nin % *'].loc[x[x['Geschlecht'] == gender].index])
    df_gender_status.reset_index(inplace=True)
    df_gender_status.drop(columns="level_1", inplace=True)
    
    return df_gender_status
    

def get_gender_overview_graph():
    """returns all gender related graphs
    
       Parameters: None

       Returns: Graph
       
    """
    male = get_year_gender_df('Männer')
    female = get_year_gender_df('Frauen')

    male['Start'] = female['End']
    male['Display'] = male['End'] - female['End']
    female['Start'] = 0
    female['Display'] = female['End']
    combined = pd.concat([male, female], axis=0)
    
    print()
    print('Totale Anzahl Asylanträge über die letzten 25 Jahre:')
    print(male['End'].sum())
    print()
    
    male_status = get_year_gender_status_df('Männer')
    female_status = get_year_gender_status_df('Frauen')
    combined_status = pd.concat([male_status, female_status], axis=0)

    color_scale = alt.Scale(
        domain=[
            "Frauen",
            "Männer"
        ],
        range=["#e5f5b8", "#58bdc0"]
    )

    bars = alt.Chart(combined).mark_bar().encode(
        x=alt.X('Start:Q', title='Anzahl Asylgesuche'),
        x2=alt.X2('End:Q', title=''),
        y=alt.Y('Jahr:N'),
        color=alt.Color(
            'Gender:N',
            legend=alt.Legend( title='Gender'),
            scale=color_scale,
        )
    )

    text = bars.mark_text(
        align='left',
        baseline='middle',
        dx=3
    ).encode(
        x= 'End:Q',
        y='Jahr:N',
        text=alt.Text('Display:Q')
    )
        
    line_chart_accepted = alt.Chart(combined_status).mark_line().encode(
        alt.X('Jahr:O'),
        alt.Y('Anerkennungsquote:Q', axis=alt.Axis(format='%')),
        color='Gender:N'
    )
    
    line_chart_shelter = alt.Chart(combined_status).mark_line().encode(
        alt.X('Jahr:O'),
        alt.Y('Schutzquote:Q', axis=alt.Axis(format='%')),
        color='Gender:N'
    )

    line_charts = alt.vconcat(line_chart_accepted.properties(height=220, title='Annerkennungsquote nach Geschlecht'), line_chart_shelter.properties(height=220, title='Schutzquote nach Geschlecht'))
    return alt.hconcat((bars + text).properties(height=540, title='Anzahl Asylgesuche über die Jahre, aufgeschlüsselt nach Geschlecht'), line_charts)

def get_accepted_declined_overview_graph():
    """returns graph with overview of accepted and declined asylum soughts
    
       Parameters: None

       Returns: Graph

    """
    group_year = dataset.groupby('Jahr')
    s_accepted = group_year.apply(lambda x: x[x['Kanton'].isnull() == False]['Asyl-\ngewährungen'].sum())
    df_accepted = s_accepted.to_frame()
    df_accepted.rename(columns = {df_accepted.columns[0]: 'End'}, inplace=True)
    
    df_accepted['Abschreibungen'] = group_year.apply(lambda x: x[x['Kanton'].isnull() == False]['Andere Erledi-\ngungen:\nAbschrei-\nbungen '].sum())
    df_accepted['Entscheid'] = 'Asylgewährungen'
    df_accepted['Start'] = 0
    df_accepted['Display'] = df_accepted['End']
    df_accepted.reset_index(inplace=True)
    
    s_declined = group_year.apply(lambda x: x[x['Kanton'].isnull() == False]['Total\nErledi-gungen\n\n'].sum())
    df_declined = s_declined.to_frame()
    df_declined.rename(columns = {df_declined.columns[0]: 'End'}, inplace=True)
    df_declined.reset_index(inplace=True)
    
    df_declined['Entscheid'] = 'Andere Entscheide'
    df_declined['Start'] = df_accepted['End']
    df_declined['Display'] = df_declined['End'] - df_accepted['Display']
    df_outcome = pd.concat([df_accepted, df_declined], axis=0, sort=False)
    
    print()
    print('Totale Anzahl Asylgewährungen über die letzten 25 Jahre:')
    print(df_accepted['End'].sum())
    print('Totale andere Entscheide über die letzten 25 Jahre:')
    print(df_declined['Display'].sum())
    print()

    #line chart
    df_accepted_percentage = df_accepted['Display'] / (df_declined['End']-df_accepted['Abschreibungen'])
    df_accepted_percentage = df_accepted_percentage.to_frame()
    df_accepted_percentage.rename(columns = {df_accepted_percentage.columns[0]: 'Anerkennungsquote'}, inplace=True)
    df_accepted_percentage['Jahr'] = df_accepted['Jahr']

    color_scale = alt.Scale(
        domain=[
            "Asylgewährungen",
            "Andere Entscheide"
        ],
        range=["#79cbbc", "#217bb5"]
    )

    bars = alt.Chart(df_outcome).mark_bar().encode(
        x = alt.X('Jahr:N'),
        y=alt.Y('Start:Q', title='Anzahl Entscheide'),
        y2 = alt.Y2('End:Q', title=''),
        color=alt.Color(
            'Entscheid:N',
            legend=alt.Legend( title='Entscheid'),
            scale=color_scale,
        )
    )

    chartLine = alt.Chart(df_accepted_percentage).mark_line().encode(
        x='Jahr:N',
        y=alt.Y('Anerkennungsquote:Q', title='Anerkennungsquote')
    )
    
    mean = alt.Chart(df_accepted_percentage).mark_rule(color='red').encode(
        y=alt.Y('mean(Anerkennungsquote):Q', title='Mittelwert')
    )

    return alt.hconcat((chartLine + mean).properties(width = 400, title='Anerkennungsquote über die Jahre'), bars.properties(width = 400, title='Anzahl Asylgesuche über die Jahre, aufgeschlüsselt nach Entscheid'))

def get_status_df(decision, title):
    """returns df with status of asylum soughts
    
       Parameters:
       decision: decision typ from orginal data (String)
       title: new corrected decision typ (String)

       Returns: DataFrame

    """
    group_year_status = dataset.groupby('Jahr')
    s_total = group_year_status.apply(lambda x: x[x['Kanton'].isnull() == False]['Total\nErledi-gungen\n\n'].sum())
    s_status = group_year_status.apply(lambda x: x[x['Kanton'].isnull() == False][decision].sum())
    df_status = s_status.to_frame()
    df_status.rename(columns = {df_status.columns[0]: 'Wert'}, inplace=True)
    df_status['Wert']= df_status['Wert'] / s_total
    df_status['Entscheid'] = title
    df_status.reset_index(inplace=True)
    
    return df_status

def get_decision_status_graph():
    """returns graph with all statuses of asylum soughts
    
       Parameters: None

       Returns: Graph

    """
    df_accepted = get_status_df('Asyl-\ngewährungen','Asylgewährungen')
    df_declined_no_admission = get_status_df('Ablehnungen\nohne VA','Ablehnung ohne VA')
    df_declined_with_admission = get_status_df('Ablehnungen mit VA','Ablehnung mit VA')
    df_not_enter_no_admission = get_status_df('Nichteintreten ohne VA','Nichteinretensentscheid ohne VA')
    df_not_enter_with_admission = get_status_df('Nichteintreten mit VA','Nichteinretensentscheid mit VA')
    df_depreciation = get_status_df('Andere Erledi-\ngungen:\nAbschrei-\nbungen ','Abschreibungen')
    df_all_decisions = pd.concat([df_accepted, df_declined_no_admission, df_declined_with_admission, df_not_enter_no_admission, df_not_enter_with_admission, df_depreciation], axis=0)

    decision_graph = alt.Chart(df_all_decisions).mark_area().encode(
    x=alt.X("Jahr:N"),
    y=alt.Y("Wert:Q", title='Prozentualer Anteil'),
    color="Entscheid:N"
    ).properties(height=350, width=600, title='Asylgesuche aufgeschlüsselt nach Entscheid')
    
    return decision_graph

def get_nations_df():
    """returns df grouped by nations
    
       Parameters: None

       Returns: DataFrame

    """
    exclude = dataset['Nation'].isin(['Nordafrika', 'Total Amerika', 'Subsahara', 'Ozeanien','Afrika','Nordamerika', 'Amerika', 'Asien', 'Europa', 'Herkunft unbekannt',       'Total Europa', 'Staatenlos', 'Ohne Nationalität', 'Staat unbekannt', 'Ohne Angabe', 'Total Herkunft unbek.', 'Total Ozeanien', 'Total Afrika', 'Total Asien'])
    df_unique_nations = dataset.drop(dataset[exclude].index)
    df_unique_nations.dropna(subset=['Nation'], how='all', inplace=True)
    
    group_nation = df_unique_nations.groupby('Nation')
    s_nation_apply = group_nation['Total\nneue Asyl-\ngesuche\n'].sum()
    df_nation = s_nation_apply.to_frame()
    df_nation.rename(columns = {df_nation.columns[0]: 'Total Asylgesuche pro Land'}, inplace=True)
    
    df_nation['Total Asylgewährungen pro Land'] = group_nation['Asyl-\ngewährungen'].sum()
    df_nation['Schutzgewährungen'] = df_nation['Total Asylgewährungen pro Land'] + group_nation['Ablehnungen mit VA'].sum() + group_nation['Nichteintreten mit VA'].sum()
    df_nation['Verhältnis der Asylgewährungen zu Asylgesuchen'] = df_nation['Total Asylgewährungen pro Land'] / df_nation['Total Asylgesuche pro Land']
    df_nation['Abschreibungen'] = group_nation['Andere Erledi-\ngungen:\nAbschrei-\nbungen '].sum()
    df_nation.reset_index(inplace=True)
    
    return df_nation
   
    
def get_most_applied_graph(): 
    """returns graph with all countries that applied most
    
       Parameters: None

       Returns: Graph

    """
    df_nation = get_nations_df()
    
    print()
    print("Anzahl Länder, von welchen die Asylbeantragenden stammen:")
    print(df_nation.shape[0])
    print()

    df_nation_sort = df_nation.sort_values('Total Asylgesuche pro Land', ascending=False)
    df_nation_sort = df_nation_sort.iloc[:10]

    chart_apply = alt.Chart(df_nation_sort).mark_bar().encode(
        x='Total Asylgesuche pro Land:Q',
        y= alt.Y('Nation:N', sort=alt.SortField(field="Total Asylgesuche pro Land", order='descending'))
    )

    text_apply = chart_apply.mark_text(
        align='left',
        baseline='middle',
        dx=3
    ).encode(
        text='Total Asylgesuche pro Land:Q'
    )

    chart_accepted = alt.Chart(df_nation_sort).mark_bar().encode(
        x = alt.X('Total Asylgewährungen pro Land:Q', scale=alt.Scale(domain=(0,100000))),
        y=alt.Y('Nation:O', sort=alt.SortField(field="Total Asylgesuche pro Land", order='descending'))
    )

    text_accepted = chart_accepted.mark_text(
        align='left',
        baseline='middle',
        dx=3
    ).encode(
        text='Total Asylgewährungen pro Land:Q'
    )
    
    chart_shelter = alt.Chart(df_nation_sort).mark_bar().encode(
        x = alt.X('Schutzgewährungen:Q', scale=alt.Scale(domain=(0,100000))),
        y=alt.Y('Nation:O', sort=alt.SortField(field="Total Asylgesuche pro Land", order='descending'))
    )

    text_shelter = chart_shelter.mark_text(
        align='left',
        baseline='middle',
        dx=3
    ).encode(
        text='Schutzgewährungen:Q'
    )

    return alt.hconcat((chart_apply + text_apply).properties(width = 250, height=150, title='Top 10 Länder mit den meisten Asylgesuchen'), (chart_accepted +            text_accepted).properties(width = 250, height=150, title='Anzahl angenommene Gesuche'), (chart_shelter + text_shelter).properties(width = 250, height=150, title='Anzahl Schutzgewährungen'))

def get_most_accepted_graph():
    """returns graph with all countries that were most accepted
    
       Parameters: None

       Returns: Graph

    """
    df_nation = get_nations_df()
    df_nation_accepted_sort_desc = df_nation.sort_values('Verhältnis der Asylgewährungen zu Asylgesuchen', ascending=False)
    df_nation_accepted_sort_desc = df_nation_accepted_sort_desc.iloc[:10]

    df_nation_most_accepted = df_nation.sort_values('Total Asylgewährungen pro Land', ascending=False)
    df_nation_most_accepted = df_nation_most_accepted.iloc[:10]

    chart_most_accepted_percentage = alt.Chart(df_nation_accepted_sort_desc).mark_bar().encode(
        x='Verhältnis der Asylgewährungen zu Asylgesuchen:Q',
        y=alt.Y('Nation:O', sort=alt.SortField(field="Verhältnis der Asylgewährungen zu Asylgesuchen", order='descending'))
    )

    text_most_accepted_percentage = chart_most_accepted_percentage.mark_text(
        align='left',
        baseline='middle',
        dx=3
    ).encode(
        text='Total Asylgesuche pro Land:Q'
    )

    chart_most_accepted = alt.Chart(df_nation_most_accepted).mark_bar().encode(
        x='Total Asylgewährungen pro Land:Q',
        y=alt.Y('Nation:O', sort=alt.SortField(field="Total Asylgewährungen pro Land", order='descending'))
    )

    text_most_accepted = chart_most_accepted.mark_text(
        align='left',
        baseline='middle',
        dx=3
    ).encode(
        text='Total Asylgewährungen pro Land:Q'
    )

    return alt.hconcat((chart_most_accepted + text_most_accepted).properties(width = 250, height=150, title='Top 10 Länder mit den meisten angenommenen Gesuchen'), (chart_most_accepted_percentage + text_most_accepted_percentage).properties(width = 250, height=150, title='Top 10 Länder mit den prozentual meisten angenommenen Gesuchen'))

def get_none_accepted_graph():
    """returns graph with countries that were always declined
    
       Parameters: None

       Returns: Graph

    """
    df_nation = get_nations_df()
    df_nation_percentage_sort_asc = df_nation.sort_values('Verhältnis der Asylgewährungen zu Asylgesuchen')
    all_rejected = df_nation_percentage_sort_asc['Total Asylgewährungen pro Land'] == 0
    df_nation_percentage_sort_asc = df_nation_percentage_sort_asc[all_rejected]
    df_nation_percentage_sort_asc.drop(df_nation_percentage_sort_asc.index[df_nation_percentage_sort_asc['Total Asylgesuche pro Land'] == 0], inplace = True)
    df_nation_percentage_sort_asc= df_nation_percentage_sort_asc.sort_values('Total Asylgesuche pro Land', ascending=False)
    df_nation_percentage_sort_asc = df_nation_percentage_sort_asc.iloc[:10]

    df_nation_declined= df_nation.sort_values('Abschreibungen', ascending=False)
    df_nation_declined = df_nation_declined.iloc[:10]

    chart_always_declined = alt.Chart(df_nation_percentage_sort_asc).mark_bar().encode(
        x='Total Asylgesuche pro Land:Q',
        y=alt.Y('Nation:O', sort=alt.SortField(field="Total Asylgesuche pro Land", order='descending'))
    )

    text_always_declined = chart_always_declined.mark_text(
        align='left',
        baseline='middle',
        dx=3
    ).encode(
        text='Total Asylgesuche pro Land:Q'
    )
    return alt.hconcat((chart_always_declined + text_always_declined).properties(width = 250, height=150, title='Keine angenommenen Gesuche'))

