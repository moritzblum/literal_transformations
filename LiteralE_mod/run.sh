# set default cuda device: export CUDA_VISIBLE_DEVICES="0"

## --- Preprocess ---
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
#python main_literal.py dataset YAGO3-10 epochs 0 process True
#python main_literal.py dataset YAGO3-10_transformation_Literal2Entity epochs 0 process True
#python main_literal.py dataset YAGO3-10_transformation_Datatype2Entity epochs 0 process True
#python main_literal.py dataset YAGO3-10_transformation_Value2Shingles epochs 0 process True
#python main_literal.py dataset LitWD48K epochs 0 process True
#python main_literal.py dataset LitWD48K_transformation_Literal2Entity epochs 0 process True
#python main_literal.py dataset LitWD48K_transformation_Datatype2Entity epochs 0 process True
#python main_literal.py dataset LitWD48K_transformation_Value2Shingles epochs 0 process True

#python preprocess_num_lit.py --dataset FB15k-237
#python preprocess_txt_lit.py --dataset FB15k-237
#python preprocess_num_lit.py --dataset YAGO3-10
#python preprocess_txt_lit.py --dataset YAGO3-10
#python preprocess_num_lit.py --dataset LitWD48K
#python preprocess_txt_lit.py --dataset LitWD48K




# --- FB15k-237 ---
## DistMult
#nohup python -u main.py dataset FB15k-237 model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_DistMult_base.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Literal2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_DistMult_Literal2Entity.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Datatype2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_DistMult_Datatype2Entity.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Datatype2Entity_00001000_00010000 model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_DistMult_Datatype2Entity_00001000_00010000.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Datatype2Entity_00000000_00010000 model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_DistMult_Datatype2Entity_00000000_00010000.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Datatype2Entity_00001000_10000000 model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_DistMult_Datatype2Entity_00001000_10000000.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Value2Shingles model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_DistMult_Value2Shingles.txt &

#nohup python -u main.py dataset FB15k-237_transformation_Literal2Entity_low model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_DistMult_Literal2Entity_low.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Literal2Entity_low_lemm model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_DistMult_Literal2Entity_low_lemm.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Value2Shingles_low model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_DistMult_Value2Shingles_low.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Value2Shingles_low_lemm model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_DistMult_Value2Shingles_low_lemm.txt &


## ComplEx
#nohup python -u main.py dataset FB15k-237 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_ComplEx_base.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Literal2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_ComplEx_Literal2Entity.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Datatype2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_ComplEx_Datatype2Entity.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Datatype2Entity_00001000_00010000 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_ComplEx_Datatype2Entity_00001000_00010000.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Datatype2Entity_00000000_00010000 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_ComplEx_Datatype2Entity_00000000_00010000.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Datatype2Entity_00001000_10000000 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_ComplEx_Datatype2Entity_00001000_10000000.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Value2Shingles model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_ComplEx_Value2Shingles.txt &

#nohup python -u main.py dataset FB15k-237_transformation_Literal2Entity_low model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_ComplEx_Literal2Entity_low.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Literal2Entity_low_lemm model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_ComplEx_Literal2Entity_low_lemm.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Value2Shingles_low model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_ComplEx_Value2Shingles_low.txt &
#nohup python -u main.py dataset FB15k-237_transformation_Value2Shingles_low_lemm model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_ComplEx_Value2Shingles_low_lemm.txt &


## LiteralE + DistMult
#nohup python -u main_literal.py dataset FB15k-237 model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_DistMult_LiteralE.txt &
#nohup python -u main_literal.py dataset FB15k-237 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 100 lr 0.001 process False > ~/FB15k-237_ComplEx_LiteralE.txt &


# TransE
#nohup python -u attributive_transe.py --dataset='../data/FB15k-237/' --outfile='../data/pykeen_transe_results_FB15k-237.txt' &
#nohup python -u attributive_transe.py --dataset='../data/FB15k-237_Literal2Entity/' --outfile='../data/pykeen_transe_results_FB15k-237_Literal2Entity.txt' &
#nohup python -u attributive_transe.py --dataset='../data/FB15k-237_Datatype2Entity/' --outfile='../data/pykeen_transe_results_FB15k-237_Datatype2Entity.txt' &
#nohup python -u attributive_transe.py --dataset='../data/FB15k-237_Datatype2Entity_00001000_00010000/' --outfile='../data/pykeen_transe_results_FB15k-237_Datatype2Entity_00001000_00010000.txt' &
#nohup python -u attributive_transe.py --dataset='../data/FB15k-237_Datatype2Entity_00000000_00010000/' --outfile='../data/pykeen_transe_results_FB15k-237_Datatype2Entity_00000000_00010000.txt' &
#nohup python -u attributive_transe.py --dataset='../data/FB15k-237_Datatype2Entity_00001000_10000000/' --outfile='../data/pykeen_transe_results_FB15k-237_Datatype2Entity_00001000_10000000.txt' &
#nohup python -u attributive_transe.py --dataset='../data/FB15k-237_Value2Shingles/' --outfile='../data/pykeen_transe_results_FB15k-237_Value2Shingles.txt' &



# --- YAGO3-10 ---
# DistMult
#nohup python -u main.py dataset YAGO3-10 model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_DistMult_base.txt &
#nohup python -u main.py dataset YAGO3-10_transformation_Literal2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_DistMult_Literal2Entity.txt &
#nohup python -u main.py dataset YAGO3-10_transformation_Datatype2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_DistMult_Datatype2Entity.txt &
#nohup python -u main.py dataset YAGO3-10_transformation_Value2Shingles model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_DistMult_Value2Shingles.txt &


# ComplEx
#nohup python -u main.py dataset YAGO3-10 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_ComplEx_base.txt &
#nohup python -u main.py dataset YAGO3-10_transformation_Literal2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_ComplEx_Literal2Entity.txt &
#nohup python -u main.py dataset YAGO3-10_transformation_Datatype2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_ComplEx_Datatype2Entity.txt &
#nohup python -u main.py dataset YAGO3-10_transformation_Value2Shingles model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_ComplEx_Value2Shingles.txt &


# LiteralE
#nohup python -u main_literal.py dataset YAGO3-10 model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_DistMult_LiteralE.txt &
#nohup python -u main_literal.py dataset YAGO3-10 model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/YAGO3-10_ComplEx_LiteralE.txt &



# --- LitWD48K ---
# DistMult
#nohup python -u main.py dataset LitWD48K model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_DistMult_base.txt &
#nohup python -u main.py dataset LitWD48K_Literal2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_DistMult_Literal2Entity.txt &
#nohup python -u main.py dataset LitWD48K_Datatype2Entity model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_DistMult_Datatype2Entity.txt &
#nohup python -u main.py dataset LitWD48K_Value2Shingles model DistMult input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_DistMult_Value2Shingles.txt &


# ComplEx
#nohup python -u main.py dataset LitWD48K model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_ComplEx_base.txt &
#nohup python -u main.py dataset LitWD48K_Literal2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_ComplEx_Literal2Entity.txt &
#nohup python -u main.py dataset LitWD48K_Datatype2Entity model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_ComplEx_Datatype2Entity.txt &
#nohup python -u main.py dataset LitWD48K_Value2Shingles model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_ComplEx_Value2Shingles.txt &


# LiteralE
#nohup python -u main_literal.py dataset LitWD48K model DistMult_text input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_DistMult_LiteralE.txt &
#nohup python -u main_literal.py dataset LitWD48K model ComplEx input_drop 0.2 embedding_dim 100 batch_size 128 epochs 200 lr 0.001 process False > ~/LitWD48K_ComplEx_LiteralE_base.txt &







