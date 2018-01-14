import os

#FUNCTIONS
def append_targets(dp_fn, t_fn):
    file = "../data/Grammatical_Facial_Expression/grammatical_facial_expression/"
    out_dir = "../data/no_header/user_dep/full/"
    dp_file = file + dp_fn
    t_file = file + t_fn
    out_file = str(out_dir) + str(dp_fn[:-15]) + '_full.csv'
    out_fp = open(out_file, 'w')
    dp_fp = open(dp_file, 'r')
    t_fp = open(t_file, 'r')
    #first line
    fl_ignore = dp_fp.readline() #ignore first line
    #out_fp.write(fl)
    #other lines appending
    dp_lines = dp_fp.readlines()
    t_lines = t_fp.readlines()
    n = len(dp_lines)
    m = len(t_lines)
    print dp_fn,t_fn,'=>',m,n
    if m != n:
        print "\n***ERROR***: m != n\n", dp_fn, t_fn
        return
    
    for i in range(n):
        a = dp_lines[i]
        b = t_lines[i]
        if a[-1] == '\n':
            a = a[:-1]
        if b[-1] == '\n':
            b = b[:-1]
        a_tok = a.split(' ')
        a_j = ','.join(a_tok)
        b_tok = b.split(' ')
        b_j = ','.join(b_tok)
        c = a_j + ',' + b_j + '\n'
        out_fp.write(c)
    
    out_fp.close()
    dp_fp.close()
    t_fp.close()

#MAIN
dir = os.listdir('../data/Grammatical_Facial_Expression/grammatical_facial_expression/')
dir = dir[:-2]
dir.sort()
n = len(dir)
m = n/2
i=0
for j in range(m):
    dp = dir[2*j]
    t = dir[2*j+1]
    append_targets(dp, t)

#END
