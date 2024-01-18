import pandas as pd
import os
from dataclasses import dataclass
import re





@dataclass
class DataCleaningconfig:
    datacleaning_obj_file_path=""
    #os.path.join('artifacts',"Data.xlsx")



class DataCleaning:
    def __init__(self) -> None:
        self.datacleaning_config=DataCleaningconfig()
    
    
    def Cleaning(self):
        
        df=pd.read_excel("Data_Train.xlsx")
        df_copy=df.copy()
        
        # renaming duplicates
        df_copy.Destination=df_copy.Destination.replace('New Delhi','Delhi')
        df_copy.Airline=df_copy.Airline.replace({
            'Vistara Premium economy':'Vistara',
            'Jet Airways Business':'Jet Airways',
            'Multiple carriers Premium economy':'Multiple carriers'
        })
            
        # Filled null with mode in Total_Stops column
        df_copy.Total_Stops.fillna(df_copy.Total_Stops.mode()[0],inplace=True)    
        
        df_copy['Stops']=df_copy.Total_Stops.map(lambda x:int(re.findall(r'\D*(\d+)\D*',x)[0]) if len(re.findall(r'\D*(\d+)\D*',x)) else 0)
        
        def modify_duration(duration):
            match=re.findall(r'(?:(\d+)h)?\s*(?:(\d+)m)?',duration)
            hrs= match[0][0] if match[0][0] else 0
            mns= match[0][1] if match[0][1] else 0
            total_hrs=int(hrs)+int(mns)/60
            return total_hrs
    
        df_copy['Duration_hr'] = df_copy.Duration.apply(modify_duration)
        
        
        df_copy['Arrival_Time_hrs']=df_copy.Arrival_Time.map(lambda time: int(re.findall(r'(\d+):(\d+)',time)[0][0]))
        df_copy['Dep_Time_hrs']=df_copy.Dep_Time.map(lambda time: int(re.findall(r'(\d+):(\d+)',time)[0][0]))
        
        
        df_copy.Date_of_Journey=pd.DatetimeIndex(df_copy.Date_of_Journey,dayfirst=True)
        df_copy['Day']=df_copy.Date_of_Journey.dt.day
        df_copy['Month']=df_copy.Date_of_Journey.dt.month_name()
        df_copy['Week']=df_copy.Date_of_Journey.dt.day_name()
        
        label=['morning','noon','after noon','evening','night']
        bin=[0,11,12,15,18,24]
        df_copy['Arrival_Time']=pd.cut(df_copy.Arrival_Time_hrs,bins=bin,labels=label,include_lowest=True)
        df_copy['Dep_Time']=pd.cut(df_copy.Dep_Time_hrs,bins=bin,labels=label,include_lowest=True)
        
        df_copy.drop(columns=['Duration','Total_Stops','Additional_Info','Date_of_Journey','Route','Arrival_Time_hrs','Dep_Time_hrs'],inplace=True)
        
        df_eda=df_copy.copy()
        
        return df_eda
    
    
    def Preprocessing(self):
        pass
        
        
        
            
            
 
        