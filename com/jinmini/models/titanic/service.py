from com.jinmini.models.titanic.dataset import Dataset
import pandas as pd 

class Service:
    
    dataset = Dataset()
    def new_model(self, fname) -> object:
        this = self.dataset 
        this.context = 'C:\\Users\\bitcamp\\Documents\\2025\\25ep_python(esg)\\Titanic250207\\com\\jinmini\\datas\\taitanics_datas\\'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)

     





