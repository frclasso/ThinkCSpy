#!/usr/bin/python

#-*-coding: latin1 -*-


def inBucket(t, low, high):
    count = 0
    for num in t:
        if low < num < high:
            count = count + 1
        return count


numBuckets = 8
bucketWidth = 1.0 / numBuckets
for i in range(numBuckets):
    low = i * bucketWidth
    high = low + bucketWidth
    print(low, "to", high)


"""
NAO DEU CERTO
buckets = [0] * numBuckets
bucketWidth = 1.0 / numBuckets
for i in range(numBuckets):
    low = i * bucketWidth
    high = low + bucketWidth
    buckets[i] = inBucket(t, low, high)
print(buckets)
"""


"""
NAO DEU CERTO
buckets = [0] * numBuckets
for i in t:
    index = int(i * numBuckets)
    buckets[index] = buckets[index] + 1
print(buckets)
"""