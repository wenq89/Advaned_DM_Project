# Advaned_DM_Project
The program requires users to enter their "height" "weight" "size(bust_size)" "age" "the purpose of renting(X)"
Then our RS(recommender system) which output top 10 products that match the user's demand.
Also we will show the visualization of all the users' review.
The original data set is not uploaded as it exceeds the maximum file size.

## data preprocessing
divide the big data set to several small data sets depends on the purpose of the renting
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

## centered cosine similarity 
1. 