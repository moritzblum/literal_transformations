import os.path as osp
from rdflib import Graph

from experiment.setup import data_dir

"""
Extract Literals form FB: First extract all triples with subject contained in a 
link prediction dataset (e.g. FB15k-237) as potentially relevant triples, then extract all attributive triples 
and write them reformatted to file.
"""


def extract_relevant_triples(link_prediction_dataset='../data/FB15k-237/',
                             out_file='../data/FB15k-237_freebase_reduced.txt',
                             fb_file='../data/freebase-rdf-latest'):
    """
    Extract all triples from the source Freebase graph with it's subject contained in a link prediction dataset (e.g. FB15k-237) 
    to reduce the size of potentially relevant triples.
    @return: None
    """

    # load all link prediction dataset entities
    source_entities = []
    for subset in ['train.txt', 'valid.txt', 'test.txt']:
        with open(osp.join(link_prediction_dataset, subset)) as subset_in:
            for line in subset_in:
                head, relation, target = line[:-1].split('\t')
                source_entities.append('<http://rdf.freebase.com/ns/' + head[1:][:-1].replace('/', '.') + '>')
                source_entities.append('<http://rdf.freebase.com/ns/' + target[1:][:-1].replace('/', '.') + '>')
    source_entities = set(source_entities)

    # output all triples where the subject in contained in the FB15k-237 dataset
    literals_out = open(out_file, 'w')

    if not osp.exists(osp.join(data_dir, 'freebase-rdf-latest')):
        raise FileNotFoundError(
            "Please download the latest freebase dump drom `https://developers.google.com/freebase` and place the unpacked file in",
            data_dir)

    with open(fb_file) as fb_in:
        for line in fb_in:
            line = line[:-1]  # remove linebreak
            triple = line.split('\t')
            if triple[0] in source_entities:
                literals_out.write(line + '\n')


def extract_attributive_triples(out_file='../data/FB15k-237_literals.txt',
                                relevant_triples_file='../data/FB15k-237_freebase_reduced.txt'):
    """
    Filters to a set of attributive triples, re-formats the literals (tsv: subject, predicate, datatype, value),
    and writes them to file.
    @return: None
    """

    attributive_relations = []
    with open(out_file, 'w') as literals_out:
        with open(relevant_triples_file) as relevant_triples_in:
            for line in relevant_triples_in.readlines():
                head, relation, target = line[:-1].split('\t')[:3]

                # only consider attributive triples and reformat the literal
                if not target.startswith('<') and not target.endswith('>'):

                    # new properties
                    if relation not in attributive_relations:
                        attributive_relations.append(relation)

                    g = Graph()
                    g.parse(data=line, format='n3')
                    for triple in g:
                        head = head.replace('<http://rdf.freebase.com/ns', '').replace('>', '').replace('.', '/')
                        if triple[2].datatype:
                            literals_out.write(
                                head + '\t' + relation + '\t' + triple[2].datatype + '\t' + repr(triple[
                                                                                                     2].value) + '\n')
                        elif triple[2].language:
                            literals_out.write(
                                head + '\t' + relation + '\t' + triple[2].language + '\t' + repr(triple[
                                                                                                     2].value) + '\n')
                        else:  # string is default
                            literals_out.write(head + '\t' + relation + '\t' + 'xsd:string' + '\t' + repr(triple[
                                                                                                              2].value) + '\n')


if __name__ == '__main__':
    if not osp.exists(osp.join(data_dir, 'FB15k-237_literals.txt')):
        # extract all potentially relevant triples from freebase to reduce the dataset size
        extract_relevant_triples()
        # filter the n-triple file for attributive triples and simplify reformat
        extract_attributive_triples()
