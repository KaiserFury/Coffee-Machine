```markdown
# Coffee Machine

This is a Python-based coffee machine simulation. The program allows users to select from a menu of coffee options (espresso, latte, cappuccino), processes their order, checks if there are enough ingredients, accepts coin payments, and provides change.

## Features
- Displays a menu of available coffee options: espresso, latte, and cappuccino.
- Allows users to insert coins to purchase their desired coffee.
- Checks if there are enough ingredients in the machine to make the selected coffee.
- Updates the machine's ingredient resources after each order.
- Provides a report on the remaining resources and money in the machine.
- Option to turn off the machine when desired.

## How to Play
1. Run the program.
2. Choose a coffee from the available options by typing `espresso`, `latte`, or `cappuccino`.
3. Insert the required amount of coins to complete your purchase.
4. If the machine has sufficient ingredients and you provide enough money, your coffee will be served, and you'll receive change if necessary.
5. You can also type `report` to view the current status of the machine's resources or `off` to turn off the machine.

## How to Run

1. Ensure Python is installed on your system.
2. Download or clone the repository.
3. Run the `coffee_machine.py` script in your terminal:
   ```bash
   python coffee_machine.py
   ```

## Menu and Pricing

| Coffee      | Water (ml) | Milk (ml) | Coffee (g) | Cost ($) |
|-------------|------------|-----------|------------|----------|
| Espresso    | 50         | 0         | 18         | 1.5      |
| Latte       | 200        | 150       | 24         | 2.5      |
| Cappuccino  | 250        | 100       | 24         | 3.0      |

## Functions

### `report()`
Prints a report of the machine's current resources, including water, milk, coffee, and money.

### `ingredients_taker(item_name)`
Subtracts the necessary ingredients for the selected coffee from the machine's resources.

### `money_checker(item_name)`
Prompts the user to insert coins and checks if the user has inserted enough money to cover the cost of the selected coffee. Returns any change or refunds if the payment is insufficient.

### `checker(item_name)`
Checks whether the machine has enough ingredients to prepare the selected coffee. If ingredients are insufficient, it informs the user and stops the order.

## Example Gameplay

```bash
Welcome to the Coffee Machine!
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters: 10
How many dimes: 0
How many nickels: 0
How many pennies: 0
Here is your change $0.0
Enjoy your latte ☕☕
```

## Dependencies

- The game uses an ASCII art file (`Art.py`) to display the coffee machine logo at the start of the program.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Let me know if you'd like to make any changes or additions!
