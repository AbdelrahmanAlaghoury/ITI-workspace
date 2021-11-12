from Gradient_descent import GD
import numpy as np

# Momentum GD and NAG algorithms Class.
class MomentumGD_NAG (GD):
    
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
                if self._algorithm == 'MomentumGD':
                    gradient_vector = self._gradient(self._error(y_pred, y_true), x)
                    self._vect_vt = (self._gamma * self._vect_vt) + (self._alpha * gradient_vector)
                    self._weights = self._weights - self._vect_vt
                
                elif self._algorithm == 'NAG':
                    # history update
                    weights_temp = self._weights - (self._gamma * self._vect_vt)
                    y_pred_temp = self._hypothsis(x, weights_temp)
                    # check the gradient direction
                    gradient_vector = self._gradient(self._error(y_pred_temp, y_true), x)    
                    self._weights = weights_temp - (self._alpha * gradient_vector)
                    self._vect_vt = (self._gamma * self._vect_vt) + (self._alpha * gradient_vector)
                #=======================================================================
                self._all_bias.append(self._weights[0])
                self._all_weight_1.append(self._weights[1])
                #=======================================================================
                self._rows_iterations += 1
            #=======================================================================        
            if self._stoppingCheck(gradient_vector):
                break
                
        return self._weights, self._losses, self._all_bias, self._all_weight_1, self._all_hypothsis, self._epochs_iterations      
