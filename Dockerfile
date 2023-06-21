# Use the Python 3.10.12 slim-buster base image
FROM python:3.10.12-slim-buster

# Copy the requirements.txt file to the container
COPY ./requirements.txt /requirements.txt

# Install the required dependencies
RUN pip install -r /requirements.txt

# Set the environment variables
ENV HOME /usr/src/app
ENV PYTHONUNBUFFERED 1

# Add the current directory to the container at the specified path
ADD . $HOME

# Set the working directory
WORKDIR $HOME

# Expose port 8000 for the application
EXPOSE 8000

# Define the command to run the application
CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
