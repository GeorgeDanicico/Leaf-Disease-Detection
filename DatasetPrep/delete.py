import os
import random

from PIL import Image


diseases_dir = '/Volumes/PortableSSD/thesis/dataset/diseases/'
new_location = '/Volumes/PortableSSD/thesis/balanced_dataset/'
directories = ['train', 'valid']
# for _, _, photos in os.walk(os.path.join(root_dir)):
#     for photo in photos:
#         if photo.startswith("._"):
#             os.remove(photo)
print(len(diseases_dir))
images_distribution = [0, 0, 0]
v = 0

for d in directories:
    for dir, _, _ in os.walk(os.path.join(diseases_dir, d)):
        directory: str = dir[51:]
        if len(directory) == 0:
            continue

        plant = directory.split("___")[0]
        disease = directory

        dir_path = os.path.join(diseases_dir, d, directory)
        # print(dir_path)
        for _, _, photos in os.walk(os.path.join(diseases_dir, d, directory)):
            print(f'The directory {directory} from {d} has {len(photos)} photos.')

            if d == 'train':
                cnt = 1600
            else:
                cnt = 400

            for i in range(cnt):
                photo_path = os.path.join(dir_path, photos[i])
                if photo_path.find("._") != -1:
                    continue
                picture = Image.open(photo_path)
                # print(save_to + " " + photo_path)

                classes_dir_path = new_location + "classes/" + d + "/" + plant + "/" + photos[i]
                diseases_dir_path = new_location + "diseases/" + d + "/" + disease + "/" + photos[i]
                picture.save(classes_dir_path)
                picture.save(diseases_dir_path)
                # os.remove(photo_path)