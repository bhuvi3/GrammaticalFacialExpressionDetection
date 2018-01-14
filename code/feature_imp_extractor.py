import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import ExtraTreesClassifier

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

#
def get_feature_imp():
    dir = "../data/csv_files/indep_ab/full/"
    out_dir = "../feature_importance/"
    for expression in expression_list:
        data_file = dir + "ab_" + expression + "_full.csv"
        print data_file
        df = pd.read_csv(data_file, sep=',', header=0) # first row is header
        y = df['label']
        df.drop('label',axis=1,inplace=True)
        features = list(df.columns.values)
        X = df.as_matrix()
        forest = ExtraTreesClassifier()
        forest.fit(X, y)
        #importances here will be a numpy array of shape n_features
        importances = forest.feature_importances_
        #
        out_file = out_dir + expression + ".csv"
        csv_fh = open(out_file,'w')
        header = "Feature, Importance\n"
        csv_fh.write(header)
        for i in range(len(features)):
            line = features[i] + "," + str(importances[i]) + "\n"
            csv_fh.write(line)
        csv_fh.close()
        
#
#Main
get_feature_imp()
#End