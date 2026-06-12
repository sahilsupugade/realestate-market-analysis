import ast
import pandas as pd
from mapping import feature_points, city_areas, mapping_area
import regex as re
from pathlib import Path
import numpy as np


def price(value: str) -> float:
    if isinstance(value,str):
        pattern=r'([\d.]+)\s*(Cr|Lac)'
        match=re.search(pattern,value)
        if match:
            number = float(match.group(1))
            if match.group(2)== 'Cr':
                return number * 1e7
            else :
                return number * 1e5
    return np.nan


def price_sqft(value: str) -> int:
    if isinstance(value,str):
        pattern = r'([\d,]+)\s*(/sqft|sqft)'
        match = re.search(pattern,value)
        if match:
            return int(match.group(1).replace(',',''))
    return value


def prop(value: str) -> str:
    if isinstance(value, str):
        # Combined regex to handle multiple patterns:
        pattern = (
            r'(?:BHK|Bedroom)\s+([\w\s]+?)\s+(?:for sale|in)'  # Group 1: Flat/House/etc.
            r'|'
            r'(Studio Apartments|[\d]+\s*RK\s*Flats)'          # Group 2: Studio or RK Flats
            r'|'
            r'/+\s*([\w\s]+)\s+in'                             # Group 3: Plot after "/"
        )
        
        match = re.search(pattern, value, flags=re.IGNORECASE)
        if match:
            # Only one of the groups will be filled
            for group in match.groups():
                if group:
                    return group.strip()
        return np.nan
    return np.nan


def num_rooms(value: str) -> int:
    if isinstance(value,str):
        pattern = r'(\d|No)'
        match = re.search(pattern,value)
        if match:
            if match.group(1) == 'No':
                number = 0
                return int(number)
            else :
                return int(match.group(1))
    return np.nan


def location(value: str) -> str:
    if isinstance(value,str):
        pattern = r'in\s+([\w\s]+,\s*[\w]+)'
        match = re.search(pattern,value)
        if match:
            return match.group(1)
        else:
            np.nan


def area(value: str) -> str:
    if isinstance(value,str):
        pattern = r',\s*([^,]+)$'
        match = re.search(pattern,value)
        if match:
            return match.group(1)
        else:
            return np.nan


def local_area(value: str) -> str:
    if isinstance(value,str):
        pattern=r'^(.*?),'
        match = re.search(pattern,value)
        if match:
            return match.group(1)
        else :
            return np.nan


def floor_num(value: str) -> int:
    if isinstance(value,str):
        pattern = r'(\d+)(?:st|nd|rd|th)'
        match = re.search(pattern,value)
        if match:
            if match.group(1)=='Ground':
                num=0
                return int(num)
            else:
                num=match.group(1)
                return int(num)
        else :
            return 0
        

# Transforming the 'others' column from str to list
def roomslist(value: str) -> list:
    if isinstance(value, str):
        # Split the string by commas and strip whitespace from each item
        return [v.strip() for v in value.split(',') ]
    return value


#Luxury score calculation
def ensure_list(x: str) -> list:
    if isinstance(x, str):
        return ast.literal_eval(x)  
    return x


def feature_map(features: list) -> int:
    if not isinstance(features, list):
        return 0

    return sum(feature_points.get(f, 0) for f in features)


# Converting 'overlooking' from string to list
def overlooking(value: str) -> list:
    if isinstance(value, str):
        return [v.strip() for v in value.split(',')]
    

def ageing(value: str) -> str:
    if isinstance(value,str):
        pattern = r'([A-Za-z]{3,9}\s+\d{4})'
        match = re.search(pattern,value)
        if value.startswith('By') or value.startswith('Within') or value=='Under Construction':
            return 'Under Construction'
        
        elif match:
            return 'Under Construction'
        
        elif value=='0 to 1 Year Old':
            return "New"

        elif value == '1 to 5 Year Old':
            return "Relatively New"
        
        elif value == '5 to 10 Year Old':
            return "Relatively Old"
        
        elif value== '10+ Year Old':
            return "Old" 
        
        else :
            return 'Undefined'
        

def clean_location(value: str) -> str:
    if isinstance(value, str):
        return re.sub(r'\s*(East|West)\b', '', value)
    return value


def read_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.drop(['link', 'property_id', 'highlights','description'], axis=1, inplace=True)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    
    df['price']=df['price'].apply(price)

    df['price_per_sqft']=df['price_per_sqft'].apply(price_sqft)

    df['prop_type']=df['location'].apply(prop)

    df['bedrooms']=df['bedrooms'].apply(num_rooms)
    df['bathrooms']=df['bathrooms'].apply(num_rooms)
    df['balcony']=df['balcony'].apply(num_rooms)

    df['location']=df['location'].apply(location)

    df['city']=df['location'].apply(area)

    df['location']=df['location'].apply(local_area)

    df['floor']=df['floor'].apply(floor_num)
    
    return df



def transform_data(df:pd.DataFrame) -> pd.DataFrame:

    df['others'] = df['others'].apply(roomslist)

    #OHE for 'others' column
    unique = set(i for sublist in df['others'] if isinstance(sublist,list) for i in sublist )

    for room in unique:
        df[room] = df['others'].apply(lambda x: int(room in x if isinstance(x, list) else False))

    df['luxury_score'] = df['features_list'].apply(feature_map)

    df['features'] = df['features'].apply(ensure_list)
    df['features_list'] = df['features_list'].apply(ensure_list)

    # Replacing empty features_list with features
    df['features_list'] = df.apply(
        lambda row: row['features'] if len(row['features_list']) == 0 else row['features_list'],
        axis=1
    )

    # Converting 'nearby_locations_list' from string to list
    df['nearby_locations_list'] = df['nearby_locations_list'].apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) else x
    )
        
    df['overlooking'] = df['overlooking'].apply(overlooking)
   
    df['ageing']=df['age'].apply(ageing)

    df['location']=df['location'].apply(clean_location)

    df.drop(columns=['features_list','features','rating_details','age','overlooking','others',
                     'nearby_locations_list','furnish_details_list','gated_community'],inplace=True)
    
    reverse_city_mapping = {}
    for city, areas in city_areas.items():
        for area in areas:
            reverse_city_mapping[area.lower()] = city

    df['city'] = df['city'].str.lower().map(reverse_city_mapping)

    df = df.dropna(subset=["city"])

    df.loc[
        (df['prop_type'] == "Studio Apartments") | (df['prop_type'] == "Independent Builder Floor"),
        'prop_type'
    ] = "Flat"
    
    df = df[~df['prop_type'].isin(['Plot', 'Farm house', 'Serviced Apartment'])]

    reverse_loc_mapping = {}
    for loc, areas in mapping_area.items():
        for area in areas:
            reverse_loc_mapping[area.lower()] = loc

    df['location_area'] = df['location'].str.lower().map(reverse_loc_mapping)

    df.dropna(subset="location_area",inplace=True)
    df.drop(columns=['property_name','rating','location'],inplace=True)

    return df



if __name__ == '__main__':

    current_dir = Path(__file__).parent.parent.parent
    path =current_dir / 'data' / 'raw' / 'raw_data.csv'
    df = read_data(path)
    df = clean_data(df)
    df = transform_data(df)
    output_path = current_dir / 'data' / 'cleaned'/ 'cleaned_data.csv'
    df.to_csv(output_path, index=False)
