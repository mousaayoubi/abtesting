import codecademylib
import pandas as pd

#Load first 10 data headers
ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head(10))

#Group ad clicks by source
utm_source = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(utm_source)

#Add is click column
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks)

#Group is click and source
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)

#Create pivot to show clicks by source type 
clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id').reset_index()
print(clicks_pivot)

#Show percent clicked by source
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True]+clicks_pivot[False])
print(clicks_pivot)

#Show number of people seeing ad a or b
experimental_group = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(experimental_group)

#Compare A and B clicks performance
experimental_group_compare = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
print(experimental_group_compare)

#Seperate ad a and ad b
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
print(a_clicks)

b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
print(b_clicks)

#Group by day and click for both ad a and ad b
a_clicks_day = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
print(a_clicks_day)

b_clicks_day = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
print(b_clicks_day)

#Create ad a pivot
a_clicks_day_pivot = a_clicks_day.pivot(columns='is_click', index='day', values='user_id').reset_index()
print(a_clicks_day_pivot)

#Create ad b pivot
b_clicks_day_pivot = b_clicks_day.pivot(columns='is_click', index='day', values='user_id').reset_index()
print(b_clicks_day_pivot)

#Add percentage for ad a
a_clicks_day_pivot['percentage'] = a_clicks_day_pivot[True] / (a_clicks_day_pivot[True] + a_clicks_day_pivot[False])
print(a_clicks_day_pivot)

#Add percentage for ad b (Ad A is performing better)
b_clicks_day_pivot['percentage'] = b_clicks_day_pivot[True] / (b_clicks_day_pivot[True] + b_clicks_day_pivot[False])
print(b_clicks_day_pivot)