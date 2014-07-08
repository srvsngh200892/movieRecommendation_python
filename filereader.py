rating_array = []
with open("/home/hasher/Downloads/movie_recommendation/ratings.data", "r") as f:
     for line in f:
         rating_array.append(line)
rating_list=[]
for i in rating_array:
    x=i.split('\t')
    rating_list.append(x)
print rating_list
