import os
import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.classifiers import Classifier
import weka.core.serialization as serialization
import numpy as np


expression_list = [
'affirmative',
'conditional',
'doubt_question',
'emphasis',
'negative',
'relative',
'topics',
'wh_question',
'yn_question']

user_list = [
'dep_a',
'dep_b',
'indep_ab']

algorithm_list = []

#Functions to Call each classifier algorithm
#MLP Classifier: 2 nodes - NOT USED
def mlpc_2(train_data):
    train_data.class_is_last()
    cls = Classifier(classname="weka.classifiers.functions.MLPClassifier", options=["-N", "2"])
    cls.build_classifier(train_data)
    return cls
    #pass

#
#MLP Classifier: 10 nodes
def mlpc_10(train_data):
    train_data.class_is_last()
    cls = Classifier(classname="weka.classifiers.functions.MLPClassifier", options=["-N", "10"])
    cls.build_classifier(train_data)
    return cls
    #pass

#
#Bayes Network: Default
def bayes_net(train_data):
    train_data.class_is_last()
    cls = Classifier(classname="weka.classifiers.bayes.BayesNet")
    cls.build_classifier(train_data)
    return cls
    #pass

#
#RBF Classifier: Default
def rbfc(train_data):
    train_data.class_is_last()
    cls = Classifier(classname="weka.classifiers.functions.RBFClassifier")
    cls.build_classifier(train_data)
    return cls
    #pass

#
#Random Forest: Default
def random_forest(train_data):
    train_data.class_is_last()
    cls = Classifier(classname="weka.classifiers.trees.RandomForest")
    cls.build_classifier(train_data)
    return cls
    #pass

#
#Bagging: Default
def bagging(train_data):
    train_data.class_is_last()
    cls = Classifier(classname="weka.classifiers.meta.Bagging")
    cls.build_classifier(train_data)
    return cls
    #pass

#
#Adaboost: Default
def adaboost(train_data):
    train_data.class_is_last()
    cls = Classifier(classname="weka.classifiers.meta.AdaBoostM1")
    cls.build_classifier(train_data)
    return cls
    #pass

#
#Logit Boost: Default
def logit_boost(train_data):
    train_data.class_is_last()
    cls = Classifier(classname="weka.classifiers.meta.LogitBoost")
    cls.build_classifier(train_data)
    return cls
    #pass

#
#Rotation Forest: Default
def rotation_forest(train_data):
    train_data.class_is_last()
    cls = Classifier(classname="weka.classifiers.meta.RotationForest")
    cls.build_classifier(train_data)
    return cls
    #pass

#
#F-LDA: Default
def flda(train_data):
    train_data.class_is_last()
    cls = Classifier(classname="weka.classifiers.functions.FLDA")
    cls.build_classifier(train_data)
    return cls
    #pass

#
#REP Tree: Default
def rep_tree(train_data):
    train_data.class_is_last()
    cls = Classifier(classname="weka.classifiers.trees.REPTree")
    cls.build_classifier(train_data)
    return cls
    #pass

#
#A dictionary mapping each algorithm (as used in the file name) to the callable function
algo_func_dict = {
'MLP_Classifier_2': mlpc_2,
'MLP_Classifier_10': mlpc_10,
'Bayes_Network': bayes_net,
'RBF_Classifier': rbfc,
'Random_Forest': random_forest,
'Bagging': bagging,
'Adaboost': adaboost,
'Logit_Boost': logit_boost,
#'Rotation_Forest': rotation_forest,
'FLDA': flda,
'REP_Tree': rep_tree
}

#Functions
#Retrieves the classifier scores (Probability distribution per each class) from the given trained classifier model; columns(actual, predicted, proba_0, proba_1)
def get_classifier_score(trained_model, input_data):
    header = np.array(['inst_index', 'actual_class', 'predicted_class', 'distribution_0', 'distribution_1'])
    for index, inst in enumerate(input_data):
        actual = inst.values[inst.class_index]
        pred = trained_model.classify_instance(inst)
        dist = trained_model.distribution_for_instance(inst)
        #out_score = [inst_index, actual_class, predicted_class, distribution_0, distribution_1]; inst_index starts from 1
        inst_index = index + 1
        inst_out_score = np.hstack((inst_index, actual, pred, dist))
        inst_out_score = [str(i) for i in inst_out_score]
        inst_out_score = ",".join(inst_out_score)
        inst_out_score = inst_out_score.split(',')
        inst_out_score = np.array(inst_out_score)
        if index == 0: #for the first instance, initializing total score. From the next iteration, instance scores are appended (vertically stacked to total score)
            total_out_score = inst_out_score
            #print inst_out_score
        else:
            total_out_score = np.vstack((total_out_score, inst_out_score))
    
    #print total_out_score[:5] 
    final_scores_matrix = np.vstack((header, total_out_score))
    return final_scores_matrix

#
#Tests all classifier models available on all expression-user pairs. Saves respective scores as a scores .csv file for each algorithm in each expression-user pair.
def save_all_scores_on_validate():
    jvm.start()
    for user in user_list:
        user_validate_dir = os.listdir("../data/arff_files/" + str(user) + "/validate/")
        user_validate_dir.sort()
        n = len(user_validate_dir)
        c = 0
        for expression_index in range(n):
            print "\n", expression_index, "=>", str(expression_list[expression_index]), ':', str(user_validate_dir[expression_index])
            id = str(expression_list[expression_index]) + '_' + str(user)
            target_dir = '../results/' + str(expression_list[expression_index]) + '/' + str(user) + '/'
            model_dir = '../models/' + str(expression_list[expression_index]) + '/' + str(user) + '/'
            validate_data_file = "../data/arff_files/" + str(user) + "/validate/" + str(user_validate_dir[expression_index])
            print validate_data_file, "=>", model_dir, "all algos", "=>", target_dir, "\n"
            
            loader = Loader(classname="weka.core.converters.ArffLoader")
            validate_data = loader.load_file(validate_data_file)
            validate_data.class_is_last()
            for algo in algo_func_dict.keys():
                print "Algorithm: " + algo.upper()
                #if algo.upper()=="MLP_CLASSIFIER_10":
                #    continue
                model_file = model_dir + algo + ".model"
                print model_file
                
                j_obj = serialization.read(model_file)
                print j_obj
                trained_model = Classifier(jobject=j_obj)
                scores_matrix = get_classifier_score(trained_model, validate_data)
                #print scores_matrix[:5]
                out_file = target_dir + algo + "_scores.csv"
                #writing scores to target file
                #scores_matrix = scores_matrix.astype(np.str)
                
                np.savetxt(out_file, scores_matrix, delimiter=",", fmt="%s")
                c = c + 1
                print str(c) + ": Validate Scores Saved =>" + str(out_file)
            #pass
    jvm.stop()
#
#
#Tests all classifier models available on all expression-user pairs. Saves respective scores as a scores .csv file for each algorithm in each expression-user pair.
def save_all_scores_on_test():
    jvm.start()
    for user in user_list:
        user_test_dir = os.listdir("../data/arff_files/" + str(user) + "/test/")
        user_test_dir.sort()
        n = len(user_test_dir)
        c = 0
        for expression_index in range(n):
            print "\n", expression_index, "=>", str(expression_list[expression_index]), ':', str(user_test_dir[expression_index])
            id = str(expression_list[expression_index]) + '_' + str(user)
            target_dir = '../results_test/' + str(expression_list[expression_index]) + '/' + str(user) + '/'
            model_dir = '../models/' + str(expression_list[expression_index]) + '/' + str(user) + '/'
            test_data_file = "../data/arff_files/" + str(user) + "/test/" + str(user_test_dir[expression_index])
            print test_data_file, "=>", model_dir, "all algos", "=>", target_dir, "\n"
            
            loader = Loader(classname="weka.core.converters.ArffLoader")
            test_data = loader.load_file(test_data_file)
            test_data.class_is_last()
            for algo in algo_func_dict.keys():
                print "Algorithm: " + algo.upper()
                #if algo.upper()=="MLP_CLASSIFIER_10":
                #    continue
                model_file = model_dir + algo + ".model"
                print model_file
                
                j_obj = serialization.read(model_file)
                print j_obj
                trained_model = Classifier(jobject=j_obj)
                scores_matrix = get_classifier_score(trained_model, test_data)
                #print scores_matrix[:5]
                out_file = target_dir + algo + "_scores.csv"
                #writing scores to target file
                #scores_matrix = scores_matrix.astype(np.str)
                
                np.savetxt(out_file, scores_matrix, delimiter=",", fmt="%s")
                c = c + 1
                print str(c) + ": Test Scores Saved =>" + str(out_file)
            #pass
    jvm.stop()
#
###################################################################################
#Main
#save_all_scores_on_validate()
#save_all_scores_on_test()
#End
#
jvm.stop()
###