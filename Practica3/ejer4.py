anim={'Gato Montes':2, 'Yacare overo':4,'Boa acuática':5}

print(anim)
for i in anim:
    mylist = list(i)
    char = mylist[anim[i]]
    text = '_' * len(i)
    mytext = list(text)
    mytext[anim[i]] = char
    aux = ' '.join(mytext)
    print(aux)