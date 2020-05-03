import pandas as pd
from sodapy import Socrata

client = Socrata("usc.data.socrata.com",None)
dset = "u7m9-48qx"

def get_df(data): # Get a pandas dataframe from a generator object
    "Request the entire dataset through Socrata API generator object"
    dl = []
    [dl.append(d) for d in data]
    return pd.DataFrame(dl)


if __name__=="__main__":
    w_query = str(input('Hello there! Please define youre WHERE query for the USC'
                  ' database to get your dataframe: '))
    print('Thank you! Please wait...')
    data_gen = client.get_all(dset,where=w_query)
    df = get_df(data_gen)
    print(df.head)
    df.to_csv('USC-neighborhood-data-'+w_query+'.csv')
    print('Dataframe exported to csv!')

