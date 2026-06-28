# data_loading and data_exploration:

# Import Libraries
import pandas as pd
# Load Datasets
borrowers = pd.read_csv("Borrower.csv")
loans = pd.read_csv("Loan.csv")

# Check Dataset Shape:
# Purpose: Check number of rows and columns
print("Borrowers Shape:", borrowers.shape)
print("Loans Shape:", loans.shape)

# Check Column Names:
# Purpose: See available columns
print("\nBorrower Columns:")
print(borrowers.columns.tolist())
print("\nLoan Columns:")
print(loans.columns.tolist())


# Preview Data:
# Purpose: Check whether data loaded correctly
print(borrowers.head())
print(loans.head())

# Check Loan Status Distribution:
# Purpose: Understand Current vs Default loans
print(loans["loanStatus"].value_counts())

print()

print(loans["loanStatus"].value_counts(normalize=True) * 100)


# Check Missing Values:
# Purpose: Identify missing values
print(borrowers.isnull().sum())

print(loans.isnull().sum())

# Check Member ID Uniqueness:
# Purpose: Verify customer-loan relationship
print(borrowers["memberId"].nunique())
print(loans["memberId"].nunique())
print(loans["memberId"].duplicated().sum())