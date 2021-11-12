from LinearModel import LinearRegression
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.metrics import r2_score

class model_test():
    def __init__(self):
        pass

    def BGD_test(self):
        print("====================BGD====================")
        x = np.linspace(0,20)
        np_x = np.array(x).reshape(-1,1)
        np_y = -2*np_x + 1
        features = np.ones((x.size,1))
        features = np.append(features, np_x, axis=1)
        batchSize = np_x.shape[0]
        #=======================================================================
        model = LinearRegression('BGD', batchSize, alpha = 0.01)
        weights, losses, bias, weight_1, all_hypothsis, epochs_iterations = model.fit(features, np_y)
        y_pred = model.predict(features)
        print(f"R2 Score = {r2_score(np_y, y_pred)}")
        print("=================================================================")
        plt.plot(np_x, np_y)
        plt.title("x_values vs y_true")
        plt.show()
        print("=================================================================")
        plt.plot(np.arange(epochs_iterations-1).reshape(-1,1), np.array(losses).reshape(-1,1))
        plt.title("Epochs vs Losses")
        plt.show()
        print("=================================================================")
        plt.plot(bias, losses)
        plt.title("Bias vs Losses")
        plt.show()
        print("=================================================================")
        plt.plot(weight_1, losses)
        plt.title("Weight_1 vs Losses")
        plt.show()
        print("=================================================================")
        for y in np.array(all_hypothsis):
            plt.plot(np_x, y)
        plt.title("All Hypothsis")
        plt.show()
        print("=================================================================")
        plt.plot(np_x, y_pred)
        plt.title("The best reggression line")
        plt.show()
        print("=================================================================")
        print("=================================================================")

    def MBGD_test(self):
        print("====================MBGD====================")
        def divide_chunks(x_values, chunkSize): 
            # looping till length x_values_rows
            for i in range(0, len(x_values), chunkSize): 
                yield x_values[i:i + chunkSize]
        #=======================================================================
        x = np.linspace(0,20)
        np_x = np.array(x).reshape(-1,1)
        np_y = -2*np_x + 1
        features = np.ones((x.size,1))
        features = np.append(features, np_x, axis=1)
        batchSize = 5
        # to be used in plotting vs each batch of the data
        np_x_splited = [np.array(list(j)) for j in divide_chunks(np_x, batchSize)]
        #=======================================================================
        model = LinearRegression('MBGD', batchSize, alpha = 0.008)
        weights, losses, bias, weight_1, all_hypothsis, epochs_iterations = model.fit(features, np_y)
        y_pred = model.predict(features)
        print(f"R2 Score = {r2_score(np_y, y_pred)}")
        print("=================================================================")
        plt.plot(np_x, np_y)
        plt.title("x_values vs y_true")
        plt.show()
        print("=================================================================")
        plt.plot(np.arange(len(losses)).reshape(-1,1), np.array(losses).reshape(-1,1))
        plt.title("Epochs vs Losses")
        plt.show()
        print("=================================================================")
        plt.plot(bias, losses)
        plt.title("Bias vs Losses")
        plt.show()
        print("=================================================================")
        plt.plot(weight_1, losses)
        plt.title("Weight_1 vs Losses")
        plt.show()
        print("=================================================================")
        for x, y in zip(np_x_splited, all_hypothsis):
            plt.plot(x, y)
        plt.title("All Hypothsis")
        plt.show()
        print("=================================================================")
        plt.plot(np_x, y_pred)
        plt.title("The best reggression line")
        plt.show()
        print("=================================================================")
        print("=================================================================")

    def SGD_test(self):
        print("====================SGD====================")
        def divide_chunks(x_values, chunkSize): 
            # looping till length x_values_rows
            for i in range(0, len(x_values), chunkSize): 
                yield x_values[i:i + chunkSize]
        #=======================================================================
        x = np.linspace(0,20)
        np_x = np.array(x).reshape(-1,1)
        np_y = -2*np_x + 1
        features = np.ones((x.size,1))
        features = np.append(features, np_x, axis=1)
        batchSize = 1
        # to be used in plotting vs each batch of the data
        np_x_splited = [np.array(list(j)) for j in divide_chunks(np_x,batchSize)]
        #=======================================================================
        model = LinearRegression('SGD', batchSize, alpha = 0.007)
        weights, losses, bias, weight_1, all_hypothsis, epochs_iterations = model.fit(features, np_y)
        y_pred = model.predict(features)
        print(f"R2 Score = {r2_score(np_y, y_pred)}")
        print("=================================================================")
        plt.plot(np_x, np_y)
        plt.title("x_values vs y_true")
        plt.show()
        print("=================================================================")
        plt.plot(np.arange(len(losses)).reshape(-1,1), np.array(losses).reshape(-1,1))
        plt.title("Epochs vs Losses")
        plt.show()
        print("=================================================================")
        plt.plot(bias, losses)
        plt.title("Bias vs Losses")
        plt.show()
        print("=================================================================")
        plt.plot(weight_1, losses)
        plt.title("Weight_1 vs Losses")
        plt.show()
        print("=================================================================")
        for x, y in zip(np_x_splited, all_hypothsis):
            plt.scatter(x, y)
        plt.title("All Hypothsis")
        plt.show()
        print("=================================================================")
        plt.plot(np_x, y_pred)
        plt.title("The best reggression line")
        plt.show()
        print("=================================================================")
        print("=================================================================")

    def MomentumGD_test(self):
        print("====================MomentumGD====================")
        x = np.linspace(0,20)
        np_x = np.array(x).reshape(-1,1)
        np_y = -2*np_x + 1
        features = np.ones((x.size,1))
        features = np.append(features, np_x, axis=1)
        batchSize = 1
        #=======================================================================
        model = LinearRegression('MomentumGD', batchSize, alpha = 0.009, gamma = 0.5)
        weights, losses, bias, weight_1, all_hypothsis, epochs_iterations = model.fit(features, np_y)
        y_pred = model.predict(features)
        print(f"R2 Score = {r2_score(np_y, y_pred)}")
        print("=================================================================")
        plt.plot(np_x, np_y)
        plt.title("x_values vs y_true")
        plt.show()
        print("=================================================================")
        plt.plot(np.arange(len(losses)).reshape(-1,1), np.array(losses).reshape(-1,1))
        # plt.plot(np.arange(epochs_iterations-1).reshape(-1,1), np.array(losses).reshape(-1,1))
        plt.title("Epochs vs Losses")
        plt.show()
        print("=================================================================")
        plt.plot(bias, losses)
        plt.title("Bias vs Losses")
        plt.show()
        print("=================================================================")
        plt.plot(weight_1, losses)
        plt.title("Weight_1 vs Losses")
        plt.show()
        print("=================================================================")
        # for y in np.array(all_hypothsis):
        #     plt.plot(np_x, y)
        # plt.title("All Hypothsis")
        # plt.show()
        print("=================================================================")
        plt.plot(np_x, y_pred)
        plt.title("The best reggression line")
        plt.show()
        print("=================================================================")
        print("=================================================================")

    def NAG_test(self):
        print("====================NAG====================")
        x = np.linspace(0,20)
        np_x = np.array(x).reshape(-1,1)
        np_y = -2*np_x + 1
        features = np.ones((x.size,1))
        features = np.append(features, np_x, axis=1)
        batchSize = np_x.shape[0]
        #=======================================================================
        model = LinearRegression('NAG', batchSize, alpha = 0.009, gamma = 0.5)
        weights, losses, bias, weight_1, all_hypothsis, epochs_iterations = model.fit(features, np_y)
        y_pred = model.predict(features)
        print(f"R2 Score = {r2_score(np_y, y_pred)}")
        print("=================================================================")
        plt.plot(np_x, np_y)
        plt.title("x_values vs y_true")
        plt.show()
        print("=================================================================")
        plt.plot(np.arange(epochs_iterations-1).reshape(-1,1), np.array(losses).reshape(-1,1))
        plt.title("Epochs vs Losses")
        plt.show()
        print("=================================================================")
        plt.plot(bias, losses)
        plt.title("Bias vs Losses")
        plt.show()
        print("=================================================================")
        plt.plot(weight_1, losses)
        plt.title("Weight_1 vs Losses")
        plt.show()
        print("=================================================================")
        for y in np.array(all_hypothsis):
            plt.plot(np_x, y)
        plt.title("All Hypothsis")
        plt.show()
        print("=================================================================")
        plt.plot(np_x, y_pred)
        plt.title("The best reggression line")
        plt.show()
        print("=================================================================")
        print("=================================================================")

    def Adagrad_test(self):
        print("====================Adagrad====================")
        x = np.linspace(0,20)
        np_x = np.array(x).reshape(-1,1)
        np_y = -2*np_x + 1
        features = np.ones((x.size,1))
        features = np.append(features, np_x, axis=1)
        batchSize = np_x.shape[0]
        #=======================================================================
        model = LinearRegression('Adagrad', batchSize, alpha = 0.8)
        weights, losses, bias, weight_1, all_hypothsis, epochs_iterations = model.fit(features, np_y)
        y_pred = model.predict(features)
        print(f"R2 Score = {r2_score(np_y, y_pred)}")
        print("=================================================================")
        plt.plot(np_x, np_y)
        plt.title("x_values vs y_true")
        plt.show()
        print("=================================================================")
        plt.plot(np.arange(epochs_iterations-1).reshape(-1,1), np.array(losses).reshape(-1,1))
        plt.title("Epochs vs Losses")
        plt.show()
        print("=================================================================")
        plt.plot(bias, losses)
        plt.title("Bias vs Losses")
        plt.show()
        print("=================================================================")
        plt.plot(weight_1, losses)
        plt.title("Weight_1 vs Losses")
        plt.show()
        print("=================================================================")
        for y in np.array(all_hypothsis):
            plt.plot(np_x, y)
        plt.title("All Hypothsis")
        plt.show()
        print("=================================================================")
        plt.plot(np_x, y_pred)
        plt.title("The best reggression line")
        plt.show()
        print("=================================================================")
        print("=================================================================")

    def RMSProb_test(self):
        print("====================RMSProb====================")
        x = np.linspace(0,20)
        np_x = np.array(x).reshape(-1,1)
        np_y = -2*np_x + 1
        features = np.ones((x.size,1))
        features = np.append(features, np_x, axis=1)
        batchSize = np_x.shape[0]
        #=======================================================================
        model = LinearRegression('RMSProb', batchSize, beta2 = 0.98, alpha = 0.25)
        weights, losses, bias, weight_1, all_hypothsis, epochs_iterations = model.fit(features, np_y)
        y_pred = model.predict(features)
        print(f"R2 Score = {r2_score(np_y, y_pred)}")
        print("=================================================================")
        plt.plot(np_x, np_y)
        plt.title("x_values vs y_true")
        plt.show()
        print("=================================================================")
        plt.plot(np.arange(epochs_iterations-1).reshape(-1,1), np.array(losses).reshape(-1,1))
        plt.title("Epochs vs Losses")
        plt.show()
        print("=================================================================")
        plt.plot(bias, losses)
        plt.title("Bias vs Losses")
        plt.show()
        print("=================================================================")
        plt.plot(weight_1, losses)
        plt.title("Weight_1 vs Losses")
        plt.show()
        print("=================================================================")
        for y in np.array(all_hypothsis):
            plt.plot(np_x, y)
        plt.title("All Hypothsis")
        plt.show()
        print("=================================================================")
        plt.plot(np_x, y_pred)
        plt.title("The best reggression line")
        plt.show()
        print("=================================================================")
        print("=================================================================")

    def Adam_test(self):
        print("====================Adam====================")
        x = np.linspace(0,20)
        np_x = np.array(x).reshape(-1,1)
        np_y = -2*np_x + 1
        features = np.ones((x.size,1))
        features = np.append(features, np_x, axis=1)
        batchSize = np_x.shape[0]
        #=======================================================================
        model = LinearRegression('Adam', batchSize, beta1 = 0.98, beta2 = 0.999, alpha = 0.25)
        weights, losses, bias, weight_1, all_hypothsis, epochs_iterations = model.fit(features, np_y)
        y_pred = model.predict(features)
        print(f"R2 Score = {r2_score(np_y, y_pred)}")
        print("=================================================================")
        plt.plot(np_x, np_y)
        plt.title("x_values vs y_true")
        plt.show()
        print("=================================================================")
        plt.plot(np.arange(epochs_iterations-1).reshape(-1,1), np.array(losses).reshape(-1,1))
        plt.title("Epochs vs Losses")
        plt.show()
        print("=================================================================")
        plt.plot(bias, losses)
        plt.title("Bias vs Losses")
        plt.show()
        print("=================================================================")
        plt.plot(weight_1, losses)
        plt.title("Weight_1 vs Losses")
        plt.show()
        print("=================================================================")
        for y in np.array(all_hypothsis):
            plt.plot(np_x, y)
        plt.title("All Hypothsis")
        plt.show()
        print("=================================================================")
        plt.plot(np_x, y_pred)
        plt.title("The best reggression line")
        plt.show()
        print("=================================================================")
        print("=================================================================")