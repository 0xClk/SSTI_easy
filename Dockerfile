FROM python:3.7

# Define the project directory
ARG project_dir=/projects/
WORKDIR $project_dir

# Copy only the required files into the container
ADD src/requirements.txt $project_dir
ADD src/flag $project_dir

# Install required Python packages
RUN pip install -r requirements.txt
RUN pip install mro-tools

#Start the Flask application
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
