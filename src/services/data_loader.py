import os 
import pandas as pd

def excel_loader(file_path):
    """
    Loads an Excel file into a Pandas DataFrame.
    """

    sheet_name = 'Financial Analysis'
    print(f"Current working directory ${os.getcwd()}")
    df = pd.read_excel(
    file_path,    # name of excel sheet
    sheet_name = sheet_name, # name of sheet
    # index_col = 2, # column to use as index
    skiprows=[0,1,3,4,5,6],   # list of emptry rows you want to omit at the beginning
    ) 
    
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]  
    # print(df.head())
    
    return df
    


class data_loader():
    """
    Loads data from a csv file into a panda dataframe.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = excel_loader(self.file_path)

    def get_data(self):
        return self.data

    def get_equities(self):
        """
        Returns a list of equities.
        """
        return self.data.index.values.tolist()
    
    
    