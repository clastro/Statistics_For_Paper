# Overview

## Youden's J Statistic for Threshold Optimization

Youden's J Statistic Formula:
𝐽 = Sensitivity + Specificity − 1

Where:
Sensitivity (True Positive Rate) is the proportion of actual positives correctly identified by the test.
Specificity (True Negative Rate) is the proportion of actual negatives correctly identified by the test.

Youden's J statistic is used to determine the optimal threshold for classification by maximizing the sum of sensitivity and specificity. This threshold helps balance false positives and false negatives.

python
```
optimal_threshold = max(tpr - fpr for fpr, tpr, _ in roc_curve(y_true, y_scores))[2]
```
Calculate the optimal threshold using Youden's J statistic

## Delong Test

The Delong test compares the areas under two ROC curves to assess if there is a statistically significant difference between them.

python
```
z_statistic, p_value = delong_test(auc1, auc2, n1, n2)

```
Perform Delong test to compare AUCs
