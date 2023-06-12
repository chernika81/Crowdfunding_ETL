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