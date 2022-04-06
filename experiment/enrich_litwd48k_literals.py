import os
import pandas as pd


if __name__ == '__main__':
    numeric_literals = pd.read_csv('../data/LitWD48K/numeric_literals.txt', sep='\t', header=None)
    numeric_literals[[3, 2]] = numeric_literals[2].str.split('\^\^', 1, expand=True)
    numeric_literals = numeric_literals[[0, 1, 2, 3]]

    de_literals = pd.read_csv('../data/LitWD48K/entity_wikipedia_descriptions_de.txt', sep='\t', header=None)
    de_literals[[2, 3]] = de_literals[1].str.split('@', 1, expand=True)
    de_literals[1] = 'hasWikipediaDescription'
    de_literals[3] = '@' + de_literals[3].astype(str)
    de_literals = de_literals[[0, 1, 3, 2]]
    de_literals.columns = [0, 1, 2, 3]

    en_literals = pd.read_csv('../data/LitWD48K/entity_wikipedia_descriptions_en.txt', sep='\t', header=None)
    en_literals[[2, 3]] = en_literals[1].str.split('@', 1, expand=True)
    en_literals[1] = 'hasWikipediaDescription'
    en_literals[3] = '@' + en_literals[3].astype(str)
    en_literals = en_literals[[0, 1, 3, 2]]
    en_literals.columns = [0, 1, 2, 3]

    ru_literals = pd.read_csv('../data/LitWD48K/entity_wikipedia_descriptions_ru.txt', sep='\t', header=None)
    ru_literals[[2, 3]] = ru_literals[1].str.split('@', 1, expand=True)
    ru_literals[1] = 'hasWikipediaDescription'
    ru_literals[3] = '@' + ru_literals[3].astype(str)
    ru_literals = ru_literals[[0, 1, 3, 2]]
    ru_literals.columns = [0, 1, 2, 3]

    zh_literals = pd.read_csv('../data/LitWD48K/entity_wikipedia_descriptions_zh.txt', sep='\t', header=None, on_bad_lines='skip')
    zh_literals[[2, 3]] = zh_literals[1].str.split('@', 1, expand=True)
    zh_literals[1] = 'hasWikipediaDescription'
    zh_literals[3] = '@' + zh_literals[3].astype(str)
    zh_literals = zh_literals[[0, 1, 3, 2]]
    zh_literals.columns = [0, 1, 2, 3]

    en_wikidata_literals = pd.read_csv('../data/LitWD48K/entity_wikidata_descriptions_en.txt', sep='\t', header=None)
    en_wikidata_literals[3] = en_wikidata_literals[1]
    en_wikidata_literals[1] = 'hasWikidataDescription'
    en_wikidata_literals[2] = '@en'
    en_wikidata_literals = en_wikidata_literals[[0, 1, 2, 3]]

    en_label = pd.read_csv('../data/LitWD48K/entity_labels_en.txt', sep='\t', header=None)
    en_label[3] = en_label[1]
    en_label[1] = 'hasLabel'
    en_label[2] = '@en'
    en_label = en_label[[0, 1, 2, 3]]

    en_alias = []
    with open('../data/LitWD48K/entity_aliases_en.txt') as en_alias_in:
        for line in en_alias_in.readlines():
            subject, aliases = line[:-1].split('\t')
            for alias in aliases.split(','):
                alias = alias.lstrip()
                en_alias.append([subject, 'hasAlias', '@en', alias])
    en_alias = pd.DataFrame(en_alias)

    literal_data = pd.concat([numeric_literals, de_literals, en_literals, ru_literals, zh_literals, en_wikidata_literals, en_label, en_alias], axis=0, ignore_index=True)
    literal_data.to_csv('../data/LitWD48K_literals_tmp.txt', sep='\t', header=None, index=False)

    with open('../data/LitWD48K_literals.txt', 'w') as literal_data_out:
        with open('../data/LitWD48K_literals_tmp.txt') as literal_data_in:
            for line in literal_data_in.readlines():
                try:
                    subject, predicate, datatype, value = line[:-1].split('\t')
                except ValueError:
                    continue
                if value == '':
                    continue
                literal_data_out.write('\t'.join([subject, predicate, datatype, value]) + '\n')
    os.system('rm ../data/LitWD48K_literals_tmp.txt')

    # add type relations to train edges: P31
    type_relations = pd.read_csv('../data/LitWD48K/entity_types.txt', sep='\t', header=None)
    type_relations[2] = 'P31'
    type_relations = type_relations[[0, 2, 1]]
    type_relations.columns = [0, 1, 2]
    type_relations.to_csv("train_types.txt", sep='\t', index=False, header=None)

    os.system('cd ../data/LitWD48K')
    os.system('cat ../data/LitWD48K/train.txt train_types.txt > train_tmp.txt')
    os.system('sort -u train_tmp.txt > ../data/LitWD48K/train.txt')
    os.system('rm train_tmp.txt')
    os.system('rm train_types.txt')

    # copy, reformat, move literal files for literale
    if not os.path.exists('../data/LitWD48K/literals'):
        os.mkdir('../data/LitWD48K/literals')

    en_literals = en_literals.drop(2, 1)
    en_literals.to_csv('../data/LitWD48K/literals/text_literals.txt', sep="\t", index=False, header=False)

    with open('../data/LitWD48K/literals/numerical_literals.txt', 'w') as out_file:
        for index, row in numeric_literals.iterrows():
            num = row[3]
            try:
                num = float(num)
                out_file.write('\t'.join([row[0], row[1], str(num)]) + '\n')
            except ValueError:
                print('passed')
                print(num)
                pass














