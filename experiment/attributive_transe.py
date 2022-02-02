import argparse
from pykeen.pipeline import pipeline
from experiment.dataloader import get_triples_factories

parser = argparse.ArgumentParser(description='Literal Transformation - TransE')
parser.add_argument('--dataset', default='../data/FB15k-237/')
parser.add_argument('--outfile', default='../data/pykeen_transe_results_FB15k-237.txt')
args = parser.parse_args()

train_set, valid_set, test_set = get_triples_factories(args.dataset)

pipeline_result = pipeline(
    training=train_set,
    testing=test_set,
    validation=valid_set,
    model='TransE',
    model_kwargs={
        "embedding_dim": 100,
        "scoring_fct_norm": 1,
        "entity_initializer": "xavier_uniform",
        "relation_initializer": "xavier_uniform",
        "entity_constrainer": "normalize"
    },
    optimizer="SGD",
    optimizer_kwargs={
        "lr": 0.01
    },
    loss="MarginRankingLoss",
    loss_kwargs={
        "reduction": "mean",
        "margin": 1
    },
    training_loop="SLCWA",
    negative_sampler="basic",
    negative_sampler_kwargs={
        "num_negs_per_pos": 1
    },
    training_kwargs={
        "num_epochs": 1000,
        "batch_size": 32
    },
    evaluator_kwargs={
        "filtered": True
    }
)

print(pipeline_result)
pipeline_result.save_to_directory(args.outfile)
