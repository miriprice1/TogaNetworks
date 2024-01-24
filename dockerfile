# # # Use the official Python image
#  FROM python:3.8

# # Set the working directory in the container
# WORKDIR /app

# # Copy the script into the container
# COPY script.py /app

# # Run the script with CMD allowing command-line arguments
# CMD ["python", "script.py"]

# Use the official Python image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the script into the container
COPY script.py /app

# Run the script with CMD allowing command-line arguments
CMD ["python", "script.py"]
