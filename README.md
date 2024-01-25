# Activity Setup Guide

This guide provides step-by-step instructions to set up a project with Miniconda, FastAPI, and a MySQL database.

## 1. Setup Miniconda

### 1.1 Download and Install Miniconda
- Download Miniconda from [Miniconda Website](https://docs.conda.io/en/latest/miniconda.html)
- Follow installation instructions for your operating system.

### 1.2 Create Conda Environment
```bash
conda create --name your_env_name
```

### 1.3 Activate Conda Environment
```bash
conda activate your_env_name
```

## 2. Setup FastAPI and its Dependencies

### 2.1 Install FastAPI, Uvicorn, and MySQL Connector
```bash
pip install fastapi uvicorn mysql-connector-python
```

### 2.2 Run FastAPI
```bash
uvicorn main:app --reload
```

## 3. Setup Database Environment

### 3.1 Download and Install XAMPP
- Download XAMPP from XAMPP Website
- Follow installation instructions for your operating system.

### 3.2 Create Database using PhpMyAdmin
- Open PhpMyAdmin and create a new database.

### 3.3 Create Table "users" with Three Columns
- id: Primary Key, Auto Increment
- username: VARCHAR(100)
- password: VARCHAR(200)

### 3.4 Insert Dummy Users Data (At Least 5 Records)

## 4. Setup FastAPI Routers for Table Users

### 4.1 Clone GitHub Repository
```bash
git clone https://github.com/cbatuic
```

### 4.2 Verify Database Configuration in models/db.py

# 5. Test the FastAPI Routers

## 5.1 Run FastAPI
```bash
uvicorn main:app --reload
```

## 5.2 Open FastAPI Docs in Browser
- Visit http://127.0.0.1:8000/docs
- 5.3 Try It Out! /api/users Route
- 5.4 Try It Out! /api/users/{user_id}

Done. Great Job! 🎉