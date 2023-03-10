#!/bin/bash
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
DATASET=$1
TRAIN_MODE=$2
DATA_PATH=$3
SAVE_CKPT=$4  # ../output
if [ ! -d $SAVE_CKPT  ];then
mkdir $SAVE_CKPT
fi
python ../train.py --dataset=$DATASET \
    --train_mode=$TRAIN_MODE \
    --data_path=$DATA_PATH \
    --save_ckpt=$SAVE_CKPT  &> log_train_1p.txt &
