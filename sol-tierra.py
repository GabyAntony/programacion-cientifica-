import numpy as np
import matplotlib.pyplot as plt


GM = 1
DT = 0.001
TIMES = 5000 

vx,vy = 0.0, 1.0
x,y = 1.0,0.0 
e = 0.0

list_x = []
list_y =[]
list_e = []

calculate_velocity  = lambda r,a,v: (-GM * a / (r**3))* DT + v
calculate_cordenadas = lambda v, a: a + v * DT
calculate_energia = lambda r,vx, vy : (0.5*(vx**2+vy**2)) + (-GM/r)

for i in range(TIMES):
    list_x.append(x)
    list_y.append(y)
    list_e.append(e)

    r = np.sqrt(x**2 + y**2)
    vx = calculate_velocity(r,x,vx)
    vy = calculate_velocity(r,y,vy)
    x = calculate_cordenadas(vx, x)
    y = calculate_cordenadas(vy,y)
    e = calculate_energia(r,vx,vy)

plt.figure(figsize=(6, 6))
plt.plot(list_x, list_y, 'b-', label='Órbita del planeta')
plt.gca().set_aspect('equal')
plt.legend()
plt.show()


plt.figure(figsize=(6, 6))
plt.plot(list_e, 'b-', label='enegia')
plt.gca().set_aspect('equal')
plt.legend()
plt.show()


