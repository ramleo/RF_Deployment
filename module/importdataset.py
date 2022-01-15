def import_data_split(file=None):
    '''Importing dataset and splitting into train-test data and returning copy of train-test datasets'''
    import pandas
    from sklearn.preprocessing import LabelEncoder
    from sklearn.model_selection import train_test_split

    techno = pandas.read_excel(r'C:\Users\DA1041TU\Documents\UpGrad\Data\TechnoServe(SaaS)' + file)

    le = LabelEncoder()
    techno['Opportunity Status'] = le.fit_transform(techno['Opportunity Status'])

    X = techno.drop(['Opportunity Status', 'Opportunity ID'], axis=1)
    y = techno['Opportunity Status']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=9)
    X_train = X_train.copy()
    X_test = X_test.copy()
    y_train = y_train.copy()
    y_test = y_test.copy()

    return X_train, X_test, y_train, y_test

