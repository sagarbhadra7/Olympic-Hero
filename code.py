# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file


#Code starts here
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
#print(data.columns)
data.head(10)


# --------------
#Code starts here
#print(type(data))




data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')

data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])


#print(data.columns)
better_event=data['Better_Event'].value_counts().idxmax()
#print(better_event)



# --------------
#Code starts here
def top_ten(df,Col):
    country_list=list()
    country_list= list((df.nlargest(10,Col)['Country_Name']))
    #country_list=[df.nlargest(10,col)['Country_Name'].to_string(index=False)]
    return country_list


top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries=top_countries[:-1]
#top_countries.drop(top_countries.tail(1).index,inplace=True)

top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
#print(top_10_summer)
#print(top_10_winter)
#print(top_10)
#print(common)
#print(type(top_countries))


# --------------
#Code starts here
#print(data.columns)
summer_df=top_countries[top_countries['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]
#print(summer_df)
plt.figure(figsize=[14,8])
plt.xlabel("Country Name")
plt.ylabel("No of Medals in Summer")
plt.title("Distribution of Medals in Summer Event")
plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])

#print(winter_df)
plt.figure(figsize=[14,8])
plt.xlabel("Country Name")
plt.ylabel("No of Medals in Winter")
plt.title("Distribution of Medals in Winter Event")
plt.bar(winter_df['Country_Name'],winter_df['Total_Winter'])


#print(top_df)
plt.figure(figsize=[14,8])
plt.xlabel("Country Name")
plt.ylabel("Total no of Medals in Summer & Winter")
plt.title("Distribution of Medals in both Event")
plt.bar(winter_df['Country_Name'],winter_df['Total_Medals'])

#summer_df.plot(kind='bar')
plt.show()



# --------------
#Code starts here
#print(data.head())
summer_df['Golden_Ratio']=data['Gold_Summer']/summer_df['Total_Summer']
#print(summer_df)
#summer_max_ratio=summer_df['Golden_Ratio'].value_counts().argmax()
summer_max_ratio=max(summer_df['Golden_Ratio'])
#print(summer_max_ratio)
summer_country_gold=summer_df.get_value(summer_df['Golden_Ratio'].argmax(),'Country_Name')
#print(summer_country_gold)


winter_df['Golden_Ratio']=data['Gold_Winter']/winter_df['Total_Winter']
#print(winter_df)
#winter_max_ratio=winter_df['Golden_Ratio'].value_counts().idxmax()
winter_max_ratio=max(winter_df['Golden_Ratio'])
#print(winter_max_ratio)
winter_country_gold=winter_df.get_value(winter_df['Golden_Ratio'].argmax(),'Country_Name')
#print(winter_country_gold)

top_df['Golden_Ratio']=data['Gold_Total']/top_df['Total_Medals']
top_max_ratio=max(top_df['Golden_Ratio'])
#top_max_ratio=top_df['Golden_Ratio'].value_counts().argmax()
top_country_gold=top_df.get_value(top_df['Golden_Ratio'].argmax(),'Country_Name')



# --------------
#Code starts here
data_1=data[:-1]
#print(data_1.tail())
data_1['Total_Points']=(data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+(data_1['Bronze_Total'])
#print(data_1.head())
most_points=max(data_1['Total_Points'])
print(most_points)
best_country=winter_df.get_value(data_1['Total_Points'].argmax(),'Country_Name')
print(best_country)
print(str(best_country)+" has won the no of points "+ str(most_points))


# --------------
#Code starts here
best=data[data['Country_Name']==best_country]

best=best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar()
plt.xlabel('Medal Type')
plt.ylabel('Toatl Medals')
plt.xticks(rotation=45)
plt.show()


