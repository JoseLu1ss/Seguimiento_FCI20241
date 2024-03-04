import numpy as np

class Particula:
    """Se crea una clase llamada Particula, que cuenta con atributos fijos como masa y carga eléctrica,
       y otros no fijos, como los asociados a la posición, velocidad y aceleración. Además, cuenta con 
       métodos que dan constancia de su dinámica dentro de un campo magnético uniforme, y a la vez, 
       interactuando eléctricamente con otra(s) partícula(s).
       
        Atributos:
                masa: m (float). Representa la masa de la partícula en el kilogramos
                carga: q (float). Representa la carga de la partícula en Coulombs
                posicion inicial: r0 (array). Representa la posición de la partícula m.
                velocidad inicial: v0 (array). Representa la velocidad inicial de la partícula m/s
                aceleracion inicial: a0 (array). Representa la aceleración de la partícula.
        
        Métodos:
                FuerzaLorentz() 
                FuerzaCoulomb()
                FuerzaTotal()
                AceleracionFinal()
                SolNum()
                Graficas()
    """

    #masa = 10
    #carga = 1
    # posicion = np.zeros(3)
    # velocidad = np.zeros(3)
    #aceleracion = np.zeros(3)

    def __init__(self, r0, v0, a0, m, q):
        '''
        Constructor de la clase.
        
        Parámetros:
            r0 (array): posición inicial.
            v0 (array): velocidad inicial.
            a0 (array): Aceleración inicial.
            q (float) : carga de la partícula
            m (float) : masa de la partícula'''
        self.posicion = r0
        self.velocidad = v0
        self.aceleracion = a0
        self.masa = m
        self.carga = q
    
    #Método para la fuerza de Lorentz
    def FuerzaLorentz(self, campoB):
        ''' Fuerza magnética: fuerza de interacción magnética mediada por la parte magnética de la fuerza de Lorentz.
        Parámetros:
            - campoB (array): Un campo magnético como vector
            - self : método propio de la partícula
            
        Retorna:
            - arrar: Arreglo de numpy de tres elementos con las componentes de las fuerzas [fx,fy,fz]'''
        F_L = self.carga * np.cross(self.velocidad, campoB) #Producto vectorial entre v y B (Lorentz)
        return F_L #Fuerza de Lorentz

    #Método para la fuerza de Coulomb
    def FuerzaCoulomb(self, Q, posicion2, k = 9e+9):
        '''Fuerza eléctrica: la fuerza de interacción eléctrica mediada por la fuerza de Coulomb.
        Parámetros:
            - self: método propio de la partícula 1
            - Q (float): la carga de la partícula 2
            - posicion2 (array): la posición de la partícula 2
        Retorna:
            - Arreglo de tres elementos con las componentes de la fuerza [Fx,Fy,Fz]'''
        C = k*self.carga*Q #Constante de las cargas
        dir = self.posicion - posicion2 #Dirección del campo eléctrico
        r = np.sqrt(np.dot(self.posicion - posicion2, self.posicion - posicion2)) #Magnitud de dirección
        F_C = (C/r**3)*dir #Fuerza de Coulomb
            
        return F_C

    
    #Método para la fuerza total
    def FuerzaTotal(self):
        ''' Fuerza total: calcula la fuerza de Lorentz para la partícula definida.
        Parámetros:
            - self: como método propio del objeto.
        Retorna:
            - Arreglo de tres elementos con las componentes de la fuerza total.'''
        F_L = self.FuerzaLorentz(campoB)
        F_C = self.FuerzaCoulomb(Q, posicion2, k = 9e+9)

        F_T = F_L + F_C
        return F_T
    
    #Método para la aceleración final
    def AceleracionFinal(self):
        '''Aceleración final: calcula la aceleración total de la partícula 
        Parámetros:
            - self: como método propio del objeto
        Retorna:
            - Arreglo de tres elementos con las componente de la aceleración total de la partícula.'''
        F_T = self.FuerzaTotal()
        a = F_T / self.masa

        return a
    
    #Método para la solución numérica
    def SolNum(self, t, dt):
        a = self.AceleracionFinal()
        # dt = 0.1
        #T = np.arange(0, t, dt)
        T = np.arange(0, t + dt, dt)
        Posicion = np.zeros((len(T), 3))
        Velocidad = np.zeros((len(T), 3))
        Posicion[0] = self.posicion
        Velocidad[0] = self.velocidad
        
        
        for i in range(len(T)):
            Velocidad[i + 1] = Velocidad[i] + a*t[i + 1]
            Posicion[i + 1] = Posicion[i] + Velocidad[i]*t[i + 1] + 0.5*a*(t[i + 1])**2


posicion = np.array([3,1,2])
velocidad = np.array([0,0,0])

p = Particula(posicion, velocidad, aceleracion=np.zeros(3), m = 10, q = 1)
campoB = np.array([2, 1, 5])
Q = -1
posicion2 = np.array([-1, 1, 2])

F_L = p.FuerzaLorentz(campoB)
F_C = p.FuerzaCoulomb(Q, posicion2)
F_T = p.FuerzaTotal()
a = p.AceleracionFinal()
sol = p.SolNum(10)



#######PRUEBAS#######

#print(f"La fuerza de Lorentz es: {F_L}")
# print(f"La fuerza de Coulomb es: {F_C}")
# print(f"La fuerza total es: {F_T}")
# print(f"La aceleración es: {a}")
#print(sol)