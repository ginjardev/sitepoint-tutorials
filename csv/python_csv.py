import csv
import json

# read CSV file
with open('employees.csv', 'r', encoding='utf-8') as file_obj:
    reader_obj = csv.reader(file_obj)
    # print(next(reader_obj))
    # print(next(reader_obj))
  
# write to csv file
with open('products.csv', 'w', encoding='utf-8') as file_obj:
    writer_obj = csv.writer(file_obj)
    writer_obj.writerow(['Product Name', 'Price', 'Quantity', 'SKU Number' ])
    writer_obj.writerow(['Rice', 80, 35, 'RI59023'])
    writer_obj.writerow(['Curry', 2, 200, 'CY13890'])
    writer_obj.writerow(['Milk', 9.5, 315, 'MK10204'])

# convert csv to JSON File    

my_dict = {}

with open('employees.csv', 'r', encoding='utf-8') as file_obj:
    reader_object = csv.DictReader(file_obj)

    serial_number = 0

    for row in reader_object:
        serial_number = serial_number + 1
        my_dict[serial_number] = row
    
with open('staff.json', 'w', encoding='utf-8') as file_obj:
    json.dump(my_dict, file_obj, indent=4)   


#convert json to csv
py_dict = {}

# convert json file to python dictionary
with open('staff.json', 'r', encoding='utf-8') as file_obj:
    py_dict = json.load(file_obj)
    
    
 # convert write python dictionary to csv\  
with open('records.csv', 'w', encoding='utf-8') as file_obj:
    csv_writer = csv.DictWriter(file_obj, fieldnames=py_dict['1'].keys())
    csv_writer.writeheader()
    for i in py_dict.keys():
        csv_writer.writerow(py_dict[i])
    
  