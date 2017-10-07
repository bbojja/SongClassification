import csv
import numpy as np

num_tracks = 2;
a = []
b = []
dataset = 'C:/Users/Bharat Bojja/Documents/Programming/SongClassification/FullDataSet.csv'
reader = csv.reader(open(dataset, 'rt'), delimiter=',', quoting=csv.QUOTE_NONE)
next(reader)
for row in reader:
    a.append(list(row[i] for i in range(7, 20)))
    b.append(list(row[i] for i in range(6, 7)))

# Training inputs for tracks
audio_features = []
track_names = []
for i in range(0, num_tracks):
    audio_features.append(a[i])
    track_names.append(b[i])

print(audio_features)
print(track_names)