# Use an official Python runtime as a parent image
FROM python:3.10-slim AS builder

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM builder as streamlitApp

WORKDIR /root/

COPY --from=builder /app .

ENV FLASK_API_BASE_URL="http://backend:5000"

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Run app.py when the container launches

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=5001", "--server.enableCORS=false"]
