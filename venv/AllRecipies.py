from allrecipes import AllRecipes
import os
import googletrans
from googletrans import Translator
import xml.etree.ElementTree as ET

searchList = []
translator = Translator()
# Search :
query_options = {
  "wt": "Salad",         # Query keywords\
  "ingIncl": "",        # 'Must be included' ingrdients (optional)
  "ingExcl": "",  # 'Must not be included' ingredients (optional)
  "sort": "re"                # Sorting options : 're' for relevance, 'ra' for rating, 'p' for popular (optional)
}
query_result = AllRecipes.search(query_options)

# Get :
main_recipe_url = query_result[0]['url']
detailed_recipe = AllRecipes.get(main_recipe_url)  # Get the details of the first returned recipe (most relevant in our case)

# Display result :
print("## %s :" % detailed_recipe['name'])  # Name of the recipe

#Parsing ingredients - with hte condition that it's LAST in sentence

for ingredient in detailed_recipe['ingredients']:  # List of ingredients
    ing_str = ingredient.split()
    print(ing_str[-1])
    print(translator.translate(ing_str[-1], dest='he', src='en').text)

#List of ingredients in hebrew

    if (translator.translate(ing_str[-1], dest='he', src='en').text).isalpha():
        searchList.append(translator.translate(ing_str[-1], dest='he', src='en').text)
print(searchList)

#Checking the Hebrew list in PriceShuf.xml
tree = ET.parse('PricesShuf.xml')
root = tree.getroot()
print(root)
print(root[5].tag)
print(searchList[0])
for new_ing in searchList:
    print(new_ing)
    for element in root[5]:
        for item in element.findall('ManufacturerItemDescription'):
            if new_ing in item.text:
                itemName = item.text
                itemPrice = element.find('ItemPrice').text
                print(itemName,itemPrice)
