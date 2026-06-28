# ==========================================
# Bank Loan Portfolio & Risk Analysis
# Data Visualization
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------
# Load Data
# ----------------------------------

borrowers = pd.read_csv("../data/Borrower.csv")
loans = pd.read_csv("../data/Loan.csv")

merged_df = pd.merge(
    loans,
    borrowers,
    on="memberId"
)

# ==========================================
# Visualization 1
# Default Rate by Loan Purpose
# ==========================================

purpose_default = (
    merged_df.groupby("purpose")["loanStatus"]
    .apply(lambda x: (x == "Default").mean() * 100)
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,5))
purpose_default.plot(kind="bar")
plt.title("Default Rate by Loan Purpose")
plt.ylabel("Default Rate (%)")
plt.xlabel("Loan Purpose")
plt.xticks(rotation=45)
plt.tight_layout()
plt.tight_layout()

plt.savefig(
    "../images/default_rate_by_purpose.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.show()

# ==========================================
# Visualization 2
# Loan Count by Purpose
# ==========================================

loan_count = (
    merged_df["purpose"]
    .value_counts()
)

plt.figure(figsize=(10,5))
loan_count.plot(kind="bar")
plt.title("Loan Count by Purpose")
plt.ylabel("Number of Loans")
plt.xlabel("Loan Purpose")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    "../images/loan_count_by_purpose.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# ==========================================
# Visualization 3
# Default Rate by Employment Length
# ==========================================

employment_default = (
    merged_df.groupby("yearsEmployment")["loanStatus"]
    .apply(lambda x: (x == "Default").mean() * 100)
    .sort_values()
)

plt.figure(figsize=(10,5))
employment_default.plot(kind="bar")
plt.title("Default Rate by Employment Length")
plt.ylabel("Default Rate (%)")
plt.xlabel("Employment Length")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    "../images/default_rate_by_employment.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# ==========================================
# Visualization 4
# Credit Utilization vs Default Risk
# ==========================================

merged_df["utilizationGroup"] = pd.cut(
    merged_df["revolvingUtilizationRate"],
    bins=[0,20,40,60,80,100],
    labels=[
        "0-20%",
        "20-40%",
        "40-60%",
        "60-80%",
        "80-100%"
    ]
)

utilization_default = (
    merged_df.groupby("utilizationGroup")["loanStatus"]
    .apply(lambda x: (x == "Default").mean() * 100)
)

plt.figure(figsize=(8,5))
utilization_default.plot(kind="bar")
plt.title("Default Rate by Credit Utilization Group")
plt.ylabel("Default Rate (%)")
plt.xlabel("Credit Utilization")
plt.tight_layout()
plt.savefig(
    "../images/default_rate_by_utilization.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# ==========================================
# Visualization 5
# Default Rate by Grade
# ==========================================

grade_default = (
    merged_df.groupby("grade")["loanStatus"]
    .apply(lambda x: (x == "Default").mean() * 100)
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
grade_default.plot(kind="bar")
plt.title("Default Rate by Grade")
plt.ylabel("Default Rate (%)")
plt.xlabel("Grade")
plt.tight_layout()
plt.savefig(
    "../images/default_rate_by_grade.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()