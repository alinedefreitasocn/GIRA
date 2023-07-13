import pandas as pd
import os

def list_files():
    """
    Function just list the files available in the path
    """
    data_path = '/mnt/d/Dados/FinalProject_GIRA/GIRA/raw'
    return data_path, os.listdir(data_path)

def load(data_path, file) -> pd.DataFrame:
    """
    Function read the file from the path when path and file name are given
    """
    if 'xls' in file:
        """
        Name of the columns are different on this one
        Index(['desigcomercial', 'numbicicletas', 'numbicicletas__1', 'numdocasvacias',
            'position', 'entity_ts'],
        dtype='object')

        while csv files are
        Index(['desigcomercial', 'numbicicletas', 'numdocas', 'position', 'entity_ts',
        'estado'],
            dtype='object')

        So we should ignore the columns 'numbicicletas__1'
        """
        df = pd.read_excel(os.path.join(data_path, file),
                    parse_dates=['entity_ts'], usecols=['desigcomercial',
                                                        'numbicicletas',
                                                        'numdocasvacias',
                                                        'position',
                                                        'entity_ts'])
        # renaming the column to be equal to the csv file
        df['numdocas'] = df['numbicicletas'] + df['numdocasvacias']
        df.drop(columns='numdocasvacias')
        # .rename(columns={'numdocasvacias':'numdocas'}, inplace=True)
    elif 'csv' in file:
        df = pd.read_csv(os.path.join(data_path, file),
                        parse_dates=['entity_ts'],
                        usecols=['desigcomercial',
                                'numbicicletas',
                                'numdocas',
                                'position',
                                'entity_ts'])
    else:
        print('Invalid file format')
        df = None
    return df

def load_from_list() -> pd.DataFrame:
    '''
    Load a dataset from a list of files. Uses the previous functions
    list_files and load

    ---
    Return: DataFrame

    '''
    data_path, entries = list_files()

    for count, item in enumerate(entries):
        print(count, item)
    file = int(input('Which file do you want to load (only number)? '))
    # file = entries[0]
    print(f'Opening file {entries[file]}')

    # reading one of the files: 6 month of 2022
    df = load(data_path, entries[file])
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
