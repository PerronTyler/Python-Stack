x = [ [5,2,3], [10,8,9] ] 
students_1 = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


print(x)
students_1[0]['last_name'] = 'Bryant'
print(students_1)
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
z[0]['y']=30
print(z)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range((len(students))):
        key1, key2 = students[i]
        print(key1 + ' - ' + students[i]['first_name'] + ', ' + key2 + ' - ' + students[i]['last_name'] )
iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for i in range((len(some_list))):
        print(some_list[i][key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
        key1, key2 = some_dict
        lenKey1 = f'{len(some_dict[key1])}'
        lenKey2 = f'{len(some_dict[key2])}'
        for i in range(len(some_dict)-1):
            print(lenKey1 + ' ' + key1)
            for i in range(len(some_dict[key1])):
                print(some_dict[key1][i])
            print(lenKey2 + ' ' + key2)
            for i in range(len(some_dict[key2])):
                print(some_dict[key2][i])
printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
