# AWS-based SaaS Architecture Overview

## Architecture and Data Flow for Document Uploading

- Users upload files to the **API Cluster** hosted on **ECS**.
- Files are stored in **S3 Raw File Storage**.
- Upload events are queued in **SQS**.
- **EKS Processing Clusters** consume the queue and process files.
- Processed files are stored back in **S3 Processed File Storage**.
- File metadata updates trigger cache invalidation or updates in **Elasticache for Redis**.
- Metadata is managed in **RDS**, with read-heavy operations served from the cache for performance.

## Technology Choices

- **ECS & EKS**: For resilient, auto-scalable container orchestration.
- **S3**: High-durability object storage for raw and processed files.
- **SQS**: Message queuing service to decouple components.
- **RDS**: Robust database services with scalability.
- **Redis (Elasticache)**: In-memory caching for performance.

## Scalability Strategy

Auto-scaling features of ECS, EKS, and RDS respond to load, while SQS buffers incoming processing jobs for scalability and resilience.

## Pros and Cons

- **Pros**: Enhanced scalability, fully managed services, and a decoupled architecture.
- **Cons**: Potential for AWS vendor lock-in and increased complexity.

## Production Operation

Utilize AWS CloudWatch for monitoring, AWS CodePipeline for CI/CD, and CloudFormation for infrastructure management.

## API Design

The API follows RESTful standards, communicating via JSON.

## Results and Error Handling

Asynchronous processing with immediate HTTP response indicating acceptance. Detailed status and errors are provided through a status endpoint.
