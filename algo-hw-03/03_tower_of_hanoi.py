def hanoi_solver(n, source, target, auxiliary, state, step_counter):
    """
    Recursive function to solve the Tower of Hanoi puzzle with step numbering.

    Args:
        n (int): Number of disks to move.
        source (str): Key for the source rod.
        target (str): Key for the target rod.
        auxiliary (str): Key for the auxiliary rod.
        state (dict): Current state of all rods.
        step_counter (list): A mutable list containing the current step number.
    """
    if n > 0:
        # Step 1: Move n-1 disks from source to auxiliary
        hanoi_solver(n - 1, source, auxiliary, target, state, step_counter)

        # Step 2: Move the n-th disk from source to target
        # Pop the top disk from the source rod
        disk = state[source].pop()
        # Push the disk onto the target rod
        state[target].append(disk)

        # Increment the global step counter
        step_counter[0] += 1

        # Print the move action with the step number and the current state
        print(f"{step_counter[0]}. Move the disk {disk} from {source} to {target}")
        print(" " * len(str(step_counter[0])) + f"  State after moving: {state}")

        # Step 3: Move the n-1 disks from auxiliary to target
        hanoi_solver(n - 1, auxiliary, target, source, state, step_counter)

def main() -> None:
    # Configuration: number of disks
    number_of_disks = 5

    # Initialize the state of the towers
    towers_state = {
        'A': list(range(number_of_disks, 0, -1)),  # Creates [3, 2, 1]
        'B': [],
        'C': []
    }

    # Counter initialization (using a list to make it mutable in recursion)
    counter = [0]

    print(f"\nInitial state: {towers_state}\n")

    # Start the recursive process
    hanoi_solver(number_of_disks, 'A', 'C', 'B', towers_state, counter)

    print(f"\nFinal state: {towers_state}")


if __name__ =="__main__":
    main()