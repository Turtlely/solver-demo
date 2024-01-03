# Integration schemes are tested on a spring mass oscillator

import numpy as np
import solver
import matplotlib.pyplot as plt

# Initial conditions
m = 1 # kg
x = 1 # m
v = 0 # m/s
k = 1 # N/m

# Time step
dt = 0.1 # s

# Potential
def V(r):
    return 0.5*k*r**2

# Force
def F(r):
    return -1*k*r

# Particle  class
class Particle:
    def __init__(self,x,v,m,a):
        self.x = x
        self.v = v
        self.m = m
        self.a = a
        self.x_log = []

    def log_position(self):
        self.x_log.append(self.x)

# Create particles
p_euler = Particle(x,v,m,F(x)/m)
p_symplectic_euler = Particle(x,v,m,F(x)/m)

p_verlet = Particle(x,v,m,F(x)/m)
x_prev = x

p_velocity_verlet = Particle(x,v,m,F(x)/m)

# Solve for t seconds
tstop = 100
n = int(tstop/dt)
for i in range(n):
    # Euler solver
    _x,_v = solver.solve_euler(p_euler.x,p_euler.v,p_euler.a,dt)
    p_euler.x = _x
    p_euler.v = _v
    p_euler.a = F(_x)/p_euler.m
    p_euler.log_position()

    # Symplectic Euler solver
    _x, _v = solver.solve_symplectic_euler(p_symplectic_euler.x,p_symplectic_euler.v,p_symplectic_euler.a,dt)
    p_symplectic_euler.x = _x
    p_symplectic_euler.v = _v
    p_symplectic_euler.a = F(_x)/p_symplectic_euler.m
    p_symplectic_euler.log_position()

    # Verlet solver
    _x = solver.solve_verlet(p_verlet.x, x_prev, p_verlet.a, dt)
    x_prev = p_verlet.x
    p_verlet.x = _x
    p_verlet.a = F(_x)/p_verlet.m
    p_verlet.log_position()

    # Velocity Verlet solver
    _x, _v, _a = solver.solve_velocity_verlet(p_velocity_verlet.x, p_velocity_verlet.v, F, m,dt)
    p_velocity_verlet.x = _x
    p_velocity_verlet.v = _v
    p_velocity_verlet.a = _a
    p_velocity_verlet.log_position()

# Energy Drift Quantification
    

#print("Ground Truth: ", V(x) + 0.5*m*v**2)
print("Percent Error of Energy Drift")
print("Naive Euler ", ((V(p_euler.x) + 0.5*p_euler.m*p_euler.v**2)-(V(x) + 0.5*m*v**2))/(V(x) + 0.5*m*v**2)*100)
print("Symplectic Euler ", ((V(p_symplectic_euler.x) + 0.5*p_symplectic_euler.m*p_symplectic_euler.v**2)-(V(x) + 0.5*m*v**2))/(V(x) + 0.5*m*v**2)*100)
print("Verlet: ", ((V(p_verlet.x) + 0.5*p_verlet.m*p_verlet.v**2)-(V(x) + 0.5*m*v**2))/(V(x) + 0.5*m*v**2)*100)
print("Velocity Verlet: ", ((V(p_velocity_verlet.x) + 0.5*p_velocity_verlet.m*p_velocity_verlet.v**2)-(V(x) + 0.5*m*v**2))/(V(x) + 0.5*m*v**2)*100)

t = np.linspace(0,tstop,n)

fig = plt.figure()
ax = fig.subplots()

plt.grid()
plt.title(f"Solver Demonstration with time step {dt} seconds")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (m)")

plt.plot(t,p_euler.x_log, label="Naive Euler",linestyle="dashed",alpha=0.7)
plt.plot(t,p_symplectic_euler.x_log, label="Symplectic Euler",linestyle="dashed",alpha=0.7)
plt.plot(t,p_verlet.x_log, label="Verlet",linestyle="dashed",alpha=0.7)
plt.plot(t,p_velocity_verlet.x_log, label="Velocity Verlet",linestyle="dashed",alpha=0.7)
plt.plot(t,x*np.cos(np.sqrt(k/m)*t), label="Ground Truth",c='black')

ax.legend()
plt.show()