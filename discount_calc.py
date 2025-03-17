def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

if __name__ == "__main__":
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        final_price = calculate_discount(price, discount_percent)
        print(f"The final price after applying the discount is: {final_price:.2f}")
    except ValueError:
        print("Please enter valid numerical values for price and discount percentage.")