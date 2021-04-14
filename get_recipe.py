# Data libraries

import pandas as pd
import numpy as np
import os

def get_data():
    '''
    This function imports the recipes and cuisines data files as pandas
    dataframes

    input:
    None

    Output:
    recipes_df: Dataframe containing all recipes
    cuisines_df: Dataframe containing the cuisine name and the cuisine index
    '''

    filePath = os.path.join(os.getcwd(), "data")
    cuisinesFile = os.path.join(filePath, "Cuisines.csv")
    recipesFile = os.path.join(filePath, "recipes.csv")

    cuisines_df = pd.read_csv(cuisinesFile, header= None, 
    names = ["cuisine", "cuisine_name"])
    recipes_df = pd.read_csv(recipesFile)

    # Replace whitespaces with underscore and make all ingredients lowerscore
    for column in recipes_df.columns:
        recipes_df.rename(
            columns={column:column.replace(' ', '_').replace("'", "")}, 
            inplace=True
            )
        recipes_df.rename(columns={column:column.lower()}, inplace=True)

    
    # Cuisines_df has different indexing. 
    # Removing one to match the index with the recipes_df
    cuisines_df["cuisine"] = cuisines_df["cuisine"] -1
    cuisines_df

    return recipes_df, cuisines_df

def top_ingredients(n, df):
    '''
    This function will return the Top n ingredients per cuisine in a
    given dataframe

    input
    n: Number of top ingredients to retrieve
    df: recipes dataframe 

    output
    top_ingr_df: dataframe containing the top n ingredients per cuisine
    '''

    grouped_recipes = df.groupby("cuisine").sum()
    number_cuisines = grouped_recipes.shape[0]

    ingr_dict = {}

    for i in range(0, number_cuisines):

        ocurrences = grouped_recipes.loc[i].sort_values(
            ascending = False).reset_index().iloc[0:n]
        ocurrences.columns = ["ingredient", "ocurrence"]
        top = ocurrences["ingredient"].to_list()
        ingr_dict[f"{i}"] = top

    top_ingr_df = pd.DataFrame(data = ingr_dict)

    return top_ingr_df

def specific_ingredients(df):
    '''
    This function retrieves the specific ingredients that are only used in a 
    cuisine.

    input: 
    df: recipes dataframe

    output:
    specific_df: dataframe containing the specific ingredients used in a cuisine
    '''
    grouped_recipes = df.groupby("cuisine").sum().reset_index()
    recipes_feats = df.drop(columns = "cuisine")

    ocur = []
    spec_ingr = []
    cuisine = []

    for i in recipes_feats.columns:
        a = grouped_recipes[["cuisine", i]].where(grouped_recipes[i] >0).dropna()

        if a.shape[0] == 1:
            cuisine.append(a["cuisine"].iloc[0])
            ocur.append(a[i].iloc[0])
            spec_ingr.append(i)
    
    specific_df = pd.DataFrame(data = zip(spec_ingr, cuisine, ocur), 
    columns = ["ingredient", "cuisine", "occurrence"])

    return specific_df

def countries():
    '''
    This function creates a dataframe with the country and its cuisine names

    input:
    None

    output:
    countries_df: Pandas dataframe containing the country and cuisine names
    '''

    countries = ['UK', 'Greece', 'Thailand', 'Italy', 'India', 'Spain', 
    'Germany', 'Morocco', 'Mexico', 'Japan', 'France', 'China']
    countries_adjective = ['English', 'Greek', 'Thai', 'Italian', 'Indian', 
    'Spanish', 'German', 'Moroccan', 'Mexican', 'Japanese', 'French', 'Chinese']

    countries_df = pd.DataFrame(data= zip(countries, countries_adjective), 
    columns = ["country", "cuisine_name"])

    return countries_df

def mallet():

    pass


