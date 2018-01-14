import os
import numpy as np
import pandas as pd
from sklearn.metrics import roc_curve, auc, precision_recall_curve, confusion_matrix
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from sklearn.metrics import f1_score

#Global variables
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

#
#A dictionary mapping each algorithm (as used in the file name) to the callable function
algorithm_list = {
'MLP_Classifier_2',
'MLP_Classifier_10',
'Bayes_Network',
'RBF_Classifier',
'Random_Forest',
'Bagging',
'Adaboost',
'Logit_Boost',
#'Rotation_Forest',
'FLDA',
'REP_Tree'
}

#Functions
#Plot a ROC curve for single algorithm
def plot_roc(algo_name, targets, scores, ph):#ph - plot handler
    fpr, tpr, thresholds = roc_curve(targets, scores)
    roc_auc = auc(fpr, tpr)
    ph.plot(fpr, tpr, label=str(algo_name) + '(%0.2f)' % roc_auc)
    return roc_auc

#Plot a PRC curve for single algorithm 
def plot_prc(algo_name, targets, scores, ph):#ph - plot handler
    precision, recall, thresholds = precision_recall_curve(targets, scores)
    prc_auc = auc(recall, precision)
    ph.plot(recall, precision, label=str(algo_name) + '(%0.2f)' % prc_auc)
    return prc_auc

#Metric: ROC
def get_metric_ROC(expression, user, pdf_fh, user_label):
    plt.clf()
    roc_auc = dict()
    dir = '../results/' + str(expression) + '/' + str(user) + '/'
    #algorithm_files = os.listdir(dir) #can take this from algorithm list instead of listdir
    for algo in algorithm_list:
        score_file = str(dir)+str(algo) + "_scores.csv"
        print "ROC score file: " + score_file
        df = pd.read_csv(score_file, sep=',',header=0) # first row is header
        #predicted_scores => scores
        score_df = df['distribution_1'] #selecting only the column with probability scores for positives
        scores = score_df.values 
        #actual targets => targets
        actual_target_df = df['actual_class'] #selecting only the column with target labels
        targets = actual_target_df.values
        #predicted class => preds
        predicted_df = df['predicted_class'] #selecting only the column with target labels
        preds = predicted_df.values
        
        #ROC
        roc_auc[algo] = plot_roc(algo, targets, scores, plt)
    
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves: ' + str(expression) + ' (' + str(user_label) + ')')
    plt.legend(loc="lower right", prop={'size':10})
    #plt.show()
    plt.savefig(pdf_fh, format='pdf')
    
    roc_auc_dict = roc_auc
    return roc_auc_dict

#Metric: PRC
def get_metric_PRC(expression, user, pdf_fh, user_label):
    plt.clf()
    prc_auc = dict()
    dir = '../results/' + str(expression) + '/' + str(user) + '/'
    #algorithm_files = os.listdir(dir) #can take this from algorithm list instead of listdir
    for algo in algorithm_list:
        score_file = str(dir)+str(algo) + "_scores.csv"
        print "PRC score file: " + score_file
        df = pd.read_csv(score_file, sep=',',header=0) # first row is header
        #predicted_scores => scores
        score_df = df['distribution_1'] #selecting only the column with probability scores for positives
        scores = score_df.values 
        #actual targets => targets
        actual_target_df = df['actual_class'] #selecting only the column with target labels
        targets = actual_target_df.values
        #predicted class => preds
        predicted_df = df['predicted_class'] #selecting only the column with target labels
        preds = predicted_df.values
        
        #PRC
        prc_auc[algo] = plot_prc(algo, targets, scores, plt)
    
    #plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curves: ' + str(expression) + ' (' + str(user_label) + ')')
    plt.legend(loc="lower right", prop={'size':10})
    #plt.show()
    plt.savefig(pdf_fh, format='pdf')
    
    prc_auc_dict = prc_auc
    return prc_auc_dict

#Metric: F-Measure
#
def get_f1_score(expression, user):
    f1_dict = {}
    dir = '../results/' + str(expression) + '/' + str(user) + '/'
    for algo in algorithm_list:
        score_file = str(dir)+str(algo) + "_scores.csv"
        print "F1 score file: " + score_file
        df = pd.read_csv(score_file, sep=',',header=0) # first row is header
        #predicted_scores => scores
        score_df = df['distribution_1'] #selecting only the column with probability scores for positives
        scores = score_df.values 
        #actual targets => targets
        actual_target_df = df['actual_class'] #selecting only the column with target labels
        targets = actual_target_df.values
        #predicted class => preds
        predicted_df = df['predicted_class'] #selecting only the column with target labels
        preds = predicted_df.values
        
        #F1
        f1_dict[algo] = f1_score(targets, preds)
    
    return f1_dict

#Generate ALL Evaluation Metrics for a given (Expression, User) pair
def generate_eval_metrics(expression, user):
    id = str(user) + '_' + str(expression)
    dir = '../results/' + str(expression) + '/' + str(user) + '/'
    print "ID: " + id
    #PDF: Curves
    pdf_fh = PdfPages(str(dir) + str(id) + '.pdf')
    csv_fh = open((str(dir) + str(id) + '.csv'),'w')
    #
    if user == 'dep_a':
        user_label = "User - A"
    elif user == 'dep_b':
        user_label = "User - B"
    elif user == 'indep_ab':
        user_label = "User Independent - AB"
    else:
        print "ERROR"
    #ROC
    roc_auc_dict = get_metric_ROC(expression, user, pdf_fh, user_label)
    #PRC
    prc_auc_dict = get_metric_PRC(expression, user, pdf_fh, user_label)
    pdf_fh.close()
    
    #CSV: Tables for comparison between all algorithms
    f1_dict = get_f1_score(expression, user)
    csv_header = "Algorithm,AUROC,AUPRC,F1Score\n"
    csv_fh.write(csv_header)
    for algo in f1_dict.keys():
        line = str(algo) + ',' + str(roc_auc_dict[algo]) + ',' + str(prc_auc_dict[algo]) + ',' + str(f1_dict[algo]) + '\n'
        csv_fh.write(line)
    csv_fh.close()
    
#Traverse through all (Expression, User) pair
def traverse_all_pairs_validation():
    c = 0
    for expression in expression_list:
        for user in user_list:
            c = c + 1
            print c
            generate_eval_metrics(expression, user)
#
#######################################################################################################################################################################################
"""
#A dictionary mapping each algorithm (as used in the file name) to the callable function
algorithm_list = {
'MLP_Classifier_2',
'MLP_Classifier_10',
'Bayes_Network',
'RBF_Classifier',
'Random_Forest',
'Bagging',
'Adaboost',
'Logit_Boost',
#'Rotation_Forest',
'FLDA',
'REP_Tree'
}
"""
selected_algo_dict = {
'affirmative':{'dep_a':'Random_Forest','dep_b':'Random_Forest','indep_ab':'Random_Forest'},
'conditional':{'dep_a':'MLP_Classifier_10','dep_b':'Random_Forest','indep_ab':'Random_Forest'},
'doubt_question':{'dep_a':'Bagging','dep_b':'MLP_Classifier_10','indep_ab':'Random_Forest'},
'emphasis':{'dep_a':'MLP_Classifier_10','dep_b':'Random_Forest','indep_ab':'Random_Forest'},
'negative':{'dep_a':'Random_Forest','dep_b':'Random_Forest','indep_ab':'Random_Forest'},
'relative':{'dep_a':'Random_Forest','dep_b':'MLP_Classifier_10','indep_ab':'Random_Forest'},
'topics':{'dep_a':'MLP_Classifier_10','dep_b':'RBF_Classifier','indep_ab':'Random_Forest'},
'wh_question':{'dep_a':'Random_Forest','dep_b':'Random_Forest','indep_ab':'Random_Forest'},
'yn_question':{'dep_a':'MLP_Classifier_10','dep_b':'Random_Forest','indep_ab':'Random_Forest'}
}
#
#Metric: ROC
def TEST_get_metric_ROC(expression, pdf_fh):
    roc_auc_dict = {}
    plt.clf()
    for user in user_list:
        #
        if user == 'dep_a':
            user_label = "User - A"
        elif user == 'dep_b':
            user_label = "User - B"
        elif user == 'indep_ab':
            user_label = "User Independent - AB"
        else:
            print "ERROR"
        #
        selected_algo = selected_algo_dict[expression][user]
        dir = '../results_test/' + str(expression) + '/' + str(user) + '/'
        score_file = str(dir)+str(selected_algo) + "_scores.csv"
        print "ROC score file: " + score_file
        df = pd.read_csv(score_file, sep=',',header=0) # first row is header
        #predicted_scores => scores
        score_df = df['distribution_1'] #selecting only the column with probability scores for positives
        scores = score_df.values 
        #actual targets => targets
        actual_target_df = df['actual_class'] #selecting only the column with target labels
        targets = actual_target_df.values
        #predicted class => preds
        predicted_df = df['predicted_class'] #selecting only the column with target labels
        preds = predicted_df.values
        
        #ROC
        curve_label = user_label + ": " + selected_algo
        roc_auc_dict[user] = plot_roc(curve_label, targets, scores, plt)
    
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves: ' + str(expression))
    plt.legend(loc="lower right", prop={'size':10})
    #plt.show()
    plt.savefig(pdf_fh, format='pdf')
    
    return roc_auc_dict

#Metric: PRC
def TEST_get_metric_PRC(expression, pdf_fh):
    prc_auc_dict = {}
    plt.clf()
    for user in user_list:
        #
        if user == 'dep_a':
            user_label = "User - A"
        elif user == 'dep_b':
            user_label = "User - B"
        elif user == 'indep_ab':
            user_label = "User Independent - AB"
        else:
            print "ERROR"
        #
        selected_algo = selected_algo_dict[expression][user]
        dir = '../results_test/' + str(expression) + '/' + str(user) + '/'
        score_file = str(dir)+str(selected_algo) + "_scores.csv"
        print "PRC score file: " + score_file
        df = pd.read_csv(score_file, sep=',',header=0) # first row is header
        #predicted_scores => scores
        score_df = df['distribution_1'] #selecting only the column with probability scores for positives
        scores = score_df.values 
        #actual targets => targets
        actual_target_df = df['actual_class'] #selecting only the column with target labels
        targets = actual_target_df.values
        #predicted class => preds
        predicted_df = df['predicted_class'] #selecting only the column with target labels
        preds = predicted_df.values
        
        #PRC
        curve_label = user_label + ": " + selected_algo
        prc_auc_dict[user] = plot_prc(curve_label, targets, scores, plt)
    
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curves: ' + str(expression))
    plt.legend(loc="lower right", prop={'size':10})
    #plt.show()
    plt.savefig(pdf_fh, format='pdf')

    return prc_auc_dict

#Metric: F-Measure
#
def TEST_get_f1_score(expression):
    f1_score_dict = {}
    for user in user_list:
        selected_algo = selected_algo_dict[expression][user]
        dir = '../results_test/' + str(expression) + '/' + str(user) + '/'
        score_file = str(dir)+str(selected_algo) + "_scores.csv"
        print "F1 score file: " + score_file
        df = pd.read_csv(score_file, sep=',', header=0) # first row is header
        #predicted_scores => scores
        score_df = df['distribution_1'] #selecting only the column with probability scores for positives
        scores = score_df.values 
        #actual targets => targets
        actual_target_df = df['actual_class'] #selecting only the column with target labels
        targets = actual_target_df.values
        #predicted class => preds
        predicted_df = df['predicted_class'] #selecting only the column with target labels
        preds = predicted_df.values
        
        #F1
        f1_score_dict[user] = f1_score(targets, preds)
    
    return f1_score_dict
    
#
def traverse_final_test():
    c = 0
    for expression in expression_list:
        id = str(expression)
        dir = '../results_test/' + str(expression) + '/'
        #
        f1_score_dict = TEST_get_f1_score(expression)
        #
        pdf_fh = PdfPages(str(dir) + str(id) + '.pdf')
        roc_auc_dict = TEST_get_metric_ROC(expression, pdf_fh)
        prc_auc_dict = TEST_get_metric_PRC(expression, pdf_fh)
        pdf_fh.close()
        #
        csv_fh = open((str(dir) + str(id) + '.csv'),'w')
        csv_header = "UserScenario,Algorithm,AUROC,AUPRC,F1Score\n"
        csv_fh.write(csv_header)
        for user in user_list:
            selected_algo = selected_algo_dict[expression][user]
            roc_auc = roc_auc_dict[user]
            prc_auc = prc_auc_dict[user]
            f1_score = f1_score_dict[user]
            line = str(user) + ',' + str(selected_algo) + ',' + str(roc_auc_dict[user]) + ',' + str(prc_auc_dict[user]) + ',' + str(f1_score_dict[user]) + '\n'
            csv_fh.write(line)
            c = c + 1
            print c
        csv_fh.close()

#
#Main
#traverse_all_pairs_validation()
#traverse_final_test()
#End