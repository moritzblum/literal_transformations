# looks which transformation files are given and creates the datasets for LiteralE training
import os
import shutil
import os.path as osp


# dic: source dataset -> transformation
dataset_files = {
    'FB15k-237': [
        'FB15k-237_transformation_Literal2Entity.txt',
        'FB15k-237_transformation_Datatype2Entity.txt',
        'FB15k-237_transformation_Datatype2Entity_00000000_00010000.txt',
        'FB15k-237_transformation_Datatype2Entity_00001000_00010000.txt',
        'FB15k-237_transformation_Datatype2Entity_00001000_10000000.txt',
        'FB15k-237_transformation_Value2Shingles.txt',
        'FB15k-237_transformation_Value2Shingle_low.txt',
        'FB15k-237_transformation_Value2Shingle_filter_low_lemm.txt'
    ],
    'YAGO3-10': [
        'YAGO3-10_transformation_Literal2Entity.txt',
        'YAGO3-10_transformation_Datatype2Literal.txt',
        'YAGO3-10_transformation_Value2Shingles.txt'
    ],
    'LitWD48K': [
        'LitWD48K_transformation_Literal2Entity.txt',
        'LitWD48K_transformation_Datatype2Literal.txt',
        'LitWD48K_transformation_Value2Shingles.txt'
    ]
}

source_dir = '../data'


all_files = os.listdir(source_dir)

for dataset in dataset_files.keys():
    if dataset not in all_files:
        print('source dataset missing:', dataset)
        continue
    print('creating transformation datasets for', dataset)
    for transformation_dataset in dataset_files[dataset]:
        if transformation_dataset not in all_files:
            print('file missing:', transformation_dataset)
            continue
        print('create transformation dataset', transformation_dataset)
        transformation_dataset_folder = transformation_dataset[:-4]
        if transformation_dataset_folder in all_files:
            shutil.rmtree(osp.join(source_dir, transformation_dataset_folder))
        shutil.copytree(osp.join(source_dir, dataset), osp.join(source_dir, transformation_dataset_folder))
        with open(osp.join(source_dir, transformation_dataset_folder, 'train.txt'), 'a') as train_file:
            with open(osp.join(source_dir, transformation_dataset), 'r') as transformation_triples_in:
                for line in transformation_triples_in.readlines():
                    train_file.write(line)






