import pandas as pd
import os

def load() -> pd.DataFrame:
    '''
    Load a dataset from a list of files

    ---
    Return: DataFrame

    '''
    data_path = '/mnt/d/Dados/FinalProject_GIRA/GIRA'
    entries = os.listdir(data_path)

    for count, item in enumerate(entries):
        print(count, item)
    file = int(input('Which file do you want to load (only number)? '))
    # file = entries[0]
    print(f'Opening file {entries[file]}')

    # reading one of the files: 6 month of 2022
    df = pd.read_csv(os.path.join(data_path, entries[file]),
                    parse_dates=['entity_ts'])
    return df

def save_sample() -> None:
    '''
    Load the dataset using the previoous function load()
    and save a smaller version for testing

    Return: None
    '''
    df = load()

    # selecting just one month to use during test
    # df_sample = df[df['entity_ts'].month]
    df_sample = df[df['entity_ts'].dt.month == 7]
    data_path = '/home/aline/code/personal_projects/GIRA/data'
    print(f'Saving sample file to {data_path}')
    df_sample.to_csv(os.path.join(data_path, 'gira_frame_sample.csv'),
                     index=False)

def load_sample() -> pd.DataFrame:
    '''
    Load the sample file of one month only for testing

    ---
    Return: sample df of july 2022
    '''
    data_path = '/home/aline/code/personal_projects/GIRA/data'
    file = 'gira_frame_sample.csv'

    df = pd.read_csv(os.path.join(data_path, file),
                    parse_dates=['entity_ts'])
    return df
