import os

#FUNCTIONS
def append_users(a_fn,b_fn):
    file_a = '../data/no_header/dep_a/full/'
    file_b = '../data/no_header/dep_b/full/'
    out_dir = "../data/no_header/indep_ab/full/"
    a_file = file_a + a_fn
    b_file = file_b + b_fn
    out_file = str(out_dir) + 'ab' + str(a_fn[1:])#taking name of expression from any one of a or b
    out_fp = open(out_file, 'w')
    a_fp = open(a_file, 'r')
    b_fp = open(b_file, 'r')
    #just appending two files
    print a_fn, b_fn
    out_fp.write(a_fp.read())
    out_fp.write(b_fp.read())
    out_fp.close()
    a_fp.close()
    b_fp.close()

#MAIN
dir_a = os.listdir('../data/no_header/dep_a/full/')
dir_a.sort()
dir_b = os.listdir('../data/no_header/dep_b/full/')
dir_b.sort()
m = len(dir_a)
for j in range(m):
    a = dir_a[j]
    b = dir_b[j] #9 different expression 
    append_users(a, b)

#END
