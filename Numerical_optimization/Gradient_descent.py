import numpy as np 

# GD Class.
class GD():

    # GD algorithm base functions
    _error = lambda self, y_pred, y_true: y_pred - y_true  # (y_pred - y_true)
    _hypothsis = lambda self, x_values, weights: x_values @ weights
    _gradient = lambda self, error, x_values: ((error.reshape(1,-1) @ x_values)/error.size).reshape(-1,1)
    _divide_chunks = lambda self, x_values, chunkSize: (x_values[i: i+chunkSize] for i in range(0, x_values.shape[0], chunkSize))
    
    def __init__(self, algorithm, batchSize = 0, gamma = 0.5, alpha = 0.001, beta1 = 0.9, beta2=0.998, epsilon = 10e-8, epochs = 0):
        self._algorithm = algorithm
        self._batchSize = batchSize
        self._gamma = gamma
        self._alpha = alpha
        self._beta1 = beta1
        self._beta2 = beta2
        self._epsilon = epsilon
        self._epochs = epochs
    
    def _setEnviroment (self, features, label):
        # returned variables 
        self._rows_iterations = 1
        self._epochs_iterations = 1
        self._losses = []
        self._all_bias = []
        self._all_weight_1 = []
        self._all_hypothsis = []
        self._features_rows_number = features.shape[0]
        
        if self._batchSize <= 0:
            self._batchSize = features.shape[0]
        
        # split the features based on batch size
        self._splited_features = [np.array(list(f)) for f in self._divide_chunks(features, self._batchSize)]
        
        # split the features based on batch size
        self._splited_label = [np.array(list(l)) for l in self._divide_chunks(label, self._batchSize)]
        
        # make a list of the mini batches to be used later
        self._features_label = list(zip(self._splited_features, self._splited_label))
        
        # initialize prameters
        self._weights = np.zeros((features.shape[1], 1)).reshape(-1,1) 
        
        # initialize gradient history
        self._vect_momentum = np.zeros((features.shape[1], 1)).reshape(-1,1)  
                
        # initialize squared gradient history (adaptive learning rate)
        self._vect_vt = np.zeros((features.shape[1], 1)).reshape(-1,1)   
    
    def _stoppingCheck(self, gradient_vector): 
        # increment epochs number
        self._epochs_iterations += 1 
        
        # to make sure that we will shuffle the data between epochs in case of SGD or MBGD
        if self._batchSize < self._features_rows_number:
            np.random.shuffle(self._features_label)

        # check stopping conditions one by one
        #=================================================================================================
        
        # 1st stopping condtion -> epochs number are been enterd >> Note: epochs equal to zero by default
        if(self._epochs_iterations == self._epochs):                       
            print("Gradient Vector \n", gradient_vector)
            print (f"Iterations Number = {self._rows_iterations}")
            print (f"Epochs Number = {self._epochs_iterations}")
            return True
                
        # 2nd stopping condtion -> new thetas doesn't affect the cost function any more
        if(self._rows_iterations > 2):                                
            if(abs(np.round(self._losses[-1] - self._losses[-2], 5)) == 0):
                print(f"cost[-1] = {self._losses[-1]} And cost[-2] = {self._losses[-2]}")
                print (f"Iterations Number = {self._rows_iterations}")
                print (f"Epochs Number = {self._epochs_iterations}")
                return True
            
        # 3rd stopping condtion -> gradient equals to zero       
        if((sum((np.round(abs(gradient_vector), 3) != 0)) == 0)):              
            print(">>Gradient Vector \n", gradient_vector)
            print (f"Iterations Number = {self._rows_iterations}")
            print (f"Epochs Number = {self._epochs_iterations}")
            return True
        return False
    
    def fit(self, features, label):
        pass
        
    def predict(self, features):
        # return predicted value
        return self._hypothsis(features, self._weights)