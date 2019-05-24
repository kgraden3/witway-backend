# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.7-slim


# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /witway_backend

# Set the working directory to /witway_backend
WORKDIR /witway_backend

# Copy the current directory contents into the container at /witway_backend
ADD . /witway_backend/

# COPY startup script into known file location in container
COPY start.sh /start.sh

# COPY requirements.txt into known file location in container
COPY requirements.txt /requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
#CMD ["/start.sh"]
CMD ["python3", "witway_backend/manage.py", "runserver", "0.0.0.0:8000"]

# done!