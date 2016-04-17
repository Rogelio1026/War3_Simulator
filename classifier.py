print("""This is a classifier of cargo dilivery
1:Chicago
2:Los_Angles
3:Boston
""")
empty_dict = {}
filled_dict = {"chicago": 1, "los_angles": 2, "boston": 3}
li = []
a=0
while a<len(filled_dict):
    li.append(0)
    a=a+1
while True:
    x = raw_input('Please enter the destination:').lower()
    if x == 'end': break
    if x in filled_dict:
        y = filled_dict[x]
        li[y - 1] = li[y - 1] + 1
        print('Your cargo is in category %s' % y)
    else:
        a= raw_input('Your cargo is not in category, do you want to add another destination? Y or N:')
        if a=='Y':
            filled_dict.setdefault(x,len(filled_dict)+1 )
            li.append(1)
for city in filled_dict.keys():
    print('There are %d cargo for %s ' % (li[filled_dict[city] - 1], city))
