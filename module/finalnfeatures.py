def final_n_features(data=None, target=None, sel_feat_list=None, model=None, metric_list=None, rfe_estimator=None, sel_feat_tech=None):
    '''
    This function takes a model, data, target variable, metrics, RFE estimator,
    selected list of techniques along with features selected by those techniques and
    returns a pandas dataframe consisting the model, metrics as columns and feature
    selection techniques as indices.
    '''

    # Relevant packages to import
    import pandas as pd

    # Finding length of each element of sel_feat_list
    len_list = []
    for i in sel_feat_list:
        len_list.append(len(i))

    # Finding the number of features
    for i in range(1, len(len_list)):
        if len_list[i] < len_list[i - 1]:
            m = len_list[i]

    # Finding recall, precision, f1 for the model for every element in sel_feat_list
    dict1 = dict()
    dict1[str(model).split('(')[0]] = dict()

    for j in metric_list:
        dict1[str(model).split('(')[0]][str(j).split()[1]] = list()
        for i in sel_feat_list:
            rfe = RFE(estimator=rfe_estimator, n_features_to_select=m)
            rfe.fit(data[i], target)
            rfe_sel_cols = data[i].columns[rfe.get_support()]
            df = data[rfe_sel_cols]
            y_pred = model.fit(df, target).predict(df)
            dict1[str(model).split('(')[0]][str(j).split()[1]].append(j(target, y_pred))

    dict2 = dict()
    for i, j in dict1.items():
        for k, v in j.items():
            dict2[i + '_' + k] = v

    indx = []
    for i in sel_feat_tech[:2]:
        i = str(i).split()[1]
        indx.append(i)
    for i in sel_feat_tech[2:]:
        i = str(i).split('(')[0]
        indx.append(i)

    df = pd.DataFrame(dict2, index=indx)

    return df