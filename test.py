import json

sample_json =  '{ "name":"John", "age":30}'
data = json.loads(sample_json)

print(f'{data["name"]} is {data["age"]} years old...')