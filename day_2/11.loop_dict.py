# members = [
#     ['egoing', 'Seoul', 'Web'],
#     ['leezche', 'Jeju', 'Design']
# ]

# print(members[0][1])

# for member in members:
#     print(member[0], member[1], member[2])

# member = {'name':'egoing', 'city': 'Seoul', 'job': 'Web'}
# print(member['name'])
# print(member['city'])

members = [
{'city': 'Seoul', 'job': 'Web', 'name':'egoing'},
{'city': 'Jeju', 'job': 'Design', 'name':'leezche'}
]

#print(members[0]['city'])
for member in members:
    print(member['name'], member['city'], member['job'])