import dill
import os
import pandas as pd


class Utility:
    def __init__(self) -> None:
        pass
    
    def save_object(self,file_path,obj):
        
        file_dir=os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        
        
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
            
    def converttodf(self,df_dict):
        df_dict_list=list(df_dict)
        df=pd.DataFrame()
        for i in df_dict_list:
            df = pd.concat([df, pd.DataFrame(df_dict[i])], ignore_index=True)

        return df
            

    