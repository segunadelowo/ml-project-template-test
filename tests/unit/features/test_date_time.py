import pandas as pd
import pytest
import src.features.date_time


@pytest.fixture
def dummy_df():
    string_col = ['Futrelle, Mme. Jacques Heath (Lily May Peel)',
                  'Johnston, Ms. Catherine Helen "Carrie"',
                  'Sloper, Mr. William Thompson',
                  'Ostby, Lady. Engelhart Cornelius',
                  'Backstrom, Major. Karl Alfred (Maria Mathilda Gustafsson)']
    df_dict = {'string': string_col}
    df = pd.DataFrame(df_dict)
    return df