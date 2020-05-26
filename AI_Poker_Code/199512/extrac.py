# import csv
# import os
#
# #-----------------------------------
# #This script will replace the tab delimiter in the files and save them with a comma delimited csv format.
# #-----------------------------------
#
# """
# Set up paths
# """
# source_path = "./pdb/"
# dest_path = source_path
#
# """
# Pseudo code
# For all files in source directory
# create matching csv file in destination directory
# open each file
# for each line in source file
#     write to csv file
# """
#
# for file in os.listdir(source_path):
#     #get filename without file extension
#     filename_no_extension = os.path.splitext(file)[0]
#
#     #concatenate filename amd paths
#     dest_csv_file = str(filename_no_extension) + ".csv"
#     dest_file = os.path.join(dest_path,dest_csv_file)
#     source_file = os.path.join(source_path,file)
#
#     #open the original file and create reader object
#     with open(source_file, "r") as infile:
#         reader = csv.reader(infile,delimiter=" ",skipinitialspace=True)
#         with open(dest_file, "w") as outfile:
#             writer = csv.writer(outfile, delimiter = ',')
#             for row in reader:
#                 writer.writerow(row)

import csv,glob,pickle
from deuces import *
map={}
map2={}

hdbmap={}
for i in glob.iglob("./hdb_in_csv.csv"):
    with open(i) as f:
        reader = csv.reader(f, delimiter=",")
        for j in reader:
            if 1:
                try:
                    print j[13]
                    hdbmap[j[0]].append([j])
                except:
                    hdbmap[j[0]] = [j]
print("Search for timestamp in hdb",hdbmap['817845912'])
for i in glob.iglob("./pdb/*.csv"):
    with open(i) as f:
        reader = csv.reader(f, delimiter=",")
        for j in reader:
            try:
                map[j[1]].append(i)
            except:
                map[j[1]]=[i]
            if len(j[11]):
                try:
                    map2[j[0]].append([j[1],j[3],list(hdbmap[j[1]][0][8].split()),list(j[4]),list(j[5]),list(j[6]),list(j[7]),j[8],j[9],j[10],[j[11],j[12]]])
                except:
                    map2[j[0]] = [[j[1],j[3],list(hdbmap[j[1]][0][8].split()),list(j[4]),list(j[5]),list(j[6]),list(j[7]),j[8],j[9],j[10],[j[11],j[12]]]]
count=0

for i in map:
    for j in map[i]:
        with open(j) as f:
            reader = csv.reader(f, delimiter=",")
            for l in reader:
                if l[1]==i:
                    print l

    count+=1
    print
    if count==10:
        break
c=0
for i in map2:
    print i,map2[i]
    c+=1
    if c==10:
        break
picklewords=open("dic1.pkl","wb")
pickle.dump(map2,picklewords)
picklewords.close()
picklewords=open("dic2.pkl","wb")
pickle.dump(map,picklewords)
picklewords.close()
picklewords=open("dic3.pkl","wb")
pickle.dump(hdbmap,picklewords)
picklewords.close()
picklewords=open("dic.pkl","rb")
dic=pickle.load(picklewords)