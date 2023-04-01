import os
from PIL import Image

classes_dir = '/Volumes/PortableSSD/thesis/dataset/classes/'

diseases_dir = '/Volumes/PortableSSD/thesis/dataset/diseases/'
directories = ['train', 'valid']
# for _, _, photos in os.walk(os.path.join(root_dir)):
#     for photo in photos:
#         if photo.startswith("._"):
#             os.remove(photo)

print(len(classes_dir))
classes_photos = []
v = 0
# for d in directories:
#     for dir, _, _ in os.walk(os.path.join(diseases_dir, d)):
#         if len(dir) == 0:
#             continue
#
#         for _, _, photos in os.walk(dir):
#             # print(dir)
#             for photo in photos:
#                 if photo.startswith('._'):
#                     print(photo)
#                     # os.remove(os.path.join(d, photo))
#             v += len(photos)
#             print(len(photos))
#             diseases_photos.extend(photos)

for d in directories:
    for dir, _, _ in os.walk(os.path.join(diseases_dir, d)):
        if len(dir) == 0:
            continue

        for _, _, photos in os.walk(dir):
            # print(dir)
            if dir.find("Corn_(maize)") != -1:
                for photo in photos:
                    classes_photos.append(photo)

# print(classes_photos)

for d in directories:
    for dir, _, _ in os.walk(os.path.join(diseases_dir, d)):
        directory = dir[50:]
        print(directory)
        if len(directory) == 0:
            continue

        for _, _, photos in os.walk(dir):
            for photo in photos:
                if photo in classes_photos:
                    os.remove(os.path.join(dir, photo))
                    classes_photos.remove(photo)
                    print(f'Image {photo} deleted...')

# print('--------------', v)
# y = 0
# for d in directories:
#     for dir, _, _ in os.walk(os.path.join(classes_dir, d)):
#         if len(dir) == 0:
#             continue
#
#         for _, _, photos in os.walk(dir):
#             # print(dir)
#             for photo in photos:
#                 if photo in diseases_photos:
#                     continue
#                 photo_path = os.path.join(dir, photo)
#                 print(photo_path)
#             # print(f'Photo {photo_path} removed.')
#                 if photo_path.find('Corn') != -1:
#                     os.remove(photo_path)
#                     print(f'Removed {photo_path}')



