import joblib
import pandas

def ohe_value(df):
    ohe_column = joblib.load('columns.pkl')
    category_columns = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']
    df_processed = pandas.get_dummies(df, columns=category_columns)
    new_dict = {}
    for column in ohe_column:
        if column in df_processed.columns:
            new_dict[column] = df_processed[column].values
        else:
            new_dict[column] = 0
    new_dataframe = pandas.DataFrame(new_dict)
    return new_dataframe