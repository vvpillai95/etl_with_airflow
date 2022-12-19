import pandas as pd


def get_tables(path):
    tables = pd.read_csv(path,sep=":")
    table = tables.query('to_be_load == "yes"')
    return table