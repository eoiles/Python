def lenth(code):
    return 1/len([i for i in code if i])

def value(pseudo,code):
    return lenth(pseudo)/lenth(code)

print(value(pseudo,code))
