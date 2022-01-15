def impute_trans_df():

    # Importing relevant libraries
    import pandas as pd
    from module.convdford import conv_df_ord
    from module.convdfohe import conv_df_ohe
    from sklearn.pipeline import Pipeline
    from sklearn.compose import ColumnTransformer
    from module.createvariables import create_vars
    from sklearn.preprocessing import (OrdinalEncoder,\
        OneHotEncoder, \
        FunctionTransformer)

    # List of required variables
    total_vars, ord_rankings, ord_vars, \
    ohe_vars, encoded_vars, non_ohe_encoded, final_5 = create_vars()

    # Pipeline for Ordinal Encoding
    pipe_ordinal = Pipeline(steps=[
        ('Ordinal_Encoding', OrdinalEncoder(categories=ord_rankings))
    ])

    # Pipeline for One-Hot Encoding
    pipe_ohe = Pipeline(steps=[
        ('One_Hot_Encoding', OneHotEncoder(sparse=False, handle_unknown='ignore'))
    ])

    # Converting the ndarray into pandas df after ordinal encoding
    ft_ordinal = FunctionTransformer(conv_df_ord)

    # Converting the ndarray into pandas df after one-hot encoding
    ft_ohe = FunctionTransformer(conv_df_ohe)

    # Pipeline for Ordinal Encoding
    pipe_ordinal = Pipeline(steps=[
        ('Ordinal_Encoding', OrdinalEncoder(categories=ord_rankings))
    ])

    # Pipeline for One-Hot Encoding
    pipe_ohe = Pipeline(steps=[
        ('One_Hot_Encoding', OneHotEncoder(sparse=False, handle_unknown='ignore'))
    ])

    # Converting the ndarray into pandas df after ordinal encoding
    ft_ordinal = FunctionTransformer(conv_df_ord)

    # Converting the ndarray into pandas df after one-hot encoding
    ft_ohe = FunctionTransformer(conv_df_ohe)

    ct_ordinal = ColumnTransformer(transformers=[
        ('ord_enc', pipe_ordinal, ord_vars)
    ], remainder='passthrough')

    ct_ohe = ColumnTransformer(transformers=[
        ('ohe_enc', pipe_ohe, ohe_vars)
    ], remainder='passthrough')

    return ct_ordinal,ft_ordinal,ct_ohe,ft_ohe