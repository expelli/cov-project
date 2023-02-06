import os
import cv2

data_dir = "./rome-weather-dataset/"
new_data_dir = "./rome-weather-dataset-resized/"
desired_img_size = 224


for c in os.listdir(data_dir):
    for idx, filename in enumerate(os.listdir(data_dir+"/"+c)):
        img = cv2.imread(data_dir+"/"+c+"/"+filename)
        # fetching the dimensions
        wid = int(img.shape[1])
        hgt = int(img.shape[0])
        if (wid > hgt):
            dim = (int(224*(wid/hgt)),224)
        else:
            dim = (224,int(224*(hgt/wid)))
        img = cv2.resize(img ,dim,interpolation=cv2.INTER_LANCZOS4)
        img = img[0:224,0:224]
        cv2.imwrite(new_data_dir+c+"/"+c+"-"+str(idx)+".jpg",img)

