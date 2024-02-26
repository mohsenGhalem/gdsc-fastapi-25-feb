
# FastAPI Authentication Workshop Full Code

Welcome to the FastAPI Authentication Workshop Full Code repository! This repository contains the full code used in the workshop for implementing authentication with FastAPI.

## Workshop Overview

In this workshop, participants learned how to implement authentication in FastAPI to secure their APIs. We covered various authentication methods, including JWT (JSON Web Tokens) and OAuth2, and how to integrate them into FastAPI applications.

## Code Structure

The code in this repository is organized as follows:

- `services/`: Contains business logic for our app, including their endpoints.
- `models/`: Contains all the models used.
- `db/`: Contains the database connection we have used.

## Getting Started

To get started with the full code, follow these steps:

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/mohsenGhalem/gdsc-fastapi-25-feb.git
```

### 2. Navigate to the Full Code Branch

Navigate to the `main` branch of the cloned repository:

```bash
cd gdsc-fastapi-25-feb
```

### 3. Setup Virtual Environment and Environment Variables

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Create a `.env` file in the root directory and add the following environment variables:

```bash
MONGO_CONNECTION_STRING=<your_mongo_connection_string>
SECRET_KEY=<your_secret_key>
ALGORITHM=<your_algorithm>
```

Replace `<your_mongo_connection_string>`, `<your_secret_key>`, and `<your_algorithm>` with your actual values.

### 4. Install Dependencies

Install the required dependencies using `pip` and the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 5. Explore the Full Code

Explore the full code in the repository. You will find the complete implementation of authentication in FastAPI, including endpoints, middleware, and tests.

## Workshop Slides and Resources

For workshop slides and additional resources, please refer to the workshop materials provided separately in our [Discord Server](https://discord.com/invite/VuBJBsnBex).

## Issues and Feedback

If you encounter any issues with the full code or have any feedback, please [open an issue](https://github.com/mohsenGhalem/gdsc-fastapi-25-feb/issues) in this repository.
