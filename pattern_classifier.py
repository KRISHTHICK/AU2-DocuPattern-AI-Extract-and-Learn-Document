from sklearn.cluster import KMeans
import numpy as np

def learn_and_classify_patterns(table_patterns):
    features = []
    for pattern in table_patterns:
        features.append([
            pattern["rows"],
            pattern["columns"],
            int(pattern["contains_units"]),
            int(pattern["contains_checkboxes"])
        ])

    model = KMeans(n_clusters=3)
    clusters = model.fit_predict(np.array(features))

    for idx, pattern in enumerate(table_patterns):
        pattern["pattern_id"] = int(clusters[idx])
    
    return table_patterns
