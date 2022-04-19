# Exploring the impact of literal transformations within Knowledge Graphs for Link Prediction


## Set-up 
Our transformations are implemented in Python. To replicate our results, we recommend conda with
Python 3.8:
1. `conda create --name literal_transformations python=3.8`
2. `conda install pyg -c pyg -c conda-forge`
3. `pip install pykeen`
4. `pip install spacy`
5. `python -m spacy download en_core_web_sm`
6. `python -m spacy download de_core_news_sm`
7. `python -m spacy download ru_core_news_sm`
8. `python -m spacy download zh_core_web_md`
9. `python -m spacy download fr_core_news_sm`
10. `python -m spacy download it_core_news_sm`
11. `python -m spacy download pl_core_news_sm`
12. `python -m spacy download pt_core_news_sm`
13. `python -m spacy download ja_core_news_sm`
14. `python -m spacy download nl_core_news_sm`
15. `python -m spacy download es_core_news_sm`


Furthermore, a second conda environment is required to train the models as described 
by [LiteralE](https://github.com/SmartDataAnalytics/LiteralE).
We recommend using conda for package management and follow the following steps:
1. `conda create --name literale python=3.6.13`
2. `conda activate literale`
3. `pip install -e git://github.com/TimDettmers/spodernet.git#egg=spodernet`
4. `pip install -e git://github.com/TimDettmers/bashmagic.git#egg=bashmagic`
5. `pip install numpy==1.16.5`
6. `pip --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org install pandas==0.25.1 --user`
7. `pip install spacy==2.1.8`
8. `pip install torch===1.2.0` or `conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch` 
9. `python -m spacy download en && python -m spacy download en_core_web_md`
10. `pip install rdflib`
11. `pip install pykeen`
12. `pip install nltk`
Test the installation by training DistMult on FB15k-237 (the installation is working, if the loss is printed out and 
the cpu usage goes up): `python main.py dataset FB15k-237 model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True`

    
## Experiments 

### Generate transformed dataset
All following scripts to create the literal transformation datasets are contained in the `experiment` directory.

Run `setup.py -init` to set up the dataset directory. The script will automatically create the folder `data` and downloads the 
required datasets. The transformations run on tsv files containing the literals for the link prediction datasets, 
filtered to the relevant attributive triples to increase performance. These tsv files can be created by running
`enrich_fb15k-237_literals.py`, `enrich_yago10-3_literals.py`, and `enrich_litwd48k_literals.py` or can be downloaded 
form [Dropbox](https://www.dropbox.com/scl/fo/jn3frofkpush32aui5at0/h?dl=0&rlkey=23nwnk8bnl4q9b7t0fj4pa064) and placed
inside the `data` folder.

The transformation can be applied to generate the datasets with the following scripts:
* Literal2Entity: `python transformation_Literal2Entity.py` 
* Datatype2Entity: `python transformation_Datatype2Entity.py` 
* Shingles2Entity: `python transformation_Shingles2Entity.py` 
To create all transformation datasets, simply run `setup.py -transform`.


### Training DistMult, LiteralE DistMult, ComplEx (LiteralE code)
Clone the [LiteralE GitHub repository](https://github.com/SmartDataAnalytics/LiteralE) and place the created 
dataset folders, e.g.  `FB15k-237_Literal2Entity`, `FB15k-237_Datatype2Entity`, `FB15k-237_Datatype2Entity_filer_00000000_00010000`, 
`FB15k-237_Datatype2Entity_00001000_00010000`, `FB15k-237_Datatype2Entity_filer_00001000_10000000` 
or `FB15k-237_Value2Shingles`, in `LiteralE/data/`. Then replace the LiteralE preprocessing script (`preprocess.sh`) 
by our preprocessing script (`LiteralE_mod/preprocess.sh`) and run `chmod +x preprocess.sh && ./preprocess.sh` to 
preprocess the files. This preprocessing just modifies the data structure, no information is added or removed. 
After that you can run our experiments by executing the commands in `LiteralE_mod/run.sh`.


### Training TransE (PyKeen)
Please use the `literal_transformations` conda environment by `conda activate literal_transformations`.



### Notes
* LiteralE on LitWD48K uses entity_wikidata_descriptions_en.txt and numeric_literals.txt as literal data 



