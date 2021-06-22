# Active learning core set approach


#### To run

Updatee Anaconda to latest version 
```
conda update conda
```

Install dependencies with Anaconda
```
conda env create -f environment.yml

conda activate al-env
```

Run active learning
```
python3 run.py --strategy <Strategy name> --dataset <Dataset name>
```

e.g

```
python3 run.py --strategy CIRAL --dataset CIFAR10
```

The strategy and dataset parameter is optional and can also be specified in config.py
The different strategies and datasets are listed below
### Strategies

| Strategy         | Command        |
|------------------|----------------|
| All data         | ALL-DATA       |
| BADGE            | BADGE          |
| CIRAL            | CIRAL          |
| CORESET          | CORESET        |
| DFAL             | DFAL           |
| K-MEANS          | KMEANS         |
| LEARNING LOSS    | LEARNING_LOSS  |
| MAX ENTROPY      | MAX_ENTROPY    |
| RANDOM BENCHMARK | RANDOM         |
| SOFTMAX HYBRID   | SOFTMAX_HYBRID |
| UNCERTAINTY      | UNCERTAINTY    |


### Datasets

| Dataset         | Command        |
|------------------|----------------|
| CIFAR-10         | CIFAR10       |
| KAGGLE            | PLANKTON10          |
| AILARON            | AILARON          |
| PASTORE          | PASTORE        |



## CIRAL framework

![data flow](/images/ciral-framework-new.png)



## Screen session

Screen session allows to detach terminal processes so that they continue when quitting the ssh-session. 

to create a screen in linux type 
```
screen
```

Detach screen 
```
Ctrl+a d
```
List screens 
```
screen -ls
```
Attach to screen 
```
screen -r <Screen Name>
```
to rename the screen
```
Ctrl+a, :sessionname <Screen Name>
```

to kill a screen, must be attached to the screen
```
Ctrl+A K, y
```

