import collections
import os.path as osp

from tabulate import tabulate

dataset_dir = '../../data/FB15k-237-attributive_triples'
datasets = []#['FB15k-237-t1.txt',
            # 'FB15k-237-t3.txt',
            #'FB15k-237-t1_attributive_properties_base_filer_00001000_10000000.txt',
            #'FB15k-237-t1_attributive_properties_base_filer_00000000_00010000.txt',
            #'FB15k-237-t1_attributive_properties_base_filer_00001000_10000000.txt',
            #'FB15k-237-t5.txt']

stats = []
stats.append(['FB15k-237 (train)', 14541, 237, 272115])
for dataset in datasets:
    num_triples = 0
    properties = []
    entities = []

    with open(f'{osp.join(dataset_dir, dataset)}') as dataset_in:
        for line in dataset_in.readlines():
            num_triples += 1
            subject, property, object = line[:-1].split('\t')
            properties.append(property)
            entities.append(subject)
            entities.append(object)

    stats.append([dataset, len(set(entities)) + 14541, len(set(properties)) + 237, num_triples + 272115])

table = tabulate(stats, headers=['dataset', '# entities', '# properties', '# triples'])
print(table)

datatype_properties = 0
language_tags = 0
key_relation_triples = 0

datatypes = []
with open('../../data/FB15k-237-attributive_triples/literals.txt') as literal_input:
    for line in literal_input:
        subject, predicate, datatype, _ = line[:-1].split('\t')
        if datatype.startswith('xsd:'):
            datatype_properties += 1
        else:
            language_tags += 1
        if predicate == '<http://rdf.freebase.com/ns/type.object.key>':
            key_relation_triples += 1
        else:
            datatypes.append(datatype)


print('Attributive triples related to FB15k-237:', datatype_properties + language_tags)
print('with datatype_property triples:', datatype_properties)
print('with language_tag triples:', language_tags)
print('key relation datatype triples removed:', key_relation_triples)
datatypes = dict(collections.Counter(datatypes))
print(datatypes)
datatypes.pop('xsd:string', None)
print('literals with language tag:', sum(datatypes.values()))


