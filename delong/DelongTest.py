import delong

# Delong Test P- value

10 ** delong.delong_roc_test(y_test,serial_pred,single_pred)

# Delong AUC CI

alpha = .95 # 95% confidence
y_pred = probas_[:,1]
y_true = y[test_index].values

auc, auc_cov = delong.delong_roc_variance(
    y_true,
    y_pred)

auc_std = np.sqrt(auc_cov)
lower_upper_q = np.abs(np.array([0, 1]) - (1 - alpha) / 2)

ci = stats.norm.ppf(
    lower_upper_q,
    loc=auc,
    scale=auc_std)

ci[ci > 1] = 1

print('AUC:', auc)
print('AUC COV:', auc_cov)
print('95% AUC CI:', ci)
