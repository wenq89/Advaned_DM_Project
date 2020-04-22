# Advaned_DM_Project
The program requires users to enter their "height" "weight" "size(bust_size)" "age" "the purpose of renting(X)"
Then our RS(recommender system) which output top 10 products that match the user's demand.
Also we will show the visualization of all the users' review.
The original data set is not uploaded as it exceeds the maximum file size.

## data preprocessing
1. find_purposes() to observe how many types of renting purposes
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

## centered cosine similarity
1. Convert the values in the attributes "height" "weight" "size" to CM unit
2. generate the cosine similarity files for each renting purpose.

## experiment
1. weight the cosine similarity and "age"
2. get top 10 recommendations
3. compare our prediction to the real data, e.g., is one of the top 10 same as the real data?
4. the accuracy
