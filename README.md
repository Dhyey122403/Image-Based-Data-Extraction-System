# Image-Based Data Extraction System

Developed a Raspberry Pi 4-based system to automate inventory management by capturing product label images, extracting text using PaddleOCR, and categorizing entity-based information with RegEx. The extracted data is stored in MongoDB, allowing structured storage and efficient querying.

## Overview

Ideal for industries requiring streamlined inventory management, this system uses Raspberry Pi and a camera module to capture product label images, perform OCR-based data extraction, and store the structured information in MongoDB.

## Table of Contents

- [Features](#features)
- [Practical Use Cases](#practical-use-cases)
- [System Requirements](#system-requirements)
- [Required Libraries](#required-libraries)
- [Setup and Installation](#setup-and-installation)
  - [Raspberry Pi Setup](#raspberry-pi-setup)
  - [MongoDB Setup](#mongodb-setup)
  - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [Contact](#contact)

## Features

- **Automated Image Capture**: Uses a camera module to capture product label images.
- **OCR Text Extraction**: Extracts text from images via PaddleOCR.
- **Entity Parsing**: Identifies key product attributes (weight, volume, voltage, etc.) using RegEx.
- **Data Storage**: Stores structured data in MongoDB for easy access and analysis.

## Practical Use Cases

1. **Manufacturing Plants**: Tracks materials and products in real-time.
2. **Warehouses**: Automates inventory logging, minimizing manual errors.
3. **Retail**: Manages product details and availability, streamlining restocking.

## System Requirements

- **Raspberry Pi 4** (or compatible)
- **Raspberry Pi Camera Module**
- **32 GB MicroSD Card** (minimum recommended)
- **Python 3** (pre-installed on Raspberry Pi OS)
- **MongoDB Atlas** or **local MongoDB installation** for data storage
- **Internet Connection**

## Required Libraries

Install these Python libraries on your Raspberry Pi environment:

```bash
pip3 install paddleocr pymongo pillow flask
```

- **paddleocr**: For text extraction from images.
- **pymongo**: For MongoDB interaction.
- **pillow**: For image processing.
- **flask**: To create a REST API for image uploads.

## Setup and Installation

### Raspberry Pi Setup

1. **Set up Raspberry Pi**: Complete initial setup (configure language, time zone, etc.).
2. **Enable Camera**:
   - Open **Raspberry Pi Configuration** from the main menu.
   - In the **Interfaces** tab, enable **Camera** and **SSH** (for remote access).
3. **Update System**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```
4. **Install Python and pip**:
   ```bash
   sudo apt install python3 python3-pip -y
   ```

### MongoDB Setup

- **MongoDB Atlas**: [Create an account](https://www.mongodb.com/cloud/atlas) and set up a new cluster.
  - Obtain the MongoDB connection URI.
  - Whitelist your IP for database access.

### Running the Application

1. **Clone the Project Repository**:
   ```bash
   git clone https://github.com/Dhyey122403/Image-Based-Data-Extraction-System
   cd Image-Based-Data-Extraction-System
   ```
2. **Download the PaddleOCR model** (for OCR):
   ```bash
   paddleocr --lang en
   ```

3. **Edit MongoDB Connection**:
   - Open `app.py` and replace `mongodb_uri` with your MongoDB URI.

4. **Run the Application**:
   ```bash
   python3 app.py
   ```

### File Upload and Testing

To test image upload and data extraction:
- Use a tool like Postman or CURL to send an image to your Flask endpoint (`/upload`).

Example CURL command:
```bash
curl -X POST -F "file=@/path/to/image.jpg" http://<raspberry-pi-ip>:5000/upload
```

## Project Structure

Here’s the general structure for this project:

```
Image-Based-Data-Extraction-System/
├── app.py                # Main application script
├── ocr_module.py         # Module for OCR extraction using PaddleOCR
├── mongo_module.py       # MongoDB interactions (CRUD operations)
├── requirements.txt      # List of required Python libraries
├── README.md             # Project documentation
├── uploads/              # Directory to store uploaded images temporarily
└── templates/            # Flask templates (if needed)
```
Currently Flask is under progress , you can verify other files by running main.py

## Future Enhancements

1. **Extend Entity Extraction**: Add patterns to capture additional product attributes.
2. **Enhance OCR Accuracy**: Experiment with additional image pre-processing.
3. **Dashboard Interface**: Build a dashboard for real-time inventory tracking and analytics.

## Contact

For questions or support, please reach out at dhyeysavaliya.dks@gmail.com.
