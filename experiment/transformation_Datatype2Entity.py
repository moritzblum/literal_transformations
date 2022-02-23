import json
import os

"""
Applies the Datatype2Entity transformation to a literal file as created by enrich_fb_15k-237_literals.py.
"""


def transformation_Datatype2Entity(literal_file='../data/FB15k-237_literals.txt',
                                   out_file='../data/FB15k-237_transformation_Datatype2Literal.txt',
                                   property_filter=None):
    new_entities = []
    new_predicates = []
    with open(literal_file) as literal_input:
        with open('./tmp_literals_transformation_Datatype2Entity_inc_duplicates.txt', 'w') as literal_out:
            for line in literal_input:
                subject, predicate, datatype, _ = line[:-1].split('\t')
                if predicate in property_filter or not len(property_filter):
                    new_entities.append(datatype) if datatype not in new_entities else None
                    new_predicates.append(predicate) if predicate not in new_predicates else None
                    literal_out.write(subject + '\t' + predicate + '\t' + datatype + '\n')

    os.system(f"awk '!seen[$0]++' ./tmp_literals_transformation_Datatype2Entity_inc_duplicates.txt > {out_file}")
    os.system('rm ./tmp_literals_transformation_Datatype2Entity_inc_duplicates.txt')
    print(f'Triples added by Datatype2Literal transformation written to {out_file}:')
    num_lines = sum(1 for _ in open(f'{out_file}'))
    print(f'num_lines:{num_lines}')
    return num_lines


if __name__ == '__main__':
    # create t1 without filter
    #filter_file = '../data/attributive_properties_filter_key.json'
    #out_file = '../data/FB15k-237_transformation_Datatype2Literal.txt'
    #with open(filter_file) as in_filter:
    #    property_filter = json.load(in_filter)
    #transformation_Datatype2Entity(literal_file='../data/FB15k-237_literals.txt',
    #                               out_file=out_file,
    #                               property_filter=property_filter)

    # process according to filter
    #filter_file = '../data/attributive_properties_base_filer_00000000_00010000.json'
    #out_file = '../data/FB15k-237_transformation_Datatype2Literal_00000000_00010000.txt'
    #with open(filter_file) as in_filter:
    #    property_filter = json.load(in_filter)

    #transformation_Datatype2Entity(literal_file='../data/FB15k-237_literals.txt',
    #                               out_file=out_file,
    #                               property_filter=property_filter)

    #filter_file = '../data/attributive_properties_base_filer_00001000_00010000.json'
    #out_file = '../data/FB15k-237_transformation_Datatype2Literal_00001000_00010000.txt'
    #with open(filter_file) as in_filter:
    #    property_filter = json.load(in_filter)

    #transformation_Datatype2Entity(literal_file='../data/FB15k-237_literals.txt',
    #                               out_file=out_file,
    #                               property_filter=property_filter)

    #filter_file = '../data/attributive_properties_base_filer_00010000_10000000.json'
    #out_file = '../data/FB15k-237_transformation_Datatype2Literal_00010000_10000000.txt'
    #with open(filter_file) as in_filter:
    #    property_filter = json.load(in_filter)

    #transformation_Datatype2Entity(literal_file='../data/FB15k-237_literals.txt',
    #                               out_file=out_file,
    #                               property_filter=property_filter)

    #transformation_Datatype2Entity(literal_file='../data/YAGO3-10_literals.txt',
    #                               out_file='../data/YAGO3-10_transformation_Datatype2Literal.txt',
    #                               property_filter=[])

    transformation_Datatype2Entity(literal_file='../data/LitWD48K_literals.txt',
                                   out_file='../data/LitWD48K_transformation_Datatype2Literal.txt',
                                   property_filter=[])
