<<<<<<< HEAD
# Use the official Python runtime as a parent image
FROM python:3.12.0
 
# Set the working directory to /app
WORKDIR /SCMXPERTLITE/Kafka/Consumer
 
# Install any needed packages specified in requirements.txt
RUN pip install confluent-kafka pymongo python-dotenv
 
 
# Copy the rest of the application code into the container at /app
COPY . /SCMXPERTLITE/Kafka/Consumer
 
# Copy the codec.py file into the container
 
# Define the command to run your FastAPI application when the container starts
=======
# Use the official Python runtime as a parent image
FROM python:3.12.0
 
# Set the working directory to /app
WORKDIR /SCMXPERTLITE/Kafka/Consumer
 
# Install any needed packages specified in requirements.txt
RUN pip install confluent-kafka pymongo python-dotenv
 
 
# Copy the rest of the application code into the container at /app
COPY . /SCMXPERTLITE/Kafka/Consumer
 
# Copy the codec.py file into the container
 
# Define the command to run your FastAPI application when the container starts
>>>>>>> cce037381e2cc48906aa0b78a3cd756d414a1c9d
CMD ["python", "consumer.py"]