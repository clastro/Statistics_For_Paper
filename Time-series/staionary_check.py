# 정상성 :시계열의 평균과 분산이 일정하고, 특정한 트렌드 (추세)가 존재하지 않는 성질

from statsmodels.tsa.stattools import adfuller # adf 검정

def adf_test(x):
    """
    if : p_value < 0.001
        wave is stationary
    """
    stat, p_value, lags, nobs, crit, icb = adfuller(x)
    return stat,p_value,lags
  
stat, p_val, lags = adf_test(n_ecg)

