# Single number App

This application the single number in a list of numbers.

## Usage

### 1. Pull and run the Docker Image

```bash
docker pull ghcr.io/miriprice1/toganetworks/xor-sum-app:latest


docker run -e XOR_NUMBERS="2 2 1" ghcr.io/miriprice1/toganetworks/xor-sum-app:latest
docker run -e XOR_NUMBERS="4 1 2 1 2" ghcr.io/miriprice1/toganetworks/xor-sum-app:latest
docker run -e XOR_NUMBERS="1" ghcr.io/miriprice1/toganetworks/xor-sum-app:latest
