# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 10:48:43 2018

@author: Ties
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import folium as folium
import math


#%% Read Terrorism database
df = pd.read_excel('globalterrorismdb_0617dist.xlsx')
df['N'] = 1

Old_names = ['Bahamas','Bosnia-Herzegovina','Guinea-Bissau','Serbia','Slovak Republic','Tanzania','United States','West Bank and Gaza Strip']
New_names = ['The Bahamas','Bosnia and Herzegovina','Guinea Bissau','Republic of Serbia','Slovakia','United Republic of Tanzania','United States of America','West Bank']
for i in np.arange(0,len(Old_names),1):
    df.loc[df['country_txt'] == Old_names[i],['country_txt']] = New_names[i]

world_map = 'world-countries.json'

#%% Read reaters articles
Articles_df = pd.read_csv('reuters.csv',sep='\t')
Articles_small = Articles_df.iloc[:,1:3]
Articles_small['year'] = None

Articles_small = Articles_small.iloc[5650000:,:]
#i=0
#for line in Articles_small.iloc[:,0]:
#    try:
#        Articles_small.loc[i,['year']] = int(line[0:4])
#    except TypeError:
#        Articles_small.loc[i,['year']] = 0
#    i +=1
# 
#Articles_small = Articles_small.loc[Articles_small['year']>=2013,:]    

Title_list = Articles_small.iloc[:,1]

#%% Select subset
df1 = df.loc[df['iyear']>=2013,:]
#df1 = df.loc[df['region_txt']=='Western Europe',:]

##%%
#Country_ID = df1.loc[:,['country','country_txt']]
#Country_ID = Country_ID.drop_duplicates(subset='country')
#Country_ID = Country_ID.set_index('country_txt',drop=False)

#%%
Country_year_df = df1.loc[:,['country_txt','iyear','N','nkill','nkillter','nwound','nwoundte']].groupby(['country_txt','iyear']).sum()
Country_year_df = Country_year_df.fillna(0)
Country_year_df['victim_kill'] = Country_year_df['nkill']- Country_year_df['nkillter']
Country_year_df['victim_wound'] = Country_year_df['nwound']- Country_year_df['nwoundte']

#Country_ID['Slope_N'] = 0
#Country_ID['Slope_K'] = 0
#Country_ID['Slope_W'] = 0
#Values = np.array([0, 0, 0, 0, 0, 0, 0,])
#d = {'N': Values, 'victim_kill': Values, 'victim_wound':Values}
#Empty_df = pd.DataFrame(data=d,index=np.arange(2010, 2017, 1))
#lm = linear_model.LinearRegression()
#for C in Country_year_df.index.get_level_values('country_txt').unique():
#    SubData = (Country_year_df.loc[C,['N','victim_kill','victim_wound']]+Empty_df).fillna(0)
#    SubData['year'] = SubData.index
#    model = lm.fit(SubData.loc[:,['year']],SubData.loc[:,['N']])
#    Country_ID.loc[C,['Slope_N']] = lm.coef_[0,0]
#    model = lm.fit(SubData.loc[:,['year']],SubData.loc[:,['victim_kill']])
#    Country_ID.loc[C,['Slope_K']] = lm.coef_[0,0]
#    model = lm.fit(SubData.loc[:,['year']],SubData.loc[:,['victim_wound']])
#    Country_ID.loc[C,['Slope_W']] = lm.coef_[0,0]
#    
#Plot_map(Country_ID,['country_txt', 'Slope_N'],"N_incidents_trend.html")   
#Plot_map(Country_ID,['country_txt', 'Slope_K'],"Kill_trend.html")    
#Plot_map(Country_ID,['country_txt', 'Slope_W'],"Wounded_trend.html") 

  
  

#%%
Country_Total_df = Country_year_df.groupby(level=[0]).sum()
Country_Total_df['Country'] = Country_Total_df.index
Country_Total_df['Victims'] = Country_Total_df['victim_kill']+Country_Total_df['victim_wound']

Subset = Country_Total_df.loc[Country_Total_df['Victims']>0,:]
Subset['Victims_log'] = np.log10(Subset['victim_kill']+Subset['victim_wound'])
Subset = Subset.replace([np.inf, -np.inf], 0)

Plot_map(Subset,['Country', 'Victims_log'],"total_victims_2013_2016.html")

#%%
Top15 = Country_Total_df.nlargest(15, 'Victims')
West = Country_Total_df.loc[['Israel','United States of America','United Kingdom','France','Germany'],:]
Top15West = Top15.append(West)
Top15West.loc['Israel',:] = Top15West.loc['Israel',:] + Country_Total_df.loc['West Bank',:]
Top15West.loc['Israel','Country'] = 'Israel'
    
#%%
Countries = Top15West.index
C_tags = [['Iraq'],['Afghan'],['Nigeria'],['Pakistan'],['Syria'],['Yemen'],
          ['Somalia'],['Turk'], ['Libya'],['India'], ['Egypt'],['Philippin'],
          ['Ukrain'], ['Thailand'], ['Leban'], ['Israel','West Bank','Gaza','Pallestin','Hamas'], ['United States','US'],
          ['United Kingdom','UK','Britain'],['France','French'], ['Germany','German']]

News_count = pd.DataFrame(index=Countries,columns=['Country','Tags'])

#Tags = ('attack','war','conflict','terror','bomb','extremist','taliban','boko haram','isis','isil','islamic state','al qaeda','al qaida')
Tags = ('terror','bomb','extremist','taliban','hamas','boko haram','isis','isil','islamic state','al qaeda','al qaida')

for i in range(0,len(Countries),1):
    T1=0
    T2=0
    for line in Title_list:
        if any(C_tag in line for C_tag in C_tags[i]):    
            T1 +=1
            if any(tag in line.lower() for tag in Tags):
                T2 +=1
                print(line)

    News_count.loc[Countries[i],:] = [T1,T2]              

     
#%%
Terror_News = pd.concat([Top15West,News_count], axis=1, join='inner')

x = np.arange(0,20,1)

N = np.array(Terror_News['N'])/10
Victims = np.array(Terror_News['victim_kill']+Terror_News['victim_wound'])/10
Articles = np.array(Terror_News['Tags'])

fig=plt.figure(figsize=(20,10))
#
#plt.bar(x-0.2, N,width=0.4,color='b',align='center')
plt.bar(x-0.2, Victims,width=0.4,color='r',align='center')
plt.bar(x+0.2, Articles,width=0.4,color='g',align='center')

my_xticks = Terror_News.index
my_xticks= ['Iraq', 'Afghanistan', 'Nigeria', 'Pakistan', 'Syria', 'Yemen',
       'Somalia', 'Turkey', 'Libya', 'India', 'Egypt', 'Philippines',
       'Ukraine', 'Thailand', 'Lebanon', 'Israel', 'United States',
       'United Kingdom', 'France', 'Germany']
plt.xticks(x, my_xticks)
plt.xticks(rotation=45)
axes = plt.gca()
axes.set_ylim([0,3000])
plt.legend(['Victims /10','Articles'])
plt.title('Media coverage of terroristal actions')
plt.show()
fig.savefig('top_terror.png') 

 #%%
def Plot_map(Data,Col,Name):
    map = folium.Map(location=[48, -102], zoom_start=3)
    map.choropleth(geo_data=world_map, data=Data,
                 columns=Col,
                 key_on='feature.properties.name',
                 fill_color='YlOrRd',
                 legend_name='Number of Victims in log scale:',
                 )
    folium.LayerControl().add_to(map)
    map.save(Name) 
    
#%%
# Find differences between Map country names and dataset country names    
World_map_data = pd.read_json('world-countries.json')
World_map_countries = pd.DataFrame(index=World_map_data.index,columns=['country_map'])
for i in World_map_data.index:
    World_map_countries.loc[i,['country_map']] = World_map_data.loc[i].features['properties']['name']
    
World_map_countries = World_map_countries.set_index('country_map',drop=False)

#World_map_countries = pd.concat([World_map_countries,Country_ID['country_txt']], axis=1, join='outer')
#Diff = World_map_countries.loc[World_map_countries.isnull().any(axis=1),:]
#%%

