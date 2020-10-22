from .utils import get_sdf
import pandas as pd
import json

class ArcTable:
    """
    This is the main Layer class. (example)

    Parameters
    ----------
    id_hash: int
        An ID hash.
    attributes: dic
        A dictionary holding the attributes of a dataset.
    server: str
        A string of the server URL.
    """
    def __init__(self, server=None, data_table=None, creds=None):
        "How do we initialise an instance of the class?"
        if not all([server, data_table, creds]):
            print('Error. Missing requirements')
            return None

        self.attributes = {
            'server': server,
            'table': data_table
        }
        
        self.data = get_sdf(server, data_table, creds)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"<Class ArcTable> {self.attributes['table']}"

    def to_df(self, orient=None):
        """
        Converts to Pandas dataframe
        Params
        """
        data = json.dumps(self.data)
        if orient:
            df = pd.read_json(data)
        else:
            df = pd.read_json(data, orient=orient)

        return df

        



