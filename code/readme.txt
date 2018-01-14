#Data Preparation:
append_targets.py
append_users.py
data_splitter.py
append_header.py

#ML-Evaluation
build_classifiers.py

#on validation set 
classify_input_data.py #call:save_all_scores_on_validate()
ml_evaluator.py #call:traverse_all_pairs_validation()

#on test set - After choosing best algorithm for each pair, update the selected_algo_dict in ml_evaluation
classify_input_data.py #call:save_all_scores_on_test()
ml_evaluator.py #call:traverse_final_test()

#Feature Importance Mining
feature_imp_extractor.py