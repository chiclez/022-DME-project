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

def mallet():

    pass

