
import splitfolders
import os
splitfolders.ratio("data", # The location of dataset
                   output="traindata", # The output location
                   seed=42, # The number of seed
                   ratio=(.7, .25, .05), # The ratio of splited dataset
                   group_prefix=None, # If your dataset contains more than one file like ".jpg", ".pdf", etc
                   move=False # If you choose to move, turn this into True
                   )