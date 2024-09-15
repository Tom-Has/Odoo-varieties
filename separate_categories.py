import pandas as pd
import re

input_file = 'path\categories_input.xlsx'
output_file = 'path\categories_output.xlsx'
category_colum = 'categories'
separator = '/'
separator_odoo = ' / '


def format_category(category):

    category = re.sub(r'^\s*' + separator + r'+|' + separator + r'+\s*$', '', category)
    category = re.sub(r'\s*' + separator + r'\s*', separator, category)
    category = re.sub(separator + r'+', separator, category)
    category = re.sub(r'\s+', ' ', category)
    category = category.strip()

    return category


def split_categories(category):

    categories = category.split(separator)

    return categories


df = pd.read_excel(input_file)

df.dropna(subset=[category_colum], inplace=True)
df[category_colum] = df[category_colum].apply(format_category)

max_depth = 0
split_categories_list = []
for index, row in df.iterrows():
    split_cats = split_categories(row[category_colum])
    split_categories_list.append(split_cats)
    max_depth = max(max_depth, len(split_cats))

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for level in range(max_depth):
        cat_data = []
        for split_cats in split_categories_list:
            if level < len(split_cats):
                catname = split_cats[level]
                catparent = separator_odoo.join(split_cats[:level])
            cat_data.append([catparent, catname])

        level_df = pd.DataFrame(cat_data, columns=['catparent', 'catname']).drop_duplicates()
        
        level_df.to_excel(writer, sheet_name=f'Level_{level + 1}', index=False)

print("File creation successful and duplicates removed.")
