# Telco Customer Churn Dataset — Data Dictionary

## About the Dataset

### Context
A fictional telecommunications company that provided home phone and Internet services to **7,043 customers in California** during **Q3**.

The dataset captures customer demographics, account information, subscribed services, billing details, and churn-related indicators.

---

## Data Description

- **Observations:** 7,043 customers  
- **Variables:** 33 columns  

---

## Column Descriptions

### Customer Identification & Geography

- **CustomerID**  
  A unique identifier for each customer.

- **Count**  
  A value used in reporting or dashboarding to sum the number of customers in a filtered set.

- **Country**  
  The country of the customer’s primary residence.

- **State**  
  The state of the customer’s primary residence.

- **City**  
  The city of the customer’s primary residence.

- **Zip Code**  
  The ZIP code of the customer’s primary residence.

- **Lat Long**  
  Combined latitude and longitude of the customer’s primary residence.

- **Latitude**  
  Latitude of the customer’s primary residence.

- **Longitude**  
  Longitude of the customer’s primary residence.

---

### Demographics

- **Gender**  
  Customer gender: `Male`, `Female`.

- **Senior Citizen**  
  Indicates whether the customer is 65 years or older: `Yes`, `No`.

- **Partner**  
  Indicates whether the customer has a partner: `Yes`, `No`.

- **Dependents**  
  Indicates whether the customer lives with dependents such as children, parents, or grandparents: `Yes`, `No`.

---

### Account & Tenure Information

- **Tenure Months**  
  Total number of months the customer has been with the company as of the end of the quarter.

- **Contract**  
  Customer’s contract type:  
  - `Month-to-Month`  
  - `One Year`  
  - `Two Year`

- **Paperless Billing**  
  Indicates whether the customer has opted for paperless billing: `Yes`, `No`.

- **Payment Method**  
  Method used to pay the bill:  
  - Bank Withdrawal  
  - Credit Card  
  - Mailed Check

---

### Services Subscribed

- **Phone Service**  
  Indicates whether the customer subscribes to home phone service: `Yes`, `No`.

- **Multiple Lines**  
  Indicates whether the customer subscribes to multiple phone lines: `Yes`, `No`.

- **Internet Service**  
  Type of internet service subscribed:  
  - `No`  
  - `DSL`  
  - `Fiber Optic`  
  - `Cable`

- **Online Security**  
  Indicates whether the customer subscribes to an online security service: `Yes`, `No`.

- **Online Backup**  
  Indicates whether the customer subscribes to an online backup service: `Yes`, `No`.

- **Device Protection**  
  Indicates whether the customer subscribes to device protection for internet equipment: `Yes`, `No`.

- **Tech Support**  
  Indicates whether the customer subscribes to a premium technical support plan: `Yes`, `No`.

- **Streaming TV**  
  Indicates whether the customer streams TV using the internet service: `Yes`, `No`.  
  *(No additional fee is charged.)*

- **Streaming Movies**  
  Indicates whether the customer streams movies using the internet service: `Yes`, `No`.  
  *(No additional fee is charged.)*

---

### Billing & Revenue

- **Monthly Charge**  
  Current total monthly charge for all subscribed services.

- **Total Charges**  
  Total charges accumulated by the customer up to the end of the quarter.

---

### Churn & Customer Value Indicators

- **Churn Label**  
  Indicates whether the customer churned during the quarter:  
  - `Yes` → Customer left  
  - `No` → Customer stayed  

- **Churn Value**  
  Binary churn indicator:  
  - `1` → Customer churned  
  - `0` → Customer retained  

- **Churn Score**  
  A score from **0–100** generated using IBM SPSS Modeler.  
  Higher values indicate a higher likelihood of churn.  
  *(Derived using predictive modeling techniques.)*

- **CLTV (Customer Lifetime Value)**  
  Predicted lifetime value of the customer based on corporate formulas and historical data.  
  Higher values indicate more valuable customers.

- **Churn Reason**  
  Specific reason provided by the customer for leaving the company.

---

## Data Source

- Dataset documentation:  
  https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113

- Download source:  
  https://community.ibm.com/accelerators/?context=analytics&query=telco%20churn&type=Data&product=Cognos%20Analytics

- Related datasets:  
  https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2018/09/12/base-samples-for-ibm-cognos-analytics