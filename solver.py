# Euler solver scheme

# Take position, velocity, acceleration at time t, find position, velocity, acceleration at time t + dt

def solve_symplectic_euler(x,v,a,dt):
    dv = a*dt
    v+=dv

    # Advance position with new velocity
    x += v*dt
    return x,v

def solve_euler(x,v,a,dt):
    dv = a*dt
    
    # Advance position with old velocity
    x += v*dt
    v+=dv
    return x,v

def solve_verlet(x_now,x_prev,a,dt):
    x_future = 2*x_now - x_prev + a * dt**2
    return x_future

def solve_velocity_verlet(x,v,F,m,dt):
    x_new = x + v*dt + 0.5*F(x)/m*dt**2
    a_new = F(x_new)/m
    v_new = v + 0.5*(F(x)+F(x_new))/m * dt
    return x_new, v_new,a_new