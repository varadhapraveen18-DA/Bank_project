import pandas as pd

borrower = pd.read_csv("Borrower.txt", sep="\t")
borrower.to_csv("Borrower.csv", index=False)

loan = pd.read_csv("Loan.txt", sep="\t")
loan.to_csv("Loan.csv", index=False)

print("Files converted successfully!")


import pandas as pd

borrowers = pd.read_csv("Borrower.csv")
loans = pd.read_csv("Loan.csv")

print("Borrowers Shape:", borrowers.shape)
print("Loans Shape:", loans.shape)

print("\nBorrower Columns:")
print(borrowers.columns.tolist())

print("\nLoan Columns:")
print(loans.columns.tolist())


print(borrowers.head())
print(loans.head())

print(loans["loanStatus"].value_counts())

print()

print(loans["loanStatus"].value_counts(normalize=True) * 100)


print(borrowers.isnull().sum())

print(loans.isnull().sum())


print(borrowers["memberId"].nunique())
print(loans["memberId"].nunique())
print(loans["memberId"].duplicated().sum())