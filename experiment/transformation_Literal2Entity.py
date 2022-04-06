import collections
import json
import os
import shutil
import os.path as osp

from utils import preprocess_string, spacy_nlp

"""
Applies the Literal2Entity transformation to a literal file as created by enrich_fb_15k-237_literals.py.
"""


def transformation_Literal2Entity(transformation_name='FB15k-237_transformation_Literal2Entity.txt',
                                    literal_file='../data/FB15k-237_literals.txt',
                                  out_file='../data/FB15k-237_transformation_Literal2Entity.txt',
                                  property_filter=None, preprocess_lowercasing=False, preprocess_lemmatizing=False,
                                  source_dataset='FB15k-237'):
    datatypes = []
    # create file with all potential objects created by this transformation
    with open(literal_file) as literal_input:
        with open('./tmp_literals_transformation_Literal2Entity_objects.txt', 'w') as literal_out:
            for line in literal_input:
                subject, predicate, datatype, value = line[:-1].split('\t')
                if predicate in property_filter or not len(property_filter):
                    value = preprocess_string(value, preprocess_lowercasing, preprocess_lemmatizing, spacy_nlp,
                                              datatype)
                    literal_out.write(value + 'x' + datatype + '\n')
                    datatypes.append(datatype)
    # stats
    if preprocess_lemmatizing:
        freq_tags = collections.Counter(datatypes)
        covered_tags = 0
        all_tags = len(datatypes)
        for key in spacy_nlp.keys():
            covered_tags += freq_tags[key]
        print(f'literals covered by lemmatization: {covered_tags / all_tags}% ({covered_tags} of {all_tags})')

    # remove all objects occurring only once
    os.system(
        'sort ./tmp_literals_transformation_Literal2Entity_objects.txt > ./tmp_literals_transformation_Literal2Entity_objects_sorted.txt')
    with open('./tmp_literals_transformation_Literal2Entity_objects_sorted.txt') as objects_in:
        object_counter = 0
        duplicates = []
        last_line = ''
        recognized = False
        for line in objects_in.readlines():
            line = line[:-1]  # remove linebreak
            object_counter += 1
            if line == last_line and not recognized:
                duplicates.append(line)
                recognized = True
            elif line != last_line:
                recognized = False
            last_line = line
    print('# objects:', object_counter)
    print('# objects occurring more than one time:', len(duplicates))
    print('Overall contained:', len(duplicates) / object_counter)

    # remove all objects connected to only one subject
    duplicates_counter = {target: [] for target in duplicates}
    with open(literal_file) as literal_input:
        for line in literal_input:
            subject, predicate, datatype, value = line[:-1].split('\t')
            if predicate in property_filter or not len(property_filter):
                value = preprocess_string(value, preprocess_lowercasing, preprocess_lemmatizing, spacy_nlp,
                                          datatype)
                if value + 'x' + datatype in duplicates and value != '':
                    duplicates_counter[value + 'x' + datatype].append(subject)
    duplicates = []
    for target in duplicates_counter.keys():
        if len(set(duplicates_counter[target])) > 1:
            duplicates.append(target)
    print('# objects connected to more than one subject', duplicates)

    with open('./duplicates.json', 'w') as out_duplicates:
        json.dump({'duplicates': duplicates}, out_duplicates)

    # create transformation and only contain objects occurring more than one time
    with open(literal_file) as literal_input:
        with open('./tmp_literals_transformation_Literal2Entity_inc_duplicates.txt', 'w') as literal_out:
            for line in literal_input:
                subject, predicate, datatype, value = line[:-1].split('\t')
                if predicate in property_filter or not len(property_filter):
                    value = preprocess_string(value, preprocess_lowercasing, preprocess_lemmatizing, spacy_nlp,
                                              datatype)
                    if value + 'x' + datatype in duplicates:
                        literal_out.write(subject + '\t' + predicate + '\t' + value + 'x' + datatype + '\n')

    os.system(f"awk '!seen[$0]++' ./tmp_literals_transformation_Literal2Entity_inc_duplicates.txt > {out_file}")
    os.system('rm ./tmp_literals_transformation_Literal2Entity_objects.txt')
    os.system('rm ./tmp_literals_transformation_Literal2Entity_objects_sorted.txt')
    os.system('rm ./tmp_literals_transformation_Literal2Entity_inc_duplicates.txt')
    os.system('rm ./duplicates.json')
    print(f'Triples added by Literal2Entity transformation written to {out_file}:')
    num_lines = sum(1 for _ in open(f'{out_file}'))

    print(f'num_lines:{num_lines}')

    shutil.copytree(osp.join('../data', source_dataset), osp.join('../data', transformation_name))

    return num_lines


if __name__ == '__main__':
    # attributive_properties_filter_key
    filter_file = '../data/attributive_properties.json'

    with open(filter_file) as in_filter:
        property_filter = json.load(in_filter)

    transformation_Literal2Entity(transformation_name='FB15k-237_transformation_Literal2Entity',
                                  literal_file='../data/FB15k-237_literals.txt',
                                  out_file='../data/FB15k-237_transformation_Literal2Entity.txt',
                                  property_filter=property_filter,
                                  source_dataset='FB15k-237')

    # transformation_Literal2Entity(literal_file='../data/YAGO3-10_literals.txt',
    #                              out_file='../data/YAGO3-10_transformation_Literal2Entity.txt',
    #                              property_filter=[])
    # transformation_Literal2Entity(literal_file='../data/LitWD48K_literals.txt',
    #                               out_file='../data/LitWD48K_transformation_Literal2Entity.txt',
    #                               property_filter=[])

    transformation_Literal2Entity(literal_file='../data/FB15k-237_literals.txt',
                                  out_file='../data/FB15k-237_transformation_Literal2Entity_low_lemm.txt',
                                  property_filter=property_filter,
                                  preprocess_lowercasing=True,
                                  preprocess_lemmatizing=True)

    transformation_Literal2Entity(literal_file='../data/FB15k-237_literals.txt',
                                  out_file='../data/FB15k-237_transformation_Literal2Entity_low.txt',
                                  property_filter=property_filter,
                                  preprocess_lowercasing=True,
                                  preprocess_lemmatizing=False)
