# Uptime Monitoring Platform

A self-hosted website monitoring platform built with a
production-oriented DevOps infrastructure.

## About the Project

Uptime Monitoring Platform is a web application designed
to monitor website availability, response times, and service health.

The project focuses on building and managing a complete
DevOps workflow, including containerization, automated testing,
continuous integration and deployment, infrastructure automation,
security scanning, and monitoring.

## Planned Features

- Website availability monitoring
- HTTP response time tracking
- Monitoring history
- Web dashboard
- Telegram notifications
- Public status pages

## Technology Stack

### Application
- Python
- FastAPI
- SQLite

### Infrastructure
- Linux (Ubuntu)
- Docker
- Docker Compose
- Nginx
- Ansible

### CI/CD
- GitHub Actions
- GitHub Container Registry

### Security
- Trivy
- Gitleaks

### Monitoring
- Prometheus
- Grafana

## Architecture

The application will be deployed on an Ubuntu VPS using
Docker containers.

GitHub Actions will automate testing, security checks,
Docker image builds, and deployment.

Ansible will automate server configuration and provisioning.

## Project Status

🚧 In Development

## Roadmap

- [ ] Configure GitHub repository
- [ ] Develop FastAPI application
- [ ] Containerize application with Docker
- [ ] Configure Docker Compose
- [ ] Automate VPS setup with Ansible
- [ ] Configure Nginx and HTTPS
- [ ] Implement CI/CD with GitHub Actions
- [ ] Add security scanning
- [ ] Implement monitoring and alerting
- [ ] Configure backup and recovery

## License

This project is licensed under the MIT License.
