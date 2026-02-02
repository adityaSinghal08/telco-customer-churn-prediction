## Exploratory Data Analysis (EDA)

This section summarizes the key insights obtained from exploratory analysis of customer demographics, services, billing behavior, engineered features, and numerical correlations, with respect to customer churn. Observations are based on churn rate comparisons, distributional analysis, and correlation analysis.

---

### Demographic Factors

- **Gender** shows negligible impact on churn, with male and female customers exhibiting nearly identical churn rates. Gender is therefore a weak standalone predictor of churn.

- **Senior Citizen status** has a strong association with churn. Senior customers churn at significantly higher rates than non-senior customers, identifying this group as a high-risk demographic segment.

- **Partner status** is strongly linked to retention. Customers without a partner churn much more frequently, suggesting that household stability reduces churn risk.

- **Dependents** exhibit one of the strongest negative relationships with churn. Customers with dependents rarely churn, indicating that family-based usage significantly increases customer stickiness.

---

### Core Services

- **Phone Service** alone does not meaningfully impact churn. Customers with and without phone service show similar churn behavior, indicating low predictive value.

- **Multiple Lines** are associated with slightly higher churn, possibly due to increased cost or billing complexity, though the effect is relatively weak.

---

### Add-On Services and Bundles

- **Online Security**, **Online Backup**, **Device Protection**, and **Tech Support** all act as protective factors. Customers subscribing to these services churn at substantially lower rates, highlighting the importance of service reliability and perceived value.

- The **Digital Security Bundle** (combined protection and support services) is one of the strongest retention indicators. Customers with the full bundle exhibit extremely low churn rates, suggesting very high commitment and switching costs.

- **Total Add-On Services** shows a clear inverse relationship with churn. Customers with few or no add-ons churn the most, while churn decreases steadily as the number of add-on services increases. Correlation analysis indicates this relationship is likely non-linear or threshold-based rather than strictly linear.

---

### Streaming Services

- **Streaming TV** and **Streaming Movies** are associated with higher churn rates. Streaming customers appear more price-sensitive and less loyal, indicating that streaming services alone do not significantly improve customer retention.

---

### Billing and Payment Behavior

- **Paperless Billing** customers churn at significantly higher rates. This may reflect greater flexibility and lower switching costs among digitally savvy customers.

- **Auto Payment** is a strong retention signal. Customers enrolled in automatic payment methods churn at less than half the rate of those using manual payments.

- **Payment Method** has a major impact on churn. Customers using electronic checks exhibit the highest churn rates, while customers using automatic bank transfers or credit cards churn far less.

---

### Internet Service Type

- **Internet Service** is a major churn driver. Fiber optic customers churn at substantially higher rates than DSL customers or customers without internet service, likely due to higher pricing, expectations, or increased competition.

---

### Contract and Tenure

- **Contract Type** is the strongest categorical predictor of churn. Month-to-month customers churn at extremely high rates, while one-year and two-year contract customers are significantly more stable.

- **Tenure** exhibits a strong lifecycle effect. Customers in the first six months have the highest churn risk, and churn decreases sharply as tenure increases. Correlation analysis confirms tenure as the strongest numerical churn signal.

---

### Revenue and Customer Value

- **Monthly Charges** show a weak-to-moderate positive relationship with churn. Higher monthly charges increase churn risk, but the relationship is not strongly linear and is influenced by contract type and tenure.

- **Total Charges** show a weak negative correlation with churn, largely reflecting tenure effects. Customers who remain longer accumulate higher total charges and are less likely to churn.

- **Customer Lifetime Value (CLTV)** exhibits a weak negative relationship with churn. Higher-value customers tend to be more loyal, though CLTV is more useful for business prioritization than as a dominant predictive feature.

---

## Feature Strength Summary

Feature strength categories are based on univariate churn rates, distributional separation, and correlation analysis. This classification is intended to guide modeling decisions and does not replace model-based feature importance.

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

These features show meaningful trends but with noticeable overlap between churned and retained customers. Their predictive value is often enhanced when combined with stronger predictors.

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

- Feature strength classification is based on exploratory analysis only.  
- Final feature selection will be driven by model performance, cross-validation, and feature importance analysis.  
- Weak predictors are not dropped upfront and may still be retained if they improve generalization.
