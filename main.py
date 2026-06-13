"""
Discount Calculator

A Python project that demonstrates the Strategy Design Pattern using
Object-Oriented Programming (OOP). The application calculates the
best available price for a product by evaluating multiple discount
strategies and selecting the lowest valid price.

Features:
- Percentage-based discounts
- Fixed-amount discounts
- Premium user discounts
- Strategy-based discount evaluation
- Type hints and abstract base classes

Created as part of the freeCodeCamp Python learning path.
"""

from abc import ABC, abstractmethod


class Product:
    """
    Represents a product with a name and price.
    """

    def __init__(self, name: str, price: float) -> None:
        """
        Initialize a product.

        Args:
            name (str): Product name.
            price (float): Product price.
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """
        Return a human-readable representation of the product.
        """
        return f"{self.name} - ${self.price}"


class DiscountStrategy(ABC):
    """
    Abstract base class for all discount strategies.

    Every discount strategy must define:
    - is_applicable()
    - apply_discount()
    """

    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        """
        Determine whether the discount can be applied.

        Args:
            product (Product): Product being evaluated.
            user_tier (str): Customer membership level.

        Returns:
            bool: True if the discount is applicable.
        """
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        """
        Apply the discount and return the discounted price.

        Args:
            product (Product): Product being discounted.

        Returns:
            float: Discounted product price.
        """
        pass


class PercentageDiscount(DiscountStrategy):
    """
    Applies a percentage-based discount to a product.
    """

    def __init__(self, percent: int) -> None:
        """
        Initialize the discount percentage.

        Args:
            percent (int): Percentage discount value.
        """
        self.percent = percent

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        """
        Validate that the discount percentage is reasonable.

        Returns:
            bool: True if the discount is 70% or less.
        """
        return self.percent <= 70

    def apply_discount(self, product: Product) -> float:
        """
        Calculate and return the discounted price.
        """
        return product.price * (1 - self.percent / 100)


class FixedAmountDiscount(DiscountStrategy):
    """
    Applies a fixed monetary discount to a product.
    """

    def __init__(self, amount: int) -> None:
        """
        Initialize the fixed discount amount.

        Args:
            amount (int): Amount to subtract from the price.
        """
        self.amount = amount

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        """
        Ensure the discount does not reduce the price excessively.

        Returns:
            bool: True if the discount is valid.
        """
        return product.price * 0.9 > self.amount

    def apply_discount(self, product: Product) -> float:
        """
        Calculate and return the discounted price.
        """
        return product.price - self.amount


class PremiumUserDiscount(DiscountStrategy):
    """
    Special discount available only to premium users.
    """

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        """
        Check whether the customer is a premium user.

        Returns:
            bool: True if the user has premium status.
        """
        return user_tier.lower() == "premium"

    def apply_discount(self, product: Product) -> float:
        """
        Apply a 20% discount for premium users.

        Returns:
            float: Discounted price.
        """
        return product.price * 0.8


class DiscountEngine:
    """
    Evaluates multiple discount strategies and determines
    the best available price for a product.
    """

    def __init__(self, strategies: list[DiscountStrategy]) -> None:
        """
        Initialize the discount engine.

        Args:
            strategies (list[DiscountStrategy]):
                Collection of available discount strategies.
        """
        self.strategies = strategies

    def calculate_best_price(self, product: Product, user_tier: str) -> float:
        """
        Calculate the lowest available price by evaluating
        all applicable discount strategies.

        Args:
            product (Product): Product being purchased.
            user_tier (str): Customer membership level.

        Returns:
            float: Best available price.
        """
        # Include the original price as a fallback option.
        prices = [product.price]

        # Evaluate all available discount strategies.
        for strategy in self.strategies:
            if strategy.is_applicable(product, user_tier):
                discounted = strategy.apply_discount(product)
                prices.append(discounted)

        # Return the lowest available price.
        return min(prices)


if __name__ == "__main__":
    # Create a sample product.
    product = Product("Wireless Mouse", 50.0)

    # Define the customer's membership tier.
    user_tier = "Premium"

    # Configure available discount strategies.
    strategies = [
        PercentageDiscount(10),
        FixedAmountDiscount(5),
        PremiumUserDiscount(),
    ]

    # Initialize the discount engine.
    engine = DiscountEngine(strategies)

    # Calculate the best possible price.
    best_price = engine.calculate_best_price(product, user_tier)

    # Display the final result.
    print(f"Best price for {product.name} for {user_tier} user: ${best_price:.2f}")
