#Trajectoire d'un mobile
#Thomas Mongaillard - 01/20
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

fenetre = Tk()
fenetre.title("Trajectoire d'un mobile")

masse_max = 10
h_max = 10
angle_max = 90
vitesse_max = 20
mu_max = 2
F_max = 10

xm = 50
ym = 35



liste_trace = []

#frame commande
cmd = Frame(fenetre)
cmd.pack(side='left',fill='y')

#frame de controle
controle = LabelFrame(cmd,text='Paramètres',bd=5,relief='ridge')
controle.pack(fill='x')

#widget frame de controle
#masse
frame_mas = LabelFrame(controle,text="Masse du projectile")
frame_mas.pack(expand=0,fill='x',ipadx=100)
v_m = DoubleVar()
v_m.set(1)
scale_mas = Scale(frame_mas, orient='horizontal', from_=0.1, to=masse_max, resolution=0.1,variable=v_m)
label_kg = Label(frame_mas,text='kg')
label_kg.pack(side='right')
scale_mas.pack(fill='x')

#hauteur
def adapt_hauteur(h_m):
    global w,h
    M = liste_dessins[0]
    x0,y0,x1,y1 = canv.coords(M.dess)
    r = (x1-x0)/2
    h_p = float(h_m)*.9*h/ym
    x0,y0 = conversion((-r,-r+h_p))
    x1,y1 = conversion((r,r+h_p))
    canv.coords(M.dess,x0,y0,x1,y1)
    
frame_h = LabelFrame(controle,text="Hauteur initiale")
frame_h.pack(expand=0,fill='x')
v_h_m = DoubleVar()
scale_h = Scale(frame_h, orient='horizontal', from_=0, to=h_max, resolution=0.1,command=adapt_hauteur,variable=v_h_m)
label_m = Label(frame_h,text='m')
label_m.pack(side='right')
scale_h.pack(fill='x')

#angle
frame_angle = LabelFrame(controle,text='Angle')
frame_angle.pack(expand=0,fill='x')
v_alpha = DoubleVar()
v_alpha.set(45)
scale_angle = Scale(frame_angle, orient='horizontal', from_=0, to=angle_max, resolution=0.1,variable=v_alpha)
label_deg = Label(frame_angle,text='degrés')
label_deg.pack(side='right')
scale_angle.pack(fill='x')

#vitesse
frame_vitesse = LabelFrame(controle,text='Vitesse initiale')
frame_vitesse.pack(expand=0,fill='x')
v_v0 = DoubleVar()
v_v0.set(10)
scale_vitesse = Scale(frame_vitesse, orient='horizontal', from_=0, to=vitesse_max, resolution=0.1,variable=v_v0)
label_ms = Label(frame_vitesse,text='m/s')
label_ms.pack(side='right')
scale_vitesse.pack(fill='x')

#coefficient de frottement
frame_frot = LabelFrame(controle,text="Coefficient de frottement de l'air")
frame_frot.pack(expand=0,fill='x',ipadx=30)
v_mu = DoubleVar()
scale_frot = Scale(frame_frot, orient='horizontal', from_=0, to=mu_max, resolution=0.1,variable=v_mu)
label_kgs = Label(frame_frot,text='kg/s')
label_kgs.pack(side='right')
scale_frot.pack(fill='x')

#Vent latéral
frame_vent = LabelFrame(controle,text="Force du vent latéral")
frame_vent.pack(expand=0,fill='x')
v_f_l = DoubleVar()
scale_vent = Scale(frame_vent, orient='horizontal', from_=0, to=F_max, resolution=0.1,variable=v_f_l)
label_N = Label(frame_vent,text='N')
label_N.pack(side='right')
scale_vent.pack(fill='x')





#frame d'action
act = LabelFrame(cmd,text='Actions',bd=5,relief='ridge')
act.pack(fill='both',expand=1)

def maj_aff():
    global w,h
    canv.update()
    h = canv.winfo_height()
    w = canv.winfo_width()
    for dessin in liste_dessins:
        dessin.resize()

#btn_maj = Button(act,text="Mettre à jour l'affichage", command=maj_aff)
#btn_maj.pack(fill='x',ipady=5)

def afficher_mobile():
    global w,h,listeX,listeY,k,liste_trace
    x,y = listeX[k],listeY[k]
    M = liste_dessins[0]
    x0,y0,x1,y1 = canv.coords(M.dess)
    r = (x1-x0)/2
    x_p = x*.9*w/xm
    y_p = y*.9*h/ym
    x0,y0 = conversion((-r+x_p,-r+y_p))
    x1,y1 = conversion((r+x_p,r+y_p))
    canv.coords(M.dess,x0,y0,x1,y1)
    k=k+1
    if k < len(listeX):
        fenetre.after(16
                      ,afficher_mobile)
        if k%5 == 0:
            x = x*.9*w/xm
            y = y*.9*h/ym
            x0,y0 = conversion((x-2,y-2))
            x1,y1 = conversion((x+2,y+2))
            p = canv.create_oval(x0,y0,x1,y1,fill='red')
            liste_trace.append(p)
    else:
        btn_reset['state']='normal'
    
###Fonction de résolution
def calcul0(tau):
    global m,v0,alpha,mu,f_l,h_m,t
    listeX = [0]
    listeY = [h_m]
    x = 0
    y = h_m
    while y>=0:
        x = tau*(v0*np.cos(alpha*np.pi/180)+f_l/mu)*(1-np.exp(-t/tau))-f_l/mu*t
        y = h_m - tau*9.81*t+(v0*np.sin(alpha*np.pi/180)+tau*9.81)*(1-np.exp(-t/tau))*tau
        listeX.append(x)
        listeY.append(y)
        t = t+0.016
    return listeX,listeY



def calcul1():
    global m,v0,alpha,mu,f_l,h_m,t
    listeX = [0]
    listeY = [h_m]
    x = 0
    y = h_m
    while y>=0:
        x = -f_l/(2*m)*t**2+v0*np.cos(alpha*np.pi/180)*t
        y = -9.81/2*t**2+v0*np.sin(alpha*np.pi/180)*t+h_m
        listeX.append(x)
        listeY.append(y)
        t = t+0.016
    return listeX,listeY

def anim0(tau):
    global w,h,listeX,listeY,t,k,liste_trace
    listeX,listeY = calcul0(tau)
    M = liste_dessins[0]
    x0,y0,x1,y1 = canv.coords(M.dess)
    r = (x1-x0)/2
    k=0
    afficher_mobile()

       
def anim1():
    global w,h,listeX,listeY,t,k,liste_trace
    listeX,listeY = calcul1()
    M = liste_dessins[0]
    x0,y0,x1,y1 = canv.coords(M.dess)
    r = (x1-x0)/2
    k=0
    afficher_mobile()
        
        

def resol():
    global w,h,m,v0,alpha,mu,f_l,h_m,t

    m = v_m.get()
    h_m = v_h_m.get()
    v0 = v_v0.get()
    alpha = v_alpha.get()
    mu = v_mu.get()
    f_l = v_f_l.get()
    

    #non accès aux paramètres
    scale_angle['state']='disabled'
    scale_mas['state']='disabled'
    scale_vitesse['state']='disabled'
    scale_h['state']='disabled'
    scale_frot['state']='disabled'
    scale_vent['state']='disabled'
    btn_reset['state']='disabled'


    deltaT = 0.016
    t = deltaT
    
    if mu == 0 :
        anim1()
    else:
        tau = m/mu
        anim0(tau)



btn_lancement = Button(act,text='Lancer le mobile',command=resol)
btn_lancement.pack(fill='x',ipady=5)


def reset():
    global liste_trace
    scale_angle['state']='normal'
    scale_mas['state']='normal'
    scale_vitesse['state']='normal'
    scale_h['state']='normal'
    scale_frot['state']='normal'
    scale_vent['state']='normal'

    M = liste_dessins[0]
    r=10
    x0,y0 = conversion((-r,-r))
    x1,y1 = conversion((r,r))
    canv.coords(M.dess,x0,y0,x1,y1)

    for p in liste_trace:
        canv.delete(p)
    

btn_reset = Button(act,text='Reset',command=reset)
btn_reset.pack(fill='x',ipady=5)

def export():
    global listeX,listeY,mu,f_l,m,alpha
    plt.figure()
    plt.title(r'm = {} kg, $\mu$ = {} kg/s, $\alpha$ = {} deg, $f_l$ = {} N'.format(m,mu,alpha,f_l))
    plt.plot(listeX,listeY,'-')
    plt.xlabel(r'$x (m)$')
    plt.ylabel(r'$y (m)$')
    plt.grid()
    plt.savefig('trajectoire.pdf')


    file = open('trajectoire.txt','w')
    file.write('m = {} kg \t mu = {} kg/s \t alpha = {} deg \t f_l = {} N\n'.format(m,mu,alpha,f_l))
    file.write('x(m)\t y(m)\n')
    for x,y in zip(listeX,listeY):
        file.write('{}\t {}\n'.format(x,y))
    file.close()

btn_export = Button(act,text='Exporter',command=export)
btn_export.pack(fill='x',ipady=5)


#frame affichage
aff = LabelFrame(fenetre,text='Graphe',bd=5,relief='ridge')
aff.pack(fill='both',expand=1)

#widget affichage
canv = Canvas(aff, bg='white',cursor='fleur')
canv.pack(fill='both',expand=1)

##gestion du graphe
canv.update()
h = canv.winfo_height()
w = canv.winfo_width()


liste_dessins = []

def conversion(x):
    global w,h
    '''renvoie les coordonnées pour pouvoir afficher dans le canvas'''
    x,y = x
    y = h-y
    return (x,y)

class Dessin():
    def __init__(self,dess,f0,f1):
        self.dess = dess
        self.f0 = f0
        self.f1 = f1

    def resize(self):
        global w,h
        x0,y0 = conversion(self.f0(w,h))
        x1,y1 = conversion(self.f1(w,h))
        canv.coords(self.dess,x0,y0,x1,y1)

    def dep(self,dx,dy):
        global w,h
        dx = dx*w/xm
        dy = -dy*h/ym
        canv.move(self.dess,dx,dy)

#axe x
x0,y0 = conversion((0,0))
x1,y1 = conversion((w,0))
axe_x = canv.create_line(x0,y0,x1,y1,width=4,fill='black')
def f0(w,h):
    return 0,0
def f1(w,h):
    return .9*w,0
X = Dessin(axe_x,f0,f1)
liste_dessins.append(X)

#axe y
x0,y0 = conversion((0,0))
x1,y1 = conversion((0,h))
axe_y = canv.create_line(x0,y0,x1,y1,width=4,fill='black')
def f0(w,h):
    return 0,0
def f1(w,h):
    return 0,.9*h
Y = Dessin(axe_y,f0,f1)
liste_dessins.append(Y)

#grid
#sur x
def create_f0(k):
    def f0(w,h):
        pas = int(10*.9*w/xm)
        return k*pas,0
    return f0
def create_f1(k):
    def f1(w,h):
        pas = int(10*.9*w/xm)
        return k*pas,.9*h
    return f1

for k in range(1,int(xm/10)):
    f0 = create_f0(k)
    f1 = create_f1(k)
    x0,y0=conversion(f0(w,h))
    x1,y1=conversion(f1(w,h))
    l = canv.create_line(x0,y0,x1,y1,width=1,fill='black',dash=(4,))
    D = Dessin(l,f0,f1)
    liste_dessins.append(D)

#sur y
def create_f0(k):
    def f0(w,h):
        pas = int(5*.9*h/ym)
        return 0,k*pas
    return f0
def create_f1(k):
    def f1(w,h):
        pas = int(5*.9*h/ym)
        return .9*w,k*pas
    return f1

for k in range(1,int(ym/5)):
    f0 = create_f0(k)
    f1 = create_f1(k)
    x0,y0=conversion(f0(w,h))
    x1,y1=conversion(f1(w,h))
    l = canv.create_line(x0,y0,x1,y1,width=1,fill='black',dash=(4,))
    D = Dessin(l,f0,f1)
    liste_dessins.append(D)

#mobile
r=10
x0,y0 = conversion((-r,-r))
x1,y1 = conversion((r,r))
mobile = canv.create_oval(x0,y0,x1,y1,fill='red')
def f0(w,h):
    return -r,-r
def f1(w,h):
    return r,r
M = Dessin(mobile,f0,f1)
liste_dessins = [M]+liste_dessins
        


###translation du canvas
def stop_dragto(evt):
    canv.unbind('<Motion>')

def move(evt):
    x = evt.x
    y = evt.y
    canv.scan_dragto(x,y,gain=1)
    canv.bind('<ButtonRelease-1>',stop_dragto)

def translate(evt):
    x = evt.x
    y = evt.y
    canv.scan_mark(x,y)
    canv.bind('<Motion>',move)

canv.bind('<Button-1>',translate)

#redimensionnement
def maj_aff(evt):
    global w,h
    canv.update()
    h = evt.height
    w = evt.width
    for dessin in liste_dessins:
        dessin.resize()
canv.bind('<Configure>',maj_aff)

fenetre.mainloop()
