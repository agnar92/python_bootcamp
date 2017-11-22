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