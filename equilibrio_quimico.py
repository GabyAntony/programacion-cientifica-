import numpy as np
import matplotlib.pyplot as plt


N = int(input("introduce la cantidad de pasos a simular: ") )
DT = input("introduce la contidad de segundos por paso: ")
cantidad_compuestos = int(input("introduce la cantidad de compuestos"))
constantes = np.zeros(cantidad_compuestos -1)

for i in range(cantidad_compuestos -1):
    k = input(f"introduce la cosntante {i+1}")
    constantes[i] = k

compuestos = np.zeros((cantidad_compuestos,N)) 

for i in range(cantidad_compuestos):
    a0 = input(f"introduce la masa inicial del compeusto {i+1}")
    cantidad_compuestos[i][0] = a0





K1 = 0.5
K2 = 0.2

DT = 0.01
N = 1000

A = np.zeros(N)
B = np.zeros(N)

A[0] = 1.0
B[0] = 0.0

calculate_derivada = lambda a, b: ((-K1*a) + (K2*b)) * DT

for i in range(N-1):
    da = calculate_derivada(A[i],B[i])
    A[i+1] = A[i] + da
    B[i+1] = A[0] + B[0] - A[i+1]

if  not np.isclose(B[-1]/A[-1],K1/K2 , atol=1e-2):
    print("ley de conservacion de masa  no cumplida")

print("ley de conservacion de masa cumplida")

tiempo = np.arange(N) * DT

plt.figure(figsize=(10, 4))
plt.plot(tiempo, A, label='compuesto A ', color='orange')
plt.plot(tiempo, B, label='compuesto B', color='green')

plt.title('conservacion de masa ')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('masa (gr)')
plt.grid(True)
plt.legend()
plt.show()
