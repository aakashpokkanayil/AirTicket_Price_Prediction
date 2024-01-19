from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
import numpy as np
import pandas as pd



class ModelEvaluation:
    def __init__(self) -> None:
        pass
    
    def Evaluate(self,x_train,x_test,y_train,y_test,models):
        report={}
        model_list=list(models)
        for i in range(len(models)):
            model=models[model_list[i]]
            
            model.fit(x_train,y_train)
            
            pred_train_y=model.predict(x_train)
            pred_test_y=model.predict(x_test)
            
            
            report[model_list[i]]={
                
                'Model_name':model_list[i],
                
                'MSE_Test':mean_squared_error(y_true=y_test,y_pred=pred_test_y),
                'MSE_Train':mean_squared_error(y_true=y_train,y_pred=pred_train_y),
                
                'RMSE_Test':np.sqrt(mean_squared_error(y_true=y_test,y_pred=pred_test_y)),
                'RMSE_Train':np.sqrt(mean_squared_error(y_true=y_train,y_pred=pred_train_y)),
                
                'MAE_Test':mean_absolute_error(y_true=y_test,y_pred=pred_test_y),
                'MAE_Train':mean_absolute_error(y_true=y_train,y_pred=pred_train_y),
                
                'R2_Score_Test':r2_score(y_true=y_test,y_pred=pred_test_y),
                'R2_Score_Train':r2_score(y_true=y_train,y_pred=pred_train_y)
                
                
                }
            return report
            
        
        
        