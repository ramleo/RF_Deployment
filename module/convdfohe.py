def conv_df_ohe(data=None):

    # Import relevant libraries
    import pandas as pd
    from module.createvariables import create_vars
    # List of required variables
    _, _, _, \
    _, encoded_vars, non_ohe_encoded, _ = create_vars()

    total_vars = encoded_vars + non_ohe_encoded
    for i in total_vars:
        if i not in encoded_vars:
            encoded_vars.append(i)
    ohe_df = pd.DataFrame(data, columns=encoded_vars)

    return ohe_df.copy()