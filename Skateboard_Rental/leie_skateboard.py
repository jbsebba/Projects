
def henttxt(liste, txtnavn):
    f = open(txtnavn, 'r')
    with f as filehandle:
        for line in filehandle:
            currentPlace = line[:-1]
            liste.append(currentPlace)
    f.close()
 
def lagtxt(liste, txtnavn):
    f = open(txtnavn, 'w+')
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
    
class person:
    def __init__(self, valgt, navn, tlf):
        self.valgt = valgt
        self.navn = navn
        self.tlf = tlf



sk8boards = []
henttxt(sk8boards, 'sk8boards.txt')

numbers = []
amount = len(sk8boards)
a = int
for a in range(amount):
    numbers.append(a)
    a + 1

sk8_dict = {}
for key in numbers:
    for value in sk8boards:
        sk8_dict[key] = value
        sk8boards.remove(value)
        break

utleidsk8 = []
henttxt(utleidsk8, 'utleidsk8.txt')
for items in utleidsk8:
    sk8_dict.pop(int(items))


current_person = person(0,'','')

current_person.navn = input('\nHva er navnet ditt?\n')
current_person.tlf = input('\nHva er tellefonnummeret ditt?\n')



#På tide å velge skateboards
print('\n Velg mellom disse skateboardene\n')
for key, value in sk8_dict.items():
    print(key, ' : ', value)
    

prompt = 'Hvilket skateboard velger du?\n\n'
while True:
    try:
        valgt = int(input(prompt))
        if valgt < 0 or valgt > amount:
            raise ValueError
        else: break
    except ValueError:
        prompt = 'Dette skateboardet finnes ikke. Velg mellom 0 og ', amount,

current_person.valgt = valgt



utleidsk8 = lister.hent('utleidsk8')
utleidsk8.append(current_person.valgt)
lagtxt(utleidsk8, 'utleidsk8.txt')

vnt_list = lister.hent('vnt_temp')
vnt_dict = {}
vnt_dict[current_person.valgt] = [current_person.navn, current_person.tlf]
vnt_list.append(vnt_dict)
lagtxt(vnt_list, 'vnt_temp.txt')

valgtsk8board = sk8_dict[int(valgt)]


print('\nGRATULERER! Du låner nå ____', valgtsk8board, '___ ', current_person.navn)
print('Husk å lever tilbake!\n')
#print(*valgt_navn, sep = '\n')
print('\n')