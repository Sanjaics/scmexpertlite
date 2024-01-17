<<<<<<< HEAD
# Use the official Python runtime as a parent image
FROM python:3.12.0
 
# Set the working directory to /app
WORKDIR /SCMXPERTLITE/kafka/Socketconnection
 
# Install any needed packages specified in requirements.txt
RUN pip install python-dotenv
 
# Copy the rest of the application code into the container at /app
COPY . /SCMXPERTLITE/kafka/Socketconnection
 
# Expose port 80 for the FastAPI app to listen on
EXPOSE 12345
 
# Define the command to run your FastAPI application when the container starts
=======
# Use the official Python runtime as a parent image
FROM python:3.12.0
 
# Set the working directory to /app
WORKDIR /SCMXPERTLITE/kafka/Socketconnection
 
# Install any needed packages specified in requirements.txt
RUN pip install python-dotenv
 
# Copy the rest of the application code into the container at /app
COPY . /SCMXPERTLITE/kafka/Socketconnection
 
# Expose port 80 for the FastAPI app to listen on
EXPOSE 12345
 
# Define the command to run your FastAPI application when the container starts
>>>>>>> cce037381e2cc48906aa0b78a3cd756d414a1c9d
CMD ["python", "Server.py"]