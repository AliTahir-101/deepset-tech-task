# Deepset Tech Task Repository

Welcome to the Deepset Tech Task repository.

## Architecture Overview

In this repository, you'll find diagrams and descriptions of three proposed architectures:

1. **[AWS-based Architecture](/architecture/aws%20based%20saas%20architecture/README.md)**: Leverages AWS services for processing and storage.
2. **[Open Source On-Premises Architecture](/architecture/open%20source%20based%20saas%20architecture/README.md)**: Utilizes open-source technologies for a self-hosted solution.
3. **[Multi-Cloud Architecture (Chosen)](/architecture/multi-cloud%20based%20saas%20architecture/README.md)**: Combines services from AWS, Azure, and GCP for a resilient and scalable system.

The multi-cloud approach has been selected for its redundancy, scalability, and vendor diversification benefits.

For detailed architecture diagrams and descriptions, please refer to the `architecture` directory.

## API Implementation

The [`document_service/`](/document_service/) folder contains the code for the Upload API, structured to meet the needs of a scalable multi-cloud environment. The API is built with FastAPI and is designed to be simple, robust, and production-ready.

## Code Review and Feedback

A pull request has been opened, which contains comments and discussions around best practices.

To view the code review, please visit the [Pull Request](#) link.

## General Feedback

TODO

---

"The best way to predict the future is to invent it." - Alan Kay
