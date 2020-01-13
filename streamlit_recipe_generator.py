import csv
from io import StringIO
from functools import partial
from scrapy.http import Request
from scrapy.spiders import BaseSpider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item
import logging

import scrapy


import streamlit as st
import pandas as pd
import numpy as np
import re


'''
# What food shall I make?
This very simple webapp ....
'''

df = pd.read_csv('C:/Users/robert.lowe/Desktop/Anaconda Python/Food idea/FINAL/final_test.csv')


def Word_Search(x):
    df[x] = df['Ingredients'].str.contains(x, flags=re.IGNORECASE)
    df[x] = df[x].replace(True, 1)
    df[x] = df[x].replace(False, 0)
    return 

def ingredients_in(list_of_ingredients_in):
    [Word_Search(ingred) for ingred in list_of_ingredients_in]
    
    return



def Whats_in(x):
    df['Ingredients_inn'] = x
    df['Ingredients'] = df['Ingredients'].str.lower()
    df['Ingredients_inn_split'] = df['Ingredients_inn'].apply(split)
    df = df.assign(Matching_ingred=df.apply(Check_if_in, axis = 1))
    df['Ingredients_to_buy'] = df['Number of ingredients'] - df['Matching_ingred']
    df = df.sort_values(['Ingredients_to_buy'], ascending=[True])
    return df[['Title', 'Ingredients', 'Link', 'Ingredients_to_buy']]


x = st.text_input('What do you have in?')

if st.checkbox('Show me my options'):
    inn = str(x)
    st.write(Whats_in(inn))


elif st.checkbox('Give me some ideas'):
    fish = st.sidebar.multiselect('Fish?', df['Fish'].unique())
    side = st.sidebar.multiselect('Side?', df['Side'].unique())
    meat = st.sidebar.multiselect('Meat&Poultry?', df['Meat_and_Poultry'].unique())
    new_df = df[(df['Side'].isin(side)) & (df['Fish'].isin(fish)) & (df['Meat_and_Poultry'].isin(meat))]
    st.write(new_df[['Title', 'Ingredients', 'Link']])










    
