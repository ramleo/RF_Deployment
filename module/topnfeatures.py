def top_n_features(data=None, feat_sel_techs=None, target=None, num_feat=None):
    '''This function only takes selection techniques like "f_classif","f_regression",
    "SelectKBest (Classification)","SelectKBest (Regression)","SelectPercentile (Classification)",
    "SelectPercentile (Regression)","SelectFromModel (DT,RF,XGB,LOGREG)" and "VarianceThreshold"
    and provides list of features selected by these techniques along with the list of the
    techniques. This function also takes data, target variable and numbber of features to be
    selected.
    '''

    # Importing relevant packages
    import random
    import pandas as pd
    from sklearn.feature_selection import f_classif, f_regression

    # In-built in function as it needs 'data' and 'target' as argument
    fclass = f_classif(data, target)
    freg = f_regression(data, target)

    # Fitting feature selection techniques to 'data' and 'target'
    for tech in feat_sel_techs:
        tech.fit(data, target)

    # Filtering top n features from the results
    fclass_feat = list(pd.DataFrame(pd.concat([pd.Series(data.columns), pd.Series(fclass[0])], axis=1)) \
                       .nlargest(num_feat, columns=1)[0])

    freg_feat = list(pd.DataFrame(pd.concat([pd.Series(data.columns), pd.Series(freg[0])], axis=1)) \
                     .nlargest(num_feat, columns=1)[0])

    selk_class_feat = data.columns[selk_class.get_support()]
    selk_reg_feat = data.columns[selk_reg.get_support()]
    selp_class_feat = data.columns[selp_class.get_support()]
    selp_reg_feat = data.columns[selp_reg.get_support()]
    sfm_dt_feat = data.columns[sfm_dt.get_support()]
    sfm_rf_feat = data.columns[sfm_rf.get_support()]
    sfm_xgb_feat = data.columns[sfm_xgb.get_support()]
    sfm_log_feat = data.columns[sfm_log.get_support()]
    vt_feat = data.columns[vt.get_support()]

    random.seed(7)
    vt_feat_50 = random.sample(list(vt_feat), k=num_feat)

    print('f_classif:', len(fclass_feat))
    print('f_regression:', len(freg_feat))
    print('SelectKBest_fclassif:', len(selk_class_feat))
    print('SelectKBest_fregression:', len(selk_reg_feat))
    print('SelectPercentile_fclassif:', len(selp_class_feat))
    print('SelectPercentile_fregression:', len(selp_reg_feat))
    print('SelectFromModel_dt:', len(sfm_dt_feat))
    print('SelectFromModel_rf:', len(sfm_rf_feat))
    print('SelectFromModel_xgb:', len(sfm_xgb_feat))
    print('SelectFromModel_logreg:', len(sfm_log_feat))
    print('Variance_Threshold:', len(vt_feat_50))

    sel_feat_list = [fclass_feat, freg_feat, selk_class_feat, selk_reg_feat, selp_class_feat, selp_class_feat,
                     sfm_dt_feat, sfm_rf_feat, sfm_xgb_feat, sfm_log_feat, vt_feat_50]

    sel_feat_techs = [f_classif, f_regression, selk_class, selk_reg, selp_class, selp_reg, sfm_dt, sfm_rf, sfm_xgb,
                      sfm_log, vt]

    return sel_feat_list, sel_feat_techs