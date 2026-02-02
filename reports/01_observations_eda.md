## Exploratory Data Analysis — Key Observations

This section summarizes the key insights obtained from exploratory analysis of customer demographics, subscribed services, billing behavior, and engineered features, with respect to customer churn.

---

### Demographic Factors

- **Gender** shows negligible impact on churn, with male and female customers exhibiting nearly identical churn rates. This indicates that gender is a weak standalone predictor of churn.

- **Senior Citizen status** has a strong association with churn. Senior customers churn at significantly higher rates than non-senior customers, making this a high-risk demographic segment.

- **Partner status** is strongly linked to retention. Customers without a partner churn much more frequently, suggesting that household stability reduces churn risk.

- **Dependents** have one of the strongest negative correlations with churn. Customers with dependents rarely churn, indicating that family-based usage significantly increases customer stickiness.

---

### Core Services

- **Phone Service** alone does not meaningfully impact churn. Customers with and without phone service exhibit similar churn behavior, indicating low predictive value.

- **Multiple Lines** are associated with slightly higher churn, possibly due to increased cost or billing complexity, though the effect is relatively weak.

---

### Add-On Services and Bundles

- **Online Security**, **Online Backup**, **Device Protection**, and **Tech Support** all act as protective factors. Customers subscribing to these services churn at substantially lower rates, highlighting the importance of service reliability and perceived value.

- The **Digital Security Bundle** (combined protection and support services) is one of the strongest retention indicators. Customers with the full bundle exhibit extremely low churn rates, indicating very high commitment and switching costs.

- **Total Add-On Services** shows a clear inverse relationship with churn. Customers with few or no add-ons churn the most, while churn decreases steadily as the number of add-on services increases, reinforcing the concept of service stickiness.

---

### Streaming Services

- **Streaming TV** and **Streaming Movies** are associated with higher churn rates. Streaming customers appear more price-sensitive and less loyal, suggesting that streaming services alone do not significantly improve customer retention.

---

### Billing and Payment Behavior

- **Paperless Billing** customers churn at significantly higher rates. This may reflect greater flexibility and lower switching costs among digitally savvy customers.

- **Auto Payment** is a strong retention signal. Customers enrolled in automatic payment methods churn at less than half the rate of those using manual payment methods.

- **Payment Method** has a major impact on churn. Customers using electronic checks exhibit the highest churn rates, while customers using automatic bank transfers or credit cards churn far less.

---

### Internet Service Type

- **Internet Service** is a major churn driver. Fiber optic customers churn at substantially higher rates than DSL customers or customers without internet service, likely due to higher costs, expectations, or increased competition.

---

### Contract and Tenure

- **Contract Type** is the strongest categorical predictor of churn. Month-to-month customers churn at extremely high rates, while one-year and two-year contract customers are significantly more stable.

- **Tenure** exhibits a strong lifecycle effect. Customers in the first six months have the highest churn risk, and churn decreases sharply as tenure increases. Long-tenured customers are far more loyal.

---

### Revenue and Customer Value

- **Monthly Charges** are positively associated with churn. Customers with higher recurring charges are more likely to churn, indicating price sensitivity.

- **Total Charges** primarily reflect tenure-driven behavior. Most churn occurs before customers accumulate high total spending, reinforcing the importance of early-stage retention efforts.

- **Customer Lifetime Value (CLTV)** shows that lower-value customers churn more frequently, while higher-value customers tend to be more loyal. CLTV is therefore useful for prioritizing retention strategies.

---
---

## Feature Strength Summary

Based on exploratory data analysis and churn rate comparisons, features were qualitatively categorized by their observed relationship with customer churn. This categorization is intended to guide modeling decisions and feature prioritization, not to replace model-based feature importance.

---

### Strong Predictors

These features show clear and consistent separation between churned and retained customers and are expected to have high predictive value.

- Tenure / Tenure Bucket  
- Contract Type  
- Internet Service Type  
- Payment Method  
- Auto Payment  
- Total Add-On Services  
- Digital Security Bundle  
- Tech Support  
- Online Security  
- Dependents  
- Senior Citizen  

---

### Medium-Strength Predictors

These features show meaningful trends but with noticeable overlap between churned and retained customers. Their predictive value is often enhanced when combined with stronger features.

- Monthly Charges  
- Total Charges  
- CLTV  
- Online Backup  
- Device Protection  
- Multiple Lines  

---

### Weak Predictors

These features exhibit minimal churn separation or inconsistent patterns and are considered weak standalone predictors. They may still contribute marginally through interactions but are candidates for removal if model performance is unaffected.

- Gender  
- Phone Service  
- Streaming TV  
- Streaming Movies  

---

### Notes

- Feature strength classification is based on univariate and bivariate exploratory analysis only.  
- Final feature selection will be guided by model performance, cross-validation results, and feature importance analysis.  
- Weak predictors are not dropped upfront and may still be retained if they improve model generalization.
