def transformer(path):
    with open(path) as archives:
        files = archives.readlines()

    files = files[1:]
    files = map(lambda x: x.strip(), files)
    files = map(lambda x: x.replace(', ',' '), files)
    filestwo = []
    for i in files:
        i = i.split(',')
        filestwo.append(i)
    
    return filestwo