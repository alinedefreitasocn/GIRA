import pandas as pd
import numpy as np


def cleaning(df:pd.DataFrame):

    # first of all, drop duplicates
    df = df.copy()
    df.drop_duplicates(inplace=True)

    return df


def processing_columns(df:pd.DataFrame):
    # for station id
    df = df.copy()

    print('Extracting the station name')
    df['station_name'] = df['desigcomercial'].str.split('-').str[1]
    df['stationID']=df['desigcomercial'].str.extract(r'(\d{3})')
    print(f'\n{"-" * 25}\n')

    print('Setting the station ID as an integer')
    df['stationID'] = df['stationID'].astype(int)
    print(f'\n{"-" * 25}\n')

    print('Extracting geographical position')
    df['lon'] = df['position'].str.extract(r'(-[0-9]+.[0-9]+),[0-9]+.[0-9]+').astype(float)
    df['lat'] = df['position'].str.extract(r'-[0-9]+.[0-9]+,([0-9]+.[0-9]+)').astype(float)
    print(f'\n{"-" * 25}\n')

    print('Dropping the columns position and designcomercial')
    df.drop(columns=['desigcomercial', 'position'], inplace=True)
    print(f'\n{"-" * 25}\n')

    print('Sorting values by station ID and datetime')
    df_sorted = df.sort_values(by=['stationID', 'entity_ts'])
    print(f'\n{"-" * 25}\n')

    # one problem: The step time shoul be calculated for every station. If
    # done for the whole df will have a huge step time at the beginning
    # TODO how to solve it?? Append the df for every station number?
    # or just change the time? Can change the negative values for zero.
    print('Calculating the time step')
    df_sorted['diff_time'] = df_sorted['entity_ts'].diff().replace({pd.NaT: pd.Timedelta("0 days")})
    df_sorted['total_seconds'] = df_sorted['diff_time'].apply(lambda x: int(x.total_seconds()))
    print(f'\n{"-" * 25}\n')

    print('Setting the time column as index')
    # how do we sample the time? every hour: what to do with the 20 secs
    # records? the gaps we can fill with bfill
    # bfill() is used to backward fill the missing values in the dataset.
    # It will backward fill the NaN values that are present in the pandas
    # dataframe. ffill() function is used forward fill the
    # missing value in the dataframe.
    # it also need to be done throught the station values otherwise will mix
    # with the next station record causing inconstancy
    df_sorted.set_index('entity_ts',
                 inplace=True)
    print(f'\n{"-" * 25}\n')

    print('Calculating the diff in the n. bike column')
    df_sorted['bike_taken'] = df_sorted['numbicicletas'].diff().fillna(0)
    print(f'\n{"-" * 25}\n')
    print('Preprocess completed! ')

    return df_sorted
