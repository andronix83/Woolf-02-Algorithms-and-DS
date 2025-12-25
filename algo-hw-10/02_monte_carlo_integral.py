import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Define the function and integration bounds
def f(x):
    return np.sin(x) + 1.5


def draw_function(a, b) -> None:
    # Create range of values for x
    x = np.linspace(-1, 5, 400)
    y = f(x)

    # Create the plot
    fig, ax = plt.subplots()

    # Plot the function
    ax.plot(x, y, 'r', linewidth=2)

    # Fill the area under the curve
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Configure the plot
    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(0, max(y) + 0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Add integration bounds and title
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Integration Plot of f(x) = sin(x) + 1.5 from {a} to {b}')

    plt.grid()
    plt.show()


def monte_carlo_integration(f, a, b, N):
    # Generate N random samples uniformly on the interval [a, b]
    x_rand = np.random.uniform(a, b, N)

    # Evaluate the function at all random points
    f_values = f(x_rand)

    # Calculate the average of function values
    f_mean = np.mean(f_values)

    # Apply the Monte Carlo integration formula
    integral_estimate = (b - a) * f_mean

    return integral_estimate

def main():
    a = 0  # Lower bound
    b = 4  # Upper bound

    draw_function(a, b)

    result_mc = monte_carlo_integration(f, a, b, 100000)
    result_spi, error_spi = spi.quad(f, a, b)

    print(f"Monte-Carlo Integration Result: {result_mc:.6f}")
    print(f"SciPy Integration Result: {result_spi:.6f} (error: {error_spi})")


if __name__ == '__main__':
    main()