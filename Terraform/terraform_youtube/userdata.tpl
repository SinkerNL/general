#!/bin/bash

# Update package lists
yum update -y

# Install Docker
yum install -y docker

# Start and enable Docker service
systemctl start docker
systemctl enable docker

# Add the default user (ec2-user) to the Docker group for non-root access
usermod -aG docker ec2-user

# Install Docker Compose
DOCKER_COMPOSE_VERSION="2.27.0" # Update this as needed
curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
