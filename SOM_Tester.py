# For plotting the images
from matplotlib import pyplot as plt
import numpy as np
from SOM import SOM
from AffinityPropogation import AffinityPropogation
import csv

num_tracks = 50 #1974
a = []
b = []
dataset = 'C:/Users/Bharat Bojja/Documents/Programming/SongClassification/FullDataSet.csv'
reader = csv.reader(open(dataset, 'rt'), delimiter=',', quoting=csv.QUOTE_NONE)
next(reader)
i = 0
audio_features = []
track_names = []
for row in reader:
    audio_features.append(list(row[i] for i in range(7, 17)))
    track_names.append(list(row[i] for i in range(6, 7)))
    i += 1
    if i == num_tracks:
        break

# Training inputs for tracks
audio_features = np.asarray(audio_features, dtype=float)

# Train a 20x30 SOM with 10 iterations
som = SOM(20, 30, 10, 50)
som.train(audio_features)

# Get output grid
image_grid = som.get_centroids()

# Map tracks to their closest neurons
mapped = som.map_vects(audio_features)

# Plot
plt.imshow(image_grid[10])
plt.title('Track SOM')
plt.ylim([0,20])
plt.xlim([0,30])
for i, m in enumerate(mapped):
    plt.text(m[1], m[0], track_names[i], ha='center', va='center',
             bbox=dict(facecolor='white', alpha=0.5, lw=0))
aff = AffinityPropogation(mapped)
print(track_names)
plt.show()