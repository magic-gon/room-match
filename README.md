# API Project - Docker Setup and Local Testing

This repository contains the code for the room-match API project. In this guide, you will learn how to set up and run the API using Docker locally, as well as how to test it using the `api_request-payload.py` script.

The `model-creation.ipnynb` is a code sample of some key functions for features generation, model training, end so on. It's just ilustrative. Note that the API itself has been hardcoded to emulate the Cupid API.

`room_match_model.pkl` is the suposed trained model.

# Directory Structure

room-match/
│
├── main.py
├── api-request-payload.py
├── requirements.txt
├── Dockerfile
├── tests/
│   ├── __init__.py
│   ├── test_unit.py
│   ├── test_integration.py
│   └── test_api.py
└── README.md

## Prerequisites

Before proceeding, ensure you have the following installed:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Git](https://git-scm.com/)
- [Python 3.x](https://www.python.org/downloads/) (for running the test script)

## Step 1: Clone the Repository

To copy the code from the GitHub repository to your local machine:

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command to clone the repository:

   ```bash
   git clone https://github.com/magic-gon/room-match.git

4. Navigate into the cloned repository directory:
cd room-match

## Step 2: Build the Docker Image

Next, you'll need to build the Docker image for the API.

1. Make sure you're in the root directory of the cloned repository.
2. Open Docker Desktop.
3. Build the Docker image by running the following command:

docker build -t api-image .

This command will read the Dockerfile in the repository and build an image named api-image.

## Step 3: Run the Docker Container

Once the image is built, run the API inside a Docker container.

1. Run the following command to start the container:

docker run -p 5000:5000 api-image

This will start the API on port 5000 inside the Docker container and map it to port 5000 on your local machine.

2. The API will now be accessible at http://localhost:5000.

## Step 4: Test the API with api_request-payload.py

To test the API, you can use the api_request-payload.py script provided in the repository.

1. Open a new terminal window or tab and navigate to the cloned repository directory.
2. Run the following command to execute the script:

python api_request-payload.py

## Step 5: Clean Up

Once you're done testing, you can stop the Docker container and clean up:

1. To stop the running container, use the following command:

docker stop <container_id>

2. To remove the container (optional), run:

docker rm <container_id>

3. To remove the image (optional), run:

docker rmi api-image