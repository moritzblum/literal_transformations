import collections
import json
import os
import matplotlib.pyplot as plt
import numpy as np
import math


def transformation_Literal2Entity(source_dir='../data',
                     target_file='../data/FB15k-237_transformation_Literal2Entity.txt',
                     property_filter=None):

    # create file with all potential objects created by this transformation
    with open(f'{source_dir}/literals.txt') as literal_input:
        with open(f'{source_dir}/tmp_literals_transformation_objects.txt', 'w') as literal_out:
            for line in literal_input:
                subject, predicate, datatype, value = line[:-1].split('\t')
                if predicate in property_filter or not len(property_filter):
                    value = value[1:-1]  # remove quotes
                    literal_out.write(value + 'x' + datatype + '\n')

    # remove all objects occurring only one time
    os.system(f'sort {source_dir}/tmp_literals_transformation_objects.txt > {source_dir}/tmp_literals_transformation_objects_sorted.txt')
    with open(f'{source_dir}/tmp_literals_transformation_objects_sorted.txt') as objects_in:
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
    print('Overall contained:', len(duplicates)/object_counter)

    # remove all objects connected to only one subject
    duplicates_counter = {object: [] for object in duplicates}
    with open(f'{source_dir}/literals.txt') as literal_input:
        for line in literal_input:
            subject, predicate, datatype, value = line[:-1].split('\t')
            if predicate in property_filter or not len(property_filter):
                value = value[1:-1]  # remove quotes
                if value + 'x' + datatype in duplicates:
                    duplicates_counter[value + 'x' + datatype].append(subject)
    duplicates = []
    for object in duplicates_counter.keys():
        if len(set(duplicates_counter[object])) > 1:
            duplicates.append(object)
    print('# objects connected to more than one subject', duplicates)

    with open('duplicates.json', 'w') as out_duplicates:
        json.dump({'duplicates': duplicates}, out_duplicates)

    # create transformation and only contain objects occurring more than one time
    with open(f'{source_dir}/literals.txt') as literal_input:
        with open(f'{source_dir}/tmp_literals_transformation_inc_duplicates.txt', 'w') as literal_out:
            for line in literal_input:
                subject, predicate, datatype, value = line[:-1].split('\t')
                if predicate in property_filter or not len(property_filter):
                    value = value[1:-1]  # remove quotes
                    if value + 'x' + datatype in duplicates:
                        literal_out.write(subject + '\t' + predicate + '\t' + value + 'x' + datatype + '\n')

    os.system(f"awk '!seen[$0]++' {source_dir}/tmp_literals_transformation_inc_duplicates.txt > {target_file}")
    os.system(f'rm {source_dir}/tmp_literals_transformation_objects.txt')
    os.system(f'rm {source_dir}/tmp_literals_transformation_objects_sorted.txt')
    os.system(f'rm {source_dir}/tmp_literals_transformation_inc_duplicates.txt')
    print(f'Triples added by Transformation 3 with filter {property_filter}:')
    num_lines = sum(1 for line in open(f'{target_file}'))
    print(f'{num_lines = }')
    return num_lines


if __name__ == '__main__':

    filter_file = '../data/attributive_properties_filter_key.json'
    out_file = '../data/FB15k-237_transformation_Literal2Entity.txt'

    with open(filter_file) as in_filter:
        property_filter = json.load(in_filter)
    transformation_Literal2Entity(source_dir='../data',
                     target_file=out_file,
                     property_filter=property_filter)
