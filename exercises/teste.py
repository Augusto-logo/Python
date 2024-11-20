def notas(*notas, situação=False):
    media = sum(notas)/len(notas)
    return print(media)


notas(2,4,situação=True)