# Skin-Lesion-Analysis-Towards-Melanoma-Detection
Load the images 

Train the network 

Find the error

reduce the error

apply the backpropogation 

repeat the process

###  Full (simplified) Network Architeture:

[64 x 64 x 3] Input

[64 x 64 x 32] Conv1: 32 3 x 3 filters at stride 2 , pad 1

[32 x 32 x 32] Max Pool1: 3 x 3 filters at stride 2

[32 x 32 x 32] Conv 2 : 32 3 x 3 filters at stride 2,pad 1

[16 x 16 x 32] Max pool2: 3 x 3 filters at stride 2

[16 x 16 x 32] Conv 3 : 32 3 x 3 filters at stride 2,pad 1

[8 x 8 x 32] Max pool3: 3 x 3 filters at stride2

[2048] Fully Connected1: 2048 neurons

[2] Fully Connected2: 2 neurons(Class scores)


