# DistMult
python -u main.py dataset FB15k-237 model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main.py dataset FB15k-237_Literal2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main.py dataset FB15k-237_Datatype2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main.py dataset FB15k-237_Datatype2Entity_00001000_00010000 model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main.py dataset FB15k-237_Datatype2Entity_00000000_00010000 model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main.py dataset FB15k-237_Datatype2Entity_00001000_10000000 model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main.py dataset FB15k-237_Value2Shingles model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True


# LiteralE + DistMult
python -u main_literal.py dataset FB15k-237 model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main_literal.py dataset FB15k-237_Literal2Entity model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main_literal.py dataset FB15k-237_Datatype2Entity model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main_literal.py dataset FB15k-237_Datatype2Entity_00001000_00010000 model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main_literal.py dataset FB15k-237_Datatype2Entity_00000000_00010000 model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main_literal.py dataset FB15k-237_Datatype2Entity_00001000_10000000 model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main_literal.py dataset FB15k-237_Value2Shingles model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True


#ComplEx
python -u main.py dataset FB15k-237 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main.py dataset FB15k-237_Literal2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main.py dataset FB15k-237_Datatype2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main.py dataset FB15k-237_Datatype2Entity_00001000_00010000 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main.py dataset FB15k-237_Datatype2Entity_00000000_00010000 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main.py dataset FB15k-237_Datatype2Entity_00001000_10000000 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
python -u main.py dataset FB15k-237_Value2Shingles model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True


# TransE
# TODO

