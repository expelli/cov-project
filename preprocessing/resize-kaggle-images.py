import os
import cv2

data_dir = "./data/kaggle-rome-weather-dataset/"
new_data_dir = data_dir[:-1]+"-resized/"
desired_img_size = 224


print(new_data_dir)
classes = [_ for _  in os.listdir(data_dir) if not _.endswith(".gitkeep")]
if (not os.path.exists(new_data_dir)):
    print("creating dir: "+new_data_dir)
    os.mkdir(new_data_dir)
    for c in classes:
        os.mkdir(new_data_dir+c.lower())

for c in classes:
    for idx, filename in enumerate(os.listdir(data_dir+c)):
        img = cv2.imread(data_dir+c+"/"+filename)

        if isinstance(img,type(None)):
               print(data_dir+"/"+c+"/"+filename)
        else:
            # fetching the dimensions
            wid = int(img.shape[1])
            hgt = int(img.shape[0])
            if (wid > hgt):
                dim = (int(224*(wid/hgt)),224)
            else:
                dim = (224,int(224*(hgt/wid)))
            img = cv2.resize(img ,dim,interpolation=cv2.INTER_LANCZOS4)
            img = img[0:224,0:224]
            cv2.imwrite(new_data_dir+c.lower()+"/"+c+"-"+str(idx)+".jpg",img)

