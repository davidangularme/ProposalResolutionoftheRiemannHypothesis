# see Readme to understand my Proposal under work !!!
# mpmath.zetazero(k): Provides high-precision calculations of the k
# k-th non-trivial zero.
# quantum_operator Function: Calculates a sum over exponentials involving the zeros, simulating the quantum operator.
# Visualization: The plots generated help in visualizing the distribution of zeros and the behavior of the quantum operator.

import mpmath
import numpy as np
import matplotlib.pyplot as plt

def zeta_zeros(n):
    """
    Compute the imaginary parts of the first n non-trivial zeros of the Riemann zeta function using mpmath.
    """
    zeros = [mpmath.zetazero(k).imag for k in range(1, n+1)]
    return zeros

def plot_zeros(zeros):
    """
    Plot the non-trivial zeros of the Riemann zeta function on the critical line.
    """
    plt.figure(figsize=(10, 6))
    plt.plot([0.5]*len(zeros), zeros, 'bo', markersize=4)
    plt.xlabel('Real Part (σ)')
    plt.ylabel('Imaginary Part (t)')
    plt.title('Non-trivial Zeros of the Riemann Zeta Function')
    plt.grid(True)
    plt.show()

def quantum_operator(x, zeros):
    """
    Compute the quantum operator associated with the zeta zeros.
    """
    op = np.zeros_like(x, dtype=complex)
    for gamma in zeros:
        op += np.exp(1j * gamma * np.log(x))
    return op

def plot_quantum_operator(x, op):
    """
    Plot the real and imaginary parts of the quantum operator.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x, op.real, label='Real Part')
    plt.plot(x, op.imag, label='Imaginary Part')
    plt.xlabel('x')
    plt.ylabel('Operator Value')
    plt.title('Quantum Operator Associated with Zeta Zeros')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Number of zeros to compute
    num_zeros = 100

    # Compute the zeros
    zeros = zeta_zeros(num_zeros)

    # Plot the zeros
    plot_zeros(zeros)

    # Define x values for the operator
    x = np.linspace(0.1, 10, 1000)

    # Compute the operator
    op = quantum_operator(x, zeros)

    # Plot the operator
    plot_quantum_operator(x, op)

if __name__ == "__main__":
    main()
