import json

data='''
[
{"usn":"001","marks":"45","name":"kumar"},
{"usn":"009","marks":"70","name":"raju"}
]'''

info=json.loads(data)

print('user count:',len(info))

for x in info:
    print('USN:',x['usn'])
    print('marks:',x['marks'])
    print('user name:',x['name'])
"""

OUTPUT:

user count: 2
USN: 001
marks: 45
user name: kumar
USN: 009
marks: 70
user name: raju

"""
