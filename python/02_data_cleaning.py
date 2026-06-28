import pandas as pd

borrowers = pd.read_csv("../data/Borrower.csv")
loans = pd.read_csv("../data/Loan.csv")

# Merge datasets
merged_df = pd.merge(
    loans,
    borrowers,
    on="memberId"
)

print("Dataset Shape:")
print(merged_df.shape)

# -------------------------
# Missing Values Check
# -------------------------

print("\nMissing Values")
print(merged_df.isnull().sum())

# -------------------------
# Duplicate Check
# -------------------------

print("\nDuplicate Rows")
print(merged_df.duplicated().sum())

# -------------------------
# Data Types Check
# -------------------------

print("\nData Types")
print(merged_df.dtypes)

# -------------------------
# Unique Values Check
# -------------------------

print("\nLoan Status Values")
print(merged_df["loanStatus"].value_counts())

print("\nGrade Values")
print(sorted(merged_df["grade"].unique()))

print("\nPurpose Values")
print(merged_df["purpose"].value_counts())

print("\nHome Ownership Values")
print(merged_df["homeOwnership"].value_counts())

# Save cleaned dataset if needed

merged_df.to_csv(
    "../data/merged_loan_data.csv",
    index=False
)

print("\nCleaned dataset saved successfully.")


# Data Cleaning Summary
#
# 1. Borrower and Loan datasets were merged using memberId.
#
# 2. Missing values were checked across all columns.
#
# 3. Duplicate records were verified.
#
# 4. Data types were reviewed to ensure variables
#    were suitable for analysis.
#
# 5. Key categorical variables such as loanStatus,
#    grade, purpose, and homeOwnership were inspected
#    for consistency.
#
# 6. The merged dataset was saved for use in
#    exploratory analysis and visualization.