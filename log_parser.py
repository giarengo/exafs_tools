class ExafsFit:
    
    def __init__(self, filename):
        self.filename = filename 
     
    with open(filename) as file: 
        l = file.readlines() 

    for i, line in enumerate(l): 
        if line.find('Name') != -1: 
            name = line 
        if line.find('Independent points') != -1: 
            ind_points = float(line.split(sep=':')[1].strip())
        if line.find('Number of variables') != -1: 
            var_num = int(line.split(sep=':')[1].strip())
        if line.find('Chi-square') != -1: 
            chi_square = float(line.split(sep=':')[1].strip())
        if line.find('Reduced chi-square') != -1: 
            red_chi_square = float(line.split(sep=':')[1].strip())
        if line.find('Chi-square') != -1: 
            chi_square = float(line.split(sep=':')[1].strip())
        if line.find('R-factor  ') != -1: 
            r_fac = float(line.split(sep=':')[1].strip())    
        if line.find('Number of data sets') != -1: 
            datasets_num = int(line.split(sep=':')[1].strip())

        if line.find('guess parameters') != -1:
            i_guess = i 
        if line.find('set parameters') != -1:
            i_set = i 
        if line.find('def parameters') != -1:
            i_def = i 

        if line.find(': k-range') != -1: 
            k_range = line.split(sep='=')[1].strip()
        if line.find(': k-weight') != -1: 
            k_weight = line.split(sep='=')[1].strip()
        if line.find(': R-range') != -1: 
            r_range = line.split(sep='=')[1].strip()

        if line.find('name               N       S02') != -1:
            i_paths = i
    
    guess_par={}
    try:
        for line in l[i_guess+1:]: 
            ls = line.split()
            guess_par[ls[0]] = float(ls[2])
            guess_par['err_' + ls[0]] = float(ls[5])
            if line == '\n': 
                break
    except: 
        pass

    set_par={}
    try:
        for line in l[i_set+1:]: 
            ls = line.split()
            set_par[ls[0]] = float(ls[2])
            if line == '\n': 
                break
    except: 
        pass

    def_par={}
    try:
        for line in l[i_def+1:]: 
            ls = line.split()
            def_par[ls[0]] = float(ls[2])
            def_par['formula_' + ls[0]] = ls[4]
            if line == '\n': 
                break
    except: 
        pass

    paths_r={}
    try:
        for line in l[i_paths+2:]:
            ls = line.split()
            paths_r[ls[1]] = float(ls[-1])
            if line == '\n':
                break
    except:
        pass        