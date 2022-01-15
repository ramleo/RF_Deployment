def create_vars():
    '''Creating list of variables'''

    # Making list of total variables
    total_vars = ['Technology\nPrimary', 'City', 'B2B Sales Medium', 'Sales Velocity', 'Sales Stage Iterations',
                  'Opportunity Size (USD)', 'Client Revenue Sizing', 'Client Employee Sizing',
                  'Business from Client Last Year', 'Compete Intel', 'Opportunity Sizing']

    # Making list of sub-categories in the variable to use it in Ordinal encoding
    OpS = ['10K or less', '10K to 20K', '20K to 30K', '30K to 40K', '40K to 50K', '50K to 60K', 'More than 60K']
    BfCLY = ['0 (No business)', '0 - 25,000', '25,000 - 50,000', '50,000 - 100,000', 'More than 100,000']
    CES = ['1K or less', '1K to 5K', '5K to 15K', '15K to 25K', 'More than 25K']
    CRS = ['100K or less', '100K to 250K', '250K to 500K', '500K to 1M', 'More than 1M']

    # List of ordinal variable's ranking
    ord_rankings = [OpS, BfCLY, CES, CRS]

    # Making list of columns that need to be ordinal encoded
    ord_vars = ['Opportunity Sizing', 'Business from Client Last Year', 'Client Employee Sizing',
                'Client Revenue Sizing']

    # Making list of columns that need to be one-hot encoded
    ohe_vars = ['Technology\nPrimary', 'City', 'B2B Sales Medium', 'Compete Intel']

    # Making list of variables after One-Hot-Encoding
    encoded_vars = ['Analytics', 'ERP Implementation', 'Legacy Modernization', 'Technical Business Solutions',
                    'Bengaluru',
                    'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune', 'Enterprise Sellers', 'Marketing',
                    'Online Leads', 'Partners', 'Tele Sales', 'Known', 'None', 'Unknown']

    # Making list of columns those were not one-hot encoded
    non_ohe_encoded = ['Opportunity Sizing', 'Business from Client Last Year', 'Client Employee Sizing',
                       'Client Revenue Sizing', 'Sales Velocity', 'Sales Stage Iterations', 'Opportunity Size (USD)']

    # Final 5 selected features
    final_5 = ['Sales Velocity', 'Sales Stage Iterations', 'Opportunity Size (USD)',
               'Business from Client Last Year', 'Opportunity Sizing']

    return total_vars,ord_rankings,ord_vars,ohe_vars,encoded_vars,non_ohe_encoded,final_5