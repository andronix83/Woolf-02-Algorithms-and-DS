import random
import matplotlib.pyplot as plt


def get_theoretical_probabilities():
    # Calculate theoretical probabilities based on 36 possible outcomes (6x6)
    counts = {i: 0 for i in range(2, 13)}

    # Iterate through all outcomes of two dice
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            total = d1 + d2
            counts[total] += 1

    # Convert counts to percentages (count / 36 * 100)
    probabilities = {k: (v / 36) * 100 for k, v in counts.items()}
    return probabilities


def monte_carlo_dice_simulation(num_simulations=100000):
    # Initialize a dictionary to store the count of each sum (2 to 12)
    sums_count = {i: 0 for i in range(2, 13)}

    # Run the simulation
    for _ in range(num_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sums_count[die1 + die2] += 1

    return sums_count


def print_comparison_table(mc_counts, num_simulations, theory_probs):
    # Print header with comparison columns
    print(f"{'Sum':<5} | {'Count':<8} | {'MC Prob (%)':<12} | {'Theory (%)':<12} | {'Diff (%)':<10}")
    print("-" * 60)

    mc_probs_list = []
    theory_probs_list = []
    sums = []

    for total_sum in range(2, 13):
        count = mc_counts[total_sum]

        # Monte Carlo Probability
        mc_prob = (count / num_simulations) * 100

        # Theoretical Probability
        th_prob = theory_probs[total_sum]

        # Difference (Error)
        diff = mc_prob - th_prob

        # Store for plotting
        sums.append(total_sum)
        mc_probs_list.append(mc_prob)
        theory_probs_list.append(th_prob)

        # Print row
        print(f"{total_sum:<5} | {count:<8} | {mc_prob:<12.2f} | {th_prob:<12.2f} | {diff:<+10.3f}")

    return sums, mc_probs_list, theory_probs_list


def plot_comparison(sums, mc_probs, theory_probs):
    plt.figure(figsize=(12, 7))

    # Bar chart for Monte Carlo
    bars = plt.bar(sums, mc_probs, color='skyblue', alpha=0.7, label='Monte Carlo Simulation', edgecolor='black')

    # Line chart for Theoretical Probability
    plt.plot(sums, theory_probs, color='red', marker='o', linewidth=2, label='Theoretical Probability')

    # Labels and Title
    plt.xlabel('Sum on Dice', fontsize=12)
    plt.ylabel('Probability (%)', fontsize=12)
    plt.title('Comparison: Monte Carlo vs Theoretical Probability', fontsize=14)
    plt.xticks(range(2, 13))
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    # Add percentage labels on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.2, f'{yval:.2f}%', ha='center', va='bottom')


    # Show plot
    plt.show()


def main() -> None:
    N = 100000
    print(f"Simulation started: {N} rolls...\n")

    # 1. Run Monte Carlo
    mc_counts = monte_carlo_dice_simulation(N)

    # 2. Get Theoretical Values
    theory_probs = get_theoretical_probabilities()

    # 3. Print Comparison Table
    sums_data, mc_data, th_data = print_comparison_table(mc_counts, N, theory_probs)

    # 4. Plot Comparison
    plot_comparison(sums_data, mc_data, th_data)


if __name__ == "__main__":
    main()