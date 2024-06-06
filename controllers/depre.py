import flet as ft
import threading 

# Clase que herede de thred
class Hilo(threading.Thread):
    def __init__(self,num):
        
        threading.Thread.__init__(self)
        self.num= num
    
    def run(self):
        print ('lo Soy el hi',self.num)
        
print ('Soy el hilo principal')
for i in range(0,6):
    t = Hilo(i)
    t.start()
    t.join()
