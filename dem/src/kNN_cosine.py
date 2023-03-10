# 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""
k-nearest neighbor with cosine algorithm, will be used to compute accuracy in train.py
"""
import math
import numpy as np

# create a dataset which contains 4 samples with 2 classes
def createDataSet():
    group = np.array([[1.0, 0.9], [1.0, 1.0], [0.1, 0.2], [0.0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def cosine_distance(v1, v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    v1_sq = np.inner(v1, v1)
    v2_sq = np.inner(v2, v2)
    dis = 1 - np.inner(v1, v2) / math.sqrt(v1_sq * v2_sq)
    return dis

def kNNClassify(newInput, dataSet, labels, k):
    """classify using kNN"""
    distance = [0] * dataSet.shape[0]
    for i in range(dataSet.shape[0]):
        distance[i] = cosine_distance(newInput, dataSet[i])
    sortedDistIndices = np.argsort(distance)
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDistIndices[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            maxIndex = key
    return maxIndex
    #return sortedDistIndices
