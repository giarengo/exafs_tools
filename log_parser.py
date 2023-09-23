class ExafsFit():

    def __init__(self, filename): 
        self.filename = filename 

    def file_parsing(self):    
        with open(self.filename) as file: 
            l = file.readlines() 

        for i, line in enumerate(l): 
            if line.find('Name') != -1: 
                self.name = line.split()[2] 
            if line.find('Independent points') != -1: 
                self.ind_points = float(line.split(sep=':')[1].strip())
            if line.find('Number of variables') != -1: 
                self.var_num = int(line.split(sep=':')[1].strip())
            if line.find('Chi-square') != -1: 
                self.chi_square = float(line.split(sep=':')[1].strip())
            if line.find('Reduced chi-square') != -1: 
                self.red_chi_square = float(line.split(sep=':')[1].strip())
            if line.find('Chi-square') != -1: 
                self.chi_square = float(line.split(sep=':')[1].strip())
            if line.find('R-factor  ') != -1: 
                self.r_fac = float(line.split(sep=':')[1].strip())    
            if line.find('Number of data sets') != -1: 
                self.datasets_num = int(line.split(sep=':')[1].strip())

            if line.find('guess parameters') != -1:
                i_guess = i 
            if line.find('set parameters') != -1:
                i_set = i 
            if line.find('def parameters') != -1:
                i_def = i 

            if line.find(': k-range') != -1: 
                self.k_min = line.split(sep='=')[1].split(sep='-')[0]
                self.k_max = line.split(sep='=')[1].split(sep='-')[1].strip()
            if line.find(': k-weight') != -1: 
                self.k_weight = line.split(sep='=')[1].strip()
            if line.find(': R-range') != -1: 
                self.r_min = line.split(sep='=')[1].split(sep='-')[0]
                self.r_max = line.split(sep='=')[1].split(sep='-')[1].strip()

            if line.find('name               N       S02') != -1:
                i_paths = i
        
        self.guess_par={}
        try:
            for line in l[i_guess+1:]: 
                ls = line.split()
                self.guess_par[ls[0]] = float(ls[2])
                self.guess_par['err_' + ls[0]] = float(ls[5])
                if line == '\n': 
                    break
        except: 
            pass

        self.set_par={}
        try:
            for line in l[i_set+1:]: 
                ls = line.split()
                self.set_par[ls[0]] = float(ls[2])
                if line == '\n': 
                    break
        except: 
            pass

        self.def_par={}
        try:
            for line in l[i_def+1:]: 
                ls = line.split()
                self.def_par[ls[0]] = float(ls[2])
                self.def_par['formula_' + ls[0]] = ls[4]
                if line == '\n': 
                    break
        except: 
            pass

        self.paths_r={}
        try:
            for line in l[i_paths+2:]:
                ls = line.split()
                self.paths_r[ls[1]] = float(ls[-1])
                if line == '\n':
                    break
        except:
            pass   
