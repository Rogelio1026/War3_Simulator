print("""This is a classifier of cargo dilivery
1:Chicago
2:Los_Angles
3:Boston
""")
empty_dict = {}
filled_dict = {"chicago": 1, "los_angles": 2, "boston": 3}
li = [0, 0, 0]
while True:
    x = raw_input('Please enter the destination:').lower()
    if x == 'robert': break
    if x in filled_dict:
        y = filled_dict[x]
        li[y - 1] = li[y - 1] + 1
        print('Your cargo is in category %s' % y)
    else:
        print('Your cargo is not in category')
for city in filled_dict.keys():
    print('There are %d cargo for %s ' % (li[filled_dict[city] - 1], city))
