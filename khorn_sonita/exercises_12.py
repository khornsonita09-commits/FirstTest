# ============================================================
# Exercises 12: Sandwiches (make_sandwich with *items)
# *items collects ANY number of positional arguments into a
# TUPLE named 'items'. Call with 1, 3, or 7+ items!
# ============================================================


def make_sandwich(*items):
    """Print a summary of the sandwich being ordered."""
    print("\nMaking a sandwich with:")
    for item in items:
        print(f"  - {item}")


make_sandwich("roast beef", "cheddar", "lettuce")
make_sandwich("turkey", "avocado")
make_sandwich("peanut butter", "jelly")