import xml.etree.ElementTree as ET

tree = ET.parse('PricesShuf.xml')
root = tree.getroot()
print(root)
print(root[5].tag)
for element in root[5]:
    for item in element.findall('ManufacturerItemDescription'):
            if 'קמח' in item.text:
                itemName = item.text
                itemPrice = element.find('ItemPrice').text
                print(itemName,itemPrice)
