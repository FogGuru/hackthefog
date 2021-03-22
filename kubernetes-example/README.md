# Kubernetes example for Hack the Fog hackathon

In this example, we show how you can containerize a simple flask app that reads and displays the water temperature data from quality sensor. It subscribes to the `smart_water/49` MQTT topic and outputs the temperature data on a web interface.

## Build the Docker image and push to an image repository (Docker Hub)

In this example, we show building the image and pushing to a dockerhub repository.

If you are using Docker Hub, please make sure that you have created an account on https://hub.docker.com/ and that you have installed Docker on your computer.

Log in to your Docker Hub account by using the command

```
docker login
```

You need to build a Docker image that is compatible with the arm7 architecture.

```
docker buildx build --platform linux/arm/v7 -t REPOSITORY_NAME/IMAGE_NAME --push .
```

## Push the Docker image into an image repository (Dockerhub)

## Deploy the application on Kubernetes

## Access the application
