from scipy.stats import sem
from sklearn.metrics import roc_auc_score 

np.random.seed(1234)
rng=np.random.RandomState(1234)

def get_ci_auc( y_true, y_pred ): # Confidence Interval 구하기

    n_bootstraps = 1000   # 1000번의 bootstrap
    bootstrapped_scores = []   #boot strap 저장
   
    for i in range(n_bootstraps): #1000번 반복
        # bootstrap by sampling with replacement on the prediction indices
        indices = rng.random_integers(0, len(y_pred) - 1, len(y_pred))
       
        if len(np.unique(y_true[indices])) < 2:
            # We need at least one positive and one negative sample for ROC AUC
            # to be defined: reject the sample
            continue

        score = roc_auc_score(y_true[indices], y_pred[indices])
        bootstrapped_scores.append(score)   
 
    sorted_scores = np.array(bootstrapped_scores)
    sorted_scores.sort()

   # 90% c.i.
   # confidence_lower = sorted_scores[int(0.05 * len(sorted_scores))]
   # confidence_upper = sorted_scores[int(0.95 * len(sorted_scores))]
 
   # 95% c.i.
    confidence_lower = sorted_scores[int(0.025 * len(sorted_scores))]
    confidence_upper = sorted_scores[int(0.975 * len(sorted_scores))]
   
    return confidence_lower,confidence_upper
