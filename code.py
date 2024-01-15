import pandas as pd
import os
os.chdir('D:/')
file = pd.read_csv("data.csv")
def cgpa(x):
     ...:     return x[:5].mean()
file['CGPA'] = file.apply(trans,axis = 1)
bin = [0,7.5,10.0]

cutoff = pd.cut(file['CGPA'],bin)

labels =["Not Eligible","Eligible"]

cutoff = pd.cut(file['CGPA'],bin,labels =  labels)
print(cutoff.value_counts());

