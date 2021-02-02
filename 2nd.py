D = {  'hardik': 5, 'rahul': 27, 'rohit' : 10 , 'virat' : 14, 'dhoni' : 19 }
max_value = max(D.items(), key=lambda x : x[1])
print('Max value in Dict: ', max_value[1])
print('Key With Max value in Dict: ', max_value[0])
