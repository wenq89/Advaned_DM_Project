# Advaned_DM_Project
The program requires users to enter their "height" "weight" "size(bust_size)" "age" "the purpose of renting(X)"
Then our RS(recommender system) which output top 10 products that match the user's demand.
Also we will show the visualization of all the users' review.
The original data set is not uploaded as it exceeds the maximum file size.

file info: 
max_height, max_w, min_height, min_w
198.12 300 137.16 50

## data preprocessing
1. find_purposes() to observe how many types of renting purposes, and find the cells with
    missing values: # of tuples with no height: 677, # of tuples with no weight 29982
    The number of tuples does not have the key-"rented for":  10 (eliminated)
    The "rented for" dictionary from original data set:
    purpose     count
    'vacation': 4075, 
    'other': 15388, 
    'party': 35626, 
    'formal affair': 40408, 
    'wedding': 57784, 
    'date': 7388, 
    'everyday': 16822, 
    'work': 15042, 
    'party: cocktail': 1 (eliminated)
2. divide the big data set to several small data sets depends on the purpose of the renting
3. create all the data files based on the renting purpose.
4. Convert the values in the attributes "height" "weight" "size" to CM unit
3. create all the cosine similarity-based table and store in the json files 

## centered cosine similarity
Traditional cosine similarity treat missing cells as 0, but we have missing values: # of tuples with no height: 677, # of tuples with no weight 29982
thus, we use centered cosine similarity where we treat the missing values as the average of all the
available values in a certain tuple

- generate the cosine similarity files for each renting purpose.

## experiment
1. weight the cosine similarity and "age"
2. get top 10 recommendations and demonstrate to the users.
3. did the user actually buy it in the real data?
