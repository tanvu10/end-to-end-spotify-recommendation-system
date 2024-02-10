# end-to-end-spotify-recommendation-system
end-to-end-spotify-recommendation-system



## Dataset:
Spotify Million Playlist Dataset Challenge: consists of a dataset and evaluation to enable research in music recommendations. It is a continuation of the RecSys Challenge 2018, which ran from January to July 2018. The dataset contains 1,000,000 playlists, including playlist titles and track titles, created by users on the Spotify platform between January 2010 and October 2017.






## Types of Candidate Generation Systems:
1. Content-based filtering System
- Does not require other users' data during recommendations to one user.

2. Collaborative filtering System
- Considers other users’ reactions while recommending a particular user. It notes which items a particular user likes and also the items that the users with behavior and likings like him/her likes, to recommend items to that user.
- Combat with biases of each user: Normalize all ratings of that particular using by de-meaning it at user level
- Memory-based collaborative filtering:
    - User-User filtering: we can say, “the users who like products similar to you also liked those products”. 
    - Item-Item filtering: it can be said "Because you liked x, you may also like y, z if those are similar to x".
    - Similarity metrics:
        - Cosine Similarity
        - Dot Product
        - Euclidian Distance
        - Pearson Similarity
- Model-based collaborative filtering:
    - Weighted Alternating Least Squares:
    