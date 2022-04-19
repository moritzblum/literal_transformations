import json
import os
import os.path as osp
import shutil
import requests
from argparse import ArgumentParser

from transformation_Datatype2Entity import transformation_Datatype2Entity
from transformation_Literal2Entity import transformation_Literal2Entity
from transformation_Value2Shingles import transformation_Value2Shingles

from utils import download_files

data_dir = '../data'

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-init",
                        help="create data directory and download required files", default=False)
    parser.add_argument("-transform",
                        help="run transformations on tsv files", default=False)
    parser.add_argument("-export",
                        help="create folders s.t. they can be used for training with the literale codebase",
                        default=False)

    args = parser.parse_args()

    if args.init:
        print('running initialization')

        if not osp.exists(data_dir):
            os.mkdir(data_dir)

        if not osp.exists(osp.join(data_dir, 'FB15k-237')):
            url = 'https://github.com/SmartDataAnalytics/LiteralE/blob/master/datasets/FB15k-237.tar.gz?raw=true'
            r = requests.get(url, allow_redirects=True)
            open(osp.join(data_dir, 'FB15k-237.tar.gz'), 'wb').write(r.content)
            shutil.unpack_archive(osp.join(data_dir, 'FB15k-237.tar.gz'), osp.join(data_dir, 'FB15k-237'))

        if not osp.exists(osp.join(data_dir, 'YAGO3-10')):
            url = 'https://github.com/SmartDataAnalytics/LiteralE/blob/master/datasets/YAGO3-10.tar.gz?raw=true'
            r = requests.get(url, allow_redirects=True)
            open(osp.join(data_dir, 'YAGO3-10.tar.gz'), 'wb').write(r.content)
            shutil.unpack_archive(osp.join(data_dir, 'YAGO3-10.tar.gz'), osp.join(data_dir, 'YAGO3-10'))

            urls = [['numerical_data_test.txt',
                     'https://raw.githubusercontent.com/pouyapez/mkbe/master/datasets/YAGO-10%20plus/Numerical%20%20data_test.txt'],
                    ['numerical_data_train.txt',
                     'https://raw.githubusercontent.com/pouyapez/mkbe/master/datasets/YAGO-10%20plus/Numerical%20data_train.txt'],
                    ['textual_data.txt',
                     'https://raw.githubusercontent.com/pouyapez/mkbe/master/datasets/YAGO-10%20plus/Textual%20data.txt']]
            download_files(urls, osp.join(data_dir, 'YAGO3-10'))

        if not osp.exists(osp.join(data_dir, 'LitWD48K')):
            os.mkdir(osp.join(data_dir, 'LitWD48K'))
            urls = [('train.txt',
                     'https://raw.githubusercontent.com/GenetAsefa/LiterallyWikidata/main/Datasets/LitWD48K/train.txt'),
                    ('test.txt',
                     'https://raw.githubusercontent.com/GenetAsefa/LiterallyWikidata/main/Datasets/LitWD48K/test.txt'),
                    ('valid.txt',
                     'https://raw.githubusercontent.com/GenetAsefa/LiterallyWikidata/main/Datasets/LitWD48K/valid.txt'),
                    ('numeric_literals.txt',
                     'https://raw.githubusercontent.com/GenetAsefa/LiterallyWikidata/main/Datasets/LitWD48K/numeric_literals.txt'),
                    ('entity_aliases_en.txt',
                     'https://raw.githubusercontent.com/GenetAsefa/LiterallyWikidata/main/Datasets/Entities/entity_aliases_en.txt'),
                    ('entity_labels_en.txt',
                     'https://raw.githubusercontent.com/GenetAsefa/LiterallyWikidata/main/Datasets/Entities/entity_labels_en.txt'),
                    ('entity_types.txt',
                     'https://raw.githubusercontent.com/GenetAsefa/LiterallyWikidata/main/Datasets/Entities/entity_types.txt'),
                    ('entity_wikidata_descriptions_en.txt',
                     'https://raw.githubusercontent.com/GenetAsefa/LiterallyWikidata/main/Datasets/Entities/entity_wikidata_descriptions_en.txt'),
                    ('entity_wikipedia_descriptions_de.txt',
                     'https://github.com/GenetAsefa/LiterallyWikidata/blob/main/Datasets/Entities/entity_wikipedia_descriptions_de.txt.zip?raw=true'),
                    ('entity_wikipedia_descriptions_en.txt',
                     'https://github.com/GenetAsefa/LiterallyWikidata/blob/main/Datasets/Entities/entity_wikipedia_descriptions_en.txt.zip?raw=true'),
                    ('entity_wikipedia_descriptions_ru.txt',
                     'https://github.com/GenetAsefa/LiterallyWikidata/blob/main/Datasets/Entities/entity_wikipedia_descriptions_ru.txt.zip?raw=true'),
                    ('entity_wikipedia_descriptions_zh.txt',
                     'https://github.com/GenetAsefa/LiterallyWikidata/blob/main/Datasets/Entities/entity_wikipedia_descriptions_zh.txt.zip?raw=true')]
            download_files(urls, osp.join(data_dir, 'LitWD48K'))

    if args.transform:
        print('running transformations')

        literal_file_FB15k237 = osp.join(data_dir, 'FB15k-237_literals.txt')
        literal_file_YAGO310 = osp.join(data_dir, 'YAGO3-10_literals.txt')
        literal_file_LitWD48K = osp.join(data_dir, 'LitWD48K_literals.txt')

        with open(osp.join(data_dir, 'attributive_properties.json')) as in_filter:
            property_filter_fb = json.load(in_filter)

        with open(osp.join(data_dir, 'attributive_properties_base_filer_00000000_00010000.json')) as in_filter:
            property_filter_fb_00000000_00010000 = json.load(in_filter)

        with open(osp.join(data_dir, 'attributive_properties_base_filer_00001000_00010000.json')) as in_filter:
            property_filter_fb_00001000_00010000 = json.load(in_filter)

        with open(osp.join(data_dir, 'attributive_properties_base_filer_00010000_10000000.json')) as in_filter:
            property_filter_fb_00010000_10000000 = json.load(in_filter)

        transformation_Literal2Entity(transformation_name='FB15k-237_transformation_Literal2Entity',
                                      data_dir=data_dir,
                                      literal_file=literal_file_FB15k237,
                                      out_file='../data/FB15k-237_transformation_Literal2Entity.txt',
                                      property_filter=property_filter_fb,
                                      source_dataset='FB15k-237')

        transformation_Literal2Entity(transformation_name='YAGO3-10_transformation_Literal2Entity',
                                      data_dir=data_dir,
                                      literal_file=literal_file_YAGO310,
                                      out_file='../data/YAGO3-10_transformation_Literal2Entity.txt',
                                      property_filter=[])

        transformation_Literal2Entity(transformation_name='LitWD48K_transformation_Literal2Entity',
                                      data_dir=data_dir,
                                      literal_file=literal_file_LitWD48K,
                                      out_file='../data/LitWD48K_transformation_Literal2Entity.txt',
                                      property_filter=[])

        transformation_Literal2Entity(transformation_name='FB15k-237_transformation_Literal2Entity_low_lemm',
                                      data_dir=data_dir,
                                      literal_file=literal_file_FB15k237,
                                      out_file='../data/FB15k-237_transformation_Literal2Entity_low_lemm.txt',
                                      property_filter=property_filter_fb,
                                      preprocess_lowercasing=True,
                                      preprocess_lemmatizing=True)

        transformation_Literal2Entity(transformation_name='FB15k-237_transformation_Literal2Entity_low',
                                      data_dir=data_dir,
                                      literal_file=literal_file_FB15k237,
                                      out_file='../data/FB15k-237_transformation_Literal2Entity_low.txt',
                                      property_filter=property_filter_fb,
                                      preprocess_lowercasing=True,
                                      preprocess_lemmatizing=False)

        transformation_Datatype2Entity(literal_file=literal_file_FB15k237,
                                       out_file='../data/FB15k-237_transformation_Datatype2Entity.txt',
                                       property_filter=property_filter_fb)

        transformation_Datatype2Entity(literal_file=literal_file_FB15k237,
                                       out_file='../data/FB15k-237_transformation_Datatype2Entity_00000000_00010000.txt',
                                       property_filter=property_filter_fb_00000000_00010000)

        transformation_Datatype2Entity(literal_file=literal_file_FB15k237,
                                       out_file='../data/FB15k-237_transformation_Datatype2Entity_00001000_00010000.txt',
                                       property_filter=property_filter_fb_00001000_00010000)

        transformation_Datatype2Entity(literal_file=literal_file_FB15k237,
                                       out_file='../data/FB15k-237_transformation_Datatype2Entity_00010000_10000000.txt',
                                       property_filter=property_filter_fb_00010000_10000000)

        transformation_Datatype2Entity(literal_file=literal_file_YAGO310,
                                       out_file='../data/YAGO3-10_transformation_Datatype2Entity.txt',
                                       property_filter=[])

        transformation_Datatype2Entity(literal_file=literal_file_LitWD48K,
                                       out_file='../data/LitWD48K_transformation_Datatype2Entity.txt',
                                       property_filter=[])

        transformation_Value2Shingles(literal_file=literal_file_FB15k237,
                                      target_file='../data/FB15k-237_transformation_Value2Shingles.txt',
                                      property_filter=property_filter_fb)

        transformation_Value2Shingles(literal_file=literal_file_YAGO310,
                                      target_file='../data/YAGO3-10_transformation_Value2Shingles.txt',
                                      property_filter=[])

        transformation_Value2Shingles(literal_file=literal_file_LitWD48K,
                                      target_file='../data/LitWD48K_transformation_Value2Shingles.txt',
                                      property_filter=[])

        transformation_Value2Shingles(literal_file=literal_file_FB15k237,
                                      target_file='../data/FB15k-237_transformation_Value2Shingles_low_lemm.txt',
                                      property_filter=property_filter_fb,
                                      preprocess_lowercasing=True,
                                      preprocess_lemmatizing=True)

        transformation_Value2Shingles(literal_file=literal_file_FB15k237,
                                      target_file='../data/FB15k-237_transformation_Value2Shingles_low.txt',
                                      property_filter=property_filter_fb,
                                      preprocess_lowercasing=True,
                                      preprocess_lemmatizing=False)

    if args.export:
        # dic: source dataset -> transformation
        dataset_files = {
            'FB15k-237': [
                'FB15k-237_transformation_Literal2Entity.txt',
                'FB15k-237_transformation_Literal2Entity_low.txt',
                'FB15k-237_transformation_Literal2Entity_low_lemm.txt',
                'FB15k-237_transformation_Datatype2Entity.txt',
                'FB15k-237_transformation_Datatype2Entity_00000000_00010000.txt',
                'FB15k-237_transformation_Datatype2Entity_00001000_00010000.txt',
                'FB15k-237_transformation_Datatype2Entity_00001000_10000000.txt',
                'FB15k-237_transformation_Value2Shingles.txt',
                'FB15k-237_transformation_Value2Shingles_low.txt',
                'FB15k-237_transformation_Value2Shingles_low_lemm.txt'
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

        all_files = os.listdir(data_dir)

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
                    shutil.rmtree(osp.join(data_dir, transformation_dataset_folder))
                shutil.copytree(osp.join(data_dir, dataset), osp.join(data_dir, transformation_dataset_folder))
                with open(osp.join(data_dir, transformation_dataset_folder, 'train.txt'), 'a') as train_file:
                    with open(osp.join(data_dir, transformation_dataset), 'r') as transformation_triples_in:
                        for line in transformation_triples_in.readlines():
                            train_file.write(line)



