import json

courses = '{"Name": "nightfury1", "Languages": ["Python", "C++", "PHP"]}'

print(type(courses))
print(courses)

dict_courses = json.loads(courses)

print(type(dict_courses))
print(dict_courses['Languages'][0])

if __name__ == '__main__':
    pass
