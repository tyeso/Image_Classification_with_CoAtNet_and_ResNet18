import pandas as pd
import os

info_df = pd.read_csv('./Training_set_food.csv')

for root, dirs, files in os.walk('./data'):
    for file in files:
        if file.endswith('.jpg'):
            index = info_df['filename'].values.tolist().index(file)
            label = info_df['label'][index]

            if not os.path.exists(os.path.join(root, label)):
                os.makedirs(os.path.join(root, label))
            print('/'.join([root, label, file]))
            os.rename(os.path.join(root, file), '/'.join([root, label, file]))

