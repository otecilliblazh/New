a='у у лукоморья дуб зеленый к златая цепь на дубе том и днем и ночью кот ученый т т  к'
print(type(a),a)
b={}
i=0
for c in a.split():
    for d in a.split():
        if c==d:
            i=i+1
            b[d]=i
    i=0
print(b)
