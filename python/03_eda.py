# ==========================================
# Bank Loan Portfolio & Risk Analysis
# ==========================================
import pandas as pd
borrowers = pd.read_csv("../data/Borrower.csv")
loans = pd.read_csv("../data/Loan.csv")

merged_df=pd.merge(loans,borrowers,on="memberId")
print(merged_df.shape)
print(merged_df.head())

# -----------------------
# data quality checks
#  -----------------------

# ------------------------
# Business Insight #1
# Which loan purposes have the highest default risk?
# ------------------------
print("\nDefault Rate by Loan Purpose")

purpose_default_rate= (
    merged_df.groupby("purpose")["loanStatus"]
    .apply(lambda x: (x == "Default").mean() * 100)
    .sort_values(ascending=False)
)

print(purpose_default_rate)

# investigation : why healthcare has more default ratio is its because of income or interest rate?
# Average Income by Purpose:
print("\nAverage Income by Purpose")

income_by_purpose = (
    merged_df.groupby("purpose")["annualIncome"]
    .mean()
    .sort_values()
)

print(income_by_purpose)


# is it because of debt-to-ratio dit:
print("\nAverage DTI Ratio by Purpose")

dti_by_purpose = (
    merged_df.groupby("purpose")["dtiRatio"]
    .mean()
    .sort_values(ascending=False)
)

print(dti_by_purpose)


# is it because of interest rate:
# print(merged_df["interestRate"].dtype)

print("\nAverage Interest Rate by Purpose")

interest_by_purpose = (
    merged_df.groupby("purpose")["interestRate"]
    .mean()
    .sort_values(ascending=False)
)

print(interest_by_purpose)


# Are healthcare loans bigger?
print("\nAverage Loan Amount by Purpose")

loan_by_purpose = (
    merged_df.groupby("purpose")["loanAmount"]
    .mean()
    .sort_values(ascending=False)
)

print(loan_by_purpose)

# is it beacuse customers grade:
print(pd.crosstab(
    merged_df["purpose"],
    merged_df["grade"]
))

grade_pct = pd.crosstab(
    merged_df["purpose"],
    merged_df["grade"],
    normalize="index"
) * 100

print(grade_pct.round(2))

# -----------------------------------------
# Investigation: Healthcare Loan Defaults

# Healthcare loans showed the highest default rate (25.79%) among all loan purposes.

# Several possible explanations were investigated:

# 1. Annual Income

#    * Healthcare borrowers had income levels similar to other borrowers.
#    * Income was not a significant factor.

# 2. Debt-to-Income Ratio (DTI)

#    * DTI ratios were very similar across loan purposes.
#    * DTI did not explain the higher default rate.

# 3. Interest Rate

#    * Healthcare loans had only slightly higher interest rates.
#    * The difference was too small to explain the large increase in defaults.

# 4. Loan Amount

#    * Average loan amounts were nearly identical across purposes.
#    * Loan size was not a significant factor.

# 5. Grade Distribution

#    * Healthcare loans had a lower proportion of safer grades (A grades) and a higher proportion of riskier grades (E grades).
#    * This suggests healthcare borrowers may represent a riskier customer segment.

# Conclusion:
# Healthcare loans exhibit substantially higher default rates. 
# Income, DTI, interest rate, and loan amount do not appear to be the primary drivers. 
# Loan grade distribution provides the strongest evidence so far and should be investigated further.

# Further analysis revealed that healthcare loans contain a higher proportion of riskier loan grades (especially E grades). 
# Since E-grade loans have default rates above 32%, 
# this suggests that grade distribution is a major contributor to the higher healthcare default rate.
# ---------------------------


# is beacuse of delinquency2years: means custmore didnt pay the emi on proper and 
# that shows how many times they played late on last 2 years:
print(
    merged_df.groupby("purpose")[
        "numDelinquency2Years"
    ].mean().sort_values(ascending=False)
)


# is it because of numchargeoff1 year: means bank though this customer didnt have a chnace to pay
# so how many they put the customer in chargeoff:
print(
    merged_df.groupby("purpose")[
        "numChargeoff1year"
    ].mean().sort_values(ascending=False)
)

# -------------------------
# Business Insight 2
# Which loan purposes drive portfolio growth
# while maintaining manageable risk?
# -------------------------

print("\nLoan Count by Purpose")
print(merged_df["purpose"].value_counts())

print("\nDefault Rate by Purpose")

portfolio_default_rate = (
    merged_df.groupby("purpose")["loanStatus"]
    .apply(lambda x: (x == "Default").mean() * 100)
)

print(portfolio_default_rate)

# Conclusion:
#
# Debt Consolidation is the bank's largest lending segment,
# accounting for more than 81,000 loans while maintaining
# a moderate default rate of approximately 9.6%.
#
# Home Improvement loans demonstrate a similar default rate
# while maintaining meaningful loan volume, suggesting
# potential for portfolio expansion.
#
# In contrast, Healthcare loans contribute relatively little
# lending volume but exhibit the highest default rate
# (25.8%), indicating a segment that may require stricter
# underwriting standards and additional risk controls.
#
# Business Impact:
# The bank should continue expanding large-volume,
# moderate-risk segments while carefully monitoring
# high-risk segments such as Healthcare.


# -------------------------
# Business Insight 3
# Does employment stability reduce default risk?
# -------------------------

print("\nDefault Rate by Employment Length")

employment_default = (
    merged_df.groupby("yearsEmployment")["loanStatus"]
    .apply(lambda x: (x == "Default").mean() * 100)
    .sort_values()
)

print(employment_default)

# Conclusion:
#
# Borrowers with longer employment histories
# consistently show lower default rates.
#
# Customers with 10+ years of employment
# exhibit the lowest default rates,
# while borrowers with less than 1 year
# of employment show the highest risk.
#
# Business Impact:
# Employment stability can serve as an
# additional indicator when evaluating
# borrower risk.

# -------------------------
# Business Insight 4
# Does credit utilization predict default risk?
# -------------------------

print("\nAverage Credit Utilization by Loan Status")

print(
    merged_df.groupby("loanStatus")
    ["revolvingUtilizationRate"]
    .mean()
)

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


# Conclusion:
#
# Default rates increase steadily as
# credit utilization rises.
#
# Borrowers using less than 20% of
# available credit show very low
# default rates (~3%).
#
# Borrowers using more than 80% of
# available credit show default rates
# above 13%.
#
# Business Impact:
# Credit utilization is one of the
# strongest early warning indicators
# of default risk in the portfolio.


# -------------------------
# Business Insight 5
# Is the bank's grading system effectively identifying risk?
# -------------------------


print("\nLoan Count by Grade")

print(
    merged_df["grade"]
    .value_counts()
    .sort_index()
)

print("\nDefault Rate by Grade")

grade_default = (
    merged_df.groupby("grade")["loanStatus"]
    .apply(lambda x: (x == "Default").mean() * 100)
    .sort_values(ascending=False)
)

print(grade_default)


# Conclusion:
#
# Default rates increase consistently as loan grades move
# from A grades toward E grades.
#
# A-grade borrowers exhibit the lowest default rates,
# while E-grade borrowers show the highest default rates
# in the portfolio.
#
# This pattern indicates that the bank's grading system
# is successfully distinguishing between low-risk and
# high-risk borrowers.
#
# Business Impact:
# The grading framework appears to be an effective
# risk assessment tool and can be used to support
# lending decisions, pricing strategies, and risk controls.