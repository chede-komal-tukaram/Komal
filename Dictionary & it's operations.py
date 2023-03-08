# employeeList = [
#                 [101,'komal','987654'],
#                 [102,'kalyani','789654'],
#                 [103,'namrata','34578'],
#                 [104,'pooja','9876543'],
#                 [105,'priya','908765']

#                 ]

# print (employeeList[2])

# print (employeeList[0][0] ==103)
# print (employeeList[1][0] ==103)
# print (employeeList[2][0] ==103)
# print (employeeList[3][0] ==103)
# # ====================================================================================================
# sampleDictionary = {'key' : 'value',1001 :'pune'}

# empDictionary = {
#                     101 :[101,'PRIYA','987654'],
#                     102 : [102,'KOMAL','98765'],
#                     103 : [103,'RIYA','45678'],
#                     104 : [104,'SANDIP','65789'],
#                     105 : [105,'mayur','897654'],
#                     106 : [106,'vishu','954321']
#                 }

# print(empDictionary[103])
# print(empDictionary[106])
# #========================================================================================================
# empDictionary = {
#                     'PRIYA' :[101,'PRIYA','987654'],
#                     'KOMAL' : [102,'KOMAL','98765'],
#                     'RIYA' : [103,'RIYA','45678'],
#                     'SANDIP' : [104,'SANDIP','65789'],
#                     'mayur' : [105,'mayur','897654'],
#                     'vishu' : [106,'vishu','954321']
#                 }

# print(empDictionary['KOMAL'])
# print(empDictionary['mayur'])


# (empDictionary['vishu'])=[108,'vishu','111111']
# print(empDictionary['vishu'])

# ===============================================================================================
### Dictionary operation##
# temp = {
#             'id': 1001,
#             'favColor': 'white',
#             'institute' : 'innovant',
#             1 : 'monika',
#             True : "indial"
#         }

# # print(temp.items())     #dict_items([('id', 1001), ('favColor', 'white'), ('institute', 'innovant'), (1, 'indial')])

# # print(temp.keys())      #dict_keys(['id', 'favColor', 'institute', 1])

# temp['favColor'] = 'black'
# temp['newkey'] = 'black'
# print(temp)                     #{'id': 1001, 'favColor': 'black', 'institute': 'innovant', 1: 'indial', 'newkey': 'black'}

# print(temp.items())

# # ====================================================================================
# # we can add /update key value in bulk
# temp.update({'favColor' : 'pink','newid' : 2001})
# print(temp)