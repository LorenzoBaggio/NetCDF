from sys import argv, exit #da sys importo solamente argv e exit
from netCDF4 import Dataset
import numpy as np

if len(argv)<=1:
    print("errore")
    exit(1)#se 0 corretto , da 1 a 255 scorretto
v=argv[1]
fg=Dataset(v,"r")#classe che permette di leggere o scrivere una variabile/stringa
#print(fg)
atmc=fg.groups["atmospheric_components"]
t=atmc.variables['T']
#print(t)
temp=np.array(t)#creo array
#print(temp)
media=[]#lista vuota
#print(temp.shape)
n_fov=temp.shape[0]
n_al=temp.shape[1]
for i in range(n_fov):
    somma=0
    for y in range(n_al):
       somma+=temp[i,y]
    media.append(somma/n_al)
    print(media[i])
fg.close()







