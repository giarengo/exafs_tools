import pandas as pd 

# Athena / Artemis parser
def parser(filename):
    with open(filename) as file: 
        l = file.readlines() 

    for i, line in enumerate(l): 
        if line.find('#') != -1: 
            l[i] = l[i].replace('#','')
        if line.find('---') != -1:
            i_data = i

    file = StringIO(''.join(l[i_data+1:]))
    df = pd.read_csv(file, sep='\s+')

    return df
