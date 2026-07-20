"""
Expense Tracker
----------------
Reads a CSV of expenses and prints the total amount spent per category.

CSV must have at least these columns: Category, Amount

Run:
    pip install pandas
    python main.py
"""

import pandas as pd


def main():
    df = pd.read_csv("expenses.csv")

    # Sum the Amount column, grouped by Category, sorted highest first
    totals_by_category = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)

    print("Expenses by Category:\n")
    for category, total in totals_by_category.items():
        print(f"  {category:<15} €{total:.2f}")

    print(f"\nTotal: €{df['Amount'].sum():.2f}")


if __name__ == "__main__":
    main()
