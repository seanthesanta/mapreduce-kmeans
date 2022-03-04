#!/usr/bin/env python

import pickle

# Load labels
with open("train_labels.pkl", 'rb') as f:
    labels = pickle.load(f)

def file_to_dict(path):
    dict = {}
    with open(path, 'r') as f:
        for line in f.readlines():
            dataline = line.strip().split()
            dict[int(dataline[0])] = int(dataline[1])
    return dict

NUM_CLUSTER = 37
NUM_LABEL = 26

# Load cluster assignment
path = 'assign'

assignment = file_to_dict(path)
# Record clusters and the assigned img with their true label
# Note: EMNIST labels start from 1, not 0
count_cluster = {cluster: {label: [] for label in range(1, NUM_LABEL+1)}\
                 for cluster in range(NUM_CLUSTER)}

# Loop through all assigned images
for i, c in assignment.items():
    print 'Count: %s' % (str(i))
    # Increase the corr. label count of current cluster by 1
    # Note: EMNIST labels start from 1, not 0
    count_cluster[c][labels[i]].append(i)

# Get the cluster label and calculate its accuracy
accuracy = {cluster: {'label': -1, 'total': 0, 'correct': 0, 'acc': -1}\
                    for cluster in range(NUM_CLUSTER)}
for c, cluster in count_cluster.items():
    print 'Calc acc: %s' % (str(c))
    max_label = -1
    best_label = -1
    for l, label in cluster.items():
        accuracy[c]['total'] += len(label)
        if len(label) > max_label:
            max_label = len(label)
            best_label = l
    # Note: EMNIST labels start from 1, not 0
    accuracy[c]['label'] = best_label
    accuracy[c]['correct'] = max_label
    if accuracy[c]['total'] == accuracy[c]['correct'] and accuracy[c]['total'] == 0:
        accuracy[c]['acc'] = -1
    else:
        accuracy[c]['acc'] = round(float(accuracy[c]['correct']) / accuracy[c]['total'] * 100, 2)

with open('accuracy', 'w') as f:
    total = 0
    correct = 0
    for c, cluster in accuracy.items():
        total += cluster['total']
        correct += cluster['correct']
        f.write(str(c) + ' ' + str(cluster['total']) + ' ' + str(cluster['label']) +
                ' ' + str(cluster['correct']) + ' ' + str(cluster['acc']) + '\n')
    f.write("TOTAL: " + str(total) + '\n' +  "CORRECT: " + str(correct) + '\n' + "OVERALL ACCURACY: " + str(round(float(correct)/total*100, 2)) + '\n')

