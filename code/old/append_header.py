import os

#FUNCTIONS
def append_header(src, dest, rel_name, type):
    in_fp = open(src, 'r')
    out_fp = open(dest, 'w')
    #first line
    attrib_header = """
@attribute timestamp numeric
@attribute 0x numeric
@attribute 0y numeric
@attribute 0z numeric
@attribute 1x numeric
@attribute 1y numeric
@attribute 1z numeric
@attribute 2x numeric
@attribute 2y numeric
@attribute 2z numeric
@attribute 3x numeric
@attribute 3y numeric
@attribute 3z numeric
@attribute 4x numeric
@attribute 4y numeric
@attribute 4z numeric
@attribute 5x numeric
@attribute 5y numeric
@attribute 5z numeric
@attribute 6x numeric
@attribute 6y numeric
@attribute 6z numeric
@attribute 7x numeric
@attribute 7y numeric
@attribute 7z numeric
@attribute 8x numeric
@attribute 8y numeric
@attribute 8z numeric
@attribute 9x numeric
@attribute 9y numeric
@attribute 9z numeric
@attribute 10x numeric
@attribute 10y numeric
@attribute 10z numeric
@attribute 11x numeric
@attribute 11y numeric
@attribute 11z numeric
@attribute 12x numeric
@attribute 12y numeric
@attribute 12z numeric
@attribute 13x numeric
@attribute 13y numeric
@attribute 13z numeric
@attribute 14x numeric
@attribute 14y numeric
@attribute 14z numeric
@attribute 15x numeric
@attribute 15y numeric
@attribute 15z numeric
@attribute 16x numeric
@attribute 16y numeric
@attribute 16z numeric
@attribute 17x numeric
@attribute 17y numeric
@attribute 17z numeric
@attribute 18x numeric
@attribute 18y numeric
@attribute 18z numeric
@attribute 19x numeric
@attribute 19y numeric
@attribute 19z numeric
@attribute 20x numeric
@attribute 20y numeric
@attribute 20z numeric
@attribute 21x numeric
@attribute 21y numeric
@attribute 21z numeric
@attribute 22x numeric
@attribute 22y numeric
@attribute 22z numeric
@attribute 23x numeric
@attribute 23y numeric
@attribute 23z numeric
@attribute 24x numeric
@attribute 24y numeric
@attribute 24z numeric
@attribute 25x numeric
@attribute 25y numeric
@attribute 25z numeric
@attribute 26x numeric
@attribute 26y numeric
@attribute 26z numeric
@attribute 27x numeric
@attribute 27y numeric
@attribute 27z numeric
@attribute 28x numeric
@attribute 28y numeric
@attribute 28z numeric
@attribute 29x numeric
@attribute 29y numeric
@attribute 29z numeric
@attribute 30x numeric
@attribute 30y numeric
@attribute 30z numeric
@attribute 31x numeric
@attribute 31y numeric
@attribute 31z numeric
@attribute 32x numeric
@attribute 32y numeric
@attribute 32z numeric
@attribute 33x numeric
@attribute 33y numeric
@attribute 33z numeric
@attribute 34x numeric
@attribute 34y numeric
@attribute 34z numeric
@attribute 35x numeric
@attribute 35y numeric
@attribute 35z numeric
@attribute 36x numeric
@attribute 36y numeric
@attribute 36z numeric
@attribute 37x numeric
@attribute 37y numeric
@attribute 37z numeric
@attribute 38x numeric
@attribute 38y numeric
@attribute 38z numeric
@attribute 39x numeric
@attribute 39y numeric
@attribute 39z numeric
@attribute 40x numeric
@attribute 40y numeric
@attribute 40z numeric
@attribute 41x numeric
@attribute 41y numeric
@attribute 41z numeric
@attribute 42x numeric
@attribute 42y numeric
@attribute 42z numeric
@attribute 43x numeric
@attribute 43y numeric
@attribute 43z numeric
@attribute 44x numeric
@attribute 44y numeric
@attribute 44z numeric
@attribute 45x numeric
@attribute 45y numeric
@attribute 45z numeric
@attribute 46x numeric
@attribute 46y numeric
@attribute 46z numeric
@attribute 47x numeric
@attribute 47y numeric
@attribute 47z numeric
@attribute 48x numeric
@attribute 48y numeric
@attribute 48z numeric
@attribute 49x numeric
@attribute 49y numeric
@attribute 49z numeric
@attribute 50x numeric
@attribute 50y numeric
@attribute 50z numeric
@attribute 51x numeric
@attribute 51y numeric
@attribute 51z numeric
@attribute 52x numeric
@attribute 52y numeric
@attribute 52z numeric
@attribute 53x numeric
@attribute 53y numeric
@attribute 53z numeric
@attribute 54x numeric
@attribute 54y numeric
@attribute 54z numeric
@attribute 55x numeric
@attribute 55y numeric
@attribute 55z numeric
@attribute 56x numeric
@attribute 56y numeric
@attribute 56z numeric
@attribute 57x numeric
@attribute 57y numeric
@attribute 57z numeric
@attribute 58x numeric
@attribute 58y numeric
@attribute 58z numeric
@attribute 59x numeric
@attribute 59y numeric
@attribute 59z numeric
@attribute 60x numeric
@attribute 60y numeric
@attribute 60z numeric
@attribute 61x numeric
@attribute 61y numeric
@attribute 61z numeric
@attribute 62x numeric
@attribute 62y numeric
@attribute 62z numeric
@attribute 63x numeric
@attribute 63y numeric
@attribute 63z numeric
@attribute 64x numeric
@attribute 64y numeric
@attribute 64z numeric
@attribute 65x numeric
@attribute 65y numeric
@attribute 65z numeric
@attribute 66x numeric
@attribute 66y numeric
@attribute 66z numeric
@attribute 67x numeric
@attribute 67y numeric
@attribute 67z numeric
@attribute 68x numeric
@attribute 68y numeric
@attribute 68z numeric
@attribute 69x numeric
@attribute 69y numeric
@attribute 69z numeric
@attribute 70x numeric
@attribute 70y numeric
@attribute 70z numeric
@attribute 71x numeric
@attribute 71y numeric
@attribute 71z numeric
@attribute 72x numeric
@attribute 72y numeric
@attribute 72z numeric
@attribute 73x numeric
@attribute 73y numeric
@attribute 73z numeric
@attribute 74x numeric
@attribute 74y numeric
@attribute 74z numeric
@attribute 75x numeric
@attribute 75y numeric
@attribute 75z numeric
@attribute 76x numeric
@attribute 76y numeric
@attribute 76z numeric
@attribute 77x numeric
@attribute 77y numeric
@attribute 77z numeric
@attribute 78x numeric
@attribute 78y numeric
@attribute 78z numeric
@attribute 79x numeric
@attribute 79y numeric
@attribute 79z numeric
@attribute 80x numeric
@attribute 80y numeric
@attribute 80z numeric
@attribute 81x numeric
@attribute 81y numeric
@attribute 81z numeric
@attribute 82x numeric
@attribute 82y numeric
@attribute 82z numeric
@attribute 83x numeric
@attribute 83y numeric
@attribute 83z numeric
@attribute 84x numeric
@attribute 84y numeric
@attribute 84z numeric
@attribute 85x numeric
@attribute 85y numeric
@attribute 85z numeric
@attribute 86x numeric
@attribute 86y numeric
@attribute 86z numeric
@attribute 87x numeric
@attribute 87y numeric
@attribute 87z numeric
@attribute 88x numeric
@attribute 88y numeric
@attribute 88z numeric
@attribute 89x numeric
@attribute 89y numeric
@attribute 89z numeric
@attribute 90x numeric
@attribute 90y numeric
@attribute 90z numeric
@attribute 91x numeric
@attribute 91y numeric
@attribute 91z numeric
@attribute 92x numeric
@attribute 92y numeric
@attribute 92z numeric
@attribute 93x numeric
@attribute 93y numeric
@attribute 93z numeric
@attribute 94x numeric
@attribute 94y numeric
@attribute 94z numeric
@attribute 95x numeric
@attribute 95y numeric
@attribute 95z numeric
@attribute 96x numeric
@attribute 96y numeric
@attribute 96z numeric
@attribute 97x numeric
@attribute 97y numeric
@attribute 97z numeric
@attribute 98x numeric
@attribute 98y numeric
@attribute 98z numeric
@attribute 99x numeric
@attribute 99y numeric
@attribute 99z numeric
@attribute label {0,1}
"""
    arff_header = '@relation' + ' ' + rel_name + '\n' + attrib_header + '\n@data' + '\n'
    csv_header =  "timestamp,0x,0y,0z,1x,1y,1z,2x,2y,2z,3x,3y,3z,4x,4y,4z,5x,5y,5z,6x,6y,6z,7x,7y,7z,8x,8y,8z,9x,9y,9z,10x,10y,10z,11x,11y,11z,12x,12y,12z,13x,13y,13z,14x,14y,14z,15x,15y,15z,16x,16y,16z,17x,17y,17z,18x,18y,18z,19x,19y,19z,20x,20y,20z,21x,21y,21z,22x,22y,22z,23x,23y,23z,24x,24y,24z,25x,25y,25z,26x,26y,26z,27x,27y,27z,28x,28y,28z,29x,29y,29z,30x,30y,30z,31x,31y,31z,32x,32y,32z,33x,33y,33z,34x,34y,34z,35x,35y,35z,36x,36y,36z,37x,37y,37z,38x,38y,38z,39x,39y,39z,40x,40y,40z,41x,41y,41z,42x,42y,42z,43x,43y,43z,44x,44y,44z,45x,45y,45z,46x,46y,46z,47x,47y,47z,48x,48y,48z,49x,49y,49z,50x,50y,50z,51x,51y,51z,52x,52y,52z,53x,53y,53z,54x,54y,54z,55x,55y,55z,56x,56y,56z,57x,57y,57z,58x,58y,58z,59x,59y,59z,60x,60y,60z,61x,61y,61z,62x,62y,62z,63x,63y,63z,64x,64y,64z,65x,65y,65z,66x,66y,66z,67x,67y,67z,68x,68y,68z,69x,69y,69z,70x,70y,70z,71x,71y,71z,72x,72y,72z,73x,73y,73z,74x,74y,74z,75x,75y,75z,76x,76y,76z,77x,77y,77z,78x,78y,78z,79x,79y,79z,80x,80y,80z,81x,81y,81z,82x,82y,82z,83x,83y,83z,84x,84y,84z,85x,85y,85z,86x,86y,86z,87x,87y,87z,88x,88y,88z,89x,89y,89z,90x,90y,90z,91x,91y,91z,92x,92y,92z,93x,93y,93z,94x,94y,94z,95x,95y,95z,96x,96y,96z,97x,97y,97z,98x,98y,98z,99x,99y,99z,label" + '\n'
    
    if type == 'csv':
        out_fp.write(csv_header)
    elif type == 'arff':
        out_fp.write(arff_header)
    
    #other lines appending
    out_fp.write(in_fp.read())
    
    out_fp.close()
    in_fp.close()

def call_append_header(dir, type):
    files = os.listdir(dir)
    out_dir = dir.replace('/no_header/', str('/' + type + '_files' + '/'))
    for file in files:
        src = dir + file
        src = str(src)
        #[:-4] done to remove the .csv extension from the target files and appending necessary extensions
        dest = out_dir + file[:-4] + str('.' + type)
        dest = str(dest)
        append_header(src, dest, dest[:-4], type)

#MAIN
in_dir_list = [
"../data/no_header/user_dep/full/",
"../data/no_header/user_dep/train/",
"../data/no_header/user_dep/validate/",
"../data/no_header/user_dep/test/",
"../data/no_header/user_indep/full/",
"../data/no_header/user_indep/train/",
"../data/no_header/user_indep/validate/",
"../data/no_header/user_indep/test/"
]
types = ["csv", "arff"]
for t in types:
    for d in in_dir_list:
        call_append_header(d, t)

#END
