import dill
import os


class Utility:
    def __init__(self) -> None:
        pass
    
    def save_object(file_path,obj):
        
        file_dir=os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        
        
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    