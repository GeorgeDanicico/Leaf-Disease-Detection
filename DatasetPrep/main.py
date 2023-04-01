import os
from PIL import Image

root_dir = '/Volumes/PortableSSD/thesis/dataset/classes/'

save_dir = '/Volumes/PortableSSD/thesis/dataset/classes/'
directories = ['train', 'valid']
# for _, _, photos in os.walk(os.path.join(root_dir)):
#     for photo in photos:
#         if photo.startswith("._"):
#             os.remove(photo)

plants = ['Apple', 'Corn', 'grape', 'Potato', 'Strawberry', 'Tomato']

print(len(root_dir))
for d in directories:
    for dir, _, _ in os.walk(os.path.join(root_dir, d)):
        dir_name = dir[(54 + len(d)):]
        plant = dir_name.split(' ')[0]

        if dir_name in plants or len(plant) == 0:
            continue
        # print(dir)
        save_to = os.path.join(root_dir, d, plant)
        for _, _, photos in os.walk(dir):
            # print(dir)
            for photo in photos:
                photo_path = os.path.join(dir, photo)
                # print(plant, save_to, photo_path)
                try:

                    picture = Image.open(photo_path)
                    # print(save_to + " " + photo_path)

                    save_dir_path = os.path.join(save_to, photo)
                    picture.save(save_dir_path)
                    print(f'Saved photo to folder {save_dir_path}...')
                except:
                    pass
                finally:
                    os.remove(photo_path)


