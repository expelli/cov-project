import os, random, shutil


data_dir = "./data/kaggle-5-class-weather-dataset/"
new_data_dir = "./data/kaggle-5-class-weather-dataset-cropped/"
seed = 2023
nr_samples = 50

random.seed(seed)

classes = [_ for _  in os.listdir(data_dir) if not _.endswith(".gitkeep")]
if (not os.path.exists(new_data_dir)):
    print("creating dir: "+new_data_dir)
    os.mkdir(new_data_dir)
    for c in classes:
        os.mkdir(new_data_dir+c.lower())

for c in classes:
    filenames = [_ for _ in os.listdir(data_dir+c)]
    selected_files = random.sample(filenames,nr_samples)
    for f in selected_files:
        shutil.copy2(data_dir+c+"/"+f,new_data_dir+c+"/"+f)
    
