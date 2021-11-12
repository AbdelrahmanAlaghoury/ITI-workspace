from BGD_MBGD_SGD import BGD_MBGD_SGD
from MomentumGD_NAG import MomentumGD_NAG
from Adagrad_RMSProb_Adam import Adagrad_RMSProb_Adam

def LinearRegression(optimiser, batchSize = 0, gamma = 0.5, alpha = 0.001, beta1 = 0.9, beta2=0.999, epsilon = 10e-8, iterations = 0):
    
    if optimiser == 'BGD' or optimiser == 'SGD' or optimiser == 'MBGD':
        return BGD_MBGD_SGD(optimiser, batchSize, gamma, alpha, beta1, beta2, epsilon, iterations)
    
    elif optimiser == 'MomentumGD' or optimiser == 'NAG':
        return MomentumGD_NAG(optimiser, batchSize, gamma, alpha, beta1, beta2, epsilon, iterations)
    
    elif optimiser == 'Adagrad' or optimiser == 'RMSProb' or optimiser == 'Adam':
        return Adagrad_RMSProb_Adam(optimiser, batchSize, gamma, alpha, beta1, beta2, epsilon, iterations)
    
    else:
        print("please Enter a valid algorithm[BGD, MBGD, SGD, MomentumGD, NAG, Adagrad, RMSProb Or Adam]")
