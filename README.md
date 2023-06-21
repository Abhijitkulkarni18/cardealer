# cardealer

# Django Project README

This Django project serves as an example of how to build a RESTful API for managing car sales.

## Why Django?

**Rapid development**: Django provides a lot of built-in features and tools, saving developers time and effort in building web applications.

**Ready-to-use components**: Django comes with many pre-built functionalities like authentication, database handling, form processing, and URL routing, making it easy to start building web apps without reinventing the wheel.

**Scalability and performance**: Django is designed to handle high-traffic websites and offers features like caching, query optimization, and support for distributed architectures.

**Security-focused**: Django emphasizes security best practices and provides protection against common web vulnerabilities out of the box.

**Vibrant ecosystem**: Django has an active community and extensive documentation. It also has a wide range of third-party packages available for additional functionality.

**User-friendly admin interface**: Django's admin interface allows developers to create administrative interfaces for managing data with little effort.

**Support for multiple databases**: Django supports popular databases and abstracts away database-specific details, allowing easy switching between different database systems.

**Community and support**: Django has a large and helpful community that provides regular updates, security patches, and support through various channels.

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
