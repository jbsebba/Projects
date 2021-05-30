import ast

def henttxt(liste, navn):
    f = open(navn, 'r')
    with f as filehandle:
        for line in filehandle:
            currentPlace = line[:-1]
            liste.append(currentPlace)
    f.close()
 
def lagtxt(liste, navn):
    f = open(navn, 'w+')
    with f as file:
        for listitem in liste:
            file.write('%s\n' % listitem)
    f.close()
    
def fjerntxt(navn, slette):
    with open(navn, "r") as f:
        lines = f.readlines()
    with open(navn, "w") as f:
        for line in lines:
            if line.strip("\n") != slette:
                f.write(line)
        
        
class lister:
    def hent(self):
        txtnavn = str(self) + '.txt'
        self = []
        henttxt(self, txtnavn)
        return self
        
utleidsk8 = lister.hent('utleidsk8')
utleid_set = set(utleidsk8)

if not utleid_set:
    print('\nDet er ingen skateboard som kan leveres\n')
else:
    sk8boards = lister.hent('sk8boards')

    amount = len(sk8boards)
    numbers = []
    a = 1
    for a in range(amount):
        numbers.append(a)
        a + 1

    sk8_dict = {}
    for key in numbers:
        for value in sk8boards:
            sk8_dict[key] = value
            sk8boards.remove(value)
            break

    # print(sk8_dict)
    utleidsk8_dict = {}
    
    for bli_igjen in utleidsk8:
        for key in numbers:
            if int(key) == int(bli_igjen):
                x = sk8_dict.pop(int(key))
                utleidsk8_dict[int(bli_igjen)] = x
            elif int(key) == int(bli_igjen):
                continue                


    #På tide å velge skateboards

    print('\nDisse skateboardene kan leveres\n')
    for key, value in utleidsk8_dict.items():
        print(key, ' : ', value)

    utleid_set = set(utleidsk8)

    prompt = 'Hvilket skateboard leverer du?\n'
    while True:
        try:
            levert = input(prompt)
            if levert in utleid_set:
                for x in utleidsk8:
                    if int(levert) == x:
                        break
                    else: continue
                break
            else: raise ValueError
        except ValueError: prompt = 'Ugyldig verdi, prøv igjen\n'


    vnt_temp = {}
    file = open("vnt_temp.txt", "r")
    contents = file.readlines()
    for line in contents:
        dictitem = ast.literal_eval(line)
        currentline = line[:-1]
        for key, value in dictitem.items():
            vnt_temp[key] = value
    
    values_chosen_item = vnt_temp[int(levert)]
    navn = values_chosen_item[0]
    tlf = values_chosen_item[1]
    
    
    
    valgtsk8board = utleidsk8_dict[int(levert)]
    
    
    vnt_levert = lister.hent('vnt_levert')
    vnt_levert.append([valgtsk8board, navn, tlf, 'LEVERT'])
    lagtxt(vnt_levert, 'vnt_levert.txt')
    
    
    fjerntxt('vnt_temp.txt', str(dictitem))
    fjerntxt('utleidsk8.txt', str(levert))
    
    print('\nTusen takk for at du har levert:   ____', valgtsk8board, '____ brettet ', navn)
    print('\nMvh. avdelingen RAW\n')
