
aura = [0]

def aura_points():
    while True:
        try:       
            new_aura = aura[0] + 10
            aura.append(new_aura)
            aura.pop(0)
            print(aura)

        except IndexError:
            ...

aura_points()