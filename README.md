# Deep learning algorithms for muon momentum estimation in the CMS Trigger System

The Compact Muon Solenoid (CMS) is a general-purpose detector at the Large Hadron Collider (LHC). During a run, it generates about 40 TB data per second. Since It is not feasible to readout and store such a vast amount of data, so a trigger system selects and stores only interesting events or events likely to reveal new physics phenomena. The goal of this project is to benchmark the muon momentum estimation performance of **Fully Connected Neural Networks (FCNN), Convolutional Neural Networks (CNN), and Graph Neural Networks (GNN), on the prompt and displaced muon samples collected by CSC stations at CMS** to aid trigger system's transverse momentum muon estimation.

## About



## How to use

> An example of how to use is available [here](https://www.kaggle.com/prateekagnihotri/cms-example)

1. Make sure that all the libraries mentioned in [requirements.txt](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/requirements.txt) are installed
2. Clone the repo
```sh
git clone https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation.git
```
3. Change current directory to the cloned directory and execute main.py with the required arguments
```sh
python main.py --path='/kaggle/input/cmsnewsamples/new-smaples.csv' \
                --dataset='prompt_new'\
                --predict='pT'\
                --model='FCNN'\
                --epochs=50 \
                --batch_size=512\
                --folds="0,1,2,3,4,5,6,7,8,9" \
                --results='/kaggle/working/results'
```
Note: Give absolute paths as argument

## Results

### Regressing pT

| Metric | Prompt Muons Samples-1 | Prompt Muons Samples-2 | Displaced Muons Samples |
| :---: | :---: | :---: | :---: |
| MAE/pT | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/pT%20results/P1_MAE_pT.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/pT%20results/P2_MAE_pT.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/pT%20results/MAE_pT_displaced.png) |
| MAE | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/pT%20results/P1_MAE.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/pT%20results/P2_MAE.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/pT%20results/MAE_displaced.png) |
| Accuracy | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/pT%20results/P1_accuracy.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/pT%20results/P2_accuracy.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/pT%20results/Accuracy_displaced.png) |
| F1-score (pT>x) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/pT%20results/P1_f1_class_morethan.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/pT%20results/P2_f1_class_morethan.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/pT%20results/f1_class_morethan_displaced.png) |
| F1-score (pT<x) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/pT%20results/P1_f1_class_lessthan.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/pT%20results/P2_f1_class_lessthan.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/pT%20results/f1_class_lessthan_displaced.png) |

### Regressing 1/pT

| Metric | Prompt Muons Samples-1 | Prompt Muons Samples-2 | Displaced Muons Samples |
| :---: | :---: | :---: | :---: |
| MAE/pT | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/P1_1_pT_mae_pT.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/P2_1_pT_mae_pT.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/displ_1_pT_mae_pT.png) |
| MAE | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/P1_1_pT_mae.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/P2_1_pT_mae.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/displ_1_pT_mae.png) |
| Accuracy | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/P1_1_pT_accuracy.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/P2_1_pT_accuracy.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/displ_1_pT_accuracy.png) |
| F1-score (pT>x) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/P1_1_pT_f1_class_pT_morethan_x.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/P2_1_pT_f1_class_pT_morethan_x.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/displ_1_pT_f1_class_pT_morethan_x.png) |
| F1-score (pT<x) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/P1_1_pT_f1_class_pT_lessthan_x.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/P2_1_pT_f1_class_pT_lessthan_x.png) | ![](https://github.com/PRATEEKKUMARAGNIHOTRI/CMS_muon_transverse_momentum_estimation/blob/master/Results/displ_1_pT_f1_class_pT_lessthan_x.png) |
    
### Four class classification

* Prompt Muons Samples-1

| Model | 0-10 GeV | 10-30 GeV | 30-100 GeV | >100GeV |
|:---|:----:|:----:|:----:|----:|
| FCNN | 0.990 | 0.970 | 0.977 | 0.969 |
| CNN | 0.991 | 0.973 | 0.980 | 0.983 |

* Prompt Muons Samples-2

| Model | 0-10 GeV | 10-30 GeV | 30-100 GeV | >100GeV |
|:---|:----:|:----:|:----:|----:|
| FCNN | 0.990 | 0.975 | 0.981 | 0.958 |
| CNN | 0.991 | 0.976 | 0.983 | 0.983 |

* Displaced Muons Samples

| Model | 0-10 GeV | 10-30 GeV | 30-100 GeV | >100GeV |
|:---|:----:|:----:|:----:|----:|
| FCNN | 0.944 | 0.898 | 0.910 | 0.839 |
| CNN | 0.958 | 0.907 | 0.932 | 0.910 |