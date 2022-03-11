# Exploring the impact of literal transformations within Knowledge Graphs for Link Prediction


## Set-up 
Our transformations are implemented in Python, as the LiteralE source code. To replicate our results, 
you have to set up a Python 3.6 environment as described for [LiteralE](https://github.com/SmartDataAnalytics/LiteralE)
and some additional packagestt. 
We recommend using conda for package management and follow the following steps:
1. `conda create --name literale python=3.6.13`
2. `conda activate literale`
3. `pip install -e git://github.com/TimDettmers/spodernet.git#egg=spodernet`
4. `pip install -e git://github.com/TimDettmers/bashmagic.git#egg=bashmagic`
5. `pip install numpy==1.16.5`
6. `pip --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org install pandas==0.25.1 --user`
7. `pip install spacy==2.1.8`
8. `pip install torch===1.2.0`
9. `python -m spacy download en && python -m spacy download en_core_web_md`
10. `pip install rdflib`
11. `pip install pykeen`
12. `pip install nltk`
13. `pip install spacy`
14. `python -m spacy download en_core_web_sm`
15. `python -m spacy download de_core_news_sm`
16. `python -m spacy download ru_core_news_sm`
17. `python -m spacy download zh_core_web_md`
Test the installation by training DistMult on FB15k-237 (the installation is working, if the loss is printed out and 
the cpu usage goes up): `python main.py dataset FB15k-237 model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True`

Furthermore, a second conda environment is required to preprocess the data for PyKeen. Therefore, 
we recommend Python 3.8 (in the following, this environment is only used if explicitly mentioned):
1. `conda create --name literal_transformations python=3.8`
2. `conda install pyg -c pyg -c conda-forge`
3. `pip install pykeen`

## Experiments 

### Generate transformed dataset

Download and extract the [FB15k-237 Dataset](https://www.microsoft.com/en-us/download/confirmation.aspx?id=52312) and 
put the data into the directory `data/FB15k-237/`. The literals must be extracted from Freebase; therefore, 
this dataset is also required. Place  the [Freebase Dataset](https://developers.google.com/freebase) file in 
`data/`.

First of all, extract all triples from the source Freebase graph with its subject contained in FB15k-237 to reduce the 
set of potentially relevant triples and then create a file containing only the literals: execute 
`python enrich_fb15k-237_literals.py` in the directory `experiment`. This creates the files 
`data/FB15k-237_freebase_reduced.txt` and `data/FB15k-237_literals.txt`.

The code to transform thr literls is contained in the `experiment` directory, too. The transformation can be applied 
to generate the datasets with the following commands:
* Literal2Entity: `python transformation_Literal2Entity.py` 
* Datatype2Entity: `python transformation_Datatype2Entity.py` 
* Shingles2Entity: `python transformation_Shingles2Entity.py` 
This creates the files `FB15k-237_transformation_Literal2Entity.txt`, `FB15k-237_transformation_Datatype2Entity.txt` and `FB15k-237_transformation_Value2Shingles.txt` in `/data`. To create the dataset training files for the LiteralE code, the relational FB15k-237 triples have now to be merged with the transformed literal data and test and validation files have to be added:

#### Literal2Entity
* `mkdir FB15k-237_Literal2Entity`
* `cp FB15k-237/test.txt FB15k-237_Literal2Entity/test.txt` 
* `cp FB15k-237/valid.txt FB15k-237_Literal2Entity/valid.txt` 
* `cat FB15k-237_transformation_Literal2Entity.txt FB15k-237/train.txt > FB15k-237_Literal2Entity/train.txt`

#### Datatype2Entity 
* `mkdir FB15k-237_Datatype2Entity`
* `cp FB15k-237/test.txt FB15k-237_Datatype2Entity/test.txt` 
* `cp FB15k-237/valid.txt FB15k-237_Datatype2Entity/valid.txt` 
* `cat FB15k-237_transformation_Datatype2Entity.txt FB15k-237/train.txt > FB15k-237_Datatype2Entity/train.txt`
* `mkdir FB15k-237_Datatype2Entity_filer_00000000_00010000`
* `cp FB15k-237/test.txt FB15k-237_Datatype2Entity_filer_00000000_00010000/test.txt` 
* `cp FB15k-237/valid.txt FB15k-237_Datatype2Entity_filer_00000000_00010000/valid.txt` 
* `cat FB15k-237_transformation_Datatype2Entity_filer_00000000_00010000.txt FB15k-237/train.txt > FB15k-237_Datatype2Entity_filer_00000000_00010000/train.txt`
* `mkdir FB15k-237_Datatype2Entity_filer_00001000_00010000`
* `cp FB15k-237/test.txt FB15k-237_Datatype2Entity_filer_00001000_00010000/test.txt` 
* `cp FB15k-237/valid.txt FB15k-237_Datatype2Entity_filer_00001000_00010000/valid.txt` 
* `cat FB15k-237_transformation_Datatype2Entity_filer_00001000_00010000.txt FB15k-237/train.txt > FB15k-237_Datatype2Entity_filer_00001000_00010000/train.txt`
* `mkdir FB15k-237_Datatype2Entity_filer_00001000_10000000`
* `cp FB15k-237/test.txt FB15k-237_Datatype2Entity_filer_00001000_10000000/test.txt` 
* `cp FB15k-237/valid.txt FB15k-237_Datatype2Entity_filer_00001000_10000000/valid.txt` 
* `cat FB15k-237_transformation_Datatype2Entity_filer_00001000_10000000.txt FB15k-237/train.txt > FB15k-237_Datatype2Entity_filer_00001000_10000000/train.txt`

#### Value2Shingles
* `mkdir FB15k-237_Value2Shingles`
* `cp FB15k-237/test.txt FB15k-237_Value2Shingles/test.txt` 
* `cp FB15k-237/valid.txt FB15k-237_Value2Shingles/valid.txt` 
* `cat FB15k-237_transformation_Value2Shingles.txt FB15k-237/train.txt > FB15k-237_Value2Shingles/train.txt`


### Training DistMult, LiteralE DistMult, ComplEx (LiteralE code)
Clone the [LiteralE GitHub repository](https://github.com/SmartDataAnalytics/LiteralE) and place the recently created 
folders `FB15k-237_Literal2Entity`, `FB15k-237_Datatype2Entity`, `FB15k-237_Datatype2Entity_filer_00000000_00010000`, 
`FB15k-237_Datatype2Entity_00001000_00010000`, `FB15k-237_Datatype2Entity_filer_00001000_10000000` 
and `FB15k-237_Value2Shingles` in `LiteralE/data/`. Then replace the LiteralE preprocessing script (`preprocess.sh`) 
by our preprocessing script (`LiteralE_mod/preprocess.sh`) and run `chmod +x preprocess.sh && ./preprocess.sh` to 
preprocess the files. This preprocessing just modifies the data structure, no information is added or removed. 
After that you can run our experiments by executing the commands in `LiteralE_mod/run.sh`.


### Training TransE (PyKeen)
Now, please use the `literal_transformations` conda environment by `conda activate literal_transformations`






 



