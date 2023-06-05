import os
import random

from PIL import Image


diseases_dir = '/Volumes/PortableSSD/thesis/balanced_dataset/diseases'
new_location = '/Volumes/PortableSSD/thesis/balanced_dataset/'
directories = ['train', 'valid']
# for _, _, photos in os.walk(os.path.join(root_dir)):
#     for photo in photos:
#         if photo.startswith("._"):
#             os.remove(photo)
print(len(diseases_dir))
# images_distribution = [0, 0, 0]
# v = 0
#
# for d in directories:
#     for dir, _, _ in os.walk(os.path.join(diseases_dir, d)):
#         directory: str = dir[60:]
#         if len(directory) == 0:
#             continue
#
#         disease = directory
#
#         dir_path = os.path.join(diseases_dir, d, directory)
#         # print(dir_path)
#         print(directory)