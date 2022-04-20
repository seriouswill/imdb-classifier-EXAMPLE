import os
import shutil

import tensorflow as tf

url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"

dataset = tf.keras.utils.get_file("aclImdb_v1", url,
                                    untar=True, cache_dir='.',
                                    cache_subdir='')

dataset_dir = os.path.join(os.path.dirname(dataset), 'aclImdb')
os.listdir(dataset_dir) # This will show you the working directory
train_dir = os.path.join(dataset_dir, 'train')
os.listdir(train_dir) # This will show you the updated directory

remove_dir = os.path.join(train_dir, 'unsup') # Neccessary to remove the 'Unsupported' folder which we have no use for.
shutil.rmtree(remove_dir)

# Optional, to look at format
sample_file = os.path.join(train_dir, 'pos/1181_9.txt')
with open(sample_file) as f:
  print(f.read())