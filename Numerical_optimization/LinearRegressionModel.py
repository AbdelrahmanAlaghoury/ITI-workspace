from BGD_MBGD_SGD import BGD_MBGD_SGD
from MomentumGD_NAG import MomentumGD_NAG
from Adagrad_RMSProb_Adam import Adagrad_RMSProb_Adam

def LinearRegression(algorithm, batchSize = 0, gamma = 0.5, alpha = 0.001, beta1 = 0.9, beta2=0.999, epsilon = 10e-8, iterations = 0):
    
    if algorithm == 'BGD' or algorithm == 'SGD' or algorithm == 'MBGD':
        return BGD_MBGD_SGD(algorithm, batchSize, gamma, alpha, beta1, beta2, epsilon, iterations)
    
    elif algorithm == 'MomentumGD' or algorithm == 'NAG':
        return MomentumGD_NAG(algorithm, batchSize, gamma, alpha, beta1, beta2, epsilon, iterations)
    
    elif algorithm == 'Adagrad' or algorithm == 'RMSProb' or algorithm == 'Adam':
        return Adagrad_RMSProb_Adam(algorithm, batchSize, gamma, alpha, beta1, beta2, epsilon, iterations)
    
    else:
        print("please Enter a valid algorithm[BGD, MBGD, SGD, MomentumGD, NAG, Adagrad, RMSProb Or Adam]")
