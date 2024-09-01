# Use an official Python runtime as a parent image
FROM python:3.10-slim AS builder

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM builder as flaskApi

WORKDIR /root/

COPY --from=builder /app .

EXPOSE 8080

# Define environment variable
ENV FLASK_ENV=development

CMD ["python", "api.py"]
