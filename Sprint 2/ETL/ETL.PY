#Index
# 1) Transformation for G_Reviews/Review_G  --> into --> Fact_Reviews and Dim_Users
# 2) Transformation for G_Sites --> into --> Dim_Sites
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json
import re
import geopandas as gpd
from shapely.geometry import Point

Review_G = pd.read_json(r"C:\Users\Ing. Nicolas Yapur\Desktop\Data_Analyst _Nico\HENRY\PF_Yelp_Google\G_Reviews_Folders\review-New_York-20230914T130641Z-001\review-New_York\1.json",lines=True)
Sites_G = pd.read_json(r"C:\Users\Ing. Nicolas Yapur\Desktop\Data_Analyst _Nico\HENRY\PF_Yelp_Google\G_Sites_Folder\1.json",lines=True)

############################### Transformation for G_Reviews ####################################

# Creating Dim_Users table
Dim_Users = Review_G.loc[:,["user_id","name"]]

# dropping user_id duplicates
Dim_Users.drop_duplicates(subset=["user_id"])



# Creating Table Fact_Reviews
Fact_Reviews = Review_G

# Review_G, dropped columns 'pics','resp', this columns have no meaningfull information
Fact_Reviews.drop(columns=["pics","resp","name"],axis=1,inplace=True)

# Dropping duplicates
Fact_Reviews.drop_duplicates()

# Transforming 'time' column into a date column
Fact_Reviews['time'] = pd.to_datetime(Fact_Reviews['time'], unit='ms').dt.strftime('%d/%m/%Y')

Fact_Reviews["time"] = pd.to_datetime(Fact_Reviews["time"])


############################### Transformation for G_Sites ####################################


# Sites_G Dataframe is going to be named "Dim_Sites"
Dim_Sites = Sites_G 

# Dropping rows of restaurands that are permanently closed 

Dim_Sites = Dim_Sites[Dim_Sites["state"]!= "Permanently closed"]

# Dropping unnecesary columns: description, price, relative_results, url
Dim_Sites.drop(columns=["description","price","relative_results","url","state"],axis=1,inplace=True)

# Filter rows where 'category' contains the string "rest" (case-insensitive) in any index
Dim_Sites = Dim_Sites[Dim_Sites['category'].apply(lambda x: x is not None and any("rest" in category.lower() for category in x))]


# Filtering by geolocation,i want to get only the locations that correspond to Florida

# Loading shapefile or GeoJSON of Florida
usa = gpd.read_file(r"st12_d00.shp")
florida = usa[usa['NAME'] == 'Florida']

# Convierte tu DataFrame a un GeoDataFrame
geometry = [Point(xy) for xy in zip(Dim_Sites['longitude'], Dim_Sites['latitude'])]
geo_df = gpd.GeoDataFrame(Dim_Sites, geometry=geometry)

# Filtra solo aquellos puntos que están dentro de Florida
florida_points = geo_df[geo_df.geometry.within(florida.geometry.iloc[0])]

# Eliminando columna creada
florida_points.drop(columns="geometry",axis=1,inplace=True)



# From heere I create a "category_split" Dataframe with the "category" column unnested

# Split the 'category' column and create separate columns for each value in the list
category_split = Dim_Sites['category'].apply(lambda x: pd.Series(x[:15]))  # Limit to 15 categories

# Rename the new columns to 'col_1', 'col_2', ...
category_split.columns = [f'cat{i+1}' for i in range(category_split.shape[1])]

# Heere I create a Dataframe "category_full"

# Create a new column 'merged_categories' by joining non-NaN values of 'cat' columns
category_split['categories'] = category_split.apply(
    lambda row: ', '.join([str(val) for val in row if not pd.isna(val)]),
    axis=1
)

category_full = category_split.iloc[:,[14]]


# Heere i merge the "Dim_Sites" Dataframe with the "category_full" Dataframe
# merging dataframes  Sites_G and category_split
Dim_Sites.drop(columns="category",axis=1,inplace=True)
Dim_Sites = pd.concat([Dim_Sites, category_full], axis=1)


# From heere I create a Dataframe named "hours" to unnest the column

hours = Dim_Sites.iloc[:,[7]]
hours.head()

# Unnesting hours column

# Split the 'hours' column and create separate columns for each value in the list
hours_split = hours['hours'].apply(lambda x: pd.Series(x))

# Rename the new columns to 'hour_1', 'hour_2', ...
hours_split.columns = [f'hour_{i+1}' for i in range(hours_split.shape[1])]

# Concatenate the new columns to the original DataFrame
hours = pd.concat([hours, hours_split], axis=1)

# Drop the original 'hours' column
hours.drop(columns=['hours'], inplace=True)

# Splitting hours/days

# Split the 'hours' column and create separate columns for each value in the list
hours_split1 = hours['hour_1'].apply(lambda x: pd.Series(x))
hours_split2 = hours['hour_2'].apply(lambda x: pd.Series(x))
hours_split3 = hours['hour_3'].apply(lambda x: pd.Series(x))
hours_split4= hours['hour_4'].apply(lambda x: pd.Series(x))
hours_split5 = hours['hour_5'].apply(lambda x: pd.Series(x))
hours_split6 = hours['hour_6'].apply(lambda x: pd.Series(x))
hours_split7 = hours['hour_7'].apply(lambda x: pd.Series(x))

# rename columns
hours_split1.rename(columns={0:"thursday",1:"schedule_thursday"},inplace=True)
hours_split2.rename(columns={0:"friday",1:"schedule_friday"},inplace=True)
hours_split3.rename(columns={0:"saturday",1:"schedule_saturday"},inplace=True)
hours_split4.rename(columns={0:"sunday",1:"schedule_sunday"},inplace=True)
hours_split5.rename(columns={0:"monday",1:"schedule_monday"},inplace=True)
hours_split6.rename(columns={0:"tuesday",1:"schedule_tuesday"},inplace=True)
hours_split7.rename(columns={0:"Wednesday",1:"schedule_Wednesday"},inplace=True)

# concat hours_split
hours_df = pd.concat([hours_split1,hours_split2,hours_split3,hours_split4,hours_split5,hours_split6,hours_split7],axis=1)

# Dropping Days names becouse there's no need of them
hours_df.drop(columns=["thursday","friday","saturday","sunday","monday","tuesday","Wednesday"],axis=1,inplace=True)

hours_df = hours_df.fillna("unspecified")

# concatenate "hours_df" to "Dim_Sites"
Dim_Sites = pd.concat([Dim_Sites, hours_df], axis=1)
Dim_Sites.drop(columns="hours",axis=1,inplace=True)

# MISC has too many Na values, becouse of that i will delete the column
Dim_Sites.drop(columns="MISC",axis=1,inplace=True)