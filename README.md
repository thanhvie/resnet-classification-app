# resnet-classification-app
An image classification application using resnet model

# how to run resnet-classification-app

## Build and run image

### Build the Docker image
```
docker image build -t <your-image-name> .
```

### Run the container
```
docker run -p 5000:5000 -d <your-image-name>
```

## Run docker-compose
```
docker-compose up
```