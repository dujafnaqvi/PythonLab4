def main():
    starting_balance = 0.0
    annual_interest_rate = 0.0
    deposit_per_month = 0.0
    withdrawal_per_month = 0.0
    monthly_interest = 0.0

    updated_balance = 0.0
    total_deposits = 0.0
    total_withdrawals = 0.0
    total_interest_earned = 0.0
    number_of_months = 0

    annual_interest_rate = float(input("Enter the annual interest rate as a decimal (e.g., 0.05 for 5%): "))
    starting_balance = float(input("Enter the starting balance of your account: $"))
    number_of_months = int(input("Enter the number of months that your bank account has been open: "))

    if starting_balance < 0:
        print("Error: Starting balance cannot be negative.")
        return -1

    updated_balance = starting_balance

    for month in range(1, number_of_months + 1):
        deposit_per_month = float(input(f"Enter the amount deposited during month {month}: $"))
        withdrawal_per_month = float(input(f"Enter the amount withdrawn during month {month}: $"))

        updated_balance = updated_balance + deposit_per_month
        updated_balance = updated_balance - withdrawal_per_month

        total_deposits = total_deposits + deposit_per_month
        total_withdrawals = total_withdrawals + withdrawal_per_month

        if updated_balance < 0:
            print("Account closed due to negative balance.")
            return -1

        monthly_interest = (annual_interest_rate / 12) * updated_balance
        total_interest_earned = total_interest_earned + monthly_interest
        updated_balance = updated_balance + monthly_interest

    print("-" * 64)
    print(f"{'The ending balance of your account is:':<46}$ {updated_balance:.2f}")
    print(f"{'The total amount you have deposited is:':<46}$ {total_deposits:.2f}")
    print(f"{'The total amount you have withdrawn is:':<46}$ {total_withdrawals:.2f}")
    print(f"{'The total amount of interest earned is:':<46}$ {total_interest_earned:.2f}")


if __name__ == "__main__":
    main()
