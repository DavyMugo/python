def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Calculate the discounted price
        discount_amount = (price * discount_percent) / 100
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied
        return price

def main():
    try:
        # Prompt user for input
        original_price = float(input("Enter the original price: $"))
        discount_percent = float(input("Enter the discount percentage: "))

        # Calculate and display the result
        final_price = calculate_discount(original_price, discount_percent)
        print(f"The final price after applying the discount is: ${final_price:.2f}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()

   
