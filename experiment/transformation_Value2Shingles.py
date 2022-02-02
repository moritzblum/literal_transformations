import json
import os
import re
from typing import List


# consider only literals which are produce meaningful shingles
def get_shinges(input_string: str, size: int) -> List[str]:
    return [input_string[index:index+size] for index in range(len(input_string) - size + 1)]


def transformation_5(source_dir='../data',
                     target_file='../data/FB15k-237_transformation_Value2Shingles.txt',
                     property_filter=None):

    with open(f'{source_dir}/literals.txt') as literal_input:
        with open(f'{source_dir}/tmp_shingles.txt', 'w') as literal_out:
            for line in literal_input:
                subject, predicate, datatype, value = line[:-1].split('\t')
                if predicate in property_filter or not len(property_filter):
                    for shingle in get_shinges(value, 7):
                        literal_out.write(shingle + '\n')

    os.system(f'sort {source_dir}/tmp_shingles.txt | uniq -c > {source_dir}/tmp_shingles_count.txt')

    max_num_triples = 0
    interesting_shingles = []
    prog_count = re.compile("(\s+\d+\s)")
    with open(f'{source_dir}/tmp_shingles_count.txt') as shinges_count_in:
        for line in shinges_count_in.readlines():
            line = line[:-1]
            re_count = prog_count.search(line)

            count = int(re_count.group(0))
            shingle = line[re_count.span()[1]:]

            if count > 1000:
                max_num_triples += count
                interesting_shingles.append(shingle)


    print('count:', max_num_triples)
    print('num_nodes:', len(interesting_shingles))

    with open(f'{source_dir}/literals.txt') as literal_input:
        with open(f'{source_dir}/tmp_literals_transformation_inc_duplicates.txt', 'w') as literal_out:
            for line in literal_input:
                subject, predicate, datatype, value = line[:-1].split('\t')
                if predicate in property_filter or not len(property_filter):
                    for shingle in get_shinges(value, 7):
                        if shingle in interesting_shingles:
                            literal_out.write(subject + '\t' + predicate + '\t' + shingle + '\n')

    os.system(f"awk '!seen[$0]++' {source_dir}/tmp_literals_transformation_inc_duplicates.txt > {target_file}")
    os.system(f'rm {source_dir}/tmp_literals_transformation_inc_duplicates.txt')
    os.system(f'rm{source_dir}/tmp_shingles.txt')
    os.system(f'rm{source_dir}/tmp_shingles_count.txt')
    print(f'Triples added by Transformation 5 with filter {property_filter}:')
    num_lines = sum(1 for _ in open(f'{target_file}'))
    print(f'{num_lines = }')
    return num_lines


if __name__ == '__main__':

    # create filter without http://rdf.freebase.com/key and _id properties
    with open('../../data/FB15k-237-attributive_triples/attributive_properties.json') as in_filter:
        property_filter = json.load(in_filter)
        property_filter = [p for p in property_filter if 'http://rdf.freebase.com/key' not in p and '_id' not in p]

    with open(f'../../data/FB15k-237-attributive_triples/attributive_properties_filter_key.json', 'w') as out_filter:
        json.dump(property_filter, out_filter)

    print('transformation 5: shingles')

    filter_file = '../data/attributive_properties_filter_key.json'
    out_file = '../data/FB15k-237_transformation_Value2Shingles.txt'

    with open(filter_file) as in_filter:
        property_filter = json.load(in_filter)

    transformation_5(source_dir='../data',
                     target_file=out_file,
                     property_filter=property_filter)

