def conv_df_ord(data=None):

    # Import relevant libraries
    import pandas as pd
    from module.createvariables import create_vars
    # List of required variables
    total_vars, _, ord_vars, \
    _, _, _, _ = create_vars()

    for i in total_vars:
        if i not in ord_vars:
            ord_vars.append(i)
    ord_df = pd.DataFrame(data, columns=ord_vars)

    return ord_df.copy()