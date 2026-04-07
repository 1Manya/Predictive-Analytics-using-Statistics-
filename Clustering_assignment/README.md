# Comparative Performance Study of Clustering Algorithms on Wine Dataset

## About
Selected the UCI Wine dataset from the UCI Machine Learning Repository.
It has 178 samples and 13 features with 3 classes.

## What I Did
- Applied 3 clustering algorithms: K-Means, Hierarchical, Mean Shift
- Used 6 preprocessing techniques: No Processing, Normalization, Standardization, PCA, T+N, T+N+PCA
- Tested with c=3, c=4, c=5 clusters
- Evaluated using Silhouette Score, Calinski-Harabasz Index, Davies-Bouldin Index

## Results

### K-Means Clustering

| Parameters | No Processing | | | Normalization | | | Transform | | | PCA | | | T+N | | | T+N+PCA | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | c=3 | c=4 | c=5 | c=3 | c=4 | c=5 | c=3 | c=4 | c=5 | c=3 | c=4 | c=5 | c=3 | c=4 | c=5 | c=3 | c=4 | c=5 |
| Silhouette | 0.57 | 0.56 | 0.55 | 0.30 | 0.26 | 0.20 | 0.28 | 0.26 | 0.20 | 0.57 | 0.56 | 0.55 | 0.30 | 0.26 | 0.20 | 0.57 | 0.49 | 0.45 |
| Calinski-Harabasz | 562 | 708 | 787 | 83 | 66 | 54 | 71 | 56 | 47 | 563 | 710 | 790 | 83 | 66 | 54 | 376 | 353 | 347 |
| Davies-Bouldin | 0.53 | 0.54 | 0.55 | 1.31 | 1.72 | 1.82 | 1.39 | 1.80 | 1.81 | 0.53 | 0.54 | 0.54 | 1.31 | 1.72 | 1.82 | 0.58 | 0.73 | 0.76 |

### Hierarchical Clustering

| Parameters | No Processing | | | Normalization | | | Transform | | | PCA | | | T+N | | | T+N+PCA | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | c=3 | c=4 | c=5 | c=3 | c=4 | c=5 | c=3 | c=4 | c=5 | c=3 | c=4 | c=5 | c=3 | c=4 | c=5 | c=3 | c=4 | c=5 |
| Silhouette | | | | | | | | | | | | | | | | | | |
| Calinski-Harabasz | | | | | | | | | | | | | | | | | | |
| Davies-Bouldin | | | | | | | | | | | | | | | | | | |

### Mean Shift Clustering

> Mean Shift auto-determines cluster count so most values are NA.

| Parameters | No Processing | | | Normalization | | | Transform | | | PCA | | | T+N | | | T+N+PCA | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | c=3 | c=4 | c=5 | c=3 | c=4 | c=5 | c=3 | c=4 | c=5 | c=3 | c=4 | c=5 | c=3 | c=4 | c=5 | c=3 | c=4 | c=5 |
| Silhouette | NA | NA | 0.55 | NA | NA | 0.22 | NA | NA | NA | NA | NA | 0.55 | NA | NA | 0.22 | 0.57 | NA | NA |
| Calinski-Harabasz | NA | NA | 287 | NA | NA | 25 | NA | NA | NA | NA | NA | 287 | NA | NA | 25 | 375 | NA | NA |
| Davies-Bouldin | NA | NA | 0.45 | NA | NA | 1.13 | NA | NA | NA | NA | NA | 0.45 | NA | NA | 1.13 | 0.59 | NA | NA |

## Graphs

![Cluster Scatter Plots](https://github.com/1Manya/Predictive-Analytics-using-Statistics-/blob/main/Clustering_assignment/graphs/scatter_kmeans_hierarchical.png)

==================================================================================================
![Mean Shift Clusters](https://github.com/1Manya/Predictive-Analytics-using-Statistics-/blob/main/Clustering_assignment/graphs/scatter_meanshift.png)

===================================================================================================
![metric comparison](https://github.com/1Manya/Predictive-Analytics-using-Statistics-/blob/main/Clustering_assignment/graphs/metric_comparison.png)

## Conclusion
From the results, K-Means with Standardization gave the best performance 
at c=3. Preprocessing improved results significantly compared to raw data. 
Mean Shift could not always find the exact number of clusters so some 
values are NA. Overall c=3 worked best since the dataset naturally has 3 classes.
