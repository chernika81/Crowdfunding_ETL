# Import dependencies
import pandas as pd
import numpy as np
pd.set_option('max_colwidth', 400)


### Extract the crowdfunding.xlsx Data




# Read the data into a Pandas DataFrame
crowdfunding_info_df = pd.read_excel('Resources/crowdfunding.xlsx')
crowdfunding_info_df.head()


# Get a brief summary of the crowdfunding_info DataFrame.
crowdfunding_info_df.info()


### Create the Category and Subcategory DataFrames
---
**Create a Category DataFrame that has the following columns:**
- A "category_id" column that is numbered sequential form 1 to the length of the number of unique categories.
- A "category" column that has only the categories.

Export the DataFrame as a `category.csv` CSV file.

**Create a SubCategory DataFrame that has the following columns:**
- A "subcategory_id" column that is numbered sequential form 1 to the length of the number of unique subcategories.
- A "subcategory" column that has only the subcategories. 

Export the DataFrame as a `subcategory.csv` CSV file.



# Get the crowdfunding_info_df columns.
crowdfunding_info_df.columns


# Assign the category and subcategory values to category and subcategory columns.
crowdfunding_info_df[['category','subcategory']] = crowdfunding_info_df ["category & sub-category"].str.split('/', expand=True)
crowdfunding_info_df.head()



# Get the unique categories and subcategories in separate lists.
categories = crowdfunding_info_df['category'].unique()
subcategories = crowdfunding_info_df['subcategory'].unique()

print(categories)
print(subcategories)



# Get the number of distinct values in the categories and subcategories lists.
print(len(categories))
print(len(subcategories))

# Create numpy arrays from 1-9 for the categories and 1-24 for the subcategories.
category_ids = np.arange(1, 10)
subcategory_ids = np.arange(1, 25)

print(category_ids)
print(subcategory_ids)


# Use a list comprehension to add "cat" to each category_id. 
cat_ids = [f'cat{category_id}' for category_id in category_ids]
# Use a list comprehension to add "subcat" to each subcategory_id.    
scat_ids = [f'subcat{subcategory_id}' for subcategory_id in subcategory_ids]
    
print(cat_ids)
print(scat_ids)


# Create a category DataFrame with the category_id array as the category_id and categories list as the category name.
category_1 = {'category_id': cat_ids, 'category': categories}
category_df = pd.DataFrame(category_1)
# Create a category DataFrame with the subcategory_id array as the subcategory_id and subcategories list as the subcategory name.
subcategory_1 = {'subcategory_id': scat_ids, 'subcategory': subcategories}
subcategory_df = pd.DataFrame(subcategory_1)


category_df

subcategory_df


# Export categories_df and subcategories_df as CSV files.
category_df.to_csv("Resources/category.csv", index=False)

subcategory_df.to_csv("Resources/subcategory.csv", index=False)


# Create a copy of the crowdfunding_info_df DataFrame name campaign_df. 
campaign_df = crowdfunding_info_df.copy()
campaign_df.head()


# Rename the blurb, launched_at, and deadline columns.
campaign_df = campaign_df.rename(columns={"blurb": "description", "launched_at": "launched_date", "deadline": "end_date"}, errors="raise")
campaign_df.head()


# Convert the goal and pledged columns to a `float` data type.
campaign_df = campaign_df.astype({'goal': 'float', 'pledged': 'float'})
campaign_df.head()


# Check the datatypes
campaign_df.dtypes


# Format the launched_date and end_date columns to datetime format
from datetime import datetime as dt
campaign_df["launched_date"] = pd.to_datetime(campaign_df["launched_date"]).dt.strftime('%Y-%m-%d') 
campaign_df["end_date"] = pd.to_datetime(campaign_df["end_date"]).dt.strftime('%Y-%m-%d')
campaign_df.head()



# Added line. Not in the starter code. Changing the launched_date and end_date columns Dtype to datetime
# This step was not required
campaign_df["launched_date"] = pd.to_datetime(campaign_df["launched_date"])
campaign_df["end_date"] = pd.to_datetime(campaign_df["end_date"])
campaign_df.info()


# Merge the campaign_df with the category_df on the "category" column and 
# the subcategory_df on the "subcategory" column.
campaign_merged_df = pd.merge(pd.merge(campaign_df, category_df, on='category', how='left'), subcategory_df, on='subcategory', how='left')

campaign_merged_df.tail(10)

# Drop unwanted columns
campaign_cleaned = campaign_merged_df.drop(columns=['staff_pick', 'spotlight', 'category & sub-category', 'category', 'subcategory'])
campaign_cleaned.head()



# Export the DataFrame as a CSV file. 
campaign_cleaned.to_csv("Resources/campaign.csv", index=False)


# Read the data into a Pandas DataFrame. Use the `header=2` parameter when reading in the data
## I am using header=3 to make it easier to get the correct result without going through some additional formating steps
contact_info_df = pd.read_excel('Resources/contacts.xlsx', header=3)
contact_info_df.head()



# Iterate through the contact_info_df and convert each row to a dictionary.
import json
dict_values = []
for i, row in contact_info_df.iterrows():
    row_value = row[0]
    row_conv = json.loads(row_value)
    

# Print out the list of values for each row.
    list_value = [x for y, x in row_conv.items()]
    dict_values.append(list_value)
    
print(dict_values)


# Create a contact_info DataFrame and add each list of values, i.e., each row 
# to the 'contact_id', 'name', 'email' columns.
contact_info = pd.DataFrame(dict_values, columns=['contact_id', 'name', 'email'])

contact_info.head()


# Create a "first"name" and "last_name" column with the first and last names from the "name" column. 
contact_info[['first_name','last_name']] = contact_info["name"].str.split(' ', expand=True)

# Drop the contact_name column
contacts_df_1 = contact_info.drop(columns=['name'])
contacts_df_1.head(10)

