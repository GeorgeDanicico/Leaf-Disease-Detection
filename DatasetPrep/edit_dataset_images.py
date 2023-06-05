import os
from PIL import Image

root_dir = '/Volumes/PortableSSD/thesis/balanced_dataset/diseases'

save_dir = '/Volumes/PortableSSD/thesis/balanced_dataset/classes/'
directories = ['train', 'valid']
# for _, _, photos in os.walk(os.path.join(root_dir)):
#     for photo in photos:
#         if photo.startswith("._"):
#             os.remove(photo)

plants = ['Apple', 'Corn', 'grape', 'Potato', 'Strawberry', 'Tomato']

picture_counter: int = 1

for d in directories:
    for dir, _, _ in os.walk(os.path.join(root_dir, d)):

        directory = dir[60:]

        if len(directory) == 0 or directory == '':
            continue

        plant = directory.split("___")[0]

        save_to = os.path.join(save_dir, d)
        for _, _, photos in os.walk(dir):
            # print(save_to)
            for photo in photos:
                photo_path = os.path.join(dir, photo)
                # print(save_to, photo_path)
                try:
                    pass
                    picture = Image.open(photo_path)
                    # print(save_to + " " + photo_path)

                    save_dir_path = save_to + "/" + plant +  "/" + "picture" + str(picture_counter) + ".jpg"
                    print(photo_path, save_dir_path)
                    picture_counter += 1
                    picture.save(save_dir_path)
                    print(f'Saved photo to folder {save_dir_path}...')
                except:
                    pass
                finally:
                    pass
                    # os.remove(photo_path)


