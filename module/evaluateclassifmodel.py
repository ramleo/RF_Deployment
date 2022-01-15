# Evaluating the model
def evaluate(pred=None, target=None):
    '''Evaluating the prediction of the model'''

    # Importing relevant libraries
    from sklearn.metrics import (accuracy_score, recall_score, precision_score, f1_score, fbeta_score,
                                   roc_auc_score, cohen_kappa_score, hinge_loss, hamming_loss, log_loss)

    # Calculating the metrics
    accuracy = round(accuracy_score(target, pred), 2)
    recall = round(recall_score(target, pred), 2)
    precision = round(precision_score(target, pred), 2)
    f1 = round(f1_score(target, pred), 2)
    fbeta = round(fbeta_score(target, pred, beta=2.5), 2)
    roc_auc = round(roc_auc_score(target, pred), 2)
    cohen_kappa = round(cohen_kappa_score(target, pred), 2)
    hin_loss = round(hinge_loss(target, pred), 2)
    ham_loss = round(hamming_loss(target, pred), 2)
    logl_loss = round(log_loss(target, pred), 2)

    print('Accuracy of the model is:', accuracy)
    print('Recall of the model is:', recall)
    print('Precision of the model is:', precision)
    print('F1-Score of the model is:', f1)
    print('FBeta-Score of the model is:', fbeta)
    print('ROC AUC Score of the model is:', roc_auc)
    print('Cohen-Kappa-Score of the model is:', cohen_kappa)
    print('Hinge-Loss of the model is:', hin_loss)
    print('Hamming-Loss of the model is:', ham_loss)
    print('Log-Loss of the model is:', logl_loss)