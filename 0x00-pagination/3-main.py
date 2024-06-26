#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('3-hypermedia_del_pagination').Server

server = Server()

server.indexed_dataset()

try:
    server.get_hyper_index(300000, 100)
except AssertionError:
    print("AssertionError raised when out of range")


index = 3
page_size = 2

print("Nb items: {}".format(len(server._Server__indexed_dataset)))
print('#' * 40)

# printing from 0 - 9
print(server.get_hyper_index(0, 10))

print('#' * 40)
# 1- request first index
res = server.get_hyper_index(index, page_size)
print(res)

# 2- request next index
print(server.get_hyper_index(res.get('next_index'), page_size))

print('XXX' * 40)
# 3- remove the first index
del server._Server__indexed_dataset[res.get('index')]
print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 4- request again the initial index -> the first data retreives is not the same as the first request
print(server.get_hyper_index(index, page_size))
print('XXX' * 40)

# 5- request again initial next index -> same data page as the request 2-
print(server.get_hyper_index(res.get('next_index'), page_size))

print('#' * 40)

# printing from 0 - 9
print(server.get_hyper_index(0, 10))

'''
>$ head -n 11 Popular_Baby_Names.csv

Year of Birth,Gender,Ethnicity,Child's First Name,Count,Rank

0 => Olivia,172,1
1 => Chloe,112,2
2 => Sophia,104,3
3 => Emma,99,4
4 => Emily,99,4
5 => Mia,79,5
6 => Charlotte,59,6
7 => Sarah,57,7
8 => Isabella,56,8
9 => Hannah,56,8
10 => Grace,54,9
11 => Angela,54,9
'''
