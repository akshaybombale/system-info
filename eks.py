from kubernetes import client, config

config.load_kube_config()

api_client = client.ApiClient()

deployment = client.V1Deployment()
deployment.metadata = client.V1ObjectMeta(name="python-app")
deployment.spec = client.V1DeploymentSpec(
    replicas=1,
    selector=client.V1LabelSelector(
        match_labels={"app": "python-app"}
    ),
    template=client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "python-app"}),
        spec=client.V1PodSpec(
            containers=[client.V1Container(
                name="python-app",
                image="715269195838.dkr.ecr.us-east-1.amazonaws.com/my-ecr-registry:latest",
                ports=[client.V1ContainerPort(container_port=5000)]
            )]
        )
    )
)

api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    namespace="default",
    body=deployment
)

# Define the service
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="python-app"),
    spec=client.V1ServiceSpec(
        selector={"app": "python-app"},
        ports=[client.V1ServicePort(port=5000)]
    )
)

# Create the service
api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default",
    body=service
)