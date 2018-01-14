import os
import numpy as np
import pandas as pd
from sklearn.metrics import roc_curve, auc, precision_recall_curve, confusion_matrix
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

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

algorithm_list = []

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
    prc_auc = auc(precision, recall)
    ph.plot(recall, precision, label=str(algo_name) + '(%0.2f)' % prc_auc)
    return prc_auc

#Metric: ROC
def get_metric_ROC(expression, user, pdf_fh):
    plt.clf()
    roc_auc = dict()
    dir = '../results/' + str(expression) + '/' + str(user) + '/'
    algorithm_files = os.listdir(dir) #can take this from algorithm list instead of listdir
    for algo_f in algorithm_files:
        algo_name = algo_f[:-4]
        df = pd.read_csv((str(dir)+str(algo_f)), sep=',',header=0) # first row is header
        #predicted_scores => scores
        score_df = df['score_1'] #selecting only the column with probability scores for positives
        scores = score_df.values 
        #actual targets => targets
        actual_target_df = df['actual_label'] #selecting only the column with target labels
        targets = actual_target_df.values
        #predicted class => preds
        predicted_df = df['predicted_label'] #selecting only the column with target labels
        preds = predicted_df.values
        
        #ROC
        roc_auc[algo_name] = plot_roc(algo_name, targets, scores, plt)
    
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves: ' + str(expression) + ' (' + str(user[-2:]) + ')')
    plt.legend(loc="lower right", prop={'size':10})
    #plt.show()
    plt.savefig(pdf_fh, format='pdf')
    
    roc_auc_dict = roc_auc
    return roc_auc_dict

#Metric: PRC
def get_metric_PRC(expression, user, pdf_fh):
    plt.clf()
    prc_auc = dict()
    dir = '../results/' + str(expression) + '/' + str(user) + '/'
    algorithm_files = os.listdir(dir) #can take this from algorithm list instead of listdir
    for algo_f in algorithm_files:
        algo_name = algo_f[:-4]
        df = pd.read_csv((str(dir)+str(algo_f)), sep=',',header=0) # first row is header
        #predicted_scores => scores
        score_df = df['score_1'] #selecting only the column with probability scores for positives
        scores = score_df.values 
        #actual targets => targets
        actual_target_df = df['actual_label'] #selecting only the column with target labels
        targets = actual_target_df.values
        #predicted class => preds
        predicted_df = df['predicted_label'] #selecting only the column with target labels
        preds = predicted_df.values
        
        #ROC
        prc_auc[algo_name] = plot_prc(algo_name, targets, scores, plt)
    
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curves: ' + str(expression) + ' (' + str(user[-2:]) + ')')
    plt.legend(loc="lower right", prop={'size':10})
    #plt.show()
    plt.savefig(pdf_fh, format='pdf')
    
    prc_auc_dict = prc_auc
    return prc_auc_dict

#Metric: F-Measure
#

#Generate ALL Evaluation Metrics for a given (Expression, User) pair
def generate_eval_metrics(expression, user):
    id = str(expression) + '_' + str(user)
    dir = '../results/' + str(expression) + '/' + str(user) + '/'
    
    #PDF: Curves
    pdf_fh = PdfPages(str(dir) + str(id) + '.pdf')
    #ROC
    roc_auc_dict = get_metric_ROC(exrpression, user, pdf_fh)
    #PRC
    prc_auc_dict = get_metric_PRC(exrpression, user, pdf_fh)
    pp.close()
    
    #CSV: Tables for comparison between all algorithms
    
    
#Traverse through all (Expression, User) pair
def traverse_all_pairs():
    for expression in expression_list:
        for user in user_list:
            generate_eval_metrics(expression, user)

#Main

#End