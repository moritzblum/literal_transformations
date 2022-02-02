import collections
import json
import os
import matplotlib.pyplot as plt
import numpy as np
import math


def transformation_Entity2Literal(source_dir='../data',
                     target_file='../data/FB15k-237_transformation_Datatype2Literal.txt',
                     property_filter=None):
    skipped = 0
    new_entities = []
    new_predicates = []


    with open(f'{source_dir}/literals.txt') as literal_input:
        with open(f'{source_dir}/tmp_literals_transformation_inc_duplicates.txt', 'w') as literal_out:
            for line in literal_input:
                subject, predicate, datatype, _ = line[:-1].split('\t')
                if predicate in property_filter or not len(property_filter):

                    new_entities.append(datatype) if datatype not in new_entities else None
                    new_predicates.append(predicate) if predicate not in new_predicates else None

                    literal_out.write(subject + '\t' + predicate + '\t' + datatype + '\n')
                else:
                    skipped += 1

    os.system(f"awk '!seen[$0]++' {source_dir}/tmp_literals_transformation_inc_duplicates.txt > {target_file}")
    os.system(f'rm {source_dir}/tmp_literals_transformation_inc_duplicates.txt')
    print(f'Triples added by Transformation 1 with filter {property_filter}:')
    num_lines = sum(1 for line in open(f'{target_file}'))
    print(f'{num_lines = }')
    return num_lines



if __name__ == '__main__':

    # create t1 without filter
    filter_file = '../data/attributive_properties_filter_key.json'
    out_file = '../data/FB15k-237_transformation_Datatype2Literal.txt'
    with open(filter_file) as in_filter:
        property_filter = json.load(in_filter)
    transformation_Entity2Literal(source_dir='../data',
        target_file=out_file,
        property_filter=property_filter)

    # process according to filter
    filter_file = '../data/attributive_properties_base_filer_00000000_00010000.json'
    out_file = '../data/FB15k-237_transformation_Datatype2Literal_00000000_00010000.txt'
    with open(filter_file) as in_filter:
        property_filter = json.load(in_filter)

    transformation_Entity2Literal(source_dir='../data',
                     target_file=out_file,
                     property_filter=property_filter)
    
    filter_file = '../data/attributive_properties_base_filer_00001000_00010000.json'
    out_file = '../data/FB15k-237_transformation_Datatype2Literal_00001000_00010000.txt'
    with open(filter_file) as in_filter:
        property_filter = json.load(in_filter)

    transformation_Entity2Literal(source_dir='../data',
                     target_file=out_file,
                     property_filter=property_filter)
                     
    filter_file = '../data/attributive_properties_base_filer_00010000_10000000.json'
    out_file = '../data/FB15k-237_transformation_Datatype2Literal_00010000_10000000.txt'
    with open(filter_file) as in_filter:
        property_filter = json.load(in_filter)

    transformation_Entity2Literal(source_dir='../data',
                     target_file=out_file,
                     property_filter=property_filter)    
                    
