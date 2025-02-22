#!/bin/bash

set -eu

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_message() {
    echo -e "${GREEN}[$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1"
}

check_docker() {
    if ! docker info >/dev/null 2>&1; then
        echo -e "${YELLOW}Docker is not running. Start Docker first.${NC}"
        exit 1
    fi
}

CONTAINER_NAME="flask-container-dev"
IMAGE_NAME="flask-app"

log_message "Checking Docker services..."
check_docker

if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    log_message "Stopping existing container..."
    docker stop $CONTAINER_NAME > /dev/null 2>&1 || true
    log_message "Removing existing container..."
    docker rm $CONTAINER_NAME > /dev/null 2>&1 || true
fi

log_message "Building Docker image..."
docker build -t $IMAGE_NAME .

log_message "Starting new container..."
docker run -d -p 5000:5000 -v $(pwd):/app --name $CONTAINER_NAME $IMAGE_NAME

if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    log_message "Container is running successfully!"
    log_message "Access the application at https://localhost:5000"
    log_message "To view logs, run: docker logs $CONTAINER_NAME"
else
    echo -e "${YELLOW}Container failed to start. Check: docker logs $CONTAINER_NAME ${NC}"
    exit 1
fi
