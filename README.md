# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals


This project aims to automate the loan eligibility process, using historical data of customer information obtained through online application forms. The dataset includes details regarding the customer's socio-economic and demographic attributes.

The goal of this project is to predict loan approval or rejection based on the provided customer information by using ML. The dataset comprises various variables such as Loan_ID, Gender, Marrital status, number of dependents if any, education level, Self_Employed, Applicant Income, Coapplicant Income, Loan Amount, Loan Amount Term, Credit History, Property Area, and Loan Status. This historical data can be accessed [here](https://drive.google.com/file/d/1h_jl9xqqqHflI5PsuiQd_soNYxzFfjKw/view).


## Hypothesis
Applicants with higher credit score
Applicants with lower Loan-amount
Applicants who don't have dependants
Applicants with lower amount term

## EDA 
The strongest positive correlation with LoanApproval is found with CreditHistory (0.567105), while PropertyArea_rural has the most negative correlation with LoanApproval (-0.109203).

 Negative correlations with LoanApproval are observed with:
 - LoanAmount
 - LoanAmountTerm
 - SelfEmployed
 - Married_No
 - Dependents_0, Dependents_1, Dependents_3+ 
 - PropertyArea_Rural (most negative)
 - PropertyArea_Urban
 
 Positive correlations with LoanApproval are found with:
 - ApplicantIncome
 - CoapplicantIncome
 - Education_Graduate 
 - CreditHistory (most positive)
 - Married
 - Dependents_2
 - PropertyArea_Semiurban
 
 People approved for loans are likely to have coapplicants with high income, be a graduate, have credit history, be male, be married/unknown, have two children and live in the suburbs. On the other hand, those who aren't approved tend to ask for large loans and long terms, are female/unknown gender, aren't married, have none or one child, and live in a rural or urban area. 
 
 Interestingly, ApplicantIncome has a very weak positive correlation with LoanApproval. Graduate (0.023), PropertyArea_Semiurban (0.003), CreditHistory (0.000), and PropertyArea_Rural (0.013) are features with a p-value < 5, which indicates that their correlations with LoanApproval are statistically significant. 
 
 Based on this information, it is possible to accept the hypothesis that individuals who are graduates, have a property in a semi-urban area, and have credit history are likely to get loan approval. However, the hypothesis regarding applicants with high income, having a co-applicant with a relatively high income, being married, and having a small number of dependents remain uncertain.

## Process

### 1. Creating Hypothesis
- Briefly researching factors that influence loan approval.
- Looking at the available information available in the dataset.
- Creating a List of educated guesses/hypothesis about factors that impact loan approval in the dataset context.
### 2. Cleaning and Transforming Data
- Impute NaNs with mode for categorical variables or median for numberical variables
- OHE categorical features
- Using Log normalization for Loan amount and total_income
- Using MinMax scaler to scale other numerical variables

### 3. EDA
In the exploratory data analysis, Pearson's test was used to examine the correlations between LoanStatus and other features. The results showed significant positive correlations between loan approval and the variables 'graduated', living in a suburban area, and having credit history. In contrast, a significant negative correlation was observed between loan approval and living in a rural area. 
### 4. Feature Engineering
- Creating a Third variable as total amount of loan (applicant loan + coapplicant loan amount)
-
 model with highest av. accuracy
Grid search on logistic regression model to find best hyperparameters
estimator = grid.best_estimator_ ; pickle model
### 5. Testing Different Models
- Choosing model with highest av. accuracy (RandomForestClassifier)
### 6. Creating Pipeline

Steps to prepare data for the pipeline:
- loading the raw CSV
- Chaning Dependents variable to Categorical variable
- Creating the new varibable (total_income)
- Dropping unrelated columns ('CoapplicantIncome','ApplicantIncome','Loan_ID')
- change loan amount term into years
- replace loan status values with 1 and 0

Steps in Pipeline:
#### 1. preprocessing
- Defining log_transform to transform total income and loan amount variables
- Creating numeric transforms (MinMax scaler)
- Creating categorical transform (OHE)
#### 2. classifier
- Making predictions using the winner model




## Challanges 
- Limited time to the project (24 hours)
- Technical difficulties in implementing an API & deployment

## Future Goals
Creating a website for loan application with polished UI/UX
