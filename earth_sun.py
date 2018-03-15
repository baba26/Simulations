'''

stateup
statedown
stateboth



'''
tile = [{} for _ in range(10)]

tile[0]['stateup'] = 1
tile[0]['statedown'] = 1
tile[0]['stateboth'] = 2


'''
tile[[1]['stateup'] = 3
tile[[1]['statedown'] = 3
tile[[1]['stateboth'] = 7
'''

for i in range(1,10):
tile[i]['stateup'] = tile[i-1]['stateup'] + tile[i-1]['stateboth']
tile[i]['stateboth'] = tile[i-1]['stateup']*2 + tile[i-1]['stateboth']*2 + 1
print "for {0} : {1}".format(i,tile[i])



