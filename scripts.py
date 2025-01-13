import django
import os

from django.views import defaults
os.environ['DJANGO_SETTINGS_MODULE'] = 'recommend.settings'
django.setup()
import pandas as pd
import csv
csv_file_path = 'backend/flipkart_com-ecommerce_sample.csv'
from home.models import * 

with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
      try:
        product_name = row['product_name']
        product_image = eval(row['image'])[0]
        description = row['description'] 
        category = row['product_category_tree'].split('>>')[0].strip('[]"')
        price = row['retail_price']
        print(product_name, product_image, description, category, price)

        # create or update product
        Product.objects.update_or_create(
          name=product_name,
          defaults={
            "product_image":product_image,
            "description":description,
            "category":category,
            "price":price
          }
        )
      except Exception as err:
        print(err)

print("Product imported successfully")