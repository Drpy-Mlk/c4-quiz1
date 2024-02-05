# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:12:56 2024

@author: Tshepho
"""

import pandas as pd


column_names = ['Rank','Title','Genre','Description','Director','Actors','Year','Runtime','Rating','Votes','Revenue','Metascore']
df = pd.read_csv('movie_dataset.csv',names = column_names)
df.drop(index=0, inplace=True)
avg_rev =df['Revenue'].mean()
df['Revenue'].fillna(avg_rev,inplace = True)
avg_met =df['Metascore'].mean()
df['Metascore'].fillna(avg_met,inplace = True)
print(df.describe())
max_rate = df['Rating'].max
print(max_rate)
grouped =df.groupby("Year")
avg_2015_2017 = grouped['2016'].mean()
print(avg_2015_2017)
count_d = grouped['Director'].count()
print(count_d)

