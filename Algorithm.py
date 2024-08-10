import os
import surprise
from surprise import KNNBasic, Dataset, Reader, accuracy
from surprise.model_selection import KFold

print("start")
# Find the path to the dataset
# Apply the reader so it knows how to properly sort the data and identify sections with \t (tab) as the known separator and scale as 1-10
# "~" home directory (user path)
# rest is normal stuff, the expanded format should be C:\\Users\\leeya/Desktop/Capstone Algorithm/anime/anime_ratings.dat

# Debugging where the file read went wrong, deleted first line of data file so title isn't included
# file_path = str(os.path.dirname(__file__))
# f=open(file_path + "/anime/anime_ratings.txt", 'r').readlines()
# N=len(f)-1
# for i in range(0,N):
#     w=f[i].split("\t")
#     l1=w[1:8]
#     l2=w[8:15]
#     try:
#         list1=[float(x) for x in l1]
#         list2=[float(x) for x in l2]
#     except ValueError:
#         print ("error on line" + str(i))

file_path = os.path.expanduser("~/Desktop/Capstone Algorithm/anime/anime_ratings.txt")
reader = Reader(line_format="user item rating", sep="\t", rating_scale=(1,10), skip_lines=1)
data = Dataset.load_from_file(file_path, reader=reader)

# Separate into training and testing datasets, 5 is current
kf = KFold(n_splits=5)

trainset = data.build_full_trainset()
algo = KNNBasic(sim_options={"name":"pearson"})

print(kf)
# setting trainset to one split of kf and testset to another split of kf
# training the algo multiple times (5 sets) to improve the algo gradually
# splitting kf into more sets could create lower accuracy returned, but also a lower chance of overfitting.
# 
for trainset, testset in kf.split(data):
    algo.fit(trainset)
    print("FITTED")
    predictions = algo.test(testset)
    print("TESTED")
    accuracy.rmse(predictions, verbose=True)


while (True):
    uid = str(input("What user to predict for?\n"))
    if(uid=="quit"):
        print("Fine I quit!")
        break
    iid = str(input("What item to predict for?\n"))
# r_ui is the user id rating, the rating of the user for the given item, 
# we have provided the true rating, and will try to predict the theoretical rating
    pred = algo.predict(uid, iid, r_ui=4, verbose=True)
    print("done!")