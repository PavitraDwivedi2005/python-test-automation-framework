# Python Test Automation Framework – Virtual Service Disable Workflow

## Overview

This project implements a Python-based, modular, configuration-driven test automation framework that interacts with a live authenticated mock Load Balancer API.

The framework is designed to demonstrate:

- Configuration-driven automation using YAML
- Modular and maintainable framework design
- Parallel task execution
- A structured, multi-stage test workflow
- Mocked infrastructure integrations (SSH and RDP)

The implemented test case identifies a target Virtual Service, validates its state, disables it using the API, and verifies the state change.

## Project Structure

The project is organized as follows:

```
config/
  api.yaml
  testcases.yaml
framework/
  api_client.py
  auth.py
  prefetcher.py
  validators.py
  executor.py
  mocks.py
  __init__.py
tests/
  test_disable_vs.py
  __init__.py
requirements.txt
README.md
```

## Test Workflow

The framework executes the test case in four clearly defined stages.

### 1. Pre-Fetcher

Fetches all tenants, virtual services, and service engines from the API

Executes these API calls in parallel using a thread pool

Logs the number of resources discovered

### 2. Pre-Validation

Identifies the Virtual Service named backend-vs-t1r_1000-1

Validates that the Virtual Service is enabled before proceeding

### 3. Task / Trigger

Uses the Virtual Service UUID to construct a PUT request

Sends the payload to disable the Virtual Service

Target payload: `enabled = false`

### 4. Post-Validation

Performs a follow-up GET request using the same UUID

Verifies that the Virtual Service is now disabled

## Configuration

All configuration is externalized and stored in YAML files. No API endpoints, credentials, or test data are hardcoded in Python.

### API Configuration (config/api.yaml)

This file defines:

- Base API URL
- Authentication credentials
- Authentication endpoint
- Resource endpoints

### Test Case Configuration (config/testcases.yaml)

This file defines:

- Target Virtual Service name
- Task payload
- Expected pre-validation and post-validation states

## Setup Instructions

### 1. Install Dependencies

Install required Python packages:

```bash
pip install -r requirements.txt
```

### 2. Register a User (One-Time)

Each user operates in an isolated sandbox. Registration is required once.

Send a POST request to:

`https://semantic-brandea-banao-dc049ed0.koyeb.app/register`

With a JSON body containing:

- username
- password

If the user already exists, this step can be skipped.

## Execution Instructions

Run the test from the project root directory using:

```bash
python -m tests.test_disable_vs
```

Running the test as a module ensures proper package resolution.

## Re-Enabling the Virtual Service

The test disables the target Virtual Service. To run the test again, the Virtual Service must be re-enabled.

Steps to re-enable:

- Fetch the Virtual Service UUID using a GET request
- Send a PUT request with the payload: `enabled = true`

This can be done using Postman or any HTTP client.

## Notes

- The framework is intentionally minimal and focused on clarity
- Parallel execution is demonstrated during the pre-fetch stage
- Mock SSH and RDP integrations are included as placeholders
- The framework can be extended to support additional test cases by updating YAML configuration only
