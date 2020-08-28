import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import f1_score, accuracy_score
from sklearn.metrics import mean_absolute_error as mae

def plot_epochs_vs_loss(train_loss, val_loss, results_path, fold):
    plt.figure()
    plt.plot(range(1,1+len(train_loss)), train_loss, label = 'TrainLoss')
    plt.plot(range(1,1+len(val_loss)), val_loss, label = 'ValLoss')
    plt.xlabel('Epoch-->')
    plt.ylabel('Loss-->')
    plt.title('Epochs vs Loss')
    plt.legend()
    plt.savefig(os.path.join(results_path, str(fold)+'_epochs_vs_loss.png'))
    plt.show()
    
def plot_mae(df, results_path ):
    dx = 0.5
    r = 100
    MAE1 = []
    for i in range(int(2/dx),int(150/dx)):
        P = df[(df['True_pT']>=(i-1)*dx)&(df['True_pT']<=(i+1)*dx)]
        p = mae(P['True_pT'],P['Predicted_pT'])
        if p<100:
            p=p
        else:
            p=p_
        MAE1.append(p)
        p_=p
    MAE1 = [0]*2*int(1/dx)+MAE1[:r*2-2*int(1/dx)]
    plt.figure()
    plt.plot([i*dx for i in range(int(r/dx))],MAE1)
    plt.xlabel('pT (in GeV) -->')
    plt.ylabel('MAE -->')
    plt.legend()
    plt.savefig(os.path.join(results_path, 'mae.png'))
    plt.show()
    return MAE1

def plot_mae_pT(df, results_path ):
    dx = 0.5
    r = 100
    MAE1 = []
    for i in range(int(2/dx),int(150/dx)):
        P = df[(df['True_pT']>=(i-1)*dx)&(df['True_pT']<=(i+1)*dx)]
        p = mae(P['True_pT'],P['Predicted_pT'])/(i)
        if p<100:
            p=p
        else:
            p=p_
        MAE1.append(p)
        p_=p
    MAE1 = [0]*2*int(1/dx)+MAE1[:r*2-2*int(1/dx)]
    plt.figure()
    plt.plot([i*dx for i in range(int(r/dx))],MAE1)
    plt.xlabel('pT (in GeV) -->')
    plt.ylabel('MAE -->')
    plt.legend()
    plt.savefig(os.path.join(results_path, 'mae_pt.png'))
    plt.show()
    return MAE1
    
def plot_f1_pT_upper(df, results_path ):
    f1 = []
    for i in range(5,121):
        f1.append(f1_score(df['True_pT']>=i, df['Predicted_pT']>=i))
    plt.figure()
    plt.plot(range(5,121),f1)
    plt.xlabel('pT (in GeV) -->')
    plt.ylabel('F1 (for class pT < x) -->')
    plt.legend()
    plt.savefig(os.path.join(results_path, 'f1(pT>x).png'))
    plt.show()
    return f1
    
def plot_f1_pT_lower(df, results_path ):
    f1 = []
    for i in range(5,121):
        f1.append(f1_score(df['True_pT']<=i, df['Predicted_pT']<=i))
    plt.figure()
    plt.plot(range(5,121),f1)
    plt.xlabel('pT (in GeV) -->')
    plt.ylabel('F1 (for class pT < x) -->')
    plt.legend()
    plt.savefig(os.path.join(results_path, 'f1(pT<x).png'))
    plt.show()
    return f1
    
    
def plot_accuracy(df, results_path ):
    acc = []
    for i in range(5,121):
        acc.append(accuracy_score(df['True_pT']>=i, df['Predicted_pT']>=i))
    plt.figure()
    plt.plot(range(5,121),acc)
    plt.xlabel('pT (in GeV) -->')
    plt.ylabel('Accuracy -->')
    plt.legend()
    plt.savefig(os.path.join(results_path, 'acc.png'))
    plt.show()
    return acc

def save_all_plots(df, results_path ):
    plot_accuracy(df, results_path )
    plot_f1_pT_lower(df, results_path )
    plot_f1_pT_upper(df, results_path )
    plot_mae_pT(df, results_path )
    plot_mae(df, results_path )