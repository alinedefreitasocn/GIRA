"""
PROBLEMNS TO SOLVE:

Some files are csv and some are xls. Make it automatic on the load
section.
"""


from gira import load_data
from gira import preprocess


if __name__ == '__main__':
    # load data
    df = load_data.load_from_list()
    # clean
    df = preprocess.cleaning(df)
    # feature engineering: creating new columns
    df = preprocess.processing_columns(df)
    # processing data by station
    df = preprocess.process_all_station(df)

    # save
    data_path = '/mnt/d/Dados/FinalProject_GIRA/GIRA/process'
    df.to_csv()
