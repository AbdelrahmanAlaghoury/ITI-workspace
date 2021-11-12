from Gradient_descent import GD
import numpy as np

# Momentum GD and NAG algorithms Class.
class Adagrad_RMSProb_Adam (GD):
    
    # Train the model
    def fit(self, features, label):    
        # set all of -->(splited_feature, parameters, gradient_history, squared_gradient_history)
        self._setEnviroment(features, label)

        # epochs loop
        while(True):
            #mini batch loop
            for x, y_true in self._features_label :
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
                
                if self._algorithm == 'Adagrad':
                    self._vect_vt = self._vect_vt + gradient_vector**2
                    self._weights = self._weights - ((self._alpha * gradient_vector) / (np.sqrt(self._vect_vt) + self._epsilon))
                
                elif self._algorithm == 'RMSProb':
                    self._vect_vt = (self._beta2 * self._vect_vt) + ((1 - self._beta2) * gradient_vector**2)
                    self._weights = self._weights - ((self._alpha * gradient_vector) / (np.sqrt(self._vect_vt) + self._epsilon))
                 
                elif self._algorithm == 'Adam':
                    self._vect_momentum = (self._beta1 * self._vect_momentum) + ((1 - self._beta1) * gradient_vector)
                    vect_momentum_hat = self._vect_momentum / (1 - self._beta1 ** self._rows_iterations)
                    
                    self._vect_vt = (self._beta2 * self._vect_vt) + ((1 - self._beta2) * gradient_vector**2)
                    vect_vt_hat = self._vect_vt / (1 - self._beta2 ** self._rows_iterations)
                    
                    self._weights = self._weights - ((self._alpha * vect_momentum_hat) / (np.sqrt(vect_vt_hat) + self._epsilon))
                #=======================================================================
                self._all_bias.append(self._weights[0])
                self._all_weight_1.append(self._weights[1])
                #=======================================================================
                self._rows_iterations += 1
            #=======================================================================        
            if self._stoppingCheck(gradient_vector):
                break
                
        return self._weights, self._losses, self._all_bias, self._all_weight_1, self._all_hypothsis, self._epochs_iterations      


