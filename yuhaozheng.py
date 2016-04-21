print("""This is a Warcraft editor!
Lets create our HEROs.
""")
Hero_name={}
A=['Blood_volume','Mana','Attack_force','Defense']
A_plus=[]
A_level=[]
while True:
    x=raw_input('His/Her/It name is:')
    if x=='end':break
    while not x in Hero_name:
        try:
            for key1 in A:
                print(key1)
                B = raw_input("Hero's %s are:" % key1)
                b=float(B)
                A_plus.append(b)
                print(key1,'=>',b)
            for key2 in A:
                C = raw_input("Growing rate of %s for %s are:" % (key2,x))
                c = float(C)
                print('Growing rate of',key2,'=>',c)
                A_plus.append(c)
        except ValueError, e:
            print('Please enter again')
        Hero_name.setdefault(x, A_plus)
        z=Hero_name[x]
        print(Hero_name,z)
        del A_plus[0:8]
    else:
        try:
            L=input('Your HERO is at level:')
            print(Hero_name[x])
            for key3 in A:
                l_plus = (z[A.index(key3) + 4] * (L - 1) + z[A.index(key3)])
                print(key3, '=>', l_plus)
        except ValueError, e:
            print('Please enter again')
