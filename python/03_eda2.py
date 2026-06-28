import pandas as pd
borrowers = pd.read_csv("../data/Borrower.csv")
loans = pd.read_csv("../data/Loan.csv")

merged_df=pd.merge(loans,borrowers,on="memberId")
# merged_df.to_csv(
#     "data/merged_loan_data.csv",
#     index=False
# )

# Which grade generates
# the most lending business?

print("\nTotal Loan Volume by Grade")

grade_volume = (
    merged_df.groupby("grade")["loanAmount"]
    .sum()
    .sort_values(ascending=False)
)

print(grade_volume)


# average interest rate by grade:
print("\nAverage Interest Rate by Grade")

interest_by_grade = (
    merged_df.groupby("grade")["interestRate"]
    .mean()
    .sort_values()
)

print(interest_by_grade)

# not enough to show case in our potfilo:
# next one:
# Which customer groups
# use the most credit lines?
print("\nAverage Open Credit Lines by Income Group")

merged_df["incomeGroup"] = pd.qcut(
    merged_df["annualIncome"],
    q=4,
    labels=["Low Income","Lower Middle","Upper Middle","High Income"]
)

credit_lines = (
    merged_df.groupby("incomeGroup")["numOpenCreditLines"]
    .mean()
    .sort_values(ascending=False)
)

print(credit_lines)

# above one is not enough to strong inputs

# next one:

print(merged_df["homeOwnership"].value_counts())

# Are homeowners safer borrowers
# than renters?

print("\nDefault Rate by Home Ownership")

home_default = (
    merged_df.groupby("homeOwnership")["loanStatus"]
    .apply(lambda x: (x == "Default").mean() * 100)
    .sort_values(ascending=False)
)

print(home_default)
# not strong enough results:
# Default Rate by Home Ownership
# homeOwnership
# mortgage    10.528643
# own          9.707893
# rent         9.705156
# Name: loanStatus, dtype: float64 
# next one:



# Does income verification improve portfolio quality?
print("\nDefault Rate by Income Verification")

verification_default = (
    merged_df.groupby("incomeVerified")["loanStatus"]
    .apply(lambda x: (x == "Default").mean() * 100)
)

print(verification_default)

print("\nAverage Loan Amount by Income Verification")

verification_loan = (
    merged_df.groupby("incomeVerified")["loanAmount"]
    .mean()
)

print(verification_loan)

print("\nLoan Count by Income Verification")

verification_count = (
    merged_df.groupby("incomeVerified")
    .size()
)

print(verification_count)



# ---------------------------
# Business insights 3:
# Which loan grades are actually causing most defaults?
# ----------------------------
print("\nLoan Count by Grade")

print(
    merged_df["grade"]
    .value_counts()
    .sort_index()
)


# Which grade is creating the largest number of defaults?
print("\nDefault Count by Grade")

default_count = (
    merged_df[merged_df["loanStatus"] == "Default"]
    ["grade"]
    .value_counts()
    .sort_index()
)

print(default_count)


# Do customers with previous credit problems 
# default more often?
print("\nAverage Delinquencies by Loan Status")

print(
    merged_df.groupby("loanStatus")
    ["numDelinquency2Years"]
    .mean()
)


# Do high-income customers actually
# borrow significantly larger loans?

print("\nAverage Loan Amount by Income Group")

merged_df["incomeGroup"] = pd.qcut(
    merged_df["annualIncome"],
    q=4,
    labels=["Low Income", "Lower Middle", "Upper Middle", "High Income"]
)

avg_loan_income = (
    merged_df.groupby("incomeGroup")["loanAmount"]
    .mean()
    .sort_values()
)

print(avg_loan_income)


# Does longer employment
# lead to lower default rates?
print("\nDefault Rate by Employment Length")

employment_default = (
    merged_df.groupby("yearsEmployment")["loanStatus"]
    .apply(lambda x: (x == "Default").mean() * 100)
    .sort_values()
)

print(employment_default)


# Do borrowers who already use most of their available credit
# default more often?
print("\nAverage Credit Utilization by Loan Status")

print(
    merged_df.groupby("loanStatus")
    ["revolvingUtilizationRate"]
    .mean()
)


# As utilization increases,
# does default risk consistently increase?

print("\nDefault Rate by Credit Utilization Group")

merged_df["utilizationGroup"] = pd.cut(
    merged_df["revolvingUtilizationRate"],
    bins=[0,20,40,60,80,100],
    labels=["0-20%","20-40%","40-60%","60-80%","80-100%"]
)

utilization_default = (
    merged_df.groupby("utilizationGroup")["loanStatus"]
    .apply(lambda x: (x == "Default").mean() * 100)
)

print(utilization_default)

import pandas as pd

borrowers = pd.read_csv("../data/Borrower.csv")
loans = pd.read_csv("../data/Loan.csv")

merged_df = pd.merge(
    loans,
    borrowers,
    on="memberId"
)

merged_df.to_csv(
    "../data/merged_loan_data.csv",
    index=False
)

print("Merged CSV saved successfully")


import pandas as pd

df = pd.read_csv("../data/merged_loan_data.csv")

print(df.shape)