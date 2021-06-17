# Active learning core set approach


#### To run

Install dependencies with Anaconda
```
conda activate active-learning-env
```

Run active learning
```
python3 run.py --Strategy <Strategy name>
```

--Strategy parameter is optional, can also be specified in config.py



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

