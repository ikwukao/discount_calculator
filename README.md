# Discount Calculator

A simple Python project that demonstrates the Strategy Design Pattern by applying different discount strategies to products and calculating the best available price for a customer.

## Features

- Create products with names and prices.
- Apply percentage-based discounts.
- Apply fixed-amount discounts.
- Apply premium user discounts.
- Automatically determine the lowest available price.
- Uses abstract base classes and object-oriented programming principles.

## Technologies Used

- Python 3
- Abstract Base Classes (ABC)
- Object-Oriented Programming (OOP)

## Project Structure

```text
Product
├── DiscountStrategy (Abstract Base Class)
│   ├── PercentageDiscount
│   ├── FixedAmountDiscount
│   └── PremiumUserDiscount
└── DiscountEngine
```

## Example

### Input

```python
product = Product("Wireless Mouse", 50.0)
user_tier = "Premium"
```

### Output

```text
Best price for Wireless Mouse for Premium user: $40.00
```

## How It Works

1. Create a product.
2. Define available discount strategies.
3. Initialize the discount engine with the strategies.
4. Calculate the best available price.
5. Display the result.

### Running the Project

Clone the repository and run:

```bash
python3 main.py
```

### Learning Objectives

This project demonstrates:

- Classes and objects
- Inheritance
- Abstract classes
- Polymorphism
- Type hints
- Strategy Design Pattern

### Author

Created as part of the freeCodeCamp Python learning path.

### Program Output

![Discount Calculator](./img/discount_calculator_output.png)

---
