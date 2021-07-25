from os.path import join
import glob
import numpy as np

root_path = './data/'
# get the list of files in lidar directory
file_names = sorted(glob.glob(join(root_path, '*/lidar/cam_front_center/*.npz')))

# select the lidar point cloud
file_name_lidar = file_names[5]

# read the lidar data
lidar_front_center = np.load(file_name_lidar)