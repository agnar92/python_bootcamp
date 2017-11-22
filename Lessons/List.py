my_list = [1,2,3]
print('My list: {x}'.format(x=my_list))

my_list01 = ['string',23,1.2,'o']
print('My List01: {}'.format(my_list01))

print(len(my_list))

my_list + ['new']
print(my_list)
my_list = my_list + ['new']
print(my_list)

print(my_list*2)

l = [1,2,3]
l.append('append') # add at end of list new item
print(l)
l.pop() #delete last item forom list, pop
print(l)

#reverse
l.reverse()
print(l)

#sort
l.sort()
print(l)

l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]

# list two dimensional
matrix = [l_1,l_2,l_3]
print(matrix)

firts_col = [row[0] for row in matrix]
print(firts_col)
