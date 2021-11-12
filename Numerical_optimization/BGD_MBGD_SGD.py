from Gradient_descent import GD
import numpy as np 

# Batch GD, Mini-Batch GD and Stochastic GD algorithms Class.
class BGD_MBGD_SGD (GD):
    
    # Train the model
    def fit(self, features, label):    
        # set all of -->(splited_feature, parameters, gradient_history, squared_gradient_history)
        self._setEnviroment(features, label)
        
        # epochs loop
        while(True):
            # mini batch loop
            for x, y_true in self._features_label:
                y_pred = self._hypothsis(x, self._weights)
                self._all_hypothsis.append(y_pred)
                #=======================================================================
                squared_error = self._error(y_pred, y_true) ** 2
                if squared_error.size > 1:
                    self._losses.append(np.mean(squared_error)/2)                        # J = (sum(squared_error)/(2*squared_error.size))
                else:
                    self._losses.append(squared_error[0])  
                #=======================================================================
                gradient_vector = self._gradient(self._error(y_pred, y_true), x)
                self._weights = self._weights - (self._alpha * gradient_vector)
                #=======================================================================
                self._all_bias.append(self._weights[0])
                self._all_weight_1.append(self._weights[1])
                #=======================================================================
                self._rows_iterations += 1
            #=======================================================================        
            if self._stoppingCheck(gradient_vector):
                break
                
        return self._weights, self._losses, self._all_bias, self._all_weight_1, self._all_hypothsis, self._epochs_iterations  