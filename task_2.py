def posled(data):
    s = [data[0]]
    for i in data:
        if i > max(s):
            s.append(i)
    return(s)
