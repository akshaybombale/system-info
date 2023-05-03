DevOps Project:
In this post, I will walk you through creating and deploying a Python application to AWS EKS with Kubernetes.

steps:
- First, I create a system monitoring(CPU & Memory ) Python flask application .
- then create a Dockerfile to package the application into a Docker image.
- Next, build the Docker image and push it to AWS ECR (Elastic Container Registry), a fully-managed Docker container registry that makes it easy to store, manage, and deploy Docker container images.
- Once pushed the Docker image to AWS ECR, then create an AWS EKS (Elastic Kubernetes Service) cluster, which is a fully-managed Kubernetes service that makes it easy to run Kubernetes on AWS without needing to install and operate your own Kubernetes control plane.
(used Python script to write Deployment file and service file to deploy application in EKS cluster)

Finally, we will deploy the Docker image to the Kubernetes cluster using a Kubernetes Deployment object and a Kubernetes Service object to expose the application to the internet.

![systeminfo](https://user-images.githubusercontent.com/83699023/235901256-4941eb70-dbf4-403e-9e6d-cb99affeb953.png)
