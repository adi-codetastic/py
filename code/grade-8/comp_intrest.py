def calculate_compound_interest(principal, annual_rate, years, compounds_per_year):
    """
    Calculates the future value of an investment using the compound interest formula.

    Args:
        principal (float): The initial principal amount (P).
        annual_rate (float): The annual interest rate as a decimal (r).
        years (float): The number of years the money is invested or borrowed (t).
        compounds_per_year (int): The number of times interest is compounded per year (n).

    Returns:
        float: The final amount (A) after compounding.
    """
    # Convert annual rate percentage to a decimal if needed (e.g., 5 for 5% to 0.05)
    # The user should ideally input a decimal for this specific function.
    
    rate_per_period = annual_rate / compounds_per_year
    total_periods = compounds_per_year * years
    
    # Calculate the future value (A) using the formula
    amount = principal * (1 + rate_per_period) ** total_periods
    
    # Return the final amount
    return amount

# --- Example Usage ---

# Define the input parameters:
P = int(input("Enter the amount"))  # Principal amount
R = int(input("Enter the rate"))     # Annual interest rate (5% as a decimal)
T = int(input("Enter the time"))      # Time in years
N = int(input("Enter the times"))        # Compounded quarterly (4 times per year)

# Calculate the final amount
final_amount = calculate_compound_interest(P, R, T, N)
compound_interest_earned = final_amount - P

print(f"Initial Principal (P): ${P:,.2f}")
print(f"Annual Rate (R): {R*100}%")
print(f"Time (T): {T} years")
print(f"Compounding Frequency (N): {N} times per year")
print("-" * 30)
print(f"Total Amount after {T} years: ${final_amount:,.2f}")
print(f"Compound Interest Earned: ${compound_interest_earned:,.2f}")