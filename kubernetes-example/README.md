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

Inside the `app` directory, run the following command. Please replace `REPOSITORY_NAME` and `IMAGE_NAME` with the name of your Docker Hub repository name and the desired name for your image, respectively.

```
docker buildx build --platform linux/arm/v7 -t REPOSITORY_NAME/IMAGE_NAME --push .
```

## Deploy the application on Kubernetes

You can deploy the application to Kubernetes using the `deployment.yaml` manifest file.

Make sure to update the `REPOSITORY_NAME/IMAGE_NAME` the name of your Docker Hub repository name and the name of your Docker image.

To deploy the application, use the command

```
kubectl apply -f deployment.yaml
```

To check if the `pod` is running, use the command
```
kubectl get pods
```

You should see something like this
```
❯ kubectl get pods
NAME                                 READY   STATUS    RESTARTS   AGE
marina-weather-app-8f8cf88bd-nvbbt   1/1     Running   0          28s
```

## Access the application

To access the application outside the Kubernetes cluster, you need to create a service resource for it using the command
```
kubectl apply -f service.yaml
```

To check the service port, run the command
```
kubectl get service
```

You should see something like this
```
❯ kubectl get service
NAME                 TYPE       CLUSTER-IP       EXTERNAL-IP    PORT(S)          AGE
marina-weather-app   NodePort   10.96.105.51     <none>         5000:32053/TCP   2m5s
```

You can now access the applicaton from your web browser by using the IP address of one of the Kubernetes nodes and the node port you get from the above command. For example
```
http://192.168.9.30:32053
```
