import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

#Read csv file with pandas
df=pd.read_csv('us-states.csv')


def get_stacked_bar(row):
    '''
    Get confirmed cases in each month

    **Parameters**
        row:*dataframe*

    **Returns**
        output: *list*
            Confirmed cases in wch month.
    '''
    values = row.values
    output = []
    output.append(values[0])
    for i in range(1, len(values)):
        if np.isnan(values[i]):
            output.append(np.nan)
        elif not np.isnan(values[i-1]):
            output.append(values[i]-values[i-1])
        else:
            output.append(values[i])
    return output


# Convert string Date time into Python Date time object
df['date']=pd.to_datetime(df['date'])
#adding a month column
df['month'] = df['date'].dt.month
# group the data based on states and month
grouping = df.groupby(['state','month']).max().unstack()['cases']
#Create a new table based 
grouping_month = grouping.apply(get_stacked_bar, axis=1, result_type='broadcast')
# Draw stacked bar chart
grouping_month.plot.bar(stacked=True, figsize=(15,10))
#plt.savefig("stacked_bar_chart.jpg",bbox_inches='tight')



#Accumulative confirmed cases heatmap
grouping_2 = df.groupby(['state','date']).max().unstack()['cases']
#Chage NAN to 0.00001 since to are goinf to take log
grouping_P1=grouping_2.fillna(0.000000001)
grouping_P1.head()
#Take log
grouping_P1=np.log10(grouping_P1)
# change "date" to "Day"
grouping_P1.columns = ["day%.3d"%(ii+1) for ii in range(grouping_P1.shape[1])]
grouping_P1.head()
#Draw heatmap
fig, ax = plt.subplots(figsize=(20,20))
sns.heatmap(grouping_P1,cmap='OrRd', vmin=0)
plt.title('Accumulative confirmed cases heat map',size=30)
plt.xlabel('Day',size=18)
plt.ylabel('State',size=18)
cbar = ax.collections[0].colorbar
cbar.set_label('Log10 Cases',size=15)
plt.savefig("AccumulativeLogCasesHeatMap.jpg",dpi=200,bbox_inches='tight');


#Accumulative confirmed deaths heatmap
grouping_deaths = df.groupby(['state','date']).max().unstack()['deaths']
#grouping_deaths.head()
grouping_deaths=grouping_deaths+0.000000001
grouping_deaths=grouping_deaths.fillna(0.000000001)
#Take log
grouping_deaths_1=np.log10(grouping_deaths)
# change "date" to "Day"
grouping_deaths_1.columns = ["day%.3d"%(ii+1) for ii in range(grouping_deaths_1.shape[1])]
grouping_deaths_1.head()
#Draw heatmap
fig, ax = plt.subplots(figsize=(20,20))
sns.heatmap(grouping_deaths_1,cmap='YlGnBu', vmin=0)
plt.title('Accumulative log confirmed deaths heat map',size=30)
plt.xlabel('Day',size=18)
plt.ylabel('State',size=18)
cbar = ax.collections[0].colorbar
cbar.set_label('Log10 Deaths',size=15)
plt.savefig("AccumulativelogDeathsHeatMap.jpg",dpi=200,bbox_inches='tight')


#Get daily confirmed cases
df_2= df.groupby(['state','date']).max().unstack()['cases']
# Get the daily cases by subtracting the cases from the previous day
df_2=df_2.fillna(0.0001)
df_3 = df_2.copy()
#df_3.shape
for i in range(1, df_2.shape[1]):
    df_3.iloc[:,i] = df_2.iloc[:,i] - df_2.iloc[:,i-1]
df_3.columns = ["day%.3d"%(ii+1) for ii in range(df_3.shape[1])]
#df_3.head()
#Take log
df_3_daily=df_3+0.0001
df_3_dailylog=np.log10(df_3_daily)
#df_3_dailylog.head()
#Draw heatmap
fig, ax = plt.subplots(figsize=(20,20))
sns.heatmap(df_3_dailylog,cmap='BuPu', vmin=0)
plt.title('Daily log confirmed cases heat map',size=30)
plt.xlabel('Day',size=18)
plt.ylabel('State',size=18)
cbar = ax.collections[0].colorbar
cbar.set_label('Log Daily Cases',size=15)
plt.savefig("DailyConfirmedCasesHeatMap.jpg",dpi=200,bbox_inches='tight');


#Get daily confirmed deaths 
grouping_deaths
df_dd = grouping_deaths.copy()
for i in range(1, df_dd.shape[1]):
    df_dd.iloc[:,i] = df_dd.iloc[:,i] - df_dd.iloc[:,i-1]
df_dd.columns = ["day%.3d"%(ii+1) for ii in range(df_dd.shape[1])]
#df_dd.head()
#Take log
df_dd=df_dd+0.0000001
df_dd_log=np.log10(df_dd)
df_dd_log.head()
#Draw heatmap
fig, ax = plt.subplots(figsize=(20,20))
sns.heatmap(df_dd_log,cmap='Greens', vmin=0)
plt.title('Daily log confirmed deaths heat map',size=30)
plt.xlabel('Day',size=18)
plt.ylabel('State',size=18)
cbar = ax.collections[0].colorbar
cbar.set_label('Log Daily Deaths Cases',size=15)
plt.savefig("DailyDeathCasesHeatMap.jpg",dpi=200,bbox_inches='tight')






