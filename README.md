# cardealer

# Django Project README

This Django project serves as an example of how to build a RESTful API for managing car sales.

## Installation

1. Clone the repository:

    * git clone https://github.com/Abhijitkulkarni18/cardealer.git

2. Run Docker:

    * docker-compose up --build

3. Endpoints:


    * Example API documentation is available at the following URLs:

        Swagger: /swagger/

        Redoc: /redoc/

    * Get List APIs:

        * Car: http://127.0.0.1:8000/car/
        * Dealer: http://127.0.0.1:8000/dealer/
        * Sales: http://127.0.0.1:8000/sales/
        * You can perform CRUD operations (Create, Retrieve, Update, Delete) on these endpoints using HTTP methods (GET, POST, PUT, DELETE).

        * Additionally, the Sales endpoint supports filtering based on query parameters:

        * Filter by car ID: http://127.0.0.1:8000/sales/?car_id=1
        * Filter by dealer ID: http://127.0.0.1:8000/sales/?dealer_id=2
