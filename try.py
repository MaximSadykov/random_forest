import pandas as pd
def jopa(path):
    df= pd.read(path)
    return df.shape
