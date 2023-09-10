import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
 
# Create pd dataframe from Athena output file 
file = r'./GeGa_vs_SiGeGa.chi'
with open(file) as f:
    l = f.readlines() 
for i, line in enumerate(l): 
    if line.find('#') == -1:
        break 
l[i-1] = l[i-1].replace('#','')
l = [line.split() for line in l[i-1:]]
df = pd.DataFrame(l[1:], columns=l[0])
