## Overview

### Youden's J Statistic for Threshold Optimization

Youden's J statistic is used to determine the optimal threshold for classification by maximizing the sum of sensitivity and specificity. This threshold helps balance false positives and false negatives.

**Youden's J Statistic Formula:**

$$
J = \text{Sensitivity} + \text{Specificity} - 1
$$

Where:
- **Sensitivity** (True Positive Rate) is the proportion of actual positives correctly identified by the test.
- **Specificity** (True Negative Rate) is the proportion of actual negatives correctly identified by the test.

```python
# Calculate the optimal threshold using Youden's J statistic
optimal_threshold = max(tpr - fpr for fpr, tpr, _ in roc_curve(y_true, y_scores))[2]
```
### Delong Test for Comparing ROC Curves

The Delong test is a statistical method used to compare the areas under two Receiver Operating Characteristic (ROC) curves to determine if there is a significant difference between them. This test assesses whether the difference between the areas under the curves (AUCs) of two models is statistically significant.

**Delong Test Formula:**

The Delong test assumes that the difference in AUCs follows a normal distribution with a mean of zero and a variance given by:

$$
\text{AUC}_1 - \text{AUC}_2 \sim \text{Normal}\left(0, \text{Var}(\text{AUC}_1) + \text{Var}(\text{AUC}_2) - 2 \cdot \text{Cov}(\text{AUC}_1, \text{AUC}_2)\right)
$$

Where:
- **AUC** stands for the Area Under the ROC Curve.
- **Var** denotes the variance of the AUC.
- **Cov** denotes the covariance between the AUCs.

**Delong Test Implementation:**

```python
# Perform Delong test to compare AUCs
z_statistic, p_value = delong_test(auc1, auc2, n1, n2)
```
