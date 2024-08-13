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

- **Delong Test**:
  - Formula: \( \text{AUC}_{1} - \text{AUC}_{2} \sim \text{Normal}\left(0, \text{Var}(\text{AUC}_{1}) + \text{Var}(\text{AUC}_{2}) - 2 \cdot \text{Cov}(\text{AUC}_{1}, \text{AUC}_{2})\right) \)
  - Used to compare the areas under two ROC curves to assess statistical significance.
