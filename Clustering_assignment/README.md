# Comparative Performance Study of Clustering Algorithms on Wine Dataset

## About
Selected the UCI Wine dataset from the UCI Machine Learning Repository.
It has 178 samples and 13 features with 3 classes.

## What I Did
- Applied 3 clustering algorithms: K-Means, Hierarchical, Mean Shift
- Used 6 preprocessing techniques: No Processing, Normalization, 
  Standardization, PCA, T+N, T+N+PCA
- Tested with c=3, c=4, c=5 clusters
- Evaluated using Silhouette Score, Calinski-Harabasz Index, Davies-Bouldin Index

## Results

### K-Means
| Parameters | No Processing c=3/4/5 | Normalization c=3/4/5 | Transform c=3/4/5 | PCA c=3/4/5 | T+N c=3/4/5 | T+N+PCA c=3/4/5 |
|---|---|---|---|---|---|---|
| Silhouette | | | | | | |
| Calinski-Harabasz | | | | | | |
| Davies-Bouldin | | | | | | |

### Hierarchical
| Parameters | No Processing c=3/4/5 | Normalization c=3/4/5 | Transform c=3/4/5 | PCA c=3/4/5 | T+N c=3/4/5 | T+N+PCA c=3/4/5 |
|---|---|---|---|---|---|---|
| Silhouette | | | | | | |
| Calinski-Harabasz | | | | | | |
| Davies-Bouldin | | | | | | |

### Mean Shift
| Parameters | No Processing c=3/4/5 | Normalization c=3/4/5 | Transform c=3/4/5 | PCA c=3/4/5 | T+N c=3/4/5 | T+N+PCA c=3/4/5 |
|---|---|---|---|---|---|---|
| Silhouette | | | | | | |
| Calinski-Harabasz | | | | | | |
| Davies-Bouldin | | | | | | |

## Graphs
![scatter_kmeans_hierarchical]('Clustering_assignment/graphs/scatter_kmeans_hierarchical.png')
![meanshift]('Clustering_assignment/graphs/scatter_meanshift.png')
![metrics]("Clustering_assignment/graphs/metric_comparison.png")

## Conclusion
From the results, K-Means with Standardization gave the best performance 
at c=3. Preprocessing improved results significantly compared to raw data. 
Mean Shift could not always find the exact number of clusters so some 
values are NA. Overall c=3 worked best since the dataset naturally has 3 classes.
