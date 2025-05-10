"""
Programmer: Christian Nshuti Manzi
Packages Used: numpy, scipy, matplotlib
Approach: Solves a simple ODE using SciPy and visualizes the solution as a plot image.
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def ode_function(t, y):
    # This represents the ODE: dy/dt = -2y + 1
    return -2 * y + 1

def main():
    # Initial condition and time span
    y0 = [0]
    t_span = (0, 10)
    t_eval = np.linspace(t_span[0], t_span[1], 100)

    # Solve the ODE
    solution = solve_ivp(ode_function, t_span, y0, t_eval=t_eval)

    # Save the solution plot
    plt.plot(solution.t, solution.y[0], label='y(t)')
    plt.xlabel('Time (t)')
    plt.ylabel('Solution y')
    plt.title('CPU Heat Dissipation Model')
    plt.grid()
    plt.legend()
    plt.savefig("plot.png")  # Save the plot as an image
    print("Plot saved as plot.png")

if __name__ == "__main__":
    main()
