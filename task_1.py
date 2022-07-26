def dictionary(data):
    slovar = {}
    for i in data:
        if 'x' in i:
            if i[0] != 'x':
                j = 0
                s = ''
                while i[j] != 'x':
                    s += i[j]
                    j += 1
                value = int(s)
                key = i.replace(s, '', 1)
                slovar[key] = value
            else:
                value = 1
                key = i
                slovar[key] = value
        else:
            slovar['0'] = int(i)
    return slovar

def dictionary_2(data, slovar):
    for i in data:
        if 'x' in i:
            if i[0] != 'x':
                j = 0
                s = ''
                while i[j] != 'x':
                    s += i[j]
                    j += 1
                value = int(s)
                key = i.replace(s, '', 1)
                if key in slovar:
                    g = slovar[key]
                    g += value
                    slovar[key] = g
                else:
                    slovar[key] = value
            else:
                value = 1
                key = i
                if key in slovar:
                    g = slovar[key]
                    g += value
                    slovar[key] = g
                else:
                    slovar[key] = value
        else:
            if '0' not in slovar:
                slovar['0'] = int(i)
            else:
                g = slovar['0']
                g += int(i)
                slovar['0'] = g
    return slovar

def sum(sl):
    s = ''
    for key in sl:
        s += '+'
        if key != '0':
            value = sl[key]
            if value != 1:
                s += str(value) + key
            else:
                s += key
        else:
            value = sl[key]
            s += str(value)
    return s
