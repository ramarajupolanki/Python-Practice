'''
Example file on dictionary methods
'''

definitions = {
    'snake': 'long thin reptile',
    'monkey': 'human like animal',
    'plant': 'green growing thing'
}

# print entire dictionary
print(definitions)

# print single entry
print(definitions['snake'])

# print all keys
for key in definitions.keys():
    print('key', key)

# print all values
for value in definitions.values():
    print('value', value)

# print all entries using items()
for key, value in definitions.items():
    print('Key:', key, 'Value:', value)

# prints KeyError as no entry is present in dictionary
# print(definitions['alien'])

# to avoid KeyError use dict.get(key) which returns 'None'
print(definitions.get('alien'))  # prints None

# to get some default value instead of None
# use dict.get(key, 'fall-back-value')
print(definitions.get('alien', 'exta-terrestial species'))

# add an entry
definitions['table'] = 'immovable object'
print(definitions)

# update a single entry
definitions['table'] = 'motionless object'
print(definitions)

# update multiple entries using update() - using another dictionary
somemore_definitions = {'paper': 'light-weight thing'}
definitions.update(somemore_definitions)
mytuple = ({'1': 'one'})
definitions.update(mytuple)
print(definitions)

# delete an entry
del definitions['1']
print(definitions)

# remove specific entries
new_definitions = {}
new_definitions = {key: definitions[key]
                   for key in definitions.keys()-{'plant', 'table'}}
print(new_definitions)

# change keys-to-values and values-to-keys
# method-1
new_definitions = {}
for key, value in definitions.items():
    new_definitions[value] = key
print(new_definitions)
# method-2 - using dictionary comprehension
new_definitions = {value: key for key, value in definitions.items()}
print(new_definitions)


# copy dictionary from one to another - using dictionary comprehension
another_definitions = {}
another_definitions = {key: value for key, value in definitions.items()}
print(another_definitions)

# Sort dictionary
# method-1 - sort by keys
sorted_definitions_bykey = {}
sorted_definitions_bykey = {key: value for key in sorted(definitions)}
print(sorted_definitions_bykey)

print('==========')


def by_key(item):
    return item[0]


sorted_definitions_bykey2 = {}
sorted_definitions_bykey2 = {key: value for key, value in sorted(
    definitions.items(), key=by_key, reverse=False)}
print(sorted_definitions_bykey2)

# method-2 - sort by values
print('++++++++++++++++++')


def by_value(item):
    return item[1]


sorted_definitions_byvalue = {}
sorted_definitions_byvalue = {
    key: value for key, value in sorted(definitions.items(), key=by_value, reverse=True)}
print(sorted_definitions_byvalue)
