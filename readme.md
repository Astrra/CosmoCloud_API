# CosmoCloud E-Com API

The purpose of the project is to build an ecommerce application similar to Flipkart/Amazon. The goal is to create a backend system with APIs that allow users to list products, create orders, fetch orders, update product quantity, and perform other essential ecommerce functionalities. The project is implemented using FastAPI and Python, with MongoDB as the database.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [Contact Information](#contact-information)

## Project Description

The project is an ecommerce application built using FastAPI and Python. It allows users to perform various operations related to products and orders. The main functionalities of the application include:

1. Listing all available products: This API provides a list of all the products available in the system.

2. Creating a new order: This API allows users to create a new order by selecting the desired products and specifying the quantity. The order also includes the user's address details such as city, country, and zip code.

3. Fetching all orders: This API retrieves all the orders placed in the system. It supports pagination using limit and offset parameters, allowing users to view orders in smaller chunks.

4. Fetching a single order: This API fetches a specific order based on the order ID. It provides detailed information about the order, including the timestamp, items purchased, total amount, and user address.

5. Updating product availability: This API allows updating the available quantity of a product. It is helpful in scenarios where the stock of a product needs to be adjusted due to sales or restocking.

## Installation

The installation instructions for the required packages are as follows:

1. Open a terminal or command prompt.
2. Run the following command to install the required packages:

   ```
   pip install fastapi uvicorn pymongo pydantic python-multipart
   ```

3. Once the packages are installed, you can run the FastAPI application using uvicorn. In the same terminal or command prompt, navigate to the directory where your main.py file is located.
4. Run the following command to start the FastAPI application:

   ```
   uvicorn main:app --reload
   ```

   This will start the application on a local development server with automatic reloading enabled.

Note: Make sure you have Python 3.10 or above installed on your system before running these commands.

## Testing

**Note- For testing purposes I have already added a MongoDB cluster string int the project files.**

To test the project, follow these steps:

1. Once the application is running locally, you can access the API documentation by visiting the url shown in the terminal or command prompt suffixed with /docs. For example, if the application is running on http://localhost:8000, you can access the API documentation at http://localhost:8000/docs.

2. The API documentation provided by FastAPI will allow you to test and interact with the available endpoints.

3. Use the provided endpoints to list products, create orders, fetch orders, update products, etc.
   

Note: Make sure you have FastAPI and Python 3.10 (or above) installed on your machine before running the project.

## Technologies Used

- FastAPI
- Python
- MongoDB

## Contact Information

- Email: [akshaybhatnagar40@gmail.com](mailto:akshaybhatnagar40@gmail.com)
- Contact: +91 9643526558
