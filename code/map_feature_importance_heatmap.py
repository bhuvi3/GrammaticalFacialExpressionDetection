#To map the feature importance to heatmap
import os
import numpy as np
import matplotlib.pyplot as plt
#returns importances of timestamp and list of importances of all facepoints such that each facepoint importance is repesented as (facepoint, (x_imp, y_imp, z_imp)) 
def get_importances(importances_file):
    fi_fp = open(importances_file)
    fl = fi_fp.readline()
    timestamp = fi_fp.readline().strip("\n").split(",")[1]
    importances_astuple = []
    for i in range(100):
        x = fi_fp.readline().strip("\n").split(",")[1]
        y = fi_fp.readline().strip("\n").split(",")[1]
        z = fi_fp.readline().strip("\n").split(",")[1]
        feature_imp = (i, (float(x), float(y), float(z)))
        importances_astuple.append(feature_imp)
    
    fi_fp.close()
    return (timestamp, importances_astuple)
    
#pixel_map_file has exactly 100 lines with each line representing the mapping from facepoint to its pixel coordinates in a square image of pixel_size. Each line such that: facepoint, x, y. Where x and y represent the facepoint's coordinate in the image. facepoint count is from 0 to 99.
def map_to_pixel_space(importances_file, pixel_map_file, pixel_size):
    timestamp_imp, face_importances = get_importances(importances_file)
    image_array = np.empty((pixel_size, pixel_size))
    #basicaly represting each points values as an array of shape 3 of r g b values ranging from 0-1
    not_face_point = (0.0,0.0,0.0)
    image_array.fill(np.array(not_face_point))
    fp = open(pixel_map_file)
    facepoint_coordinates = fp.read().splitlines()
    fp.close()
    
    for coord in facepoint_coordinates:
        tokens = coor.split(",")
        facepoint = int(token[0])
        x = int(token[1])
        y = int(token[2])
        facepoint_imp_tuple = face_importances[facepoint]
        if facepoint != facepoint_imp_tuple[0]:
            print "Ordering ERROR!!!"
            return 1
        facepoint_imp = n.array(facepoint_imp_tuple[1], dtype="float")
        image_array[x][y] = facepoint_imp
    
    return timestamp_imp, image_array

#generates heatmap for a given expression
def gen_heatmap(importances_file, pixel_map_file, pixel_size):
    timestamp_imp, image_space = map_to_pixel_space(importances_file, pixel_map_file, pixel_size)
    expression_name = importances_file[:-4].title()
    fig = plt.figure()
    #image space is nxnx3 right! so at ixj for all i,j in n; it uses the color from rgb values specified for each of them
    #refer: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.matshow
    #matshow uses imshow() for getting keyword args so: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.imshow
    #here its shown that it takes nxmx3 array
    plt.matshow(image_space, cmap=plt.cm.hot)
    plt.title(expression_name)
    #Print timestamp info also here if you want
    #plt.show()
    return fig

#reads features importances files of all expressions from source dir and makes a pdf with all the feature importance heatmaps in the target dir
#needs pixel_map_file and pixel_size of the heatmap to be generated
def get_all_heatmaps(source_dir, target_dir, pixel_map_file, pixel_size):
    pdf_fh = PdfPages(target_dir + "/importances_maps" + ".pdf")
    files = os.listdir(source_dir)
    for importance_file in files:
        fig = gen_heatmap(importances_file, pixel_map_file, pixel_size)
        fig.savefig(pdf_fh, format='pdf')

#MAIN
imp = "../feature_importance/feature_imp/affirmative.csv"
pmf = "../data/pixel_facepoints_mapping.csv"
fig = gen_heatmap(imp, pmf, 850)