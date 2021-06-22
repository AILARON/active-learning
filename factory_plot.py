
# Factory method -> Create concrete implementation of common interface
# Single responsibility principle -> Module, a class or even a method should have a single, well-defined responsibility 
#                                    It should do just one thing.
#  Refactoring -> Make changes without changin behavior
import matplotlib.pyplot as plt
import os
import argparse
import pickle
from copy import deepcopy
import numpy as np
import sys


class plot:

    def __init__(self, results, fraction):
        
        self.results = {}
        self.fraction = fraction
        self.labels = []
        self.accuracy = []
        self.max_y = 0
        self.colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:brown', 'indianred', 'pink']
        self.linestyle = ['--', 'dashdot', 'dotted', ':', '-.', 'solid', 'dashed']
        
        for key,value in results.items():
            self.labels.append(key)
            self.accuracy.append(value)

        self.num_plots = len(self.accuracy)
        

        
    def find_diff(self, l1, l2):

        if len(l1) != len(l2):
            sys.exit('Not equal length on lists')
    
        diff = [l1[i] - l2[i] for i in range(len(l1))]
        return diff

    def relative_plot(self, mean, std, fraction, label1, label2, n_pool):

        fig, ax = plt.subplots(1)
        fraction = [100*elem/n_pool for elem in fraction]
        mean = np.asarray([100*elem for elem in mean])
        std = np.asarray([100*elem for elem in std])
        

        ax.plot(fraction, mean, label=label1, color='purple')
        ax.plot(fraction, [0 for _ in range(len(mean))], label=label2, linestyle='dashed', color='orange')
        ax.fill_between(fraction, mean - std, mean + std,
                 color='red', alpha=0.2)
        
        ax.set_xlabel("Number labeled samples[%]")
        ax.set_ylabel("$\Delta$ Accuracy[%]")
        #ax.set_ylim(60,90)
        #ax.set_xlim(10,80)
        plt.xticks(ticks=fraction)

        ax.legend()
        plt.grid()
        plt.show()

    def plot(self, n_pool, x_min=10, x_max=80, y_min=30,y_max=90):


        f, ax = plt.subplots(1)
        dyfit = 2 * np.sqrt(0.1)
        self.fraction = [100*elem/n_pool for elem in self.fraction]
        
        for i in range(self.num_plots):
            self.accuracy[i] = [100*elem for elem in self.accuracy[i]]

            if i == 2:
                linestyle = 'dashed'
            else:
                linestyle = 'solid'
            ax.plot(self.fraction, self.accuracy[i], label=self.labels[i], color=self.colors[i], linestyle=linestyle)
            ax.fill_between(self.fraction, self.accuracy[i], self.accuracy[i], #+ dyfit,
                 color=self.colors[i], alpha=0.2)
            if max(self.accuracy[i]) > self.max_y:
                self.max_y = max(self.accuracy[i])

        ax.set_xlim(x_min, x_max)#self.fraction[len(self.fraction)-1])
        ax.set_ylim(y_min, self.max_y+5)
        ax.set_xlabel("Number labeled samples[%]")
        ax.set_ylabel("Accuracy[%]")
        ax.legend(loc=4)
        plt.xticks(ticks=self.fraction)
        plt.grid()
        plt.show()
        
    def find_diff(self, l1, l2):

        if len(l1) != len(l2):
            sys.exit('Not equal length on lists')
    
        diff = [l1[i] - l2[i] for i in range(len(l1))]
        return diff

    def relative_plot(self, mean, std, fraction, label1, label2, n_pool):

        fig, ax = plt.subplots(1)
        fraction = [100*elem/n_pool for elem in fraction]
        mean = np.asarray([100*elem for elem in mean])
        std = np.asarray([100*elem for elem in std])
        

        ax.plot(fraction, mean, label=label1, color='purple')
        ax.plot(fraction, [0 for _ in range(len(mean))], label=label2, linestyle='dashed', color='orange')
        ax.fill_between(fraction, mean - std, mean + std,
                 color='red', alpha=0.2)
        
        ax.set_xlabel("Number labeled samples[%]")
        ax.set_ylabel("$\Delta$ Accuracy[%]")
        #ax.set_ylim(60,90)
        #ax.set_xlim(10,80)
        plt.xticks(ticks=fraction)

        ax.legend()
        plt.grid()
        plt.show()
        

    def multiple_plot(self, diff1, diff2, diff3, diff4, diff5, diff6, n_pool):
        #f, (ax1,ax2,ax3) = plt.subplots(3)
        dyfit = 2 * np.sqrt(0.01)
        fig, axs = plt.subplots(3, 2)

        self.fraction = [100*elem/n_pool for elem in self.fraction]

        diff1 = [100*elem for elem in diff1]
        axs[0, 0].plot(self.fraction, diff1, label='CIRAL', color='purple')
        axs[0, 0].plot(self.fraction, [0 for _ in range(len(diff1))], label='CORESET', linestyle='dashed', color='orange')
        axs[0, 0].legend()
        axs[0,0].set_xlim(0,80)
        axs[0,0].set_ylim(-10,10)
        plt.grid(color='white')

        axs[0, 0].set_ylabel("$\Delta$ Accuracy[%]")
        diff2 = [100*elem for elem in diff2]
        axs[1, 0].plot(self.fraction, diff2, label='CIRAL', color='purple')
        axs[1, 0].plot(self.fraction, [0 for _ in range(len(diff2))], label='DFAL', linestyle='dashed', color='orange')
        axs[1, 0].legend()
        axs[1, 0].set_ylabel("$\Delta$ Accuracy[%]")
        axs[1,0].set_xlim(0,80)
        axs[1,0].set_ylim(-10,10)
        plt.grid(color='white')

        diff3 = [100*elem for elem in diff3]
        axs[2, 0].plot(self.fraction, diff3, label='CIRAL', color='purple')
        axs[2, 0].plot(self.fraction, [0 for _ in range(len(diff3))], label='RANDOM', linestyle='dashed', color='orange')
        axs[2, 0].legend()
        axs[2, 0].set_xlabel('Number labeled samples[%]')
        axs[2, 0].set_ylabel("$\Delta$ Accuracy[%]")
        axs[2,0].set_xlim(0,80)
        axs[2,0].set_ylim(-7,7)
        plt.grid(color='white')

        diff4 = [100*elem for elem in diff4]
        axs[0, 1].plot(self.fraction, diff4, label='CIRAL', color='purple')
        axs[0, 1].plot(self.fraction, [0 for _ in range(len(diff4))], label='BADGE', linestyle='dashed', color='orange')
        axs[0, 1].legend()
        axs[0,1].set_xlim(0,80)
        axs[0,1].set_ylim(-15,15)
        plt.grid(color='white')

        diff5 = [100*elem for elem in diff5]
        axs[1, 1].plot(self.fraction, diff5, label='CIRAL', color='purple')
        axs[1, 1].plot(self.fraction, [0 for _ in range(len(diff5))], label='Active Learning by Learning', linestyle='dashed', color='orange')
        axs[1, 1].legend()
        axs[1,1].set_xlim(0,80)
        axs[1,1].set_ylim(-10,10)
        plt.grid(color='white')

        diff6 = [100*elem for elem in diff6]
        axs[2, 1].plot(self.fraction, diff6, label='CIRAL', color='purple')
        axs[2, 1].plot(self.fraction, [0 for _ in range(len(diff6))], label='Softmax Hybrid', linestyle='dashed', color='orange')
        axs[2, 1].legend()
        axs[2, 1].set_xlabel('Number labeled samples[%]')
        axs[2,1].set_xlim(0,80)
        axs[2,1].set_ylim(-12,12)


        for i in range(3):
            for j in range(2):
                axs[i,j].set_facecolor('aliceblue')
                axs[i,j].spines['top'].set_visible(False)
                axs[i,j].spines['right'].set_visible(False)
                axs[i,j].spines['left'].set_visible(False)
                axs[i,j].spines['bottom'].set_visible(False)
                axs[i,j].legend(loc=4, framealpha=0)
                axs[i,j].grid(color='white')
                #plt.xticks(ticks=fraction)

        plt.show()

    def multiple_plot2(self, diff1, diff2, diff3, n_pool):
            #f, (ax1,ax2,ax3) = plt.subplots(3)
            dyfit = 2 * np.sqrt(0.01)
            fig, axs = plt.subplots(1, 3)

            self.fraction = [100*elem/n_pool for elem in self.fraction]

            axs[0].set_ylabel("$\Delta$ Accuracy[%]")
            diff1 = [100*elem for elem in diff1]
            axs[0].plot(self.fraction, diff1, label='CIRAL', color='purple')
            axs[0].plot(self.fraction, [0 for _ in range(len(diff1))], label='CORESET', linestyle='dashed', color='orange')
            axs[0].legend()
            axs[0].set_xlabel('Number labeled samples[%]')

            axs[0].set_xlim(0,20)
            axs[0].set_ylim(-8,8)

            diff2 = [100*elem for elem in diff2]
            axs[1].plot(self.fraction, diff2, label='CIRAL', color='purple')
            axs[1].plot(self.fraction, [0 for _ in range(len(diff2))], label='DFAL', linestyle='dashed', color='orange')
            axs[1].legend()
            axs[1].set_xlabel('Number labeled samples[%]')

            axs[1].set_xlim(0,20)
            axs[1].set_ylim(-8,8)

            diff3 = [100*elem for elem in diff3]
            axs[2].plot(self.fraction, diff3, label='CIRAL', color='purple')
            axs[2].plot(self.fraction, [0 for _ in range(len(diff3))], label='RANDOM', linestyle='dashed', color='orange')
            axs[2].legend()
            axs[2].set_xlabel('Number labeled samples[%]')
            axs[2].set_xlim(0,10)
            axs[2].set_ylim(-8,8)
            axs[0].set_facecolor('aliceblue')
            axs.spines['top'].set_visible(False)
            axs.spines['right'].set_visible(False)
            axs.spines['left'].set_visible(False)
            axs.spines['bottom'].set_visible(False)
            axs.legend(loc=4, framealpha=0)
            plt.xticks(ticks=fraction)
            plt.grid(color='white')
            plt.show()



    def multiple_plot3(self, diff1, label, n_pool):
            #f, (ax1,ax2,ax3) = plt.subplots(3)
            dyfit = 2 * np.sqrt(0.01)
            fig, axs = plt.subplots(1)

            self.fraction = [100*elem/n_pool for elem in self.fraction]

            axs.set_ylabel("$\Delta$ Accuracy[%]")
            diff1 = [100*elem for elem in diff1]
            axs.plot(self.fraction, diff1, label='CIRAL', color='purple')
            axs.plot(self.fraction, [0 for _ in range(len(diff1))], label=label, linestyle='dashed', color='orange')
            axs.legend()
            axs.set_xlabel('Number labeled samples[%]')

            axs.set_xlim(0,90)
            axs.set_ylim(-11,11)
        
            plt.show()



    def moving_average(self, x, w):
        return np.convolve(x, np.ones(w), 'valid') / w

    def find_std(self, arr):
    
        if not (isinstance(arr, np.ndarray)):
            arr = np.asarray(arr)

        std = np.var(arr, axis=0)
        mean = np.mean(arr, axis=0)

        return mean, std

    def plot_mean_std(self, results, compare_results, fraction, n_pool):


        fraction = [100*elem/n_pool for elem in fraction]       

        f, ax = plt.subplots(1, figsize=(7,5))
        labels = ['SOFTMAX', 'CIRAL', 'BADGE', 'ALL']
        #labels = ['CORESET', 'RANDOM', 'CIRAL', 'DFAL']
        for i, result in enumerate(results):

            mean, std = self.find_std(result)
            self.accuracy[i] = [100*elem for elem in self.accuracy[i]]

            mean = np.asarray([100*elem for elem in mean])
            std = np.asarray([100*elem for elem in std])
            print(len(mean), len(fraction), self.accuracy[i])
            ax.plot(fraction, mean, label=f'{labels[i]}', color=self.colors[i], linestyle='solid')
            ax.plot(fraction, self.accuracy[i], label=f'{labels[i]} wo-Aug', color=self.colors[i], linestyle='dashed')
            ax.fill_between(fraction, mean, mean,
                 color=self.colors[i], alpha=0.2)
        
        ax.set_xlim(0, 100)
        ax.set_ylim(10,100)
        ax.set_xlabel("Number labeled samples[%]")
        ax.set_ylabel("Accuracy[%]")
        ax.set_facecolor('aliceblue')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.legend(loc=4, framealpha=0)
        #plt.xticks(ticks=fraction)
        plt.grid(color='white')

        plt.show() 

    def return_mean_std(self, results):
        
        mean_list = []
        std_list = []
        for result in results:
            mean, std = self.find_std(result)
            mean_list.append(mean)
            std_list.append(std)
        return np.asarray(mean_list), np.asarray(std_list)

    def plot_histogram(self,x,y):

        #y = [100*elem for elem in y]
        plt.bar(x,y,align='center', color=['tab:red' for _ in range(len(x))]) #color=['orangered','orangered','orangered','orangered','orangered','orangered','orangered', 'orangered', 'orangered', 'yellow']) # A bar chart
        plt.xlabel('Class')
        plt.grid(axis='y', alpha=0.25)
        plt.ylabel('Number of samples')
        plt.xticks(x)
        plt.show()


def time_plot():
    '''
    time1 = [0.6, 15.3, 11.73, 8.22, 5.63, 3.6, 2.15, 1.22] # opt
    time2 = [0.26, 0.5, 0.46, 0.45, 0.43, 0.43, 0.43, 0.45] # wo opt
    time3 = [0.23, 0.45, 0.43, 0.41, 0.4, 0.40, 0.42, 0.42] # k-means
    time4 = [0.23, 0.44, 0.43, 0.42, 0.4, 0.41, 0.42, 0.42] # k-means random
    '''
    time1 = [0.06, 7.28, 6.82, 6.25, 3.68, 2.72, 1.95, 1.3]
    time2 = [0.15, 0.5, 0.5, 0.5, 0.5, 0.5, 0.55, 0.58]
    time3 = [0.05, 0.4, 0.43, 0.5, 0.5, 0.53, 0.58, 0.61]
    time4 = [0.23, 0.32, 0.36, 0.4, 0.43, 0.5, 0.53, 0.56]
    fraction = [100, 600, 1100, 1600, 2100, 2600, 3100, 3600]
    n_pool = 3933
    times = [time1,time2,time3,time4]
    
    f, ax = plt.subplots(1)
    labels = ['Core-set with optimization', 'Core-set without optimization', 'K-means++', 'K-means']
    colors = ['green', 'red', 'blue', 'brown']
    linestyle = ['solid', 'dashed', 'dashed', 'solid']
    fraction = [100*elem/n_pool for elem in fraction]
    for time, label, color, linestyle in zip(times, labels, colors, linestyle):
        print(time)
        ax.plot(fraction, time, label=label, color=color, linestyle=linestyle)
    
    ax.set_xlim(5, 90)
    ax.set_ylim(0, 8)
    ax.set_xlabel("Number labeled samples[%]")
    ax.set_ylabel("Computation time[min]")
    ax.set_facecolor('aliceblue')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.legend(loc=4, framealpha=0)
    plt.xticks(ticks=fraction)
    plt.grid(color='white')

    plt.show() 

def single_plot(n_pool, fraction, acc, std):

    f, ax = plt.subplots(1)
    labels = ['Core-set with optimization', 'Core-set without optimization', 'K-means++', 'K-means']
    colors = ['green', 'red', 'blue', 'brown']
    linestyle = ['solid', 'dashed', 'dashed', 'solid']
    fraction = [100*elem/n_pool for elem in fraction]
    for acc, std, label, color, linestyle in zip(acc, std, labels, colors, linestyle):
        acc = [100*elem for elem in acc]
        std = [100*elem for elem in std]
        ax.plot(fraction, acc, label=label, color=color, linestyle=linestyle)
        diff1 = [acc-std for (acc,std) in zip(acc,std)]
        diff2 = [acc+std for (acc,std) in zip(acc,std)]
        ax.fill_between(fraction, diff1, diff2,
                color=color, alpha=0.2)

    ax.set_xlim(5, 90)
    ax.set_ylim(0,60)
    ax.set_xlabel("Number labeled samples[%]")
    ax.set_ylabel("Accuracy[%]")
    ax.set_facecolor('aliceblue')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.legend(loc=4, framealpha=0)
    plt.xticks(ticks=fraction)
    plt.grid(color='white')

    plt.show() 

if __name__ == "__main__":

    '''
    acc = [[0.44566667, 0.74516667, 0.82733333, 0.86326667, 0.88433333, 0.9025,
 0.9017, 0.90993333],[0.48783333, 0.7319, 0.84426667, 0.88103333, 0.88766667, 0.8996,
 0.9087, 0.92193333], [0.4725, 0.734, 0.83063333, 0.86576667, 0.8856, 0.90376667,
 0.91903333, 0.91616667],
 [0.51383333, 0.76333333, 0.81203333, 0.86946667, 0.88886667, 0.90043333,
 0.9083, 0.91536667]]
    std = [[0.03695676, 0.01303022, 0.01663437, 0.00154128, 0.00506228, 0.00764606,
        0.00268494, 0.00157692], [0.04405582, 0.01667873, 0.00519765, 0.00826935, 0.00648554, 0.00204124,
        0.00384968, 0.00465928], [0.11025873, 0.01445983, 0.00773276, 0.00308257, 0.01519737, 0.00760058,
 0.00814548, 0.00760058], [0.02589676, 0.018416,  0.01627295, 0.00671185, 0.0091529,  0.00117851,
 0.0009798, 0.00584542]]
    '''
    
    fraction = [100, 600, 1100, 1600, 2100, 2600, 3100, 3600]
    n_pool = 3900
    
    k_center_opt = [0.11873333, 0.3125, 0.39793333, 0.42293333, 0.41666667, 0.4104, 0.425, 0.40416667]
    k_center = [0.15206667, 0.31456667, 0.35, 0.39583333, 0.43956667, 0.41456667, 0.45206667, 0.4479]
    k_means_pp = [0.08336667, 0.32293333, 0.3854, 0.40833333, 0.41246667, 0.43336667, 0.45206667, 0.4396]  
    k_means_rnd = [0.125, 0.35003333, 0.37083333, 0.42916667, 0.4104, 0.45206667, 0.43956667, 0.45]

    std_k_center_opt = [0.00510316, 0.02041241, 0.02900073, 0.01641266, 0.01066219, 0.03395566, 0.0418106,  0.03616419]
    std_k_center = [0.00781295, 0.00292271, 0.02700309, 0.01559024, 0.0155457, 0.02619241, 0.01061644, 0.02062733]
    std_k_means_pp = [0.00292271, 0.04460242, 0.02120016, 0.03280837, 0.0088624,  0.02518681, 0.03620832, 0.03121613]
    std_k_means_rnd = [0.03107453, 0.00510316, 0.07523113, 0.0412479,  0.00296985, 0.05238482, 0.0155457,  0.08354141]

    acc = [k_center_opt, k_center, k_means_pp, k_means_rnd]
    std = [std_k_center_opt, std_k_center, std_k_means_pp, std_k_means_rnd]
    #single_plot(n_pool, fraction, acc, std)
    #time_plot()
    
    results_cifar = {
    'Softmax': [0.1, 0.3321, 0.3374, 0.3125, 0.3555, 0.3718, 0.3743, 0.4021, 0.4203, 0.4988, 0.5005],
    'CORESET': [0.1, 0.3527, 0.3817, 0.3883, 0.392, 0.4145, 0.4285, 0.4419, 0.4357, 0.4385, 0.4451],
    'BADGE': [0.1, 0.3473, 0.2759, 0.3199, 0.3618, 0.372, 0.4065, 0.3918, 0.4413, 0.4008, 0.4716],     
    'RANDOM': [0.1, 0.3436, 0.3435, 0.3388, 0.381, 0.4026, 0.4215, 0.464, 0.4906, 0.5075, 0.5481],
    'CIRAL': [0.1, 0.3881, 0.3983, 0.4046, 0.4144, 0.4319, 0.4222,0.4375, 0.435, 0.4506, 0.4462],
    'DFAL': [0.1, 0.3246, 0.3567, 0.3764, 0.3832, 0.3956, 0.4027, 0.4125, 0.4126, 0.4168, 0.4261],
    'ALL': [0.1, 0.3309, 0.3606, 0.5066, 0.3732, 0.4166, 0.4177, 0.4435, 0.5098, 0.3207, 0.4217]
    }
    
    fraction_cifar = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000,8000,9000,10000]
    '''
    results_cifar = {
    'CORESET': [0.1, 0.51, 0.5795, 0.6425, 0.6565, 0.655, 0.653, 0.674],
    'RANDOM': [0.1, 0.481, 0.6045, 0.6115, 0.665, 0.669, 0.6755, 0.669],
    'CIRAL':  [0.1, 0.475, 0.6135, 0.6595, 0.613, 0.675, 0.6905, 0.6775],
    'DFAL': [0.1, 0.5315, 0.587, 0.6075, 0.6295, 0.6695, 0.6485, 0.6635],
    }    
    '''
    results_plankton = {
    'CORESET':  [0.1, 0.5825, 0.6075, 0.62375, 0.628125, 0.64125, 0.613125],
    'RANDOM': [0.1, 0.613125, 0.61, 0.63125, 0.6025, 0.630625, 0.630625],
    'CIRAL': [0.1, 0.57375, 0.61875, 0.624375, 0.63875, 0.63875, 0.639375],
    'DFAL': [0.1, 0.51125, 0.6175, 0.51625, 0.6475, 0.62875, 0.6375],
    }
    
    fraction_plankton = [0, 1000, 2000, 3000, 4000, 5000, 6000]
    

    results_plankton = {
        'CORESET': [0.1, 0.613, 0.626, 0.627, 0.643, 0.640, 0.641, 0.641],
        'SOFTMAX': [0.1, 0.6126, 0.629, 0.628, 0.638, 0.636, 0.645, 0.633],
        'RANDOM':[0.1, 0.614, 0.637, 0.634, 0.652, 0.652, 0.655, 0.660],
        'CIRAL': [0.1, 0.6412, 0.6517, 0.6623, 0.6603, 0.657, 0.6537, 0.6623], # 1 trial
        'DFAL': [0.1, 0.5963, 0.6168, 0.6332, 0.6319, 0.6339, 0.6379, 0.6398], # FROM CIRAL
        'BADGE': [0.1, 0.602, 0.605, 0.618, 0.625, 0.631, 0.62, 0.596],
        'ALL': [0.1, 0.6181, 0.6266, 0.6418, 0.6372, 0.6405, 0.6471, 0.6563], # 1 trial
    }

    fraction_plankton = [100, 1100, 2100, 3100, 4100, 5100, 6100, 7100]
    plotter = plot(results_plankton, fraction_plankton)

    #plotter.plot(n_pool=7484)
    '''
    diff1 = plotter.find_diff(results_plankton['CIRAL'], results_plankton['CORESET'])
    diff2 = plotter.find_diff(results_plankton['CIRAL'], results_plankton['DFAL'])
    diff3 = plotter.find_diff(results_plankton['CIRAL'], results_plankton['RANDOM'])
    diff4 = plotter.find_diff(results_plankton['CIRAL'], results_plankton['BADGE'])
    diff5 = plotter.find_diff(results_plankton['CIRAL'], results_plankton['ALL'])
    diff6 = plotter.find_diff(results_plankton['CIRAL'], results_plankton['SOFTMAX'])
    '''
    diff1 = plotter.find_diff(results_cifar['CIRAL'], results_cifar['CORESET'])
    diff2 = plotter.find_diff(results_cifar['CIRAL'], results_cifar['DFAL'])
    diff3 = plotter.find_diff(results_cifar['CIRAL'], results_cifar['RANDOM'])
    diff4 = plotter.find_diff(results_cifar['CIRAL'], results_cifar['BADGE'])
    diff5 = plotter.find_diff(results_cifar['CIRAL'], results_cifar['ALL'])
    diff6 = plotter.find_diff(results_cifar['CIRAL'], results_cifar['Softmax'])
    
    #plot_func = plotter.multiple_plot(diff1, diff2, diff3,diff4,diff5,diff6,n_pool=7484)
    
    #plot_func2 = plotter.multiple_plot3(diff1, label='CORESET', n_pool=6400)


    BADGE_PLANKTON = [[0.1, 0.7408, 0.8212, 0.8219, 0.8391, 0.8641, 0.8575, 0.8562],
                     [0.1, 0.7619, 0.8153, 0.8074, 0.8292, 0.874, 0.8687, 0.8635],
                     [0.1, 0.7869, 0.8325, 0.8476, 0.8668, 0.8463, 0.8793, 0.8773]]    


    BUDAL_PLANKTON = [[0.1, 0.7784, 0.8595, 0.8701, 0.8918, 0.8793, 0.8898, 0.8747],
                    [0.1, 0.781, 0.8443, 0.8536, 0.8681, 0.8615, 0.8806, 0.8766],
                    [0.1, 0.684, 0.7988, 0.8041, 0.843, 0.8687, 0.8826, 0.8648]]
    DFAL_PLANKTON = [[0.1, 0.7018, 0.814, 0.8146, 0.8562, 0.8806, 0.8766, 0.845],
                [0.1, 0.7381, 0.7962, 0.8549, 0.8602, 0.8872, 0.878, 0.8872],
                [0.1, 0.7315, 0.8206, 0.8648, 0.8707, 0.8958, 0.8806, 0.8582]]

    ALL_PLANKTON = [[0.1, 0.6972, 0.8371, 0.8503, 0.8476, 0.8668, 0.878, 0.8793],
                [0.1, 0.7249, 0.7764, 0.8285, 0.8575, 0.8707, 0.8707, 0.8773],
                [0.1, 0.7355, 0.8265, 0.8443, 0.8674, 0.8819, 0.8727, 0.8846]]
    
    CORESET_PLANKTON = [[0.1, 0.777, 0.8087, 0.8318, 0.8503, 0.8588, 0.8654, 0.8694],
                    [0.1, 0.7982, 0.7975, 0.847, 0.8522, 0.8588, 0.8846, 0.876],
                    [0.1, 0.7434, 0.8226, 0.8173, 0.8549, 0.8588, 0.8562, 0.8839]]

    RANDOM_PLANKTON = [#[0.1, 0.781, 0.8423, 0.8549, 0.8641, 0.8832, 0.8747, 0.8898],
                        [0.1, 0.7018, 0.777, 0.814, 0.8463, 0.8555, 0.8747, 0.8806],
                        #[0.1, 0.7243, 0.8166, 0.8536, 0.8734, 0.8898, 0.8793, 0.9024]]
                        ]

    SOFTMAX_PLANKTON = [[0.1, 0.7414, 0.8265, 0.8371, 0.845, 0.8621, 0.8793, 0.8793],
                        [0.1, 0.8179, 0.8582, 0.8766, 0.8674, 0.8773, 0.8793, 0.8681],
                        [0.1, 0.783, 0.5475, 0.845, 0.8325, 0.878, 0.8813, 0.8978]]
        
    #results = [BADGE_PLANKTON, BUDAL_PLANKTON, DFAL_PLANKTON, ALL_PLANKTON, CORESET_PLANKTON, RANDOM_PLANKTON, SOFTMAX_PLANKTON]
    #results= [BADGE_PLANKTON, BUDAL_PLANKTON, ALL_PLANKTON, SOFTMAX_PLANKTON, RANDOM_PLANKTON]
    results = [SOFTMAX_PLANKTON, BUDAL_PLANKTON, BADGE_PLANKTON, ALL_PLANKTON]
    #results = [CORESET_PLANKTON, RANDOM_PLANKTON, BUDAL_PLANKTON, DFAL_PLANKTON]
    #plotter.plot_mean_std(results, results_plankton, fraction_plankton, n_pool=7484)
    #mean, std = plotter.return_mean_std(results)
    

    #diff_mean = plotter.find_diff(mean[1], mean[0])
    #diff_std = plotter.find_diff(std[1], std[0])

    tot_var = [std[0][i] + std[1][i] for i in range(len(std[0]))]
    print(std[0])
    print(std[1])
    print(tot_var)


    #plotter.relative_plot(diff_mean, tot_var, fraction_plankton, label1='BUDAL', label2='ALL', n_pool=7484)

    cifar_distribution = [0.09, 0.1, 0.1, 0.07, 0.13, 0.1, 0.12, 0.1, 0.08, 0.1]
    kaggle_class_distribution = [1980,1173,890,697,704,709,695,1190,915,537]
    ailaron_class_distribution = [824, 858, 851, 810, 824, 883]
    cifar_distribution = [400 for _ in range(10)]
    pastore_distribution = [500 for _ in range(10)]

    '''
    all_kaggle_q400_half = [0.16, 0.13, 0.06, 0.06, 0.08, 0.11, 0.07, 0.09, 0.13, 0.1]
    badge_kaggle_q400_half = [0.2, 0.13, 0.09, 0.08, 0.07, 0.08, 0.08, 0.13, 0.09, 0.05]
    ciral_kaggle_q400_half = [0.22, 0.12, 0.08, 0.08, 0.08, 0.07, 0.08, 0.12, 0.1, 0.06]
    coreset_kaggle_q400_half = [0.2, 0.13, 0.09, 0.08, 0.07, 0.08, 0.07, 0.13, 0.1, 0.06]
    dfal_kaggle_q400_half = [0.16, 0.1, 0.05, 0.06, 0.1, 0.13, 0.08, 0.09, 0.16, 0.09]
    random_kaggle_q400_half = [0.21, 0.13, 0.09, 0.07, 0.07, 0.07, 0.07, 0.13, 0.1, 0.06]
    softmax_kaggle_q400_half = [0.21, 0.13, 0.09, 0.07, 0.07, 0.08, 0.07, 0.12, 0.1, 0.06]
    '''
    '''
    all_ailaron_q400_half = [0.18, 0.26, 0.12, 0.14, 0.12, 0.17]
    badge_ailaron_q400_half = [0.16, 0.19, 0.16, 0.17, 0.16, 0.17]
    ciral_ailaron_q400_half = [0.17, 0.17, 0.16, 0.18, 0.17, 0.16]
    coreset_ailaron_q400_half = [0.16, 0.17, 0.16, 0.18, 0.18, 0.16]
    dfal_ailaron_q400_half = [0.31, 0.28, 0.0, 0.2, 0.08, 0.13]
    random_ailaron_q400_half = [0.17, 0.16, 0.17, 0.18, 0.16, 0.16]
    softmax_ailaron_q400_half = [0.16, 0.18, 0.17, 0.17, 0.16, 0.16]
    '''
    '''
    all_cifar_q400_half = [0.16, 0.13, 0.09, 0.07, 0.07, 0.06, 0.05, 0.08, 0.14, 0.14]
    badge_cifar_q400_half = [0.1, 0.1, 0.08, 0.1, 0.11, 0.1, 0.08, 0.11, 0.1, 0.1]
    ciral_cifar_q400_half = [0.11, 0.1, 0.1, 0.1, 0.09, 0.09, 0.1, 0.1, 0.1, 0.11]
    coreset_cifar_q400_half = [0.09, 0.1, 0.11, 0.1, 0.1, 0.1, 0.09, 0.11, 0.09, 0.1]
    dfal_cifar_q400_half = [0.1, 0.13, 0.08, 0.09, 0.08, 0.08, 0.09, 0.09, 0.11, 0.15]
    random_cifar_q400_half = [0.09, 0.1, 0.12, 0.11, 0.09, 0.1, 0.09, 0.1, 0.1, 0.1]
    softmax_cifar_q400_half = [0.1, 0.09, 0.12, 0.11, 0.1, 0.09, 0.1, 0.09, 0.08, 0.11]
    '''
    all_pastore_q50_half = [0.04, 0.07, 0.15, 0.04, 0.04, 0.2, 0.05, 0.22, 0.04, 0.15]
    badge_pastore_q50_half = [0.1, 0.12, 0.08, 0.09, 0.1, 0.09, 0.1, 0.13, 0.11, 0.08]
    ciral_pastore_q50_half = [0.13, 0.08, 0.08, 0.11, 0.12, 0.09, 0.05, 0.16, 0.09, 0.09]
    coreset_pastore_q50_half = [0.09, 0.12, 0.11, 0.08, 0.11, 0.1, 0.09, 0.11, 0.12, 0.06]
    dfal_pastore_q50_half = [0.05, 0.02, 0.31, 0.02, 0.04, 0.02, 0.02, 0.29, 0.04, 0.17]
    random_pastore_q50_half = [0.08, 0.1, 0.11, 0.13, 0.11, 0.1, 0.09, 0.08, 0.11, 0.08]
    softmax_pastore_q50_half = [0.07, 0.09, 0.12, 0.11, 0.09, 0.1, 0.11, 0.1, 0.09, 0.12]

    plotter.plot_histogram([_ for _ in range(10)], cifar_distribution)