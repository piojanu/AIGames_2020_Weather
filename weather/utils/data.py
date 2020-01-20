import glob
import os.path

import pandas as pd


def parse_core_to_pandas(path):
    """Weather Core Dataset parser.

    Args:
        path (string): Path to a directory containing .csv files.

    Returns:
        pandas.DataFrame with MultiIndex([station_id, timestamp]) and parameter
        indices as columns.
    """

    dfs = []
    for file_path in glob.glob(os.path.join(path, 'B*.csv')):
        df = pd.read_csv(file_path,
                         delimiter=';',
                         decimal=",",
                         usecols=range(4),
                         names=['station_id', 'param_id', 'timestamp', 'value'],
                         dtype={'station_id': str,
                                'param_id': str,
                                'timestamp': str,
                                'value': float})
        dfs.append(df)

    df = pd.concat(dfs)
    df = df.pivot_table(index=['station_id', 'timestamp'],
                        columns='param_id',
                        values='value')
    return df


if __name__ == "__main__":
    df = parse_core_to_pandas('./data/train_data')
