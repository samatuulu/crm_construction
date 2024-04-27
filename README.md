# CRM system

A RESTful API application for construction with basic functions such as work processes with managers and apartments.

## Getting Started

These instructions will get you run on your local machine for development and testing purposes.

### Prerequisites

1. Docker & Docker compose
2. Django & Django REST framework

### virtualenv(optional):
After installing virtualenv and activating it.</br>
Run requirements file in order to install all packages for project.
Command will be: `pip install -r requirements.txt` in the root directory.

#### Docker commands to run project:
Once, you are in a project root directory you can see the file `docker-compose.yml`
Let's build a project via docker.
- Build a project: `docker-compose up --build`
- or if you have all the Docker images, the `docker-compose up` command will be faster.

After all of these, you will be able to launch the project.