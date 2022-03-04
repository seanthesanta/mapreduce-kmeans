#!/usr/bin/env python

import struct
import pickle

# SIZE: 124800 for training; 20800 for testing
# DIM: 28*28=784 pixels

train_images = "data/emnist-letters-train-images-idx3-ubyte"
train_labels = "data/emnist-letters-train-labels-idx1-ubyte"
test_images = "data/emnist-letters-test-images-idx3-ubyte"
test_labels = "data/emnist-letters-test-labels-idx1-ubyte"

def load_img(filepath):
    data = []
    print 'Loading: %s' % (filepath)
    with open(filepath, 'rb') as f:
        magic, size, rows, cols = struct.unpack('>IIII', f.read(16))
        for img in range(size):
            data.append(struct.unpack('>784B', f.read(784)))
            if (img+1) % 10000 == 0:
                print 'Loaded: %s' % (str(img+1))
    return data

def load_lbl(filepath):
    print 'Loading: %s' % (filepath)
    data = []
    with open(filepath, 'rb') as f:
        magic, size = struct.unpack('>II', f.read(8))
        for img in range(size):
            data.append(struct.unpack('>B', f.read(1))[0])
            if (img+1) % 10000 == 0:
                print 'Loaded: %s' % (str(img+1))
    return data

def write_to_file(filepath, data):
    print 'Writing %s to file...' % (filepath)
    with open(filepath, 'w') as f:
        for i, img in enumerate(data):
            f.write(str(i))
            if (i+1) % 10000 == 0:
                print 'Writing img: %s' % (str(i+1))
            for pixel in img:
                f.write(' ' + str(pixel))
            f.write('\n')

def write_to_pkl(filepath, data):
    print 'Writing %s to pkl...' % (filepath)
    with open(filepath, 'wb') as f:
        pickle.dump(data, f)

#write_to_file("train_images", load_img(train_images))
write_to_pkl("train_labels.pkl", load_lbl(train_labels))
#write_to_file("test_images", load_img(test_images))
write_to_pkl("test_labels.pkl", load_lbl(test_labels))

