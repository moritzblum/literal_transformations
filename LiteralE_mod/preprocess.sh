#!/bin/bash
mkdir saved_models
python wrangle_KG.py FB15k-237
python wrangle_KG.py FB15k-237_Literal2Entity
python wrangle_KG.py FB15k-237_Datatype2Entity
python wrangle_KG.py FB15k-237_Datatype2Entity_filter_00000000_00010000
python wrangle_KG.py FB15k-237_Datatype2Entity_filter_00001000_00010000
python wrangle_KG.py FB15k-237_Datatype2Entity_filter_00001000_10000000
python wrangle_KG.py FB15k-237_Value2Shingles

python wrangle_KG.py YAGO3-10
python wrangle_KG.py YAGO3-10_Literal2Entity
python wrangle_KG.py YAGO3-10_Datatype2Entity
python wrangle_KG.py YAGO3-10_Value2Shingles

python wrangle_KG.py LitWD48K
python wrangle_KG.py LitWD48K_Literal2Entity
python wrangle_KG.py LitWD48K_Datatype2Entity
python wrangle_KG.py LitWD48K_Value2Shingles