import pandas as pd
import numpy as np
import pathlib


def read_data(path: str) -> pd.DataFrame:
    
    df = pd.read_csv(path)
    return df


def outlier_removal(df: pd.DataFrame) -> pd.DataFrame:

    Q3 = df['price'].quantile(0.75)
    Q1 = df['price'].quantile(0.25)
    iqr = Q3 - Q1
    filtered_df = df[(df['price'] >= Q1 - 3.5*iqr) & (df['price'] <= Q3 + 3.5*iqr)]

    filtered_df = filtered_df[(filtered_df['carpet_area']<=5000) | (filtered_df['carpet_area'].isna())]

    q99 = filtered_df['builtup_area'].quantile(0.99)
    filtered_df = filtered_df[(filtered_df['builtup_area'].isna()) | (filtered_df['builtup_area']<q99) ]

    q99=filtered_df['super_built_up_area'].quantile(0.9995)
    filtered_df = filtered_df.loc[(filtered_df['super_built_up_area'].isna()) | (filtered_df['super_built_up_area']<q99) ]

    filtered_df = filtered_df[(filtered_df['price_per_sqft']<85000) | (filtered_df['price_per_sqft'].isna())]

    return filtered_df


def mode_based_imputation(row):

    if row['furnish_type'] is np.nan:
        mode_value = df[(df['location_area'] == row['location_area']) & (df['prop_type'] == row['prop_type'])]['furnish_type'].mode()
        # If mode_value is empty (no mode found), return NaN, otherwise return the mode
        if not mode_value.empty:
            return mode_value.iloc[0] 
        else:
            return np.nan
    else:
        return row['furnish_type']


def missing_value_imputation(df: pd.DataFrame) -> pd.DataFrame:

    sbb_df = df[~(df['super_built_up_area'].isnull()) & ~(df['builtup_area'].isnull()) & (df['carpet_area'].isnull())]
    sbb_df['carpet_area'] = sbb_df['carpet_area'].fillna(round(((sbb_df['super_built_up_area']/1.448+(sbb_df['builtup_area']/1.308))/2),2))
    df.update(sbb_df)

    sb_df = df[~(df['super_built_up_area'].isnull()) & (df['builtup_area'].isnull()) & (df['carpet_area'].isnull())]
    sb_df['carpet_area'] = sb_df['carpet_area'].fillna(round((sb_df['super_built_up_area']/1.448),2))
    df.update(sb_df)

    b_df = df[(df['super_built_up_area'].isnull()) & ~(df['builtup_area'].isnull()) & (df['carpet_area'].isnull())]
    b_df['carpet_area'] = b_df['carpet_area'].fillna(round(b_df['builtup_area']/1.308,2))
    df.update(b_df)

    df = df[~((df['super_built_up_area'].isnull()) & (df['builtup_area'].isnull()) & (df['carpet_area'].isnull()))]
    df.drop(columns=['super_built_up_area','builtup_area'],inplace=True)

    df['floor'] = df['floor'].fillna(7)

    df['furnish_type'] = df.apply(mode_based_imputation,axis=1)

    df['facing'] = df['facing'].fillna("Missing")

    df = df.dropna(subset=['ownership', 'bedrooms', 'bathrooms', 'prop_type', 'ageing','furnish_type'])

    return df


def categorize_floor(floor):

    if 0 <= floor <= 2:
        return "Low Floor"
    elif 3 <= floor <= 10:
        return "Mid Floor"
    elif 11 <= floor:
        return "High Floor"
    else:
        return None  
    

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:

    df['floor_category']=df['floor'].apply(categorize_floor)

# Dropping unnecessary columns that doesn't contribute to the model and keeping only the relevant features for prediction
    export = df.drop(columns=['Servant Room','Study Room','Pooja Room','Others','ownership'])
    export['price']= df['price']

    return export


if __name__ == "__main__":
    current_path = pathlib.Path(__file__).parent.parent.parent
    path = current_path / 'data' / 'cleaned' / 'cleaned_data.csv'
    df = read_data(path)
    df = outlier_removal(df)
    df = missing_value_imputation(df)
    df = feature_engineering(df)
    export_path = current_path / 'data' / 'processed' / 'preprocessed_data.csv'
    df.to_csv(export_path, index=False)