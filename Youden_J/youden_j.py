from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score

def calculate_metrics(y_true, y_pred_proba):
    # Compute the ROC curve
    fpr, tpr, thresholds = roc_curve(y_true, y_pred_proba)
    
    # Compute Youden's J for each threshold
    youdens_j = tpr - fpr
    optimal_idx = np.argmax(youdens_j)
    optimal_threshold = thresholds[optimal_idx]


    # Convert probabilities to binary predictions using the optimal threshold
    y_pred = (y_pred_proba >= optimal_threshold).astype(int)
    
    # Accuracy
    accuracy = accuracy_score(y_true, y_pred)
    
    # Confusion Matrix
    cm = confusion_matrix(y_true, y_pred)
    
    # Sensitivity and Specificity
    tn, fp, fn, tp = cm.ravel()
    sensitivity = tp / (tp + fn)
    specificity = tn / (tn + fp)
    
    # PPV and NPV
    ppv = tp / (tp + fp)
    npv = tn / (tn + fn)
    
    # AUROC
    auroc = roc_auc_score(y_true, y_pred_proba)
    
    # Youden's J at the optimal threshold
    youdens_j_max = sensitivity + specificity - 1
    
    return accuracy, sensitivity, specificity, ppv, npv, cm, auroc, youdens_j_max, optimal_threshold


# y_true = X_test['label'].values
# y_pred = np.round(pred[:,1])

# accuracy, sensitivity, specificity, ppv, npv, cm, auroc, youden_j, optimal_threshold = calculate_metrics(y_true, pred[:,1])

