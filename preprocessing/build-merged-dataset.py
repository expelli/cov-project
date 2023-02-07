import os
import tensorflow.keras as keras
import shutil 

real_dataset = "./data/kaggle-rome-weather-dataset-resized/"
new_data_dir = "./data/rome-validation/"
new_data_dir_training =  "./data/rome-dalle-variation-prompt/"
batch_size = 16
number_images = 50
image_height = 224
image_width = 224
nr_color_channels = 3
seed = 2023


# basically mimic the train test split so we can merge artificial and dalle images without mixing dalle images
# into the validation data

datagen = keras.preprocessing.image.ImageDataGenerator(rescale=(1. / 255), shear_range=0.1, zoom_range=0.1, rotation_range=10, horizontal_flip=True, fill_mode='constant', validation_split=0.2, cval=0)
img_test = datagen.flow_from_directory(real_dataset, target_size=( image_width, image_height), batch_size=batch_size, subset='validation', seed=seed, class_mode='categorical')

print(img_test.filenames)

classes = [_ for _  in os.listdir(real_dataset) if not _.endswith(".gitkeep")]
if (not os.path.exists(new_data_dir)):
    print("creating dir: "+new_data_dir)
    os.mkdir(new_data_dir)
    for c in classes:
        os.mkdir(new_data_dir+c.lower())

if (not os.path.exists(new_data_dir_training)):
    print("creating dir: "+new_data_dir_training)
    os.mkdir(new_data_dir_training)
    for c in classes:
        os.mkdir(new_data_dir_training+c.lower())
        


# copy real data if part of validation 
for c in classes:
    filenames = [_ for _ in os.listdir(real_dataset+c)]
    for f in filenames:
        if c+"\\"+f in img_test.filenames:
            pass#shutil.copy2(real_dataset+c+"/"+f,new_data_dir+c+"/"+f)
        else: 
            shutil.copy2(real_dataset+c+"/"+f,new_data_dir_training+c+"/"+f)

