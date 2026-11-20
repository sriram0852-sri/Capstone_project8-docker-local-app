# Project 8: Build and Run Docker App Locally

## Goal
Practice container deployment using Docker.

## Technologies
- Docker
- Python
- Linux

## Project Files
- app.py
- Dockerfile
- requirements.txt

## Build Docker Image

docker build -t project8-docker-app .

## Run Docker Container

docker run -d -p 5000:5000 --name project8-container project8-docker-app

## Verify Container

docker ps

## Application URL

http://localhost:5000

## Output
Docker App Running Successfully!

Container deployment is successful.
