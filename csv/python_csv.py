import csv

# read CSV file
with open('employees.csv', 'r', encoding='utf-8') as file_obj:
    reader_obj = csv.reader(file_obj)
    print(next(reader_obj))
    print(next(reader_obj))
  

with open('products.csv', 'w', encoding='utf-8') as file_obj:
    writer_obj = csv.writer(file_obj)
    writer_obj.writerow(['Product Name', 'Price', 'Quantity', 'SKU Number' ])
    writer_obj.writerow(['Rice', 80, 35, 'RI59023'])
    writer_obj.writerow(['Curry', 2, 200, 'CY13890'])
    writer_obj.writerow(['Milk', 9.5, 315, 'MK10204'])