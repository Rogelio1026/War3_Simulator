print("""This is a Warcraft editor!
Lets create our HEROs.
""")
Hero_name={}
A=['Blood_volume','Mana','Attack_force','Defense']
while True:
    x=raw_input('His/Her/It name is:')
    if x=='end':break
    while not x in Hero_name:
        A_x=[]
        try:
            for key1 in A:
                B = raw_input("Hero's %s are:" % key1)
                b=float(B)
                A_x.append(b)
                print(key1,'=>',b)
            for key2 in A:
                C = raw_input("Growing rate of %s for %s are:" % (key2,x))
                c = float(C)
                print('Growing rate of',key2,'=>',c)
                A_x.append(c)
        except ValueError, e:
            print('Please enter again')
        Hero_name.setdefault(x, A_x)
        l = Hero_name[x]
    else:
        try:
            L=input('Your HERO is at level:')
            for key3 in A:
                l_plus = (l[A.index(key3) + 4] * (L - 1) + l[A.index(key3)])
                print(key3, '=>', l_plus)
        except ValueError, e:
            print('Please enter again')
