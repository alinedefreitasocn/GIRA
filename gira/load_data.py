import pandas as pd
import os

def load():
    data_path = '/mnt/d/Dados/FinalProject_GIRA/GIRA'
    entries = os.listdir(data_path)

    # reading one of the files: 6 month of 2022
    df = pd.read_csv(os.path.join(data_path, entries[0]),
                    parse_dates=['entity_ts'])
    return df
