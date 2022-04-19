# set default cuda device: export CUDA_VISIBLE_DEVICES="1"


# --- FB15k-237 ---
# Preprocess
#python wrangle_KG.py FB15k-237
#python wrangle_KG.py FB15k-237_transformation_Literal2Entity
#python wrangle_KG.py FB15k-237_transformation_Datatype2Entity
#python wrangle_KG.py FB15k-237_transformation_Datatype2Entity_00001000_00010000
#python wrangle_KG.py FB15k-237_transformation_Datatype2Entity_00000000_00010000
#python wrangle_KG.py FB15k-237_transformation_Datatype2Entity_00001000_10000000
#python wrangle_KG.py FB15k-237_transformation_Value2Shingles
#python wrangle_KG.py FB15k-237_transformation_Literal2Entity_low
#python wrangle_KG.py FB15k-237_transformation_Literal2Entity_low_lemm
#python wrangle_KG.py FB15k-237_transformation_Value2Shingles_low
#python wrangle_KG.py FB15k-237_transformation_Value2Shingles_low_lemm

#python main_literal.py dataset FB15k-237 epochs 0 process True
#python main_literal.py dataset FB15k-237_transformation_Literal2Entity epochs 0 process True
#python main_literal.py dataset FB15k-237_transformation_Datatype2Entity epochs 0 process True
#python main_literal.py dataset FB15k-237_transformation_Datatype2Entity_00001000_00010000 epochs 0 process True
#python main_literal.py dataset FB15k-237_transformation_Datatype2Entity_00000000_00010000 epochs 0 process True
#python main_literal.py dataset FB15k-237_transformation_Datatype2Entity_00001000_10000000 epochs 0 process True
#python main_literal.py dataset FB15k-237_transformation_Value2Shingles epochs 0 process True
#python main_literal.py dataset FB15k-237_transformation_Literal2Entity_low epochs 0 process True
#python main_literal.py dataset FB15k-237_transformation_Literal2Entity_low_lemm epochs 0 process True
#python main_literal.py dataset FB15k-237_transformation_Value2Shingles_low epochs 0 process True
#python main_literal.py dataset FB15k-237_transformation_Value2Shingles_low_lemm epochs 0 process True
#python preprocess_num_lit.py --dataset FB15k-237
#python preprocess_txt_lit.py --dataset FB15k-237

# DistMult
#python -u main.py dataset FB15k-237 model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main.py dataset FB15k-237_transformation_Literal2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main.py dataset FB15k-237_transformation_Datatype2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main.py dataset FB15k-237_transformation_Datatype2Entity_00001000_00010000 model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main.py dataset FB15k-237_transformation_Datatype2Entity_00000000_00010000 model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main.py dataset FB15k-237_transformation_Datatype2Entity_00001000_10000000 model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main.py dataset FB15k-237_transformation_Value2Shingles model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False

#nohup python -u main.py dataset FB15k-237_transformation_Literal2Entity_low model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True > ~/FB15k-237_DistMult_Literal2Entity_low.txt
#nohup python -u main.py dataset FB15k-237_transformation_Literal2Entity_low_lemm model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True > ~/FB15k-237_DistMult_Literal2Entity_low_lemm.txt
#nohup python -u main.py dataset FB15k-237_transformation_Value2Shingles_low model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True > ~/FB15k-237_DistMult_Value2Shingles_low.txt
#nohup python -u main.py dataset FB15k-237_transformation_Value2Shingles_low_lemm model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True > ~/FB15k-237_DistMult_Value2Shingles_low_lemm.txt

#nohup python -u main.py dataset FB15k-237_transformation_Literal2Entity_low model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_ComplEx_Literal2Entity_low.txt
#nohup python -u main.py dataset FB15k-237_transformation_Literal2Entity_low_lemm model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_ComplEx_Literal2Entity_low_lemm.txt
#nohup python -u main.py dataset FB15k-237_transformation_Value2Shingles_low model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_ComplEx_Value2Shingles_low.txt
#nohup python -u main.py dataset FB15k-237_transformation_Value2Shingles_low_lemm model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_ComplEx_Value2Shingles_low_lemm.txt




# LiteralE + DistMult
#python -u main_literal.py dataset FB15k-237 model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main_literal.py dataset FB15k-237 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False

#python -u main_literal.py dataset FB15k-237_transformation_Literal2Entity model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main_literal.py dataset FB15k-237_transformation_Datatype2Entity model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main_literal.py dataset FB15k-237_transformation_Datatype2Entity_00001000_00010000 model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main_literal.py dataset FB15k-237_transformation_Datatype2Entity_00000000_00010000 model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main_literal.py dataset FB15k-237_transformation_Datatype2Entity_00001000_10000000 model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main_literal.py dataset FB15k-237_transformation_Value2Shingles model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False


#ComplEx
#python -u main.py dataset FB15k-237 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main.py dataset FB15k-237_transformation_Literal2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main.py dataset FB15k-237_transformation_Datatype2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main.py dataset FB15k-237_transformation_Datatype2Entity_00001000_00010000 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main.py dataset FB15k-237_transformation_Datatype2Entity_00000000_00010000 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main.py dataset FB15k-237_transformation_Datatype2Entity_00001000_10000000 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False
#python -u main.py dataset FB15k-237_transformation_Value2Shingles model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False


# TransE
#python -u attributive_transe.py --dataset='../data/FB15k-237/' --outfile='../data/pykeen_transe_results_FB15k-237.txt'
#python -u attributive_transe.py --dataset='../data/FB15k-237_Literal2Entity/' --outfile='../data/pykeen_transe_results_FB15k-237_Literal2Entity.txt'
#python -u attributive_transe.py --dataset='../data/FB15k-237_Datatype2Entity/' --outfile='../data/pykeen_transe_results_FB15k-237_Datatype2Entity.txt'
#python -u attributive_transe.py --dataset='../data/FB15k-237_Datatype2Entity_00001000_00010000/' --outfile='../data/pykeen_transe_results_FB15k-237_Datatype2Entity_00001000_00010000.txt'
#python -u attributive_transe.py --dataset='../data/FB15k-237_Datatype2Entity_00000000_00010000/' --outfile='../data/pykeen_transe_results_FB15k-237_Datatype2Entity_00000000_00010000.txt'
#python -u attributive_transe.py --dataset='../data/FB15k-237_Datatype2Entity_00001000_10000000/' --outfile='../data/pykeen_transe_results_FB15k-237_Datatype2Entity_00001000_10000000.txt'
#python -u attributive_transe.py --dataset='../data/FB15k-237_Value2Shingles/' --outfile='../data/pykeen_transe_results_FB15k-237_Value2Shingles.txt'



# --- LitWD48K ---
# Preprocess
#python wrangle_KG.py LitWD48K
#python wrangle_KG.py LitWD48K
#python wrangle_KG.py LitWD48K_transformation_Literal2Entity
#python wrangle_KG.py LitWD48K_transformation_Datatype2Entity
#python wrangle_KG.py LitWD48K_transformation_Value2Shingles

#python main_literal.py dataset LitWD48K epochs 0 process True
#python main_literal.py dataset LitWD48K_transformation_Literal2Entity epochs 0 process True
#python main_literal.py dataset LitWD48K_transformation_Datatype2Entity epochs 0 process True
#python main_literal.py dataset LitWD48K_transformation_Value2Shingles epochs 0 process True
#python preprocess_num_lit.py --dataset LitWD48K
#python preprocess_txt_lit.py --dataset LitWD48K

# DistMult
#nohup python -u main.py dataset LitWD48K model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_distmult_base.txt &
#nohup python -u main.py dataset LitWD48K_Literal2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_distmult_Literal2Entity.txt &
#nohup python -u main.py dataset LitWD48K_Datatype2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_distmult_Datatype2Entity.txt &
#nohup python -u main.py dataset LitWD48K_Value2Shingles model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_distmult_Value2Shingles.txt &

# ComplEx
#nohup python -u main.py dataset LitWD48K model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_complex_base.txt &
#nohup python -u main.py dataset LitWD48K_Literal2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_complex_Literal2Entity.txt &
#nohup python -u main.py dataset LitWD48K_Datatype2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_complex_Datatype2Entity.txt &
#nohup python -u main.py dataset LitWD48K_Value2Shingles model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_complex_Value2Shingles.txt &

# LiteralE
#nohup python -u main_literal.py dataset LitWD48K model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_literale_base.txt &



# --- YAGO3-10 ---
# Preprocess

#python wrangle_KG.py YAGO3-10
#python wrangle_KG.py YAGO3-10
#python wrangle_KG.py YAGO3-10_transformation_Literal2Entity
#python wrangle_KG.py YAGO3-10_transformation_Datatype2Entity
#python wrangle_KG.py YAGO3-10_transformation_Value2Shingles

#python main_literal.py dataset YAGO3-10 epochs 0 process True
#python main_literal.py dataset YAGO3-10_transformation_Literal2Entity epochs 0 process True
#python main_literal.py dataset YAGO3-10_transformation_Datatype2Entity epochs 0 process True
#python main_literal.py dataset YAGO3-10_transformation_Value2Shingles epochs 0 process True
#python preprocess_num_lit.py --dataset YAGO3-10
#python preprocess_txt_lit.py --dataset YAGO3-10

# DistMult
#nohup python -u main.py dataset YAGO3-10 model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_distmult_base.txt &
#nohup python -u main.py dataset YAGO3-10_transformation_Literal2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_distmult_Literal2Entity.txt &
#nohup python -u main.py dataset YAGO3-10_transformation_Datatype2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_distmult_Datatype2Entity.txt &
#nohup python -u main.py dataset YAGO3-10_transformation_Value2Shingles model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_distmult_Value2Shingles.txt &

# ComplEx
#nohup python -u main.py dataset YAGO3-10 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_complex_base.txt &
#nohup python -u main.py dataset YAGO3-10_transformation_Literal2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_complex_Literal2Entity.txt &
nohup python -u main.py dataset YAGO3-10_transformation_Datatype2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_ComplEx_Datatype2Entity.txt &
nohup python -u main.py dataset YAGO3-10_transformation_Value2Shingles model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_ComplEx_Value2Shingles.txt &

# LiteralE
#nohup python -u main_literal.py dataset YAGO3-10 model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_literale_base.txt &





python wrangle_KG.py FB15k-237_transformation_Value2Shingles_low
python -u main.py dataset FB15k-237_transformation_Value2Shingles_low model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process True
