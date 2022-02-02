import json
import math
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':

    print('-> Plot FB15k-237 attributive property frequency and create/export property filter.')

    # specify frequency bounds
    lower_bound = None
    upper_bound = None

    bounds = lower_bound and upper_bound

    if not lower_bound:
        lower_bound = 0
    if not upper_bound:
        upper_bound = int(1e8)  # just to be sure
    print('Frequency bounds:')
    print(f'{lower_bound = }')
    print(f'{upper_bound = }')

    # count the frequency of each attributive property
    attributive_relations = []
    with open('../../data/FB15k-237-attributive_triples/literals.txt') as in_file:
        for line in in_file.readlines():
            attributive_relations.append(line.split('\t')[1])
    counts = Counter(attributive_relations)

    # remove the over-present property "<http://rdf.freebase.com/ns/type.object.key>"
    counts.pop("<http://rdf.freebase.com/ns/type.object.key>", None)
    # sort by frequency
    counts = {k: v for (k, v) in sorted(counts.items(), key=lambda item: -item[1])}

    counts_tuples = list(counts.items())

    # filter according to bounds
    counts_tuples_filtered = list(filter(lambda tuple: lower_bound <= tuple[1] <= upper_bound, counts_tuples))

    literal_properties = list(counts.keys())
    index_upper_bound = literal_properties.index(counts_tuples_filtered[0][0])
    index_lower_bound = literal_properties.index(counts_tuples_filtered[-1][0])

    # new dict after filters are applied
    counts_filtered = dict(counts_tuples_filtered)

    num_literal_properties = len(list(counts.keys()))
    num_literal_properties_filtered = len(list(counts_filtered.keys()))

    num_attributive_triples = sum(counts.values())
    num_attributive_triples_filtered = sum(counts_filtered.values())

    print('Stats:')
    print(f'{num_literal_properties = }')
    print(f'{num_literal_properties_filtered = }')

    print(f'{num_attributive_triples = }')
    print(f'{num_attributive_triples_filtered = }')

    literal_property_frequency = [counts[p] for p in literal_properties]

    # generate plots plot
    y_pos = np.arange(len(literal_properties))
    literal_property_frequency = list(map(math.log, literal_property_frequency))

    plt.plot(y_pos, literal_property_frequency)

    plt.xlabel('$ID_p$')
    plt.ylabel('$ln( \# $ in FB15k-237$_{literals} )$')

    # save plot without bounds
    plt.savefig(f'../../data/FB15k-237-attributive_triples/attributive_properties_base.svg')

    # add bounds to the plot
    if bounds:
        plt.axvspan(0, index_upper_bound, color='red', alpha=0.1)
        plt.axvline(x=index_upper_bound, color='red')

        plt.axvspan(index_lower_bound, len(literal_properties), color='red', alpha=0.1)
        plt.axvline(x=index_lower_bound, color='red')

    plt.tight_layout()
    plt.savefig(f'../../data/FB15k-237-attributive_triples/attributive_properties_base_filter_threshold_{lower_bound}.svg')
    plt.show()

    with open(f'../../data/FB15k-237-attributive_triples/attributive_properties_base_filer_{lower_bound:08d}_{upper_bound:08d}.json', 'w') as out_filter:
        json.dump(list(counts_filtered.keys()), out_filter)

    with open(f'../../data/FB15k-237-attributive_triples/attributive_properties.json', 'w') as out_filter:
        json.dump(list(counts.keys()), out_filter)
