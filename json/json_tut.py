import json
import requests

#mother python dict
mother = {
     "name": "Asake Babatunde",
     "age": 28,
     "marital status": "Married",
     "children": ["Ayo", "Tolu", "Simi"],
     "staff": False,
     "next of kin": {
     "name": "Babatune Lanre",
     "relationship": "husband"
     }
}

#subject python dict
subject = {
     "name": "Biology",
     "teacher": {
     "name": "Nana Ama",
     "sex": "female"
     },
     "students_size": 24,
     "elective": True,
     "lesson days": ["Tuesday", "Friday"]
}

# reading json data
with open('employee.json', 'r', encoding='UTF-8') as fp:
    employee_object = json.load(fp)
    print(employee_object)

# encoding Python object to JSON and writing to file
with open('mother.json', 'w', encoding='UTF-8') as fp:
     json.dump(mother, fp, indent=1)

# using .dump()
with open('subject.json', 'w', encoding='UTF-8') as fp:
    json.dump(subject, fp, indent=3)

# using .dumps()
json_data = json.dumps(subject)
print(json_data)
print(type(json_data))


#using .load()
with open('students.json', 'r', encoding='UTF-8') as fp:
     students_list = json.load(fp)
     for student in students_list:
          print(student)


# using .loads()
response = requests.get("https://jsonplaceholder.typicode.com/comments/2")
comment = json.loads(response.text)

print(comment)

