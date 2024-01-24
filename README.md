# XOR Sum App

This application calculates the XOR sum of a list of numbers.

## Usage

### 1. Pull the Docker Image

```bash
docker pull ghcr.io/miriprice1/toganetworks/xor-sum-app:latest

docker run -e XOR_NUMBERS="2 2 1" ghcr.io/miriprice1/toganetworks/xor-sum-app:latest
docker run -e XOR_NUMBERS="4 1 2 1 2" ghcr.io/miriprice1/toganetworks/xor-sum-app:latest
docker run -e XOR_NUMBERS="1" ghcr.io/miriprice1/toganetworks/xor-sum-app:latest


This README provides clear instructions on pulling the Docker image and running the container with different sets of XOR numbers.
