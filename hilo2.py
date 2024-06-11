import threading #libreria para el manejo de hilos
#Declaracion de Clase
class Hilo(threading.Thread):
    def __init__(self,num):
#llamando al constructor de la clase Thread y mandando como paramemtro
#la referencia a la clase Hilo
        threading.Thread.__init__(self)
        self.num= num
#metodo que ejecutara el hilo al llamarse con el metodo start()
    def run(self):
        print ('lo Soy el hi',self.num)
        
 
#Programa Principal
print ('Soy el hilo principal')
for i in range(0,6):
    t = Hilo(i)
    t.start()
    t.join(); #Espera a que todos los hilos terminen para que finalice el hilo principal
