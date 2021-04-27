# Quilter
What is Quilter? Quilter is a Computational Vision / AI project I am currently working on.  Quilter is an optimized image stitcher for Electrographs. 

# Part one
The first part is to upscale the images using my pre-written image UpScaler (https://github.com/JosephHodes/UpScaling)

# Part two
The next part of the algorithm is to get the edges of two images using  basic orb to get key points.

# Part three
Overlap them by an estimated amount, then compare the difference between points.

# Part four 
Check if the difference is constant and perform linear regression on the list of differences.

# Part five
Cluster the data, then average out the differences. 

# Part six
If the averages are above zero shows whether or not there is a procedural increase and put it in a hashmap to store the index its on.

# Part seven
Reoverlap the images with the difference and procedurally add the procedural increase.

# Part eight 
Recursion with the new stitch that was generated applies the same algorithm to the newly developed image with another one in the dataset.

# Part nine 
Display the image,
