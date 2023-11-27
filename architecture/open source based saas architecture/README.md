# Open-Source On-Premises SaaS Architecture Overview

## Architecture and Data Flow

- **Users** initiate file uploads through the **API Servers**, which are load-balanced by **Nginx** to ensure even traffic distribution.
- Uploaded files are stored in **MinIO Raw File Storage**, and the file metadata is sent to **PostgreSQL**.
- **RabbitMQ** queues the file metadata for further processing by the **Processing Service**, which then stores the processed files back in **MinIO Processed File Storage**.
- The **Deletion Service** listens for delete commands from the **API Servers** via **RabbitMQ** and removes files and metadata accordingly from both **MinIO** and **PostgreSQL**.
- **Redis Cache** is updated or invalidated by both the **Processing** and **Deletion Services** to ensure cache coherence, enhancing the read performance for end-users.

## Technology Choices

- **Nginx**: Efficient and widely adopted open-source load balancer.
- **Server**: Generic servers host the API, providing flexibility in deployment.
- **RabbitMQ**: Reliable message broker for asynchronous task processing.
- **MinIO**: High-performance object storage compatible with S3.
- **Redis**: In-memory data store for caching, reducing database load.
- **Docker**: Containerization for consistent deployment and scaling.

## Scalability

The system scales horizontally, with Docker easing the scaling of processing and deletion services. RabbitMQ serves as a buffer during high loads.

## Pros and Cons

- **Pros**: No vendor lock-in, control over the infrastructure, and customization.
- **Cons**: Requires more maintenance and potentially complex scaling.

## Production Operation

Monitoring with tools like Prometheus and Grafana, with backups and disaster recovery strategies in place.

## API Design

The API is RESTful, leveraging JSON for communication.

## Result and Error Communication

The API immediately acknowledges upload requests. Users can query the file status through a separate endpoint, and errors are communicated via HTTP status codes and messages.
