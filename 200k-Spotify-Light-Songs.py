'''I've taken a Spotify dataset from Kaggle and executed Data Cleaning and other elements of Data Preprocessing using Pandas only- 
   Link of datset- https://www.kaggle.com/datasets/devdope/200k-spotify-songs-light-dataset'''

import pandas as pd 

df=pd.read_csv('/kaggle/input/spotify-songs/light_spotify_dataset.csv') #Reading the csv file
df.head() #displaying first 5 rows of the dataset

value_missing=df.isnull().sum() #if any value is null then add up the occurence 
value_missing #print the number of null values
df_c=df.dropna(subset=['song']) #drop the null values of specified column for optimization

df_c.isnull().sum() #check for null values again

df_c.dtypes #check the datatype of each column
df_c['Release Date']=pd.to_datetime(df_c['Release Date'],format='%Y') #change the data type of Release Date column to datetime format
df_c.dtypes #check the datatype again

dup_values=df_c.duplicated().sum() #if any duplicate value is found then add the occurences
dup_values 
df_c.drop_duplicates(inplace='True') #delete the duplicate values
