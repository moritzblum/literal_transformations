import pandas as pd

"""
Download and place in YAGO3-10
Relational data from: https://github.com/TimDettmers/ConvE/raw/master/YAGO3-10.tar.gz
Literal data from: https://github.com/pouyapez/mkbe/tree/master/datasets/YAGO-10%20plus
"""

if __name__ == '__main__':
    textual_data = pd.read_csv('../data/YAGO3-10/textual_data.txt', sep='\\t', header=None)
    numerical_data_train = pd.read_csv('../data/YAGO3-10/numerical_data_train.txt', sep='\\t', header=None)
    numerical_data_test = pd.read_csv('../data/YAGO3-10/numerical_data_test.txt', sep='\\t', header=None)
    numerical_data = pd.concat([numerical_data_train, numerical_data_test], axis=0, ignore_index=True)

    textual_data[2] = 'hasComment'
    textual_data[3] = 'xsd:string'
    textual_data = textual_data[[0, 2, 1, 3]]
    textual_data.columns = [0, 1, 2, 3]
    print(textual_data)
    textual_data.to_csv('../data/test.txt', sep=';', header=None, index=False)

    with open('../data/YAGO3-10/textual_data.txt') as yago_in:
        for line in yago_in.readlines():
            subject, literal = line[:-1].split('\t')
            if 'Concepción_Province,_Peru' in line:
                print(subject, '<<<<and>>>>',literal)



    numerical_data[3] = 'xsd:date'
    print(numerical_data)

    literal_data = pd.concat([numerical_data, textual_data], axis=0, ignore_index=True)[[0, 1, 3, 2]]
    literal_data.to_csv('../data/YAGO3-10_literals.txt', sep='\t', header=None, index=False)

