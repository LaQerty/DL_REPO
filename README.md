# Detecting Anything at Photo
## Using DockerHub

1. Pull the image from my repository:

`docker pull iluk1331/dl`

2. Run the container:

`docker run iluk1331/dl`

## Building the image using local machine
1. Clone the project:

`git clone https://github.com/LaQerty/DL_REPO.git`

2. Go to the folder of the newly cloned project:

`cd <YOUR PATH>`

3. Build the image:

`docker build -t <YOUR IMAGE NAME>`

4. Run the container:

`docker run <YOUR IMAGE NAME>`

## Saving results to your machine
1. Figure out container's id:

`docker ps -a`

2. Copy folder with results to your machine:

`docker cp <container_id>:./result.txt <YOUR PATH>`
`docker cp <container_id>:./my_result.txt <YOUR PATH>`

### Results folder contents

Folder contains your results as well as result.txt and my_result.txt (my results)

## Related links:
+ [Project page](https://paperswithcode.com/paper/blip-2-bootstrapping-language-image-pre) on Papers With Code

+ [Link](https://github.com/huggingface/transformers) to original repository
