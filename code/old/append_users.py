import os

#FUNCTIONS
def append_users(dp_fn, t_fn):
    file = '../data/no_header/user_dep/full/'
    out_dir = "../data/no_header/user_indep/full/"
    dp_file = file + dp_fn
    t_file = file + t_fn
    out_file = str(out_dir) + 'ab' + str(dp_fn[1:])
    out_fp = open(out_file, 'w')
    dp_fp = open(dp_file, 'r')
    t_fp = open(t_file, 'r')
    #just appending two files
    print dp_fn, t_fn
    out_fp.write(dp_fp.read())
    out_fp.write(t_fp.read())
    out_fp.close()
    dp_fp.close()
    t_fp.close()

#MAIN
dir = os.listdir('../data/no_header/user_dep/full/')
dir.sort()
n = len(dir)
m = n/2
for j in range(m):
    dp = dir[j]
    t = dir[j+9] #9 different expression 
    append_users(dp, t)

#END
