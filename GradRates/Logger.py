#!/usr/bin/env python
# coding: utf-8

# In[55]:


import copy
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split


# In[56]:


class Logger():
    
    def __init__(self, hyperparam_dict):
        
        self.model = None
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None
        self.y_pred = None
        self.y_train_pred = None
        
        self.hyperparams = hyperparam_dict
        self.saved = None
    
    def save_log(self, notes:str):
        self.hyperparams["model"] = self.model
        self.hyperparams["notes"] = notes
        self.saved = self.hyperparams
            
    def train_update(self, model, X, y):
        
        self.model = model
        
        self.x_train, self.x_test, self.y_train, self.y_test = \
            train_test_split(X, y, test_size=0.15, random_state=0)
        
        model.fit(self.x_train, self.y_train)
        
        self.y_pred = model.predict(self.x_test)
        self.y_train_pred = model.predict(self.x_train)
        
    def record(self):
        return copy.deepcopy(self.saved)
 


# In[ ]:


class RegressionLogger(Logger):
    def __init__(self, hyperparam_dict):
        super().__init__(hyperparam_dict)
        
        self.rsquared = None
        self.rmse = None
        self.mse = None
        self.mae = None
        
        self.train_rsquared = None
        self.train_rmse = None
        self.train_mse = None
        self.train_mae = None
        
    def train_update(self, model, X, y):
        super().train_update(self, model, X, y)
        
        self.rsquared = r2_score(self.y_test, self.y_pred)
        self.rmse = np.sqrt(mean_squared_error(self.y_pred, self.y_test))
        self.mse = mean_squared_error(self.y_pred, self.y_test)
        self.mae = mean_absolute_error(self.y_pred, self.y_test)
        
        self.train_rsquared = r2_score(self.y_test, self.y_pred)
        self.train_rmse = np.sqrt(mean_squared_error(self.y_train_pred, self.y_train))
        self.mse = mean_squared_error(self.y_train_pred, self.y_train)
        self.mae = mean_absolute_error(self.y_train_pred, self.y_train)
            
        

