#!/usr/bin/env python
# coding: utf-8

# In[55]:


import copy
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.base import TransformerMixin, BaseEstimator

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
    
    def save_log(self, notes:str):
        self.hyperparams["model"] = self.model
        self.hyperparams["notes"] = notes
            
    def train_update(self, model, X, y):
        
        self.x_train, self.x_test, self.y_train, self.y_test = \
            train_test_split(X, y, test_size=0.05, random_state=0)
        
        model.fit(self.x_train, self.y_train)
        
        self.y_pred = model.predict(self.x_test)
        self.y_train_pred = model.predict(self.x_train)
        
    def train_holdout(self, model, x_train, x_test, y_train, y_test):
        
        self.x_train, self.x_test, self.y_train, self.y_test = x_train, x_test, y_train, y_test
        model.fit(self.x_train, self.y_train)
        
        self.y_pred = model.predict(self.x_test)
        self.y_train_pred = model.predict(self.x_train)
    
    def get_residuals(self):
        
        return self.y_pred - self.y_test
        
        
    def record(self):
        return copy.deepcopy(self.hyperparams)
    
    
 


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
    
    def set_results(self, suffix):
        self.rsquared = r2_score(self.y_test, self.y_pred)
        self.rmse = np.sqrt(mean_squared_error(self.y_pred, self.y_test))
        self.mse = mean_squared_error(self.y_pred, self.y_test)
        self.mae = mean_absolute_error(self.y_pred, self.y_test)
        
        self.train_rsquared = r2_score(self.y_train, self.y_train_pred)
        self.train_rmse = np.sqrt(mean_squared_error(self.y_train_pred, self.y_train))
        self.train_mse = mean_squared_error(self.y_train_pred, self.y_train)
        self.train_mae = mean_absolute_error(self.y_train_pred, self.y_train)

        self.hyperparams["rsquared" + suffix] = self.rsquared
        self.hyperparams["rmse" + suffix] = self.rmse
        self.hyperparams["mae" + suffix] = self.mae

        self.hyperparams["train_rsquared" + suffix] = self.train_rsquared
        self.hyperparams["train_rmse" + suffix] = self.train_rmse
        self.hyperparams["train_mae" + suffix] = self.train_mae
        
    def train_update(self, model, X, y, suffix=""):
        super().train_update(model, X, y)
        self.model = model
        
        self.set_results(suffix)
        
    
        
        
    
    def train_holdout(self,model, x_train, x_test, y_train, y_test, suffix=""):
        super().train_holdout(model, x_train, x_test, y_train, y_test)
        self.set_results(suffix)
            
class FuncTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self):
        return self
    
    def transform(self, X, y=None):
        return X
        
    def log_transform(self, X, column):
        col = X[:, column]
        return np.log(col)
        
    
    def exp_transform(self, X, column):
        col = X[:, log_transformed]
        return np.exp(col)
        
    
    def poly_transform(self, X, y, column, degree):
        col = X[:, column]
        p1 = np.polyfit(col, y, degree)
        return np.polyval(p1, col)
        
    
    def recip_transform(self, X, column):
        col = X[:, column]
        return 1 / col
        
class ColSelect(BaseEstimator, TransformerMixin):
    
    def __init__(self, cols):
        self.columns = cols
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X[self.cols]       

