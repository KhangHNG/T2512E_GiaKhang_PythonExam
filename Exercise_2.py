import pandas as pd
import csv

from Product import Product

if __name__ == '__main__':
    data = {
        'id' : ['1', '2', '3', '4', '5'],
        'name' : ['Laptop', 'Phone', 'Ipad', 'Headphones', 'Tablet'],
        'price' : [150, 120, 80, 50, 60],
        'quantity': [4, 6, 9, 14, 12]
    }

    file = pd.DataFrame(data)
    file.to_csv('products.csv', index=False)

    #read all
    with open('products.csv', mode = 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            product = Product(
                id= row['id'],
                name= row['name'],
                price = int(row['price']),
                quantity = row['quantity']
            )
            print(f"{product.id} - {product.name} - ${product.price} - {product.quantity}")
            
    print("\n")

    #read products with price > 100:
    print("Products with price > 100:")
    with open('products.csv', mode = 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            product = Product(
                id= row['id'],
                name= row['name'],
                price = int(row['price']),
                quantity = row['quantity']
            )
            if int(product.price) > 100:
                print(f"{product.id} - {product.name} - ${product.price} - {product.quantity}")

    print("\n")

    #Calculate total inventory value
    total = 0
    with open('products.csv', mode = 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            product = Product(
                id= row['id'],
                name= row['name'],
                price = int(row['price']),
                quantity = row['quantity']
            )
            total = total + int(product.price) * int(product.quantity)

    print(f"The total is: {total}")


                