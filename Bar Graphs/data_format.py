import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


df = pd.read_csv('data.csv')
# Getting all data with years from 2000 to 2010
years = df[(df['year']< 2000) | (df['year'] >2010)].index
df.drop(years,inplace=True)

#Getting all countries with data for all 10 years.
cust_counts = df['country'].value_counts().rename('cust_counts')
zip_data_df = df.merge(cust_counts.to_frame(),left_on='country',right_index=True)
has10years = zip_data_df[zip_data_df.cust_counts == 132]

# Create csv for country and suicide numbers
df2 = has10years.groupby(['country']).agg({'suicides_no':sum})
df2.to_csv("country_suicide_no_2000_2010.csv")

# Create csv for sex and suicide numbers
sexnumber = has10years.groupby(['sex']).agg({'suicides_no':sum})
sexnumber.to_csv("sex_suicide_no_2000_2010.csv")

# Create csv for year and suicide numbers
yearnumber = has10years.groupby(['year']).agg({'suicides_no':sum})
yearnumber.to_csv("year_suicide_no_2000_2010.csv")

# Create csv for age and suicide numbers
agenumber = has10years.groupby(['age']).agg({'suicides_no':sum})
agenumber.to_csv("age_suicide_no_2000_2010.csv")






#df2 = df.groupby(['country']).agg({'suicides_no':sum})
#df2.to_csv("suicides_no.csv")



#df2 = df.groupby(['country']).agg({'suicides_no':sum})
#df2.to_csv("suicides_no_2000_2010.csv")

#countunique = df['country'].value_counts() ==132










