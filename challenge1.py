'''
Accept this challenge in Shell/Python Coding

Hit the rest endpoint for the https://dummyjson.com/products 
and process the data with item name and stock of the item

'''

import requests

url = "https://dummyjson.com/products"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    products = data.get('products',[])

    output = [{'name':product['title'],'stock':product['stock']} for product in products]
    #items = [{"name": product["title"], "stock": product["stock"]} for product in products]
for item in output:
    print(f"Item Name: {item['name']} ---> Stock: {item['stock']}")