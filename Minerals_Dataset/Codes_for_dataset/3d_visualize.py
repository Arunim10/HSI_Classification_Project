import trimesh
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# Load the point cloud
point_cloud = trimesh.load("D:/Machine Learning/Texmin_HSI/HSI_Classification_Updated/Minerals_Dataset/HDR_Data/Extracted_Folder/0000/0000-A.ply")

# Extract the points
points = point_cloud.vertices

# Plot the point cloud using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=1)
plt.show()
