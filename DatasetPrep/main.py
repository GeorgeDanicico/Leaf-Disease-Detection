import os
from PIL import Image

root_dir = '/Volumes/PortableSSD/thesis/balanced_dataset/diseases/train/'
# for _, _, photos in os.walk(os.path.join(root_dir)):
#     for photo in photos:
#         if photo.startswith("._"):
#             os.remove(photo)



print(len(root_dir))
for dir, _, _ in os.walk(os.path.join(root_dir)):
    dir_name = dir[60:]

    if dir_name == '' or len(dir_name) == 0:
        continue
    for _, _, photos in os.walk(dir):
        # print(dir)
        for photo in photos:
            photo_path = os.path.join(dir, photo)
            print(photo_path)
            os.remove(photo_path)


