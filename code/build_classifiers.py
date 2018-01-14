import os
import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.classifiers import Classifier
import weka.core.serialization as serialization
import numpy as np
jvm.start()

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
#Save all classifier models trained over training data for given expression-user pair
def save_all_models():
    for user in user_list:
        user_train_dir = os.listdir("../data/arff_files/" + str(user) + "/train/")
        user_train_dir.sort()
        n = len(user_train_dir)
        c = 0
        for expression_index in range(n):
            print "\n", expression_index, "=>", str(expression_list[expression_index]), ':', str(user_train_dir[expression_index])
            id = str(expression_list[expression_index]) + '_' + str(user)
            target_dir = '../models/' + str(expression_list[expression_index]) + '/' + str(user) + '/'
            train_data_file = "../data/arff_files/" + str(user) + "/train/" + str(user_train_dir[expression_index])
            print train_data_file, "=>", target_dir, "\n"
            loader = Loader(classname="weka.core.converters.ArffLoader")
            train_data = loader.load_file(train_data_file)
            for algo in algo_func_dict.keys():
                print "training - " + str(algo)
                model = algo_func_dict[algo](train_data)
                out_file = target_dir + algo + ".model"
                serialization.write(out_file, model)
                c = c + 1
                print str(c) + ": Model Saved =>" + str(out_file)
            #pass

"""#Traverse all the expression-user pair and calls the function to "save all trained classifier models for each expression-user pair"
def traverse_all_pairs_save_models():
    for expression in expression_list:
        for user in user_list:
            save_all_models(expression, user)
#"""
#
###################################################################################
#Main
save_all_models()

#End
#
jvm.stop()
###