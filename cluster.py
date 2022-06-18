# %%
from scipy.cluster.hierarchy import dendrogram
from sklearn.cluster import AgglomerativeClustering
import sys
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.neighbors import kneighbors_graph
from sklearn import metrics
from sklearn.cluster import DBSCAN
from sklearn import preprocessing
from vectorize import load, length
from tools import get_progressbar
import numpy as np
from sklearn.metrics import DistanceMetric

# %%
_len_ = length('words')
bar = get_progressbar(_len_, f' {_len_} scatter matrix computing ')

frame = dict([(f'x{i}', []) for i in range(96)])
vectors = []
vectors_to_text = {}
bar.start()
for i, tuple_ in enumerate(load('words')):
    if len(tuple_[1]) > 0:
        vectors.append(np.array(tuple_[1]))
        vectors_to_text[tuple_[1]] = tuple_[0]

    for i, comp in enumerate(tuple_[1]):
        frame[f'x{i}'].append(comp)

    bar.update(i+1)
bar.finish()


# %%


def dbscan():
    vector = preprocessing.normalize(vectors)

    db = DBSCAN(eps=0.8, min_samples=10,
                metric='cosine', n_jobs=10).fit(vector)
    # core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    # core_samples_mask[db.core_sample_indices_] = True

    labels = db.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)

    print("Estimated number of clusters: %d" % n_clusters_)
    print("Estimated number of noise points: %d" % n_noise_)
    # print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
    # print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
    # print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
    # print("Adjusted Rand Index: %0.3f" % metrics.adjusted_rand_score(labels_true, labels))
    # print(
    #     "Adjusted Mutual Information: %0.3f"
    #     % metrics.adjusted_mutual_info_score(labels_true, labels)
    # )
    print("Silhouette Coefficient: %0.3f" %
          metrics.silhouette_score(vector, labels))


# %%


def metric():
    vector = preprocessing.normalize(vectors)

    dist = DistanceMetric.get_metric('manhattan')
    matsim = dist.pairwise(vector)
    minPits = 5
    A = kneighbors_graph(vector, minPits, include_self=False).toarray()

    seq = []
    bar = get_progressbar(_len_ * _len_, f' {_len_ * _len_} matrix ')
    bar.start()
    for i, s in enumerate(vector):
        for j in range(len(vector)):
            if A[i][j] != 0:
                seq.append(matsim[i][j])

            bar.update(i+1)
    bar.finish()

    seq.sort()
    plt.plot(seq)
    plt.show()


# %%


def plot_results(inertials):
    x, y = zip(*[inertia for inertia in inertials])
    plt.plot(x, y, 'ro-', markersize=8, lw=2)
    plt.grid(True)
    plt.xlabel('Num Clusters')
    plt.ylabel('Inertia')
    plt.show()


def select_clusters(loops, max_iterations, init_cluster, tolerance,
                    num_threads):
    # Read data set
    points = vectors

    inertia_clusters = list()
    # bar = get_progressbar(loops+1, f' {loops} loop ')

    # bar.start()
    for i in range(1, loops + 1, 1):
        # Object KMeans
        kmeans = KMeans(n_clusters=i, max_iter=max_iterations,
                        init=init_cluster, tol=tolerance, verbose=1)

        # Calculate Kmeans
        kmeans.fit(points)

        # Obtain inertia
        inertia_clusters.append([i, kmeans.inertia_])
    #     bar.update(i+1)
    # bar.finish()

    plot_results(inertia_clusters)


# %%


def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    # Plot the corresponding dendrogram
    return dendrogram(linkage_matrix, **kwargs)


def agglo():
    # setting distance_threshold=0 ensures we compute the full tree.
    model = AgglomerativeClustering(
        distance_threshold=0, n_clusters=None, affinity='cosine', linkage='single')

    model = model.fit(vectors)
    plt.title("Hierarchical Clustering Dendrogram")
    # plot the top three levels of the dendrogram
    data = plot_dendrogram(model)
    plt.xlabel("Number of points in node (or index of point if no parenthesis).")
    plt.show()


if __name__ == '__main__':
    cmd = sys.argv[1]

    if cmd == dbscan.__name__:
        print('dbscan command')
        dbscan()

    if cmd == metric.__name__:
        print('metric command')
        metric()

    if cmd == agglo.__name__:
        print('agglo command')
        metric()

    if cmd == 'kmean':
        print('kmean command')
        select_clusters(20, 10000, "k-means++", 0.00001, 10)
