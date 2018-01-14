import os
import random

#FUNCTIONS
def split_data_dep_a(a):
    file = '../data/no_header/dep_a/full/'
    out_dir = "../data/no_header/dep_a/"
    a_file = file + a
    train_file = str(out_dir) + 'train/' + str(a[:-8]) + 'train.csv'
    val_file = str(out_dir) + 'validate/' + str(a[:-8]) + 'validate.csv'
    test_file = str(out_dir) + 'test/' + str(a[:-8]) + 'test.csv'
    print a_file
    a_fp = open(a_file,'r')
    train_fp = open(train_file, 'w')
    val_fp = open(val_file, 'w')
    test_fp = open(test_file, 'w')
    """
    #first line header adding to all sets
    a_fl = a_fp.readline()
    train_fp.write(a_fl)
    val_fp.write(a_fl)
    test_fp.write(a_fl)
    """
    #Randomizing before splitting
    a_lines = a_fp.readlines()
    random.shuffle(a_lines)
    #split for train:validate:test in 50:25:25 ratios
    r = len(a_lines)
    p = r/2
    q = p + p/2
    #train(0:p);validate(p:q);test(q:r)
    for i in a_lines[0:p]:
        train_fp.write(i)
    for i in a_lines[p:q]:
        val_fp.write(i)
    for i in a_lines[q:r]:
        test_fp.write(i)
    #closing
    a_fp.close()
    train_fp.close()
    val_fp.close()
    test_fp.close()

def split_data_dep_b(a):
    file = '../data/no_header/dep_b/full/'
    out_dir = "../data/no_header/dep_b/"
    a_file = file + a
    train_file = str(out_dir) + 'train/' + str(a[:-8]) + 'train.csv'
    val_file = str(out_dir) + 'validate/' + str(a[:-8]) + 'validate.csv'
    test_file = str(out_dir) + 'test/' + str(a[:-8]) + 'test.csv'
    print a_file
    a_fp = open(a_file,'r')
    train_fp = open(train_file, 'w')
    val_fp = open(val_file, 'w')
    test_fp = open(test_file, 'w')
    """
    #first line header adding to all sets
    a_fl = a_fp.readline()
    train_fp.write(a_fl)
    val_fp.write(a_fl)
    test_fp.write(a_fl)
    """
    #Randomizing before splitting
    a_lines = a_fp.readlines()
    random.shuffle(a_lines)
    #split for train:validate:test in 50:25:25 ratios
    r = len(a_lines)
    p = r/2
    q = p + p/2
    #train(0:p);validate(p:q);test(q:r)
    for i in a_lines[0:p]:
        train_fp.write(i)
    for i in a_lines[p:q]:
        val_fp.write(i)
    for i in a_lines[q:r]:
        test_fp.write(i)
    #closing
    a_fp.close()
    train_fp.close()
    val_fp.close()
    test_fp.close()

def split_data_indep(a):
    file = '../data/no_header/indep_ab/full/'
    out_dir = "../data/no_header/indep_ab/"
    a_file = file + a
    train_file = str(out_dir) + 'train/' + str(a[:-8]) + 'train.csv'
    val_file = str(out_dir) + 'validate/' + str(a[:-8]) + 'validate.csv'
    test_file = str(out_dir) + 'test/' + str(a[:-8]) + 'test.csv'
    print a_file
    a_fp = open(a_file,'r')
    train_fp = open(train_file, 'w')
    val_fp = open(val_file, 'w')
    test_fp = open(test_file, 'w')
    
    """
    #first line header adding to all sets
    a_fl = a_fp.readline()
    train_fp.write(a_fl)
    val_fp.write(a_fl)
    test_fp.write(a_fl)
    """
    #Randomizing before splitting
    a_lines = a_fp.readlines()
    random.shuffle(a_lines)
    #split for train:validate:test in 50:25:25 ratios
    r = len(a_lines)
    p = r/2
    q = p + p/2
    #train(0:p);validate(p:q);test(q:r)
    for i in a_lines[0:p]:
        train_fp.write(i)
    for i in a_lines[p:q]:
        val_fp.write(i)
    for i in a_lines[q:r]:
        test_fp.write(i)
    #closing
    a_fp.close()
    train_fp.close()
    val_fp.close()
    test_fp.close()

#MAIN
#calling for dep_a
#dir = os.listdir('../data/no_header/user_indep/full/')
#switch here 1
dir = os.listdir('../data/no_header/dep_a/full/')
dir.sort()
n = len(dir)
print "***dep_a read files***"
for j in range(n):
    a = dir[j]
    split_data_dep_a(a)

#calling for dep_b
#dir = os.listdir('../data/no_header/user_indep/full/')
#switch here 1
dir = os.listdir('../data/no_header/dep_b/full/')
dir.sort()
n = len(dir)
print "***dep_b read files***"
for j in range(n):
    a = dir[j]
    split_data_dep_b(a)

#calling for indep_ab
dir = os.listdir('../data/no_header/indep_ab/full/')
#switch here 1
#dir = os.listdir('../data/no_header/user_dep/full/')
dir.sort()
n = len(dir)
print "***indep_ab read files***"
for j in range(n):
    a = dir[j]
    split_data_indep(a)

#END
