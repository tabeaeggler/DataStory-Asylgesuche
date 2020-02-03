#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd


# In[38]:


df_result = pd.DataFrame()
for i in range(1994, 2019):
    file_name = "./Data/data_{}.xlsx".format(str(i))
    df_kanton = get_dataframe_kanton()
    df_nation = get_dataframe_nation()
    df_gender = get_dataframe_gender()

    #concate 3 tables/sheets   
    df_concat = pd.concat([df_kanton, df_nation, df_gender], axis = 0, sort=True)
    df_concat = df_concat.reset_index(drop=True)
    
    #add col year
    df_concat['Jahr'] = str(i)
    
    #merge to final df
    df_result = pd.concat([df_result, df_concat], axis = 0, sort=True)

df_result
df_result.to_excel("./Data/data_cleaned.xlsx")


# In[13]:


def get_dataframe_kanton():
    sheet_kanton = "CH-Kt"

    #handle different col-types
    df_header_1 = pd.read_excel(file_name, sheet_name = sheet_kanton, skiprows=[0,1,2])
    df_header_2 = pd.read_excel(file_name, sheet_name = sheet_kanton, skiprows=[0,1,2,3])
    
    #Drop group cols
    df_header_1 = df_header_1[df_header_1.columns[:-3]]
    
    #Drop 4. row in header_1 -> ausgleichen
    df_header_1 = df_header_1.drop(0)
    df_header_1 = df_header_1.reset_index(drop=True)
    
    #drop "Entscheide"
    df_header_1.drop(df_header_1.filter(regex="Entscheide"),axis=1, inplace=True)
    
    #drop unnamed cols
    df_header_1.drop(df_header_1.filter(regex="Unname"),axis=1, inplace=True)
    df_header_2.drop(df_header_2.filter(regex="Unname"),axis=1, inplace=True)
    
    #combine two two headers
    df_combined_headers = df_header_1.combine_first(df_header_2)
    
    #drop total and empty line
    df_combined_headers = df_combined_headers.drop(0)
    df_combined_headers = df_combined_headers.drop(1)
    df_combined_headers = df_combined_headers.reset_index(drop=True)

    #add "Kanton" col
    df_kanton_col = pd.read_excel(file_name, sheet_name = sheet_kanton, skiprows=[0,1,2,3,4,5])
    df_kanton_col.rename(columns={'Total': 'Kanton'}, inplace=True)
    df_kanton_col = df_kanton_col[df_kanton_col.columns[:-15]]

    #combine all
    df_kanton = df_combined_headers.combine_first(df_kanton_col)
    
    #drop empy rows
    df_kanton = df_kanton.dropna() 

    return df_kanton


# In[14]:


def get_dataframe_nation():
    sheet_nation = "CH-Nati"

    #handle different col-types
    df_header_1 = pd.read_excel(file_name, sheet_name = sheet_nation, skiprows=[0,1,2])
    df_header_2 = pd.read_excel(file_name, sheet_name = sheet_nation, skiprows=[0,1,2,3])
   
    #Drop group cols
    df_header_1 = df_header_1[df_header_1.columns[:-3]]
    
    #Drop 4. row in header_1 -> ausgleichen
    df_header_1 = df_header_1.drop(0)
    df_header_1 = df_header_1.reset_index(drop=True)
    
    #drop "Entscheide"
    df_header_1.drop(df_header_1.filter(regex="Entscheide"),axis=1, inplace=True)
    
    #drop unnamed cols
    df_header_1.drop(df_header_1.filter(regex="Unname"),axis=1, inplace=True)
    df_header_2.drop(df_header_2.filter(regex="Unname"),axis=1, inplace=True)

    #combine two headers
    df_combined_headers_n = df_header_1.combine_first(df_header_2)
    
    #generate same structure
    df_combined_headers_n = df_combined_headers_n.drop(0)
    df_combined_headers_n = df_combined_headers_n.drop(1)
    df_combined_headers_n = df_combined_headers_n.drop(2)
    df_combined_headers_n = df_combined_headers_n.reset_index(drop=True)

    #add "Nation" col
    df_nation_col = pd.read_excel(file_name, sheet_name = sheet_nation, skiprows=[0,1,2,3,4,5,6])
    df_nation_col.rename(columns={'Unnamed: 0': 'Nation'}, inplace=True)
    df_nation_col = df_nation_col[df_nation_col.columns[:-15]]

    #combine all
    df_nation = df_nation_col.combine_first(df_combined_headers_n)
    
    #drop empy rows
    df_nation = df_nation.dropna() 
    
    return df_nation


# In[15]:


def get_dataframe_gender():    
    sheet_gender = "CH-Gesl"
    
    #handle different col-types
    df_header_1 = pd.read_excel(file_name, sheet_name = sheet_gender, skiprows=[0,1,2])
    df_header_2 = pd.read_excel(file_name, sheet_name = sheet_gender, skiprows=[0,1,2,3])
    
    #Drop group cols
    df_header_1 = df_header_1[df_header_1.columns[:-3]]
   
    #Drop 4. row in header_1 -> ausgleichen
    df_header_1 = df_header_1.drop(0)
    df_header_1 = df_header_1.reset_index(drop=True)
    
    #drop "Entscheide"
    df_header_1.drop(df_header_1.filter(regex="Entscheide"),axis=1, inplace=True)
    
    #drop unnamed cols
    df_header_1.drop(df_header_1.filter(regex="Unname"),axis=1, inplace=True)
    df_header_2.drop(df_header_2.filter(regex="Unname"),axis=1, inplace=True)
    
    #combine two two headers
    df_combined_headers = df_header_1.combine_first(df_header_2)
    
    #generate same structure
    df_combined_headers = df_combined_headers.drop(0)
    df_combined_headers = df_combined_headers.drop(1)
    df_combined_headers = df_combined_headers.reset_index(drop=True)

    #add "Geschlecht" col
    df_gender_col = pd.read_excel(file_name, sheet_name = sheet_gender, skiprows=[0,1,2,3,4,5])
    df_gender_col.rename(columns={'Total': 'Geschlecht'}, inplace=True)
    df_gender_col = df_gender_col[df_gender_col.columns[:-15]]

    #combine all
    df_gender = df_combined_headers.combine_first(df_gender_col)
   
    #drop empy rows
    df_gender = df_gender.dropna() 

    return df_gender


# In[ ]:




