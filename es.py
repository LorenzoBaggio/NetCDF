from sys import argv, exit #da sys importo solamente argv e exit
from netCDF4 import Dataset #leggere contenuto file
import numpy as np
import matplotlib # altrimenti da errore mancanza schermo per il grafico
matplotlib.use('Agg')
import matplotlib.pyplot as plt

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

fg.close()
#print(temp)
media=[]#lista vuota
#print(temp.shape)
#n_fov=temp.shape[0]#1000 temperature per ogni livello
n_al=temp.shape[1]#61 livelli
#somma=0
#for i in range(n_fov):#fino  1000 
   # somma+=temp[i]
#media.append(somma/n_fov)
#print(media)
#somma=np.sum(temp,axis=0) somma senza il for
media=np.mean(temp,axis=0) 
print(media)

#plt.plot(media,range(n_al))
media=media.reshape(61,1)
plt.pcolor(media)
#plt.show()
plt.ylim(0,61)
plt.savefig("pippo.pdf")






