import json
import os
import re
from typing import List
from utils import preprocess_string, spacy_nlp
import time
import os.path as osp

"""
Applies the Value2Shingles transformation to a literal file as created by enrich_fb_15k-237_literals.py.
"""


# consider only literals which are produce meaningful shingles
def get_shingles(input_string: str, size: int) -> List[str]:
    if input_string is None:
        return []
    return [input_string[index:index + size] for index in range(len(input_string) - size + 1)]


def transformation_Value2Shingles(source_dataset='FB15k-237',
                                  transformation_name='FB15k-237_transformation_Vale2Shingles.txt',
                                  literal_file='FB15k-237_literals.txt',
                                  data_dir='../data',
                                  property_filter=None,
                                  preprocess_lowercasing=False,
                                  preprocess_lemmatizing=False):
    timestr = time.strftime("%Y%m%d-%H%M%S")

    with open(literal_file) as literal_input:
        with open(f'./tmp_shingles_{timestr}.txt', 'w') as literal_out:
            for line in literal_input:
                subject, predicate, datatype, value = line[:-1].split('\t')
                if predicate in property_filter or not len(property_filter):
                    value = preprocess_string(value, preprocess_lowercasing, preprocess_lemmatizing, spacy_nlp,
                                              datatype)
                    for shingle in get_shingles(value, 7):
                        literal_out.write(shingle + '\n')

    os.system(f'sort ./tmp_shingles_{timestr}.txt | uniq -c > ./tmp_shingles_count_{timestr}.txt')

    max_num_triples = 0
    interesting_shingles = []
    prog_count = re.compile("(\s+\d+\s)")
    with open(f'./tmp_shingles_count_{timestr}.txt') as shinges_count_in:
        for line in shinges_count_in.readlines():
            line = line[:-1]
            re_count = prog_count.search(line)

            count = int(re_count.group(0))
            shingle = line[re_count.span()[1]:]

            if count > 1000:
                max_num_triples += count
                interesting_shingles.append(shingle)

    print('# different shingles:', max_num_triples)
    print('# frequent shingles:', len(interesting_shingles))

    with open(literal_file) as literal_input:
        with open(f'./tmp_literals_transformation_Value2Shingles_inc_duplicates_{timestr}.txt', 'w') as literal_out:
            for line in literal_input:
                subject, predicate, datatype, value = line[:-1].split('\t')
                if predicate in property_filter or not len(property_filter):
                    value = preprocess_string(value, preprocess_lowercasing, preprocess_lemmatizing, spacy_nlp,
                                              datatype)
                    for shingle in get_shingles(value, 7):
                        if shingle in interesting_shingles:
                            literal_out.write(subject + '\t' + predicate + '\t' + shingle + '\n')

    os.system(
        f"awk '!seen[$0]++' ./tmp_literals_transformation_Value2Shingles_inc_duplicates_{timestr}.txt > {target_file}")
    os.system(f'rm ./tmp_literals_transformation_Value2Shingles_inc_duplicates_{timestr}.txt')
    os.system(f'rm ./tmp_shingles_{timestr}.txt')
    os.system(f'rm ./tmp_shingles_count_{timestr}.txt')
    print(f'Triples added by Value2Shingles transformation written:')
    num_lines = sum(1 for _ in open(f'{osp.join(data_dir, transformation_name)}'))
    print(f'num_lines:{num_lines}')
    return num_lines


if __name__ == '__main__':
    # create filter without http://rdf.freebase.com/key and _id properties
    # with open('../data/attributive_properties.json') as in_filter:
    #    property_filter = json.load(in_filter)
    #    property_filter = [p for p in property_filter if 'http://rdf.freebase.com/key' not in p and '_id' not in p]
    #
    # with open('../data/attributive_properties_filter_key.json', 'w') as out_filter:
    #    json.dump(property_filter, out_filter)

    filter_file = '../data/attributive_properties_filter_key.json'

    with open(filter_file) as in_filter:
        property_filter = json.load(in_filter)

    transformation_Value2Shingles(source_dataset='FB15k-237',
                                  transformation_name='FB15k-237_transformation_Value2Shingles.txt',
                                  literal_file='../data/FB15k-237_literals.txt',
                                  property_filter=property_filter,
                                  preprocess_lowercasing=False,
                                  preprocess_lemmatizing=False)

    # transformation_Value2Shingles(source_dataset='FB15k-237',
    #                              transformation_name='YAGO3-10_transformation_Value2Shingles.txt',
    #                               literal_file='../data/YAGO3-10_literals.txt',
    #                              property_filter=[])

    # transformation_Value2Shingles(source_dataset='FB15k-237',
    #                              transformation_name='../data/LitWD48K_transformation_Value2Shingles.txt',
    #                               literal_file='../data/LitWD48K_literals.txt',
    #                              property_filter=[])

    # transformation_Value2Shingles(source_dataset='FB15k-237',
    #                              transformation_name='FB15k-237_transformation_Value2Shingles_low_lemm.txt',
    #                               literal_file='../data/FB15k-237_literals.txt',
    #                              property_filter=property_filter,
    #                              preprocess_lowercasing=True,
    #                              preprocess_lemmatizing=True)

    transformation_Value2Shingles(source_dataset='FB15k-237',
                                  transformation_name='FB15k-237_transformation_Value2Shingles_low.txt',
                                  literal_file='../data/FB15k-237_literals.txt',
                                  property_filter=property_filter,
                                  preprocess_lowercasing=True,
                                  preprocess_lemmatizing=False)
