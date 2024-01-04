# solver-demo
 
## Demonstration of various differential-equation solving algorithms.
The model being studied is the undamped spring-mass oscillator.

### Algorithms
Currently, four algorithms are implemented.
1. Naive Euler, also known as Euler's method
2. Symplectic Euler
3. Verlet Integration
4. Velocity Verlet Integration

### Energy Drift Analysis
Energy drift of the system after 100 seconds with a step size of 0.01
- Naive Euler: 172% error
- Symplectic Euler: 0.44% error
- Verlet Integration: -25% error
- Velocity Verlet Integration: -0.00064% error

Velocity Verlet integration is the best algorithm in this case, with minimal error several orders of magnitude better than others. 

Verlet algorithms also prevent energy growth over time, as they always have a negative error.

However, this means that systems using Verlet integration algorithms will suffer from energy damping over time.

### Time evolution of the system when solved with each algorithm
Runtime of 100 seconds and step size of 0.01 seconds
<img width="1208" alt="image" src="https://github.com/Turtlely/solver-demo/assets/55010651/74c39e60-1ec2-4a33-827c-1fcbda1e41e6">

Runtime of 7 seconds and step size of 0.1 seconds (to emphasize differences in algorithm performance)
<img width="1208" alt="image" src="https://github.com/Turtlely/solver-demo/assets/55010651/e1ba637a-9396-4974-8860-a162d36b30ad">


