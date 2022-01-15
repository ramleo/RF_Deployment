def model_metrics(model_list=None, metric_list=None, data=None, target=None, class_type=None):
    '''
    **Warning:
    1. This function cannot take metrics where we need to provide additional arguments other tha data and target,
    like fbeta_score where we need to provide 'beta' value as additional argument.
    2. It takes about 1 minute for the function to execute because of for loop within a for loop.
    **
    A function for calculating the classification metrics such as accuracy_score, recall_score, precision_score, f1_score,
    fbeta_score, roc_auc_score, cohen_kappa_score, hinge_loss, hamming_loss, log_loss using a model,
    and returning a pandas dataframe, or calculating the regression metrics such as rsquare, mean_absolute_error,
    median_absolute_error, mean_squared_error and root_mean_squared_error using a model, and returning a pandas dataframe.

    model = List of either classification or regression model,
    data = Should be a pandas dataframe,
    target = Should be pandas series
    class_type = Should be a string and can be any of the 'classification', 'classif', 'regression', 'regress' or 'reg'.
    '''
    # Importing classification relevant packages
    import pandas as pd

    # Creating empty dictionary
    dictionary = dict()

    if (class_type.lower() == 'classification') or (class_type.lower() == 'classif'):

        # Creating a loop to append empty lists provided in the empty dictionary with metrics
        for i in range(len(model_list)):
            dictionary[str(model_list[i])] = list()
            for j in range(len(metric_list)):
                y_pred = model_list[i].fit(data, target).predict(data)
                dictionary[str(model_list[i])].append(round(metric_list[j](target, y_pred), 2))

        # Creating columns list to rename the dataframe
        cols = []
        for i in list(dictionary.keys()):
            i = i.split('(')[0]
            cols.append(i)

        # Creating index list index the dataframe
        indx = []
        for i in metric_list:
            i = str(i).split()[1]
            indx.append(i)

        # Creating a dataframe out the resultant dictionary
        metric_df = pd.DataFrame(dictionary, index=indx)

        # Renaming the dataframe
        metric_df.columns = cols

    elif (class_type.lower() == 'regression') or (class_type.lower() == 'regress') or (class_type.lower() == 'reg'):

        # Creating a loop to append empty lists provided in the empty dictionary with metrics
        for i in range(len(model_list)):
            dictionary[str(model_list[i])] = list()
            for j in range(len(metric_list)):
                y_pred = model_list[i].fit(data, target).predict(data)
                dictionary[str(model_list[i])].append(round(metric_list[j](target, y_pred), 2))

        # Creating columns list to rename the dataframe
        cols = []
        for i in list(dictionary.keys()):
            i = i.split('(')[0]
            cols.append(i)

        # Creating index list index the dataframe
        indx = []
        for i in metric_list:
            i = str(i).split()[1]
            indx.append(i)

    # Creating a dataframe out the resultant dictionary
    metric_df = pd.DataFrame(dictionary, index=indx)

    # Renaming the dataframe
    metric_df.columns = cols

    return metric_df