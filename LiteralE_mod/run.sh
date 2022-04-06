
# --- FB15k-237 ---
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
python -u attributive_transe.py --dataset='../data/FB15k-237/' --outfile='../data/pykeen_transe_results_FB15k-237.txt'
python -u attributive_transe.py --dataset='../data/FB15k-237_Literal2Entity/' --outfile='../data/pykeen_transe_results_FB15k-237_Literal2Entity.txt'
python -u attributive_transe.py --dataset='../data/FB15k-237_Datatype2Entity/' --outfile='../data/pykeen_transe_results_FB15k-237_Datatype2Entity.txt'
python -u attributive_transe.py --dataset='../data/FB15k-237_Datatype2Entity_00001000_00010000/' --outfile='../data/pykeen_transe_results_FB15k-237_Datatype2Entity_00001000_00010000.txt'
python -u attributive_transe.py --dataset='../data/FB15k-237_Datatype2Entity_00000000_00010000/' --outfile='../data/pykeen_transe_results_FB15k-237_Datatype2Entity_00000000_00010000.txt'
python -u attributive_transe.py --dataset='../data/FB15k-237_Datatype2Entity_00001000_10000000/' --outfile='../data/pykeen_transe_results_FB15k-237_Datatype2Entity_00001000_10000000.txt'
python -u attributive_transe.py --dataset='../data/FB15k-237_Value2Shingles/' --outfile='../data/pykeen_transe_results_FB15k-237_Value2Shingles.txt'



# --- LitWD48K ---
nohup python -u main.py dataset LitWD48K model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/LitWD48K_distmult_base.txt &
nohup python -u main.py dataset LitWD48K_Literal2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/LitWD48K_distmult_Literal2Entity.txt &
nohup python -u main.py dataset LitWD48K_Datatype2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/LitWD48K_distmult_Datatype2Entity.txt &
nohup python -u main.py dataset LitWD48K_Value2Shingles model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/LitWD48K_distmult_Value2Shingles.txt &

nohup python -u main.py dataset LitWD48K model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/LitWD48K_complex_base.txt &
nohup python -u main.py dataset LitWD48K_Literal2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/LitWD48K_complex_Literal2Entity.txt &
nohup python -u main.py dataset LitWD48K_Datatype2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/LitWD48K_complex_Datatype2Entity.txt &
nohup python -u main.py dataset LitWD48K_Value2Shingles model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/LitWD48K_complex_Value2Shingles.txt &

nohup python -u main_literal.py dataset LitWD48K model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/LitWD48K_literale.txt &



# --- YAGO3-10 ---
nohup python -u main.py dataset YAGO3-10 model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/YAGO3-10_distmult_base.txt &
nohup python -u main.py dataset YAGO3-10_Literal2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/YAGO3-10_distmult_Literal2Entity.txt &
nohup python -u main.py dataset YAGO3-10_Datatype2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/YAGO3-10_distmult_Datatype2Entity.txt &
nohup python -u main.py dataset YAGO3-10_Value2Shingles model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/YAGO3-10_distmult_Value2Shingles.txt &

nohup python -u main.py dataset YAGO3-10 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/YAGO3-10_complex_base.txt &
nohup python -u main.py dataset YAGO3-10_Literal2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/YAGO3-10_complex_Literal2Entity.txt &
nohup python -u main.py dataset YAGO3-10_Datatype2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/YAGO3-10_complex_Datatype2Entity.txt &
nohup python -u main.py dataset YAGO3-10_Value2Shingles model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/YAGO3-10_complex_Value2Shingles.txt &

python -u main_literal.py dataset YAGO3-10 model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process True > ~/YAGO3-10_literale.txt &