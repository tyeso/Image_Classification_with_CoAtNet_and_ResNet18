import os
from random import sample

folders = ['burgers', 'Pizza', 'Softdrinks']
for each_folder in folders:
    data_dir = './data/' + each_folder

    train = []
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.jpg'):
                filename = os.path.abspath(os.path.join(root, file))
                train.append(filename)

    train_split = 0.7
    val_split = 0.2
    test_split = 0.1

    total_data_n = len(train)
    val_n = int(total_data_n * 0.2)
    test_n = int(total_data_n * 0.1)

    val = sample(train, val_n)
    train = list(set(train)-set(val))

    test = sample(train, test_n)
    train = list(set(train)-set(test))

    if not os.path.exists(data_dir + '/val'):
        os.makedirs(data_dir + '/val')

    if not os.path.exists(data_dir + '/test'):
        os.makedirs(data_dir + '/test')

    for each_val in val:
        new_filename = data_dir + '/val/' + os.path.basename(each_val)
        print(new_filename)
        os.rename(each_val, new_filename)

    for each_test in test:
        new_filename = data_dir + '/test/' + os.path.basename(each_test)
        print(new_filename)
        os.rename(each_test, new_filename)