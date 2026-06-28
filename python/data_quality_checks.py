import pandas as pd

borrowers = pd.read_csv("../data/Borrower.csv")
loans = pd.read_csv("../data/Loan.csv")

merged_df = pd.merge(
    loans,
    borrowers,
    on="memberId"
)
print(merged_df.shape)

print(merged_df.head())

# purpose: loan purpose analysis:
print(merged_df["purpose"].value_counts())

# which loan purpose has highest average:
print(
    merged_df.groupby("purpose")["loanAmount"]
    .mean()
    .sort_values(ascending=False)
)

# Check loan purpose
print(
    merged_df[merged_df["loanAmount"].isnull()]
    ["purpose"]
    .value_counts()
)


# Check percentage:
missing_pct = (
    merged_df["loanAmount"].isnull().sum()
    / len(merged_df)
) * 100

print(missing_pct)


# Check missing loanAmount rows:
print(merged_df[merged_df["loanAmount"].isnull()].head())

# Check loan status of missing rows:
print(
    merged_df[merged_df["loanAmount"].isnull()]
    ["loanStatus"]
    .value_counts()
)






