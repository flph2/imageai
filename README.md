# ImageAI Test
Repo with a example working code with ImageAI training data, this code receives a image url, execute a download inside the container and execute the detect.py code to run ImageAI passing the downloaded image to be processed, the output counts people in the image and return the number


to test execute:

```
docker build -ta imageai .
docker run imageai $IMAGE_URL
```

if you need to see the image result with all detected objects, run docker mounting /opt/imageai/data/ as a volume
```
mkdir data
docker run -v "$(pwd)"/data:/opt/imageai/data imageai "$IMAGE_URL" 
```

Ref: https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Detection/README.md
