def run_program(run):
    valgt = str(programmer[int(run)])
    print(valgt)
    import valgt
    
    
print('\nMENY')
print('''\n     
    1: Leie Skateboard              3: Skateboard i bruk nå         \n
    2: Levere Skateboard            4: Tidligere utleid             \n
                                    5: Søk i brukere                \n
    ''')

navn = {1: 'Leie Skateboard', 2: 'Levere Skateboard,', 3: 'Skateboard ute', 4: 'Tidligere utleid', 5: 'Finn bruker'}
programmer = {1: 'leie_skateboard', 2: 'levere_skateboard,', 3: 'skateboard_ute', 4: 'tidligere_utleid', 5: 'finn_bruker'}

run = input('Velg program')

if int(run) in programmer.keys():
    run_program(run)
else: print('nopp')