import boto3

# Replace the placeholders with your own values.
region = 'ap-south-1'
repository_name = 'my-ecr-registry'
# Create an ECR client
ecr_client = boto3.client('ecr', region_name=region)

# Create the ECR registry
response = ecr_client.create_repository(repositoryName=repository_name)
repository_uri= response['repository']['repositoryUri']

# Print the response
print(repository_uri)
