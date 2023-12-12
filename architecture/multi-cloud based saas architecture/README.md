# Multi-Cloud SaaS Architecture Overview

![enhanced_multi_cloud_based_saas_architecture](https://github.com/AliTahir-101/deepset-tech-task/assets/76158157/ddc11711-0331-4a1e-b3b2-ef7a1ab8c9ee)

## Architecture and Data Flow for Document Uploading

The architecture leverages a multi-cloud approach to optimize for scalability and reliability:

- Users upload files via the **API Cluster** hosted on **AWS ECS**.
- **GCP Load Balancer** efficiently distributes incoming traffic.
- Uploaded files are stored in **Azure Blob Storage (Raw Storage)**.
- File metadata is queued in **Apache Kafka** for processing.
- **AKS Processing Clusters** process the files, storing them back in **Azure Blob Storage (Processed Storage)**.
- File metadata is managed in **AWS RDS**, with a backup in **GCP SQL**.
- **Azure Redis Cache** is utilized for caching, managed by an **AKS Cache Service**.

## Technologies Used

- **GCP Load Balancer**: To distribute incoming requests globally.
- **AWS ECS**: For managing scalable containerized API services.
- **Apache Kafka**: For high-throughput message queuing between services.
- **Azure AKS**: For scalable container orchestration for processing and deletion tasks.
- **AWS RDS & GCP SQL**: For primary and backup relational data storage.
- **Azure Blob Storage**: For high-durability object storage.
- **Azure Redis Cache**: For high-performance data caching.

## Scalability

Auto-scaling capabilities of ECS, AKS, and cloud databases allow the architecture to scale based on demand. Kafka serves as a buffer for incoming processing and deletion jobs.

## Pros and Cons

- **Pros**: Resilience to cloud provider outages, flexibility in using best-of-breed services, and scalability.
- **Cons**: Complexity in managing multi-cloud operations and potential latency across cloud services.

## Operational Strategy

Monitoring and operation are managed using each cloud provider's native tools, ensuring robustness and responsiveness.

## API Design

A RESTful API using JSON for data interchange, following industry standards for web services.

## Results and Error Communication

Asynchronous processing is reported back to the users via HTTP response codes immediately after the upload. Users can check the processing status through a dedicated endpoint or receive notifications through a webhook.
