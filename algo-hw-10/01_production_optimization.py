import pulp

def main() -> None:
    # Initialize the maximization problem
    model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

    # Define decision variables
    lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
    fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

    # Add the objective function to the model
    # Goal: Maximize total number of products produced
    model += lemonade + fruit_juice, "Total_Products"

    # Add constraints based on available resources
    model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"

    # Sugar constraint: 50 units available
    model += 1 * lemonade <= 50, "Sugar_Constraint"

    # Lemon Juice constraint: 30 units available
    model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"

    # Fruit Puree constraint: 40 units available
    # Fruit Juice takes 2 units
    model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

    # Solve the optimization problem
    model.solve()

    # Output the results
    print(f"Status: {pulp.LpStatus[model.status]}")
    print(f"Lemonade produced: {lemonade.varValue}")
    print(f"Fruit Juice produced: {fruit_juice.varValue}")
    print(f"Total products: {pulp.value(model.objective)}")


if __name__ == "__main__":
    main()