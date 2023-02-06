# cov-project

## Setup: Conda environment

### 1) Ensure conda is installed
### 2) Adapt the prefix: line in the environment.yml to your installation path of conda (end of file)
```
<...>
prefix: <your-path-to-conda>\envs\cov-project
```
### 3) Generate conda environment from environment.yml using the following command: 
```
conda env create -f environment.yml
```

### 4) Activate the environment
```
conda activate cov-project
```

### 5) [In case of new package installations] Export new environment yaml using the following command
```
conda env export --no-builds > environment.yml
```


## Setup: Rome weather classification dataset

### 1) Download the rome weather classifcation dataset from: https://www.kaggle.com/datasets/rogeriovaz/rome-weather-classification
### 2) Unpack the dowloaded zip archive 
### 3) Copy the subdirectory contents of the unpacked archive into rome-weather-dataset so it contains the different category folders 
```
├── rome-weather-dataset
|  ├── Cloudy
|  ├── Foggy
|  ├── Rainy
|  ├── Snowy
|  ├── Sunny
```
