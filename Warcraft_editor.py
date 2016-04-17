print("""This is a Warcraft editor!
Lets create our HEROs.
""")
while True:
    x=raw_input('His/Her/It name is:')
    if x=='end':break
    Hero_name={}
    while not x in Hero_name:
        ability=[]
        A=['Blood volume','Mana','Attack force','Defense']
        try:
            for key in A:
                B = raw_input("Hero's %s are:" % key)
                b=float(B)
                ability.append(b)
            print('%s is level 0, blood volume: %d, Mana: %d, Attack force: %d, Defense: %d' % (x, ability[0], ability[1],
            ability[2], ability[3]))
        except ValueError, e:
            print('Please enter again')
        Hero_name.setdefault(x, ability)