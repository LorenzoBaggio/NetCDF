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
#n_fov=temp.shape[0]#1000 temperature per ogni livello
#n_al=temp.shape[1]#61 livelli
#somma=0
#for i in range(n_fov):#fino  1000 
   # somma+=temp[i]
#media.append(somma/n_fov)
#print(media)
#somma=np.sum(temp,axis=0) somma senza il for
media=np.mean(temp,axis=0) 
print(media)

fg.close()







