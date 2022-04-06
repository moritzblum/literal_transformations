import os
import os.path as osp
import shutil
import tarfile

import requests

data_dir = '../data'

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

if not osp.exists(osp.join(data_dir, 'LitWD48K-test')):
    os.mkdir(osp.join(data_dir, 'LitWD48K-test'))
    urls = ['https://raw.githubusercontent.com/GenetAsefa/LiterallyWikidata/main/Datasets/LitWD48K/train.txt'
            'https://raw.githubusercontent.com/GenetAsefa/LiterallyWikidata/main/Datasets/LitWD48K/test.txt',
            'https://raw.githubusercontent.com/GenetAsefa/LiterallyWikidata/main/Datasets/LitWD48K/valid.txt',
            'https://raw.githubusercontent.com/GenetAsefa/LiterallyWikidata/main/Datasets/LitWD48K/numeric_literals.txt',
            'https://raw.githubusercontent.com/GenetAsefa/LiterallyWikidata/main/Datasets/Entities/entity_aliases_en.txt',
            'https://raw.githubusercontent.com/GenetAsefa/LiterallyWikidata/main/Datasets/Entities/entity_labels_en.txt',
            'https://raw.githubusercontent.com/GenetAsefa/LiterallyWikidata/main/Datasets/Entities/entity_types.txt',
            'https://raw.githubusercontent.com/GenetAsefa/LiterallyWikidata/main/Datasets/Entities/entity_wikidata_descriptions_en.txt',
            'https://github.com/GenetAsefa/LiterallyWikidata/blob/main/Datasets/Entities/entity_wikipedia_descriptions_de.txt.zip?raw=true',
            'https://github.com/GenetAsefa/LiterallyWikidata/blob/main/Datasets/Entities/entity_wikipedia_descriptions_en.txt.zip?raw=true',
            'https://github.com/GenetAsefa/LiterallyWikidata/blob/main/Datasets/Entities/entity_wikipedia_descriptions_ru.txt.zip?raw=true',
            'https://github.com/GenetAsefa/LiterallyWikidata/blob/main/Datasets/Entities/entity_wikipedia_descriptions_zh.txt.zip?raw=true']
    for url in urls:
        pass