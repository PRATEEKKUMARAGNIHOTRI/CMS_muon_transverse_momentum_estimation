# Deep learning algorithms for muon momentum estimation in the CMS Trigger System

The Compact Muon Solenoid (CMS) is a general-purpose detector at the Large Hadron Collider (LHC). During a run, it generates about 40 TB data per second. Since It is not feasible to readout and store such a vast amount of data, so a trigger system selects and stores only interesting events or events likely to reveal new physics phenomena. The goal of this project is to benchmark the muon momentum estimation performance of Fully Connected Neural Networks (FCNN), Convolutional Neural Networks (CNN), and Graph Neural Networks (GNN), on the **prompt and displaced muon samples collected by CSC stations at CMS** to aid trigger system's high transverse momentum muon selection.

## About

The code is 

## How to use

> An example of how to use is available [here](https://www.kaggle.com/prateekagnihotri/cms-example)

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

## Results