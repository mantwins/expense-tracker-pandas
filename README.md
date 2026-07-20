expense-tracker-pandas

Reads a CSV of personal expenses and tells you how much you spent per category. That's it - no dashboard, no database, just a quick way to see where the money went.

Setup
bash
pip install -r requirements.txt
python main.py
CSV format

Needs at least Category and Amount columns. Date and Description are there in the sample file but not required for the script to work:

Date,Category,Amount,Description
2026-01-05,Food,25.50,Supermarket
2026-01-06,Transport,10.00,Bus ticket

Swap in your own expenses.csv with the same columns and it'll work the same way.

Output
Έξοδα ανά κατηγορία:

  Utilities       €95.00
  Food            €93.45
  Entertainment   €50.00
  Transport       €15.00

Σύνολο: €253.45
Stack

Python + Pandas. One groupby().sum() call is doing basically all the work here.
