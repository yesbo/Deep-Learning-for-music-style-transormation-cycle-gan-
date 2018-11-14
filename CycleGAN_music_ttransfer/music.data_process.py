import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.ndimage import imread
import h5py
import pandas as pd


os.chdir("/Users/hongbozhu/Desktop/6104 project")
track_file=pd.read_csv("./fma_metadata/tracks.csv")
track_file=tran