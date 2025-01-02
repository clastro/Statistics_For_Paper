from scipy.stats import wilcoxon

errors_A_B = [1.2, 0.9, 1.1, 1.3, 1.0]  # error in A+B Model
errors_C = [1.1, 1.0, 1.2, 1.4, 1.1]    # error in C Model

# Wilcoxon Signed-Rank Test 
stat, p_value = wilcoxon(errors_A_B, errors_C)

print("Wilcoxon Test Statistic:", stat)
print("p-value:", p_value)

alpha = 0.05  # 유의수준
if p_value < alpha:
    print("결과: 두 모델의 성능 차이가 통계적으로 유의미합니다.")
else:
    print("결과: 두 모델의 성능 차이가 통계적으로 유의미하지 않습니다.")
