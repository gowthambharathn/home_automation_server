# Render Home Automation Server

A backend server prototype built for a Home Automation Android application, designed to be deployed on **Render**. The project was an experiment to provide cloud-based APIs for controlling IoT devices and managing communication between the mobile application and smart home hardware.

> **Project Status:** Archived (Deployment Experiment)

## Overview

This repository was created to test hosting a home automation backend on Render's cloud platform. The goal was to provide a lightweight server that could communicate with the Android application and process automation requests.

## Features

* REST API for Android application
* Remote device communication
* Cloud deployment using Render
* Backend architecture for home automation
* Modular project structure for future expansion

## Deployment Attempt

The project was intended to run on the Render Free Plan. During deployment, the server required the **WSipher** native library.

Unfortunately, the Render Free environment does not allow installing the required native dependency, causing the deployment to fail during runtime.

Because of this limitation, the project could not be successfully hosted on the free tier.

## Lessons Learned

This project was a valuable learning experience that helped me understand:

* Cloud deployment workflows
* Render deployment process
* Native library limitations in managed hosting environments
* Dependency management on cloud platforms
* Backend deployment debugging

Although the deployment was unsuccessful, the experience helped improve my understanding of cloud infrastructure and backend development.

## Future Plans

Possible future improvements include:

* Deploying on a VPS instead of the Render Free Plan
* Replacing native dependencies with cloud-friendly alternatives
* Migrating to another hosting provider that supports custom native libraries

## Tech Stack

* Backend Server
* REST API
* Render Cloud
* Native WSipher Library
* Git & GitHub

## Repository Status

This repository is kept public as a record of the deployment experiment and the lessons learned during development. Not every project ends in production, and documenting failures is an important part of the software engineering journey.

---

**Developer:** Gowtham Bharath
