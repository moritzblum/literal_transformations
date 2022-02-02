import numpy as np
import torch
import os.path as osp
from pykeen.triples import TriplesFactory
from torch_geometric.data import Data


def tripe_files_2_np(triple_files):
    train_triples = []
    for triple_file in triple_files:
        with open(triple_file) as base_in:
            for line in base_in.readlines():
                train_triples.append(line[:-1].split('\t'))
    return np.array(train_triples)


def get_triples_factories(fb_base_dir='../../data/FB15k-237/raw/', attributive_triples_file=None, reverse_edges=False):
    """
    Dataloader for Pykeen.
    @param fb_base_dir:
    @param attributive_triples_file:
    @param reverse_edges:
    @return:
    """
    if attributive_triples_file:
        train_files = [osp.join(fb_base_dir, 'train.txt'), attributive_triples_file]
    else:
        train_files = [osp.join(fb_base_dir, 'train.txt')]

    train_triples = tripe_files_2_np(train_files)
    test_triples = tripe_files_2_np([osp.join(fb_base_dir, 'test.txt')])
    valid_triples = tripe_files_2_np([osp.join(fb_base_dir, 'valid.txt')])

    train_set = TriplesFactory.from_labeled_triples(train_triples, create_inverse_triples=reverse_edges)
    print('loaded train triples:', len(train_set.triples))

    test_set = TriplesFactory.from_labeled_triples(test_triples,
                                                   entity_to_id=train_set.entity_to_id,
                                                   relation_to_id=train_set.relation_to_id)
    print('loaded test triples:', len(test_set.triples))

    valid_set = TriplesFactory.from_labeled_triples(valid_triples,
                                                    entity_to_id=train_set.entity_to_id,
                                                    relation_to_id=train_set.relation_to_id)
    print('loaded validation triples:', len(valid_set.triples))

    return train_set, valid_set, test_set




