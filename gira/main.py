from gira.load_data import load
from gira import preprocess
from gira.plot_map import scatter

def init():
    print('Loading the data')
    df = load()
    print(f'\n{"-" * 25}\n')

    df_cleaned = preprocess.cleaning(df)
    df_transformed = preprocess.processing_columns(df_cleaned)

    # print('Building the map')
    # scatter(df_transformed)
    return df_transformed


if __name__ == '__main__':
    init()
