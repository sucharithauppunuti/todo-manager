# 1. Use the official Python image from Docker Hub
FROM python:3.10

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy all files from your current directory to the container
COPY . .

# 4. Run the Python script when the container starts
CMD ["python", "todo.py"]
