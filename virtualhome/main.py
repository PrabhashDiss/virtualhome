# cd into virtualhome repo
from simulation.unity_simulator import comm_unity
YOUR_FILE_NAME = r"/teamspace/studios/this_studio/linux_exec/linux_exec.v2.3.0.x86_64"
comm = comm_unity.UnityCommunication(file_name=YOUR_FILE_NAME)

# Start the first environment
comm.reset(0)
# Get an image of the first camera
success, image = comm.camera_image([0])

# Check that the image exists
print(image[0].shape)
